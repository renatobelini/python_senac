import sqlite3
db = sqlite3.connect("senac.db")
cursor = db.cursor()
cursor.execute("""
CREATE TABLE verbos (
verbo_d integer primary key autoincrement,
usuario varchar(20) not null,
verbo varchar(50) not null,
qtd integer )
""")

db.commit()
