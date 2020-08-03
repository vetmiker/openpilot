import os
import json
from common.numpy_fast import clip
from common.realtime import sec_since_boot
from selfdrive.config import Conversions as CV


# by Zorrobyte
# version 4
# modified by ShaneSmiskol to add speed and curve direction as learning factors
# version 5 due to json incompatibilities


class CurvatureLearner:  # todo: disable when dynamic camera offset is working
  def __init__(self):
    self.curvature_file = '/data/curvature_offsets.json'
    rate = 1 / 20.  # pathplanner is 20 hz
    self.learning_rate = 2.6e-3 * rate  # equivalent to x/12000
    self.write_frequency = 60 * 2  # in seconds
    self.min_lr_prob = .75

    self.directions = ['left', 'right']
    self.speed_bands = ['slow', 'medium', 'fast']
    self.angle_bands = ['center', 'inner', 'outer']
    self._load_curvature()

  def update(self, angle_steers, d_poly, lane_probs, v_ego):
    offset = 0
    lr_prob = lane_probs[0] + lane_probs[1] - lane_probs[0] * lane_probs[1]
    angle_band, direction = self.pick_angle_band(angle_steers)

    if angle_band is not None:  # don't learn/return an offset if not in a band
      speed_band = self.pick_speed_band(v_ego)  # will never be none
      if lr_prob >= self.min_lr_prob:  # only learn when lane lines are present; still use existing offset
        learning_sign = 1 if angle_steers >= 0 else -1
        self.learned_offsets[direction][speed_band][angle_band] -= d_poly[3] * self.learning_rate * learning_sign  # the learning
      offset = self.learned_offsets[direction][speed_band][angle_band]

    if sec_since_boot() - self._last_write_time >= self.write_frequency:
      self._write_curvature()
    return clip(offset, -0.35, 0.35)

  def pick_speed_band(self, v_ego):
    if v_ego <= 35 * CV.MPH_TO_MS:
      return 'slow'
    if v_ego <= 55 * CV.MPH_TO_MS:
      return 'medium'
    return 'fast'

  def pick_angle_band(self, angle_steers):
    direction = 'left' if angle_steers > 0 else 'right'
    if abs(angle_steers) >= 0.1:
      if abs(angle_steers) < 2:  # between +=[.1, 2)
        return 'center', direction
      if abs(angle_steers) < 5.:  # between +=[2, 5)
        return 'inner', direction
      return 'outer', direction  # between +=[5, inf)
    return None, direction  # return none when below +-0.1, removes possibility of returning offset in this case

  def _load_curvature(self):
    self._last_write_time = 0
    try:
      with open(self.curvature_file, 'r') as f:
        self.learned_offsets = json.load(f)
    except:  # can't read file or doesn't exist
      self.learned_offsets = {d: {s: {a: 0 for a in self.angle_bands} for s in self.speed_bands} for d in self.directions}
      self._write_curvature()  # rewrite/create new file

  def _write_curvature(self):
    with open(self.curvature_file, 'w') as f:
      f.write(json.dumps(self.learned_offsets, indent=2))
    os.chmod(self.curvature_file, 0o777)
    self._last_write_time = sec_since_boot()
