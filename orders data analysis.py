
#!pip install kaggle
import kaggle

!kaggle datasets download ankitbansal06/retail-orders -f orders.csv


import zipfile
zip_ref = zipfile.ZipFile('orders.csv.zip') 
zip_ref.extractall() 
zip_ref.close() 




#read data from the file and handle null values
import pandas as pd
df = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
df['Ship Mode'].unique()


df.rename(columns={'Order Id':'order_id', 'City':'city'})
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df.head(5)



df['discount']=df['list_price']*df['discount_percent']*.01
df['sale_price']= df['list_price']-df['discount']
df['profit']=df['sale_price']-df['cost_price']
df


# In[162]:


#convert order date from object data type to datetime
df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")




#drop cost price list price and discount percent columns
df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)




#load the data into sql server using replace option
import sqlalchemy as sal
engine = sal.create_engine('mssql://ANKIT\SQLEXPRESS/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()



df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')


