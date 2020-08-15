import os
import ast
import numpy as np
from scipy import interpolate
import scipy
import matplotlib.pyplot as plt

os.chdir('C:\Git')

data = []
with open('latcontrol_pid_data', 'r') as f:
  for line in f.read().split('\n'):
    if line != '':
      try:
        data.append(ast.literal_eval(line))
      except:
        print(line)
        raise Exception()
print(data[0])

derivative_samples = [line for line in data if line['derivative']][:-163000]
non_derivative_samples = [line for line in data if not line['derivative']][:-14686]
print('derivative samples: {}'.format(len(derivative_samples)))
print('non-derivative samples: {}'.format(len(non_derivative_samples)))

print('derivative MAE: {}'.format(np.mean([abs(line['angle_steers'] - line['angle_steers_des']) for line in derivative_samples])))
print('non-derivative MAE: {}'.format(np.mean([abs(line['angle_steers'] - line['angle_steers_des']) for line in non_derivative_samples])))

plt.figure(0)
plt.title('derivative')
plt.ylim(-55, 55)
plt.plot([line['angle_steers'] for line in derivative_samples], label='angle_steers')
plt.plot([line['angle_steers_des'] for line in derivative_samples], label='angle_steers_des')
plt.legend()

plt.figure(1)
plt.title('non derivative')
plt.ylim(-55, 55)
plt.plot([line['angle_steers'] for line in non_derivative_samples], label='angle_steers')
plt.plot([line['angle_steers_des'] for line in non_derivative_samples], label='angle_steers_des')
plt.legend()

# plt.figure(2)
# x = [17.88, 26.82]
# y = [.05, .085]
# i = scipy.interpolate.interp1d(x, y, fill_value='extrapolate')
# x.insert(0, 0)
# y.insert(0, i(3.5))
#
# x.append(35)
# y.append(.1)
#
# plt.plot(x, y)
# plt.xlim(0, 35)
# plt.ylim(0, .15)
# plt.show()
