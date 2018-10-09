# 동아리경진대회 서버구축관련내용 협의안건(공통)

본 문서의 세부 사항은 다음과 같습니다.

|   항목    |                    내용                    |
| :-------: | :----------------------------------------: |
| 설계 목적 |                 대회 출전                  |
| 구축 환경 | Flask, MongoDB, AWS, Docker, Swagger(미정) |
|  참여자   |               인상민, 김재훈               |

## DB 설계

Collection **UserInfo**

```json
{
    "userID": "string",
    "userName": "string",
    "password": "string",
    "email": "string",
}
```

Collection **Questions**

```json
{
    "quizNum": "string",
    "question": "string",
    "answer": "string",
    "GTRAP": [					// Got The Right Answer People
        {
            "userID": "string",
            "date": "string"
        }
    ]
}
```

~~주석은 참고용으로만 사용할 것(운용시 주석 삭제 권고)~~

Collection **Teams**

```json
{
    "teamName": "string",
    "totalPoint": "string",
    "players": [
        {
            "userID": "string"
        }
    ]
}
```

