#csv and json files with pandas 

import pandas as pd

books=pd.read_csv('./bestsellers-with-categories.csv', sep=',', header=0, names=[])
books=pd.read_json('./bestsellers-with-categories.csv', sep=',', header=0, names=[])

#Series y Data Frames

import pandas as pd

pd.Series(
    ['Juan', 'David', 'Juanelo', 'Pepe'],
    index=[1,7,10,30]
    )

pd.Series(
    ['Juan', 'David', 'Juanelo', 'Pepe']
    )

dict={1:'Juan', 7:'David', 10:'Juanelo', 30:'Pepe'}
pd.Series(dict)

dict2={'Jugador': ['Juan', 'David', 'Juanelo', 'Pepe'],
 'Altura': [183,176,220,221],
 'Goles': [2,20,22,25]
 }

players=pd.DataFrame(dict2,index=[1,7,10,30])
players.columns
players.index

#Filtering with LOC ILOC

import pandas as pd
books=pd.read_csv('./bestsellers-with-categories.csv', sep=',', header=0)
databooks=pd.DataFrame(books)
databooks
databooks['Name','Author','Year']
databooks.loc[:]
databooks.loc[0:4, ['Name','Author']]
databooks.loc[0:4, ['Reviews']]*-1
databooks.loc[:, ['Author']] == 'JJ Smith'
databooks.iloc[:]
databooks.iloc[:,0:3]
databooks.iloc[1,3]
databooks.iloc[:2,:3]

#Deleting and adding data with panda
import pandas as pd
import numpy as np
books=pd.read_csv('./bestsellers-with-categories.csv', sep=',', header=0)
databooks=pd.DataFrame(books)
databooks.drop('Genre', axis=1).head(2) #It is deleted from the output. Axis 1 = columns 
databooks.drop('Genre', axis=1, inplace=True) #It deletes it from the input 
databooks.drop('Genre', axis=0).head(2) #Axis 0 = columns 
databooks.drop([0,10], axis=0).head(2) #Deletes first 10 rows (0 to 9)
databooks['Nueva columna']=np.nan
databooks.shape[0] #Counting how many registers there are in the column
data = np.arange(0,databooks.shape[0]) #Creating a range from 0 to the count of registers in the column
data
databooks['Rango'] = data #Asisgning the count to the column Rango
databooks

#Managing empty values
import pandas as pd
import numpy as np
dict = {'Col1':[1,2,3,np.nan],
        'Col2':[4,np.nan,6,7],
        'Col 3':['a','b','c', None]
        }
df = pd.DataFrame(dict)
df.isnull()
df.isnull()*1
df.fillna('Missing')
df.fillna(df.mean())
df.interpolate()
df.dropna()

#Filter per conditions
import pandas as pd
import numpy as np
books=pd.read_csv('./bestsellers-with-categories.csv', sep=',', header=0)
databooks=pd.DataFrame(books)
over2016=databooks['Year'] > 2016 #Books with release year after 2016
databooks[over2016]#Books with release year after 2016
databooks[~over2016]#Books with release year before 2016
genre_fiction = databooks['Genre'] == 'Fiction'
databooks[over2016&genre_fiction] 

#Pandas principal functions
import pandas as pd
import numpy as np
books=pd.read_csv('./bestsellers-with-categories.csv', sep=',', header=0)
databooks=pd.DataFrame(books)
databooks.info() #Datatypes and no Null count
databooks.describe() #General statistics arond the data
databooks.tail(2) #last two registers
databooks.head(2) #first two registers
databooks.memory_usage(deep=True) #How much memory I am using in my dataframe
databooks['Author'].value_counts() #Count of values grouped by the column name
databooks.iloc[0] #Viewing dataset[[index0]]
databooks = databooks.append(databooks.iloc[0]) #Adding a duplicate value to the dataset from index 0
databooks.drop_duplicates()
databooks.sort_values('Year', ascending = True) #Sort data per column by ascending or descending

#Group By with Pandas

