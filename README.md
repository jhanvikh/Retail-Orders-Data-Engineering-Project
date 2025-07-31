# 🛒 Retail Orders ETL & Analytics Pipeline  

## 📌 Project Overview  
This project demonstrates an **end-to-end Data Engineering workflow** using **Python, Pandas, SQLAlchemy, and SQL Server** to analyze retail orders data.  

It covers the complete **ETL (Extract, Transform, Load)** process along with **advanced SQL analytics**, showcasing practical skills for a **Data Engineering role**.  

---

## 🔑 Key Features  
- **Extract:** Automated dataset download from Kaggle API.  
- **Transform:**  
  - Data cleaning (handling nulls, renaming columns).  
  - Derived metrics like `discount`, `sale_price`, and `profit`.  
  - Converted dates to proper datetime format.  
- **Load:** Inserted cleaned data into **SQL Server** using `SQLAlchemy`.  
- **Analyze:** Performed **SQL analytics** with complex queries, including CTEs and window functions.  

---

## 🛠 Tech Stack  
- **Languages:** Python (Pandas, SQLAlchemy)  
- **Database:** SQL Server  
- **Tools:** Kaggle API, Jupyter Notebook  
- **SQL Concepts Used:**    
  - Window functions (`ROW_NUMBER()`)  
  - Aggregations (SUM, GROUP BY)  
  - Date-based analytics (`YEAR`, `MONTH`, `FORMAT`)  

---

## 📂 ETL Workflow  
1. **Extract:**  
   - Used Kaggle API to download `orders.csv` from [Ankit Bansal’s Retail Orders dataset](https://www.kaggle.com/datasets/ankitbansal06/retail-orders).  
   
2. **Transform:**  
   ```python
   df = pd.read_csv('orders.csv', na_values=['Not Available', 'unknown'])
   df['profit'] = df['sale_price'] - df['cost_price']
   df['order_date'] = pd.to_datetime(df['order_date'], format="%Y-%m-%d")
   df.drop(columns=['list_price', 'cost_price', 'discount_percent'], inplace=True)

3. **Load**
   ```python
   import sqlalchemy as sal
    engine = sal.create_engine('mssql://SERVER_NAME/DB_NAME?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
    df.to_sql('df_orders', con=engine, index=False, if_exists='append')
