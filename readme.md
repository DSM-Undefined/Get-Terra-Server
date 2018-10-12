# 동아리경진대회 서버구축관련내용 협의안건(공통사항)

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
		- resource
			- Login.py
			- TeamInfo.py
			- NewTeamInfo.py
			- Question.py
			- NewUserInfo.py
			- connect.py
		- runserver.py
	- LICENSE
	- readme.md
	- .gitignore
```

## API 명세

API에 대한 자세한 내용은 다음과 같다.

| HTTP 메소드 |            이름            |       URI       |
| :---------: | :------------------------: | :-------------: |
|    POST     |           로그인           |   /api/login    |
|    POST     |        팀 정보 얻기        | /api/team-info  |
|     PUT     |      팀 정보 수정하기      | /api/team-Ninfo |
|     GET     | 문제 불러오기(유형은 랜덤) |  /api/question  |
|     PUT     |     개인정보 수정하기      | /api/user-Ninfo |

### /api/login

|       required        |   Response    |              비고               |
| :-------------------: | :-----------: | :-----------------------------: |
|   userID, password    | JWT(미정)_205 |    ID, PW 로 가입 유저 확인     |
| userName, email, team |  SUCCESS_205  |            회원가입             |
|                       |      405      |          로그인 실패시          |
|                       |      405      | 회원가입 실패시(아이디 중복 등) |

### /api/team-info

| required  |  response   |   비고    |
| :-------: | :---------: | :-------: |
| teamName  | SUCCESS_205 | 점수 확인 |
| groupName | SUCCESS_205 | 설명 확인 |
|           | FAILURE_405 | 오류 발생 |

### /api/team-Ninfo

| Required | response | 비고 |
| :------: | :------: | :--: |
| teamName |          |      |
|          |          |      |
|          |          |      |



### /api/question

### /api/user-Ninfo

## 논의 안건

- DB 서비스 제공자 이용 여부
  - mlab 등의 서비스를 이용할 것인지 Docker로 Mongo를 구동할 것인지 결정해야
- 