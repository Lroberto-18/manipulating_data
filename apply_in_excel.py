import pandas as pd
import numpy as np
#Carregando o arquivo 
df = pd.read_excel("UF-Data.xlsx", sheet_name = "DB")

#criando os vetores com os dados
City = []
UF = []
for i in range(df.shape[0]): 
  UF.append(df.at[i,list(df.columns)[0]])#comparar 
  City.append(df.at[i,list(df.columns)[1]])

#Criar data frame de saída
out = {'ID': np.arange(1,len(UF))}
df_out = pd.DataFrame(out)
df_out.drop('ID', axis=1, inplace=True)#removendo a coluna ID
UF_columns = set(UF) #remover repetidos
for i in range(len(UF_columns)):
  df_out.insert(0, list(UF_columns)[i],'') #Inserir novas colunas
df_out.sort_index(axis=1, inplace=True) #ordenar colunas
display(df_out)

#distribuir os dados
for x in range(df_out.shape[1]): #percorrer colunas
  z=0
  for y in range(df_out.shape[0]): #percorrer linhas
    control=True
    while(control and z<len(UF)):
      if(UF[z]==list(df_out.columns)[x]): #comparar Estado com o index da coluna
        #atribuir Cidade na linha e na coluna de seu Estado
        df_out.at[y,list(df_out.columns)[x]] = City[z]
        control=False
      z+=1
#remover linhas em branco      
for y in range(df_out.shape[0]):
  control=0
  for x in range(df_out.shape[1]):
    if(df_out.at[y,list(df_out.columns)[x]]==""):
      control+=1
  if(control==df_out.shape[1]):
    df_out.drop(y, inplace=True)

#exportando o arquivo
df_out.to_excel("dados.xlsx", index=False)