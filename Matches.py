# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 20:46:01 2021

@author: Nishant
"""

import sqlite3

database = 'C:\\sqlite\\test.db'

conn=sqlite3.connect(database)

c=conn.cursor()

c.execute("select distinct a.title,c.averagerating,c.numvotes from bbc_schedule a,title_basics b,title_ratings c where lower(a.title)=lower(b.primarytitle) and b.tconst=c.tconst")

print(c.fetchall())

conn.commit()

conn.close()