import pandas as pd
import matplotlib.pyplot as plt
import itertools
import seaborn as sns

markers = itertools.cycle(('.', '+', 's', 'o', '*', 'v', 'H', 'D'))
palette = itertools.cycle(sns.color_palette())

data = pd.read_csv('../RESU/coil.dat',delim_whitespace=True,header=None)

names_file = open('../RESU/coil.dat.names')
data.columns = [line.split('res: ')[1].replace('\n','') for line in names_file.readlines() if 'res:' in line]

print (data)
plt.plot(data['time'], data['i_component(1)'], color = next(palette), marker = next(markers), label='Coil 1')
plt.plot(data['time'], data['i_component(2)'], color = next(palette), marker = next(markers), label='Coil 2')
plt.plot(data['time'], data['i_component(3)'], color = next(palette), marker = next(markers), label='Coil 3')
plt.plot(data['time'], data['i_is1'], color = next(palette), label='Source 1')
plt.plot(data['time'], data['i_is2'], color = next(palette), label='Source 2')
plt.legend()
plt.savefig('../Figures/ramp.png')
