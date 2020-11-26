import sqlite3 

bd = sqlite3.connect("Pacman.sqlite")

cur = bd.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS RECORDS(
	score INTEGER
)""")

def insert_result(score):
	cur.execute("""
		INSERT INTO RECORDS VALUES (?)
	""", (score,))
	bd.commit()

def get_best():
	cur.execute("""
	SELECT max(score) Score FROM RECORDS
	order by score DESC
	LIMIT 1
	""")
	return cur.fetchall()
