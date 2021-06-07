import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('RESU/coil_energization.dat',delim_whitespace=True,header=None)

names_file = open('RESU/coil_energization.dat.names')
data.columns = [line.split('res: ')[1].replace('\n','') for line in names_file.readlines() if 'res:' in line]

print (data)
plt.plot(data['time'], data['i_component(3)'], label='Coil 3')
plt.plot(data['time'], data['i_component(4)'], label='Coil 4')
plt.plot(data['time'], data['i_d2'], label='Dump Resistor')
#plt.plot(data['time'], data['i_s2'], label='Source')
plt.legend()
plt.savefig('Figures/ramp_coils.png')
plt.show()
