# 동아리경진대회 서버구축관련내용 협의안건(공통)

본 문서의 세부 사항은 다음과 같습니다.

|   항목    |                      내용                      |
| :-------: | :--------------------------------------------: |
| 설계 목적 |                   대회 출전                    |
| 구축 환경 | Flask, MongoDB, AWS, Docker, ~~Swagger(미정)~~ |
|  참여자   |                 인상민, 김재훈                 |

## DB 설계

Collection **UserInfo**(유저 정보)

```json
{
    "userID": "string",
    "userName": "string",
    "password": "string",
    "email": "string",
    "team": "string"
}
```

Collection **OXQuestions**(OX 퀴즈 문항)

```json
{
    "question": "string",
    "currectAns": "string"
}
```

Collection **4wayQuestions**(4지선다 문항)

```json
{
    "question": "string",
    "firstAnswer": "string",
    "secondAnswer": "string",
    "thirdAnswer": "string",
    "fourthAnswer": "string",
    "currectAns": "integer"
}
```

Collection **SubjectiveQuestions**(주관식 문항)

```json
{
    "question": "string",
    "answer": "string",
}
```

Collection **Teams**(팀 정보)

```json
{
    "teamName": "string",
    "totalPoint": "string"
}
```

Collection **GroupInfo**(그룹 정보)

```json
{
    "groupName": "string",
    "introduction": "string"
}
```

## 파일 구조

```
Get-Terra-Server
	- terra-flask
		- refact
			- login.py
			- connect.py
		- runserver.py
	- LICENSE
	- readme.md
```

## 논의 안건

- DB 서비스 제공자 이용 여부
  - mlab 등의 서비스를 이용할 것인지 Docker로 Mongo를 구동할 것인지 결정해야
- 