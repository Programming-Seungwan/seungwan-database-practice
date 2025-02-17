import redis
import sqlite3
import json

rdsConn= redis.Redis(host="localhost", port=6379, decode_responses=True)

rdsConn.set("hello", "world")

print(rdsConn.get("hello"))

sltConn = sqlite3.connect("movies.db")
cur = sltConn.cursor()

def make_expensive_query():
  redis_key = "director:movies"
  cashed_results = rdsConn.get(redis_key)

  if cashed_results:
    print('cache hit')
    return json.loads(cashed_results)
  else:
    print("cache miss")
    res = cur.execute("select count(*), director from movies group by director;") # 파이썬 객체를 문자열로 변환
    all_rows = res.fetchall()
    rdsConn.set(redis_key, json.dumps(all_rows), ex=20) # 그냥 쿼리한 것은 파이썬 튜플로 저장되므로 쿤자열로 바꿔줄 필요가 있음. json 객체를 사용
    return all_rows


v = make_expensive_query()

sltConn.commit()
sltConn.close()
rdsConn.close()