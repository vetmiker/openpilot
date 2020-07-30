import os
import json
from numpy import clip
from common.basedir import BASEDIR
from common.realtime import sec_since_boot
from selfdrive.config import Conversions as CV

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

    self.speed_bands = ['sng', 'traffic', 'highway']
    self.angle_bands = ['center', 'inner', 'outer']

    self._load_curvature()

  def update(self, angle_steers, d_poly, v_ego):
    offset = 0
    angle_band = self.pick_angle_band(angle_steers)

    if angle_band is not None:  # don't return an offset if not between a band
      speed_band = self.pick_speed_band(v_ego)  # will never be none
      self.learned_offsets[angle_band][speed_band] -= d_poly[3] * self.learning_rate * copysign(angle_steers)  # the learning
      offset = self.learned_offsets[angle_band][speed_band]

    if sec_since_boot() - self._last_write_time >= self.write_frequency:
      self._write_curvature()
    return clip(offset, -0.3, 0.3)

  def pick_speed_band(self, v_ego):
    if v_ego <= 10 * CV.MPH_TO_MS:
      return 'sng'
    if v_ego <= 50 * CV.MPH_TO_MS:
      return 'traffic'
    return 'highway'

  def pick_angle_band(self, angle_steers):
    if abs(angle_steers) >= 0.1:
      if abs(angle_steers) < 2:  # between +=[.1, 2)
        return 'center'
      if abs(angle_steers) < 5.:  # between +=[2, 5)
        return 'inner'
      return 'outer'  # between +=[5, inf)
    return None  # return none when below +-0.1, removes possibility of returning offset in this case

  def _load_curvature(self):
    self._last_write_time = 0
    try:
      with open(self.curvature_file, 'r') as f:
        self.learned_offsets = json.load(f)
      return
    except:  # can't read file or doesn't exist
      self.learned_offsets = {a: {s: 0 for s in self.speed_bands} for a in self.angle_bands}
      self._write_curvature()  # rewrite/create new file

  def _write_curvature(self):
    with open(self.curvature_file, 'w') as f:
      json.dump(self.learned_offsets, f)
    os.chmod(self.curvature_file, 0o777)
    self._last_write_time = sec_since_boot()
