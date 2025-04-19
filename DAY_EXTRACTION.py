import pandas as pd;

data = pd.read_csv('dataset.csv')

#pd.options.display.max_rows=10


#contailns null values or notM=data.isnull().sum() to check if the dATA  

#print(M)

data['Date']= pd.to_datetime(data['Date'])

#data['Time'] = pd.to_datetime(data['Time'], format='%H:%M').dt.time


#data['Day']= ''



data['Day'] = data['Date'].dt.day_name()


data['Day']=pd.to_datetime(data['Date'], dayfirst=True).dt.day_name()
data['Date'] = pd.to_datetime(data['Date'], dayfirst=False, errors='coerce')
data.to_csv('dataset.csv' , index=False)
print(data.head())

print(data.describe())

print(data.groupby('Day')['Total'].mean())

print(data.groupby('Customer type')['Total'].mean())



#nt(data.columns)

#data['Day'] = data['Date'].dt.day

#for date in data['Date']:
 
  #print(date)

#for index, row  in data.iterrows():
    
   # print(row)




    