import pandas as pd
import numpy as np
books=pd.read_csv('./bestsellers-with-categories.csv', sep=',', header=0)
databooks=pd.DataFrame(books)
databooks.groupby('Author').count() #Different operations grouping by authors
databooks.groupby('Author').max()
databooks.groupby('Author').min()
databooks.groupby('Author').sum()
databooks.groupby('Author').sum().loc['William Davis'] #Lookfor information only for William Davis
databooks.groupby('Author').sum().reset_index() #Reset the index of what you have worked with the dataset
databooks.groupby('Author').agg(['min','max'])
databooks.groupby('Author').agg({'Reviews':['min','max'],'User Rating':'sum'})
databooks.groupby(['Author','Year']).count()

#Combingin Dataframes(Merge, Concats, Joins, Pivot, Melt, Apply)
import pandas as pd
import numpy as np
books=pd.read_csv('./bestsellers-with-categories.csv', sep=',', header=0)
databooks=pd.DataFrame(books)

#Merge and Concat 
import pandas as pd
import numpy as np

df1 =  pd.DataFrame({
'A': ['A0', 'A1', 'A2', 'A3'],
'B': ['B0', 'B1', 'B2', 'B3'],
'C':['C0','C1','C2','C3'],
'D':['D0','D1','D2','D3']
})

df2 = pd.DataFrame({
'A':['A4', 'A5', 'A6', 'A7'],
'B':['B4', 'B5', 'B6', 'B7'],
'C':['C4', 'C5', 'C6', 'C7'],
'D':['D4', 'D5', 'D6', 'D7']    
})

pd.concat([df1,df2]) #It appends  two dataframes. Does not ignore the indexes
pd.concat([df1,df2], ignore_index=True) #It appends  two dataframes. Ignore the indexes
pd.concat([df1,df2], axis=0) #Appends row level
pd.concat([df1,df2], axis=1) #Appends column level

izq = pd.DataFrame({
'Key': ['key0','key1', 'key2', 'key3'],
'A': ['A0', 'A1', 'A2', 'A3'],
'B': ['B0', 'B1', 'B2', 'B3']
})

der = pd.DataFrame({
'Key': ['key0', 'key1', 'key2', 'key3'],
'C':['C0','C1','C2','C3'],
'D':['D0','D1','D2','D3']
})

izq
der

izq.merge(der) #Merges from key column. It detects automatically the Foreign key 
izq.merge(der, on='Key') #If you don't want to trust the automatic FK detection you can write this 
izq.merge(der, left_on='Key1', right_on='Key2') #If you have the FK with different names this is a way to specify it
izq.merge(der, left_on='Key1', right_on='Key2', how='inner') #It relates the type of join you want to make

#Join
izq1=pd.DataFrame({
'A': ['A0', 'A1', 'A2'],
'B': ['B0', 'B1', 'B2']},
index=['k0','k1','k2']
)

der1=pd.DataFrame({
'C':['C0','C1','C2'],
'D':['D0','D1','D2']},
index=['k0','k2','k3']
)

izq1.join(der1)
izq1.join(der1, how='inner')
izq1.join(der1, how='outer')
izq1.join(der1, how='left')
izq1.join(der1, how='right')

#Pivot and Melt
import pandas as pd
import numpy as np
books=pd.read_csv('./bestsellers-with-categories.csv', sep=',', header=0)
databooks=pd.DataFrame(books)
databooks.pivot_table(index = 'Author', columns = 'Genre', values = 'User Rating')
databooks[['Name','Genre']].head(5)
databooks[['Name','Genre']].head(5).melt()
databooks.melt(id_vars='Year',value_vars='Genre')

#Apply 

def two_times(value):
    return value *2 

databooks['Rating_2']=databooks['User Rating'].apply(two_times)
databooks

databooks['Rating_2']=databooks['User Rating'].apply(lambda x: x*3)
databooks.head()

databooks.apply (lambda x: x['Uer Rating'] * 2 if x['Genre'] == 'Fiction' else x['User Rating'], axis=1)
databooks