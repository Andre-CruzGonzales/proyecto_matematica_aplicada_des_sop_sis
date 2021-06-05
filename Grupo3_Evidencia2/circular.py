import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.frame import DataFrame


valor=pd.read_csv('./pm02Abril2021.csv',sep='|',engine="python",encoding='utf-8',header=0)
df=DataFrame(valor)
in_positivo=df['RESULTADO']=='POSITIVO '
edad_positivo=df[in_positivo]
edad=edad_positivo['edadpaciente_c']
labels=edad.dropna().drop_duplicates()
sizes=edad.value_counts(dropna=True)
print(sizes)
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title("GRAFICA DE CASOS POSITIVOS POR EDAD")    
plt.show()
