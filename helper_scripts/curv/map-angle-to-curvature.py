import os
import json
import numpy as np
from selfdrive.config import Conversions as CV


os.chdir(os.getcwd())

data = []
for fi in os.listdir():
  if not fi.endswith('.py'):
    with open(fi) as f:
      for line in f.read().split('\n')[:-1]:
        line = line.replace('array([', '[').replace('])', ']')  # formats dpoly's np array
        line = line.replace("'", '"')  # for json
        try:
          data.append(json.loads(line))
        except:
          print('error: {}'.format(line))

min_angle = .1
center_max = 2.
inner_max = 5.
outer_max = float('inf')
TR = 1.8
data_banded = {'center': [], 'inner': [], 'outer': []}

for line in data:
  if line['v_ego'] < 15 * CV.MPH_TO_MS:
    continue
  angle_steers = line['angle_steers']
  if abs(angle_steers) >= min_angle:
    if abs(angle_steers) < 2:  # between +=[.1, 2)
      data_banded['center'].append(line)
      continue
    if abs(angle_steers) < 5.:  # between +=[2, 5)
      data_banded['inner'].append(line)
      continue
    data_banded['outer'].append(line)

avg_center_angle = np.mean([abs(line['angle_steers']) for line in data_banded['center']])
avg_inner_angle = np.mean([abs(line['angle_steers']) for line in data_banded['inner']])
avg_outer_angle = np.mean([abs(line['angle_steers']) for line in data_banded['outer']])
print('mean absolute center angle: {}'.format(avg_center_angle))
print('mean absolute inner angle: {}'.format(avg_inner_angle))
print('mean absolute outer angle: {}'.format(avg_outer_angle))

min_angle = {'center': 1.5, 'inner': 3.8, 'outer': 8}
avg_curvs = {'center': [], 'inner': [], 'outer': []}
for band in data_banded:
  for line in data_banded[band]:
    if abs(line['angle_steers']) > min_angle[band]:
      dist = line['v_ego'] * TR
      lat_pos = np.polyval(line['d_poly'], dist)  # lateral position in meters at 1.8 seconds
      avg_curvs[band].append(lat_pos)


avg_center_curv = np.max(np.abs(avg_curvs['center']))
avg_inner_curv = np.max(np.abs(avg_curvs['inner']))
avg_outer_curv = np.max(np.abs(avg_curvs['outer']))
print('mean absolute center curv: {}'.format(avg_center_curv))
print('mean absolute inner curv: {}'.format(avg_inner_curv))
print('mean absolute outer curv: {}'.format(avg_outer_curv))
