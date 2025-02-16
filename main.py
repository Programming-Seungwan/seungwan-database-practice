import sqlite3

conn = sqlite3.connect("users.db")

cur = conn.cursor() # 데이터베이스를 읽고, 쓰는 데 도와주는 인터페이스임

def init_table():
  cur.execute("""
  create table users(
  user_id integer primary key autoincrement,
  username text not null,
  password text not null
  );""")

  cur.execute("""
  insert into users (username, password) values("seungwan", "1234"), ("sik", "4567");
""") # 이것만으로는 트랜잭션이 저장된 상태가 아님. commit까지 이루어져야 함

def print_all_users():
  res = cur.execute("select * from users") # cursor 타입을 반환하는 함수
  data = res.fetchall() # 전부 다 가져오기
  print(data)

init_table()

conn.commit()

print_all_users()

conn.close()