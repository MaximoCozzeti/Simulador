import numpy as np

import matplotlib.pyplot as plt

#Mi primera chamba
x = [6,7,8,9,10,11]
y = [87,88,89,90,91,92]

fig=plt.figure(figsize=(4,3),dpi=300)
plt.plot(x,y,'--go')

plt.title('Mi primer plot',fontweight='bold')

plt.xlabel('Abcisas')
plt.ylabel('Ordenadas')
plt.grid(axis='both')


fig.savefig('Primer plot.png',dpi=300)
