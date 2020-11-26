import sqlite3 

bd = sqlite3.connect("Pacman.sqlite")

cur = bd.cursor()
cur.execute("""
create table if not exists RECORDS(
	score integer
)""")

def insert_result(score):
	cur.execute("""
		insert into RECORDS values (?)
	""", (score),)
	bd.commit()

def get_best():
	cur.execute("""
	SELECT max(score) Score FROM RECORDS
	order by score DESC
	LIMIT 1
	""")
	return cur.fetchall()

print(get_best())

