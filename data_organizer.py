import pandas as pd
import numpy as np

data_rooms = ['Sala 01','Sala 02', 'Sala 03', 
              'Sala 01','Sala 02', 'Sala 03', 
              'Sala 01','Sala 02', 'Sala 03', 
              'Sala 04','Sala 01']
data_names = ['Carlos Vinicius','Maria Santos','Marta Coelho','Ricardo Nobre',
              'Julho Almeida','Breno Aguiar','Alex Menezes','Manuela Mendes', 
              'Jefferson Cardoso','Marcos Silva', 'Roberto Nunes']
df_in = {'Rooms':data_rooms, 'Team':data_names}
d_outIn = pd.DataFrame(df_in)
display(d_outIn)
ids = np.arange(1,len(data_rooms))
#contruir data Frame
df = {'ID':ids}
dataFrame = pd.DataFrame(df)
w1 = set(data_rooms) #remover repetidos
for i in range(len(w1)):
  dataFrame.insert(0, list(w1)[i],'')
  
dataFrame.drop('ID',axis=1, inplace=True) #remover coluna id
#distribuir os dados
for x in range(dataFrame.shape[1]):
  z=0
  for y in range(dataFrame.shape[0]):
    control=True
    while(control and z<len(data_rooms)):
      if(data_rooms[z]==list(dataFrame.columns)[x]):
        dataFrame.at[y,list(dataFrame.columns)[x]] = data_names[z]
        control=False
      z+=1
#remover linhas em branco      
for y in range(dataFrame.shape[0]):
  control=0
  for x in range(dataFrame.shape[1]):
    if(dataFrame.at[y,list(dataFrame.columns)[x]]==""):
      control+=1
  if(control==4):
    dataFrame.drop(y, inplace=True)
display(dataFrame)