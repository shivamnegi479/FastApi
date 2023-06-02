import psycopg2

conn = psycopg2.connect("dbname=fastapi user=postgres password=26547234s@S")
cur=conn.cursor()
cur.execute("""SELECT * FROM post where id=(%s)"""%(2))
all_post=cur.fetchone()
print(all_post)



