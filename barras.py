import matplotlib.pyplot as plt
import pandas as pd

valor=pd.read_csv('./pm02Abril2021.csv',sep='|',engine="python",encoding='utf-8',header=0)
df=pd.DataFrame(valor)
contador=df['RESULTADO']=='POSITIVO '
barra=contador.value_counts()
#positivo_negativo=df['RESULTADO'].dropna().drop_duplicates()
positivo_negativo=['negativo','positivo']
print(barra)
plt.bar(range(2),barra)
plt.xticks(range(2),positivo_negativo)
plt.show()