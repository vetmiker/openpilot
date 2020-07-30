import os
import json
from numpy import clip
from common.basedir import BASEDIR
from common.realtime import sec_since_boot

# by Zorrobyte
# version 4

def copysign(n):
  return 1 if n >= 0 else -1


class CurvatureLearner:  # todo: disable when dynamic camera offset is working
  def __init__(self):
    self.curvature_file = '{}/curvaturev4.json'.format(BASEDIR)
    rate = 1 / 20.  # pathplanner is 20 hz
    self.learning_rate = 1.6666e-3 * rate  # equivalent to x/12000
    self.write_frequency = 2 * 60  # in seconds
    self.offset = 0.
    self._load_curvature()

  def update(self, angle_steers, d_poly, v_ego):
    angle_band = None
    if abs(angle_steers) >= 0.1:  # not between -.1 and .1
      if abs(angle_steers) < 2:
        angle_band = 'center'
      elif 2 <= abs(angle_steers) < 5.:
        angle_band = 'inner'
      elif 5 <= abs(angle_steers):
        angle_band = 'outer'

    if angle_band is not None:
      self.learned_offsets[angle_band] += d_poly[3] * self.learning_rate * -copysign(angle_steers)  # add when negative, subtract when positive
      self.offset = self.learned_offsets[angle_band]

    if sec_since_boot() - self._last_write_time >= self.write_frequency:
      self._write_curvature()
    return clip(self.offset, -0.3, 0.3)

  def _load_curvature(self):
    self._last_write_time = 0
    try:
      with open(self.curvature_file, 'r') as f:
        self.learned_offsets = json.load(f)
      return
    except:  # can't read file or doesn't exist
      self.learned_offsets = {'center': 0., 'inner': 0., 'outer': 0.}
      self._write_curvature()  # rewrite/create new file

  def _write_curvature(self):
    with open(self.curvature_file, 'w') as f:
      json.dump(self.learned_offsets, f)
    os.chmod(self.curvature_file, 0o777)
    self._last_write_time = sec_since_boot()
