import sqlite3

conn = sqlite3.connect("movies.db")

cur = conn.cursor() # 데이터베이스를 읽고, 쓰는 데 도와주는 인터페이스임

res = cur.execute("select movie_id, title from movies order by movie_id")

for movies in res:
  print(movies)


conn.commit()
conn.close()