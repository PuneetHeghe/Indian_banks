import sqlite3
import pandas as pd
from sqlalchemy import create_engine

d = pd.read_csv('bank_branches.csv')
 
engine = create_engine ('sqlite://',echo=False)
d.to_sql('myBank',engine)

def ifsc_get(ifsc_code):
	conn = sqlite3.connect('myBank.db')
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM myBank where ifsc=?;", (ifsc_code,) )
	branch = cursor.fetchall()
	conn.commit()
	return branch

def branch_city_get(bank_name,city):
	conn = sqlite3.connect('myBank.db')
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM myBank where bank_name=? and city=?;", (bank_name,city,) )
	branches = cursor.fetchall()
	conn.commit()
	return branches