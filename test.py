# -*- coding:utf-8 -*-
"""
cmd:    python test.py
import: 
input:  
output: 
description: 
"""

from SQLiteManager import SQLiteManager
sqlm = SQLiteManager("test.sqlite")
#sqlm.queryF("CREATE TABLE test(id INT NOT NULL PRIMARY KEY, url TEXT NOT NULL);")
#sqlm.queryF("CREATE TABLE test(id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT NOT NULL);")
#sqlm.queryF("INSERT INTO test(url) VALUES('http://www.google.co.jp/');")
#sqlm.queryF("INSERT INTO test(url) VALUES('http://www.yahoo.co.jp/');")
res = sqlm.query("SELECT * FROM test")
for row in res:
	print row["id"], row[1]



# D.S.G.