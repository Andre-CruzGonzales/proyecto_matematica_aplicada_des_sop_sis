import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

datos=pd.read_csv('data.csv')
x=datos['year']
y=datos['cases']
z=datos['deaths']

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.scatter3D(x,y,z,c=z,cmap='Set1')
plt.show()