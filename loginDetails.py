import sqlite3
import pandas as pd
import os
from pandas import DataFrame

conn=sqlite3.connect('login.db')
c=conn.cursor()
cwd=os.getcwd()
c.execute('''CREATE TABLE PROGRESS([USERNAME] text PRIMARY KEY,[TASK] int,FOREIGN KEY(USERNAME) REFERENCES DETAILS(USERNAME))''')
read_details=pd.read_csv(str(cwd) + '\progress.csv')
read_details.to_sql('PROGRESS',conn,if_exists='append',index=False)