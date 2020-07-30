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
    self._load_curvature()

  def update(self, angle_steers, d_poly, v_ego):
    offset = 0
    angle_band = self.pick_angle_band(angle_steers)

    if angle_band is not None:  # don't return an offset if not between a band
      self.learned_offsets[angle_band] -= d_poly[3] * self.learning_rate * copysign(angle_steers)
      offset = self.learned_offsets[angle_band]

    if sec_since_boot() - self._last_write_time >= self.write_frequency:
      self._write_curvature()
    return clip(offset, -0.3, 0.3)

  def pick_angle_band(self, angle_steers):
    if abs(angle_steers) >= 0.1:  # not between -.1 and .1
      if abs(angle_steers) < 2:
        return 'center'
      elif 2 <= abs(angle_steers) < 5.:
        return 'inner'
      elif 5 <= abs(angle_steers):
        return 'outer'
    return None

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
