# -*- coding:utf-8 -*-
"""
cmd:    python programs/
import: 
input:  
output: 
description: 
"""

import os.path
import sqlite

class SQLiteManager:
	def __init__(self, dbpath):
		"""
		コンストラクタ。
		@param string dbpath SQLiteのDBファイルのパス
		"""
		self.__con = sqlite.connect(dbpath)
		self.__cur = self.__con.cursor()
	def __del__(self):
		"""
		デストラクタ。
		"""
		self.close()
	def close(self):
		"""
		データベースを解除する。
		"""
		self.__cur.close()
		self.__con.close()
	def getInsertId(self):
		pass #実装予定
	def query(self, sql):
		"""
		クエリを実行する。読み込み専用。
		@param string sql SQL文
		"""
		self.__cur.execute(sql)
		return self.__cur
	def queryF(self, sql):
		"""
		クエリを実行する。DBへの書き込みが可能。
		@param string sql SQL文
		"""
		self.__cur.execute(sql)
		self.__con.commit()
			
		



# D.S.G.