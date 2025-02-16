# Database practice with JS and Python

## sqlite
sqlite는 다른 mySQL, postgreSQL과는 다르게 os 자체에 미리 설치가 되어 있고, 파일 기반으로 동작하기에 프로세스를 돌릴 필요가 없다.<br />
즉, server를 `brew services start {프로세스명}`의 명령어를 적용할 필요가 없다는 것이다. 그냥 파이썬의 드라이버를 이용해서 connection을 만들고 트랜잭션을 실행하면 된다. 다만, commit이 이루어져야 트랜잭션 내용이 적용된다.

### sql injection
파이썬의 f를 이용한 문자열 보간을 통해서 쿼라를 진행하면 해커의 악의적인 sql 인젝션 공격에 취약할 수 있다. sqlite의 경우에는 이럴 때 문자열 자체에 `?`를 이용하여 변수를 잡아주면 데이터베이스 엔진이 자체적으로 sql 인젝션 공격을 막아준다.

### insert many data
`?` 나 `:` 를 이용하고 `executemany()` 함수를 이용하여 삽입

### query data
데이터베이스에는 cursor라는 개념이 있다. `fetchall()`함수를 실행하더라도 커서 다음의 모든 것들을 가져오는 것이고, `fetchmany(20)`이라고 하면 커서 오른쪽의 20개 튜플을 가져오고 그 다음에는 커서를 그만큼 옮기는 것이다.


## postgreSQL
`psycopg2` 라는 db connector를 통해서 파이썬 프로그램에서 접속한다. 기존의 sqlite에서는 데이터 바인딩을 ? 연산자로 해주었지만 postgreSQL에서는 `%s`로 진행함.

``` python
cursor.execute("SELECT * FROM users WHERE id = %s", (user_input,))
```

## mySQL
mySQL은 db connector로 `mysql-connector`를 이용한다. 쿼리의 데이터 바인딩은 postgreSQL과 마찬 가지로 `%s`를 이용한다.

``` python
cursor.execute("SELECT * FROM users WHERE id = %s", (user_input,))
```

객체의 필드를 각각 알맞게 이어주고 싶은 경우에는 다음과 같은 코드로 구현한다.
``` python
import psycopg2

# 데이터베이스 연결
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="password",
    database="test_db"
)
cursor = conn.cursor()

# 예제 객체
class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

user = User(2, "jane_doe", "jane@example.com")

# 딕셔너리 바인딩
query = "INSERT INTO users (id, username, email) VALUES (%(user_id)s, %(username)s, %(email)s);"
cursor.execute(query, vars(user))  # 객체를 딕셔너리로 변환하여 실행
conn.commit()

print("User inserted successfully")

cursor.close()
conn.close()
```