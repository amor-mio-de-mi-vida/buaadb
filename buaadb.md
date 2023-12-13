---
title: buaadb v1.0.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.17"

---

# buaadb

> v1.0.0

Base URLs:

# Authentication

# 通用功能

## POST 用户注册

POST /buaa_db/register/

> Body Parameters

```yaml
id: "21371477"
name: amor_mio_di_mi_vida
password: "666666"
password_again: "666666"
role: "0"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» id|body|string| yes |如果是学生的话要用学工号注册|
|» name|body|string| yes |用户的昵称|
|» password|body|string| yes |用户的密码|
|» password_again|body|string| yes |确认密码|
|» role|body|string| yes |0:学生 1:团队管理员 2:系统管理员|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|没有权限|Inline|
|402|[Payment Required](https://tools.ietf.org/html/rfc7231#section-6.5.2)|学工号重复|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|两次密码不一致|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|非POST请求|Inline|

### Responses Data Schema

## POST 登录

POST /buaa_db/login/

> Body Parameters

```yaml
id: "21371477"
password: "666666"
role: "0"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» id|body|string| no |学工号|
|» password|body|string| no |密码|
|» role|body|string| no |0:学生 1:团队管理员 2:系统管理员|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|
|300|[Multiple Choices](https://tools.ietf.org/html/rfc7231#section-6.4.1)|密码错误|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|未注册|Inline|

### Responses Data Schema

## POST 登出

POST /buaa_db/logout/

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 修改密码

POST /buaa_db/change_password/

> Body Parameters

```yaml
old_password: "666666"
new_password: "123456"
new_password_again: "123456"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» old_password|body|string| no |旧密码|
|» new_password|body|string| no |新密码|
|» new_password_again|body|string| no |确认新密码|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|两次密码不一致|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|旧密码错误|Inline|

### Responses Data Schema

## POST 获取个人信息

POST /buaa_db/get_personal_profile/

> Response Examples

> 200 Response

```json
{
  "username": "string",
  "name": "string",
  "real_name": "string",
  "phone_id": "string",
  "id_number": "string",
  "wx_id": "string",
  "faculty_id": "string",
  "image_id": "string",
  "role": "string"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» username|string|true|none|学工号/账号|none|
|» name|string|true|none|昵称|none|
|» real_name|string|true|none|真实姓名|none|
|» phone_id|string|true|none|电话号|none|
|» id_number|string|true|none|身份证号|none|
|» wx_id|string|true|none|微信号|none|
|» faculty_id|string|true|none|院系号|none|
|» image_id|string|true|none|头像id|none|
|» role|string|true|none|角色|0/1/2|

## POST 修改个人信息

POST /buaa_db/modify_personal_profile/

刚注册的时候如果是学生身份一定要让他修改个人信息，这个需要约束一下

> Body Parameters

```yaml
real_name: xxx
phone_id: "12312341234"
id_number: "12313412515135135"
wx_id: amor_mio_de_mi_vida
faculty_id: "6"
image: string

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» real_name|body|string| no |真实姓名|
|» phone_id|body|string| no |电话号|
|» id_number|body|string| no |身份证号|
|» wx_id|body|string| no |微信号|
|» faculty_id|body|string| no |学院号|
|» image|body|string(binary)| no |上传头像|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 获取所有团队

POST /buaa_db/get_teams/

返回的为团队id的list
（需要返回团队{id, name}的list

> Response Examples

> 200 Response

```json
{
  "teams": [
    {
      "id": "string",
      "name": "string"
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» teams|[object]|true|none||none|
|»» id|string|true|none||none|
|»» name|string|true|none||none|

## POST 获取团队信息

POST /buaa_db/get_team_profile/

> Body Parameters

```yaml
team_id: "2"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» team_id|body|string| no |团队的id|

> Response Examples

> 200 Response

```json
{
  "name": "string",
  "profile": "string",
  "image_id": "string",
  "image_url": "string",
  "image_post_time": "string",
  "projects": [
    {
      "name": "string",
      "id": "string"
    }
  ],
  "students": [
    {
      "name": "string",
      "id": "string"
    }
  ],
  "managers": [
    {
      "name": "string",
      "id": "string"
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» name|string|true|none||none|
|» profile|string|true|none||none|
|» image_id|string|true|none||none|
|» image_url|string|true|none||none|
|» image_post_time|string|true|none||none|
|» projects|[object]|true|none||none|
|»» name|string|true|none||none|
|»» id|string|true|none||none|
|» students|[object]|true|none||none|
|»» name|string|true|none||none|
|»» id|string|true|none||none|
|» managers|[object]|true|none||none|
|»» name|string|true|none||none|
|»» id|string|true|none||none|

## POST 获取项目

POST /buaa_db/get_project/

对于学生和团体管理员：可以看到自己团队内的所有项目和其他公开的项目
对于系统管理员可以看到所有项目

> Response Examples

> 200 Response

```json
{
  "projects": [
    {
      "id": "string",
      "name": "string",
      "time": "string"
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» projects|[object]|true|none||project_id 的list|
|»» id|string|true|none||none|
|»» name|string|true|none||none|
|»» time|string|true|none||none|

## POST 获取项目详情

POST /buaa_db/get_project_profile/

> Body Parameters

```yaml
project_id: "3"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» project_id|body|string| no |项目id|

> Response Examples

> 200 Response

```json
{
  "name": "string",
  "time": "string",
  "place": "string",
  "profile": "string",
  "state": "string",
  "quest_url": "string",
  "check": true,
  "private": true,
  "team_name": "string",
  "tags": [
    "string"
  ],
  "managers": [
    "string"
  ],
  "students": [
    "string"
  ],
  "role": "string"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» name|string|true|none|项目名称|none|
|» time|string|true|none|项目时间|none|
|» place|string|true|none|项目地点|none|
|» profile|string|true|none|项目简介|none|
|» state|string|true|none|项目状态|none|
|» quest_url|string|true|none|问卷链接|可以先不用管这个|
|» check|boolean|true|none|是否审核通过|none|
|» private|boolean|true|none|是否团体私有|none|
|» team_name|string|true|none|团体名称|若项目非公开的，则显示其所属的团体|
|» tags|[string]|true|none|标签list|none|
|» managers|[string]|true|none|manager_ID list|none|
|» students|[string]|true|none|student_id list|none|
|» role|string|true|none|当前用户角色|0/1/2|

## POST 获取他人信息

POST /buaa_db/get_other_profile/

> Body Parameters

```yaml
username: "21371476"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» username|body|string| no |他人的学工号|

> Response Examples

> 200 Response

```json
{
  "username": "string",
  "name": "string",
  "image_url": "string",
  "real_name": "string",
  "phone_id": "string",
  "id_number": "string",
  "wx_id": "string",
  "faculty_id": "string"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» username|string|true|none||none|
|» name|string|true|none||none|
|» image_url|string|true|none||none|
|» real_name|string|true|none||none|
|» phone_id|string|true|none||none|
|» id_number|string|true|none||none|
|» wx_id|string|true|none||none|
|» faculty_id|string|true|none||none|

# 通知相关功能

## POST 发布通知

POST /buaa_db/pub_notice/

团体管理员/系统管理员发布通知

> Body Parameters

```yaml
text: 这是一个通知
images: string
files: string
reciever: "21371476"
type: "2"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» text|body|string| no |通知文字内容|
|» images|body|string(binary)| no |图片|
|» files|body|string(binary)| no |文件|
|» reciever|body|string| no |接收方id（团队id或项目id或用户id）|
|» type|body|string| no |0: 团体内消息 1: 项目内消息 2: 某个用户的消息|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 删除通知

POST /buaa_db/delete_notice/

团体管理员/系统管理员删除通知

> Body Parameters

```yaml
notice_id: "1"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» notice_id|body|string| no |通知id|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 获取已发布的通知

POST /buaa_db/get_send_notice/

团体管理员/系统管理员获取自己发布的通知

> Response Examples

> 200 Response

```json
{
  "notices": [
    "string"
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» notices|[string]|true|none|notice_id的list|none|

## POST 获取接收到的通知列表

POST /buaa_db/get_receive_notice_list/

团体管理员/学生获取接收到的通知
//或者项目通知和团队通知可以分开

> Response Examples

> 200 Response

```json
{
  "senders": [
    {
      "name": "string",
      "id": "string",
      "type": "string"
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» senders|[object]|true|none||none|
|»» name|string|true|none|发送方名称|none|
|»» id|string|true|none|发送方id|none|
|»» type|string|true|none|发送方类别|0:团队 1:项目 2:系统管理员|

## POST 获取接收到的特定发送方的通知

POST /buaa_db/get_receive_notice/

> Body Parameters

```yaml
type: "2"
id: "1"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» type|body|string| no |type为0 代表|
|» id|body|string| no |none|

> Response Examples

> 200 Response

```json
{
  "notices": [
    {
      "text": "string",
      "time": "string"
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» notices|[object]|true|none||none|
|»» text|string|true|none||none|
|»» time|string|true|none||none|

# 团体相关功能

## POST 查看申请加入团队的学生

POST /buaa_db/get_in_team/

查看申请加入团队的学生/管理员，当前用户为系统管理员时返回申请加入团队的团体管理员，当前用户为团体管理员时返回申请加入团队的学生

> Body Parameters

```yaml
{}

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|

> Response Examples

> 200 Response

```json
{
  "applies": [
    {
      "student_id": "string",
      "student_name": "string",
      "project_id": "string",
      "project_name": "string"
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» applies|[object]|true|none||none|
|»» student_id|string|true|none||none|
|»» student_name|string|true|none||none|
|»» project_id|string|true|none||none|
|»» project_name|string|true|none||none|

## POST 团队管理员获取管理的团队

POST /buaa_db/get_manage_teams/

> Response Examples

> 200 Response

```json
{
  "teams": [
    {
      "id": "string",
      "name": "string"
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» teams|[object]|true|none||none|
|»» id|string|true|none||none|
|»» name|string|true|none||none|

## POST 查看申请退出团队的学生

POST /buaa_db/get_out_team/

列出管理的所有团队的退出申请

> Body Parameters

```yaml
{}

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|

> Response Examples

> 200 Response

```json
{
  "applies": [
    {
      "student_name": "string",
      "student_id": "string",
      "team_name": "string",
      "team_id": "string"
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» applies|[object]¦null|true|none||none|
|»» student_name|string|true|none||none|
|»» student_id|string|true|none||none|
|»» team_name|string|true|none||none|
|»» team_id|string|true|none||none|

## POST 审核申请团队信息

POST /buaa_db/check_team/

审核学生/团体管理员申请团队信息，审核后会自动给对应的学生/团体管理员发notice（存储到数据库中）
(申请加入和退出是同一个吗)

> Body Parameters

```yaml
receiver_id: "2"
team_id: "1"
result: 通过
reason: 申请的很好

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» receiver_id|body|string| no |none|
|» team_id|body|string| no |none|
|» result|body|string| no |none|
|» reason|body|string| no |none|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 申请加入团体

POST /buaa_db/apply_team_in/

> Body Parameters

```yaml
team_id: string

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» team_id|body|string| no |none|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 申请退出团体

POST /buaa_db/apply_team_out/

> Body Parameters

```yaml
team_id: ad

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» team_id|body|string| no |none|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 团队管理员创建团队

POST /buaa_db/man_create_team/

> Body Parameters

```yaml
name: 6系学生会
profile: 这是6系官方实践队
image: string

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» name|body|string| no |none|
|» profile|body|string| no |none|
|» image|body|string(binary)| no |none|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|团队名字重复|Inline|

### Responses Data Schema

## POST 团队管理员修改团队信息

POST /buaa_db/man_modify_team_profile/

> Body Parameters

```yaml
team_id: 2系学生会
profile: 这个是2系官方实践队
image: string

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» team_id|body|string| no |none|
|» profile|body|string| no |none|
|» image|body|string(binary)| no |none|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 获得团队中的管理者信息

POST /buaa_db/get_team_managers/

> Body Parameters

```yaml
team_id: "2"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» team_id|body|string| no |团队id|

> Response Examples

> 200 Response

```json
{
  "managers": "string"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» managers|string|true|none||manager_id 的 list|

## POST 获得团队中的项目信息

POST /buaa_db/get_team_projects/

> Body Parameters

```yaml
team_id: "2"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» team_id|body|string| no |团队的id|

> Response Examples

> 200 Response

```json
{
  "projects": [
    {
      "name": "string",
      "time": "string",
      "place": "string"
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» projects|[object]|false|none||none|
|»» name|string|true|none||none|
|»» time|string|true|none||none|
|»» place|string|true|none||none|

## POST 获得团队中的学生信息

POST /buaa_db/get_team_students/

> Body Parameters

```yaml
team_id: "4"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» team_id|body|string| no |团队id|

> Response Examples

> 200 Response

```json
{
  "students": [
    {
      "name": "string",
      "id": "string"
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» students|[object]|true|none||none|
|»» name|string|true|none|姓名|none|
|»» id|string|true|none|学工号|none|

# 项目相关功能

## POST 团队管理员获取管理的全部项目

POST /buaa_db/get_manage_projects/

> Response Examples

> 200 Response

```json
{
  "teams": [
    {
      "name": "string",
      "position": "string",
      "time": "string"
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» teams|[object]|true|none||none|
|»» name|string|true|none||none|
|»» position|string|true|none||none|
|»» time|string|true|none||none|

## POST 获取feedback的详细信息

POST /buaa_db/get_feedback_profile/

> Body Parameters

```yaml
feedback_id: "2"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» feedback_id|body|string| no |反馈id|

> Response Examples

> 200 Response

```json
{
  "student_id": "string",
  "project_id": "string",
  "profile": "string",
  "file_profile": [
    "string"
  ],
  "image_profile": [
    "string"
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» student_id|string|true|none||none|
|» project_id|string|true|none||none|
|» profile|string|true|none||none|
|» file_profile|[string]|true|none||none|
|» image_profile|[string]|true|none||none|

## POST 学生申请加入项目

POST /buaa_db/stu_apply_project_in/

> Body Parameters

```yaml
project_id: "4"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» project_id|body|string| no |项目id|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 学生申请退出项目

POST /buaa_db/stu_apply_project_out/

> Body Parameters

```yaml
project_id: "4"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» project_id|body|string| no |项目id|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 学生发布项目反馈

POST /buaa_db/stu_pub_feedback/

> Body Parameters

```yaml
project_id: "2"
profile: 这个是项目反馈
images: string
files: string

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» project_id|body|string| no |项目id|
|» profile|body|string| no |简介|
|» images|body|string(binary)| no |照片|
|» files|body|string(binary)| no |文档|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 学生获取已发布的项目反馈

POST /buaa_db/stu_get_feedback/

> Body Parameters

```yaml
project_id: "2"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» project_id|body|string| no |none|

> Response Examples

> 200 Response

```json
{
  "feedbacks": [
    "string"
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» feedbacks|[string]|true|none|feedback_id 的list|none|

## POST 学生删除反馈

POST /buaa_db/stu_delete_feedback/

> Body Parameters

```yaml
feedback_id: "3"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» feedback_id|body|string| no |none|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 团队管理员创建项目

POST /buaa_db/man_create_project/

> Body Parameters

```yaml
name: 这是一个项目
time: 项目从xxx点到xxx点
place: 项目在这个位置进行
profile: 这个是一个示例项目
private: "0"
team_id: "2"
tags: 公益志愿
quest_url: http://xxxxxxxx
images: string
files: string
state: "0"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» name|body|string| no |项目名称|
|» time|body|string| no |项目时间|
|» place|body|string| no |项目地点|
|» profile|body|string| no |项目简介|
|» private|body|integer| no |是否私有|
|» team_id|body|string| no |所属团队id|
|» tags|body|string| no |标签内容|
|» quest_url|body|string| no |问卷链接|
|» images|body|string(binary)| no |图片信息|
|» files|body|string(binary)| no |文件信息|
|» state|body|string| no |审核状态|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 团体管理员删除项目

POST /buaa_db/man_delete_project/

> Body Parameters

```yaml
project_id: "2"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» project_id|body|string| no |项目id|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 团队管理员获取申请加入项目的学生

POST /buaa_db/man_get_stu_in_project/

获取管理员管理的*全部项目*的加入申请

> Body Parameters

```yaml
{}

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|

> Response Examples

> 200 Response

```json
{
  "applies": [
    {
      "student_id": "string",
      "student_name": "string",
      "project_id": "string",
      "project_name": "string"
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» applies|[object]|true|none||none|
|»» student_id|string|true|none||none|
|»» student_name|string|true|none||none|
|»» project_id|string|true|none||none|
|»» project_name|string|true|none||none|

## POST 团队管理员获取申请退出项目的学生

POST /buaa_db/man_get_stu_out_project/

获取管理员管理的全部项目的退出申请

> Response Examples

> 200 Response

```json
{
  "applies": [
    {
      "student_id": "string",
      "student_name": "string",
      "project_id": "string",
      "project_name": "string"
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» applies|[object]|true|none||none|
|»» student_id|string|true|none||none|
|»» student_name|string|true|none||none|
|»» project_id|string|true|none||none|
|»» project_name|string|true|none||none|

## POST 团队管理员处理学生申请项目信息

POST /buaa_db/man_check_stu_project/

> Body Parameters

```yaml
receiver_id: "21371476"
project_id: "2"
result: 不通过
reason: 不通过

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» receiver_id|body|string| no |接收者id|
|» project_id|body|string| no |项目id|
|» result|body|string| no |结果|
|» reason|body|string| no |原因|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 团队管理员获取反馈

POST /buaa_db/man_get_project_feedback/

> Body Parameters

```yaml
project_id: "2"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» project_id|body|string| no |项目id|

> Response Examples

> 200 Response

```json
{
  "feedback": "string"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» feedback|string|true|none||只存在一个文件|

## POST 学生获取加入的团队

POST /buaa_db/stu_get_team/

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 学生获取加入的项目

POST /buaa_db/stu_get_project/

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

# 项目相关功能/讨论/评论相关功能 

## POST 发布评论

POST /buaa_db/pub_message/

> Body Parameters

```yaml
receiver_id: "21371476"
discussion_id: "22371476"
text: 这是一个回复
images: string
files: string

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» receiver_id|body|string| no |接收者的id|
|» discussion_id|body|string| no |讨论的id|
|» text|body|string| no |讨论的内容|
|» images|body|string(binary)| no |讨论的图片|
|» files|body|string(binary)| no |讨论的文件|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 创建讨论

POST /buaa_db/create_discussion/

学生/团体管理员创建讨论

> Body Parameters

```yaml
project_id: "2"
profile: 这是一个讨论
type: 提问
title: 这是标题

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» project_id|body|string| yes |none|
|» profile|body|string| yes |none|
|» type|body|string| yes |none|
|» title|body|string| yes |none|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 删除讨论

POST /buaa_db/delete_discussion/

> Body Parameters

```yaml
discussion_id: "2"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» discussion_id|body|string| no |讨论的id|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 获取讨论

POST /buaa_db/get_discussion/

学生/团体管理员获取项目中的discussion

> Body Parameters

```yaml
project_id: "1"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» project_id|body|string| yes |项目id|

> Response Examples

> 200 Response

```json
{
  "discussions": [
    {
      "id": "string",
      "student_id": "string",
      "student_name": "string",
      "time": "string",
      "text": "string"
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» discussions|[object]|true|none||none|
|»» id|string|true|none||none|
|»» student_id|string|true|none||none|
|»» student_name|string|true|none||none|
|»» time|string|true|none||none|
|»» text|string|true|none||none|

## POST 获取讨论下回复

POST /buaa_db/get_discussion_replies/

学生/团体管理员获取讨论的详情

> Body Parameters

```yaml
discussion_id: "2"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» discussion_id|body|string| yes |讨论id|

> Response Examples

> 200 Response

```json
{
  "replies": [
    {
      "student_name": "string",
      "student_id": "string",
      "time": "string",
      "text": "string"
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» replies|[object]|true|none||none|
|»» student_name|string|true|none||none|
|»» student_id|string|true|none||none|
|»» time|string|true|none||none|
|»» text|string|true|none||none|

## POST 删除评论

POST /buaa_db/delete_message/

> Body Parameters

```yaml
id: "2"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|id|query|string| no |message的id|
|body|body|object| no |none|
|» id|body|string| no |评论的id|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

# 系统管理员相关

## POST 系统管理员处理待审核团体

POST /buaa_db/admin_check_apply_team/

> Body Parameters

```yaml
team_id: "2"
result: 通过
reason: 通过

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» team_id|body|string| no |团队id|
|» result|body|string| no |结果|
|» reason|body|string| no |原因|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 系统管理员查看待审核团体

POST /buaa_db/admin_get_apply_team/

> Response Examples

> 200 Response

```json
{
  "teams": [
    {
      "name": "string",
      "id": "string",
      "time": "string"
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» teams|[object]|true|none||team_id的list|
|»» name|string|true|none|团体名|none|
|»» id|string|true|none|团体id|none|
|»» time|string|false|none|提交申请时间|none|

## POST 系统管理员查看待审核项目

POST /buaa_db/admin_get_apply_project/

> Response Examples

> 200 Response

```json
{
  "projects": [
    {
      "name": "string",
      "id": "string",
      "time_start": "string",
      "time_end": "string",
      "location": "string"
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» projects|[object]|true|none||project_id的array|
|»» name|string|true|none|项目名称|none|
|»» id|string|true|none|项目id|none|
|»» time_start|string|true|none||none|
|»» time_end|string|true|none||none|
|»» location|string|true|none||none|

## POST 系统管理员处理待审核项目

POST /buaa_db/admin_check_apply_project/

> Body Parameters

```yaml
project_id: "2"
result: 通过
reason: 通过审核

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» project_id|body|string| no |项目id|
|» result|body|string| no |结果|
|» reason|body|string| no |原因|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

# 新功能

## POST 团体管理员发布签到

POST /buaa_db/man_pub_sign/

> Body Parameters

```yaml
project_id: "2"
name: 第一次签到
latitude: "102"
longitude: "333"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» project_id|body|string| no |要发布签到的项目|
|» name|body|string| no |签到的名字|
|» latitude|body|string| no |经度|
|» longitude|body|string| no |纬度|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 团队管理员查看发布的签到列表

POST /buaa_db/man_get_signList/

> Body Parameters

```yaml
project_id: "2"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» project_id|body|string| no |项目id|

> Response Examples

> 200 Response

```json
{
  "sign_id": "string",
  "name": "string",
  "time": "string"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» sign_id|string|true|none||none|
|» name|string|true|none||none|
|» time|string|true|none||none|

## POST 团体管理员修改某次签到的状态

POST /buaa_db/man_modify_sign/

> Body Parameters

```yaml
sign_id: "2"
student_username: "21371476"
state: 已签到
message: 无

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» sign_id|body|string| no |签到id|
|» student_username|body|string| no |学生用户名|
|» state|body|string| no |签到状态|
|» message|body|string| no |备注|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 团体管理员查看签到的具体信息

POST /buaa_db/man_get_signprofile/

> Body Parameters

```yaml
sign_id: "2"
project_id: "3"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» sign_id|body|string| no |签到的id|
|» project_id|body|string| no |项目的id|

> Response Examples

> 200 Response

```json
{
  "student_username": "string",
  "student_name": "string",
  "state": "string",
  "message": "string"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» student_username|string|true|none||none|
|» student_name|string|true|none||none|
|» state|string|true|none||none|
|» message|string|true|none||none|

## POST 学生获取某个项目的签到列表

POST /buaa_db/stu_get_signlist/

> Body Parameters

```yaml
project_id: "2"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» project_id|body|string| no |项目的id|

> Response Examples

> 200 Response

```json
{
  "sign_id": "string",
  "sign_name": "string",
  "state": "string",
  "message": "string"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» sign_id|string|true|none||none|
|» sign_name|string|true|none||none|
|» state|string|true|none||none|
|» message|string|true|none||none|

## POST 学生签到

POST /buaa_db/stu_signin/

> Body Parameters

```yaml
sign_id: "3"
latitude: "103"
longitude: "45"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» sign_id|body|string| no |签到的id|
|» latitude|body|string| no |经度|
|» longitude|body|string| no |纬度|

> Response Examples

> 200 Response

```json
{}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

## POST 按照指定标签搜索项目

POST /buaa_db/search_project_tag/

> Body Parameters

```yaml
tag: 公益志愿

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» tag|body|string| no |tag的名字|

> Response Examples

> 200 Response

```json
{
  "project_id": "string"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» project_id|string|true|none||none|

## POST 生成项目内学生信息的表格

POST /buaa_db/gen_stu_profile_form/

> Body Parameters

```yaml
project_id: string

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» project_id|body|string| no |none|

> Response Examples

> 200 Response

```json
{
  "form_url": "string"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» form_url|string|true|none||none|

## POST 生成签到结果的表格

POST /buaa_db/gen_sign_result_form/

> Body Parameters

```yaml
sign_id: "2"

```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» sign_id|body|string| no |签到的id|

> Response Examples

> 200 Response

```json
{
  "form_url": "string"
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» form_url|string|true|none||none|

# Data Schema

<h2 id="tocS_StudentSign">StudentSign</h2>

<a id="schemastudentsign"></a>
<a id="schema_StudentSign"></a>
<a id="tocSstudentsign"></a>
<a id="tocsstudentsign"></a>

```python
{
class StudentSign(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, db_column='student_ID')
    sign = models.ForeignKey('Sign', on_delete=models.CASCADE, db_column='sign_ID')
    state = models.BooleanField(db_column='state', default=False)
    message = models.TextField(max_length=4096, db_column='message', default="未签到")

    class Meta:
        db_table = 'StudentSign'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|student|[Student](#schemastudent)|true|none|学生|none|
|sign|[Sign](#schemasign)|true|none|签到|none|
|state|boolean|true|none|签到状态|none|
|message|string|true|none|签到备注|none|

<h2 id="tocS_Sign">Sign</h2>

<a id="schemasign"></a>
<a id="schema_Sign"></a>
<a id="tocSsign"></a>
<a id="tocssign"></a>

```python
{
class Sign(models.Model):
    id = models.AutoField(primary_key=True, db_column='sign_ID')
    name = models.CharField(max_length=255, db_column='name')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, db_column='class_id')
    latitude = models.CharField(max_length=255, db_column='latitude')
    longitude = models.CharField(max_length=255, db_column='longitude')
    time = models.CharField(max_length=255, db_column='time')

    class Meta:
        db_table = 'Sign'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|id|string|true|none|签到id|none|
|name|string|true|none|签到名|none|
|project|[Project](#schemaproject)|true|none|签到所属项目|none|
|latitude|string|true|none|经度|none|
|longitude|string|true|none|纬度|none|
|time|string|true|none|发布时间|none|

<h2 id="tocS_AMessageB">AMessageB</h2>

<a id="schemaamessageb"></a>
<a id="schema_AMessageB"></a>
<a id="tocSamessageb"></a>
<a id="tocsamessageb"></a>

```python
{
class AMessageB(models.Model):
    sender_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Message_sender', on_delete=models.CASCADE,
                                  db_column='sender_id')
    receiver_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Message_receiver', on_delete=models.CASCADE,
                                    db_column='receiver_id')
    message_id = models.ForeignKey('Message', on_delete=models.CASCADE, db_column='message_id')

    class Meta:
        db_table = 'A_message_B'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|sender_id|[User](#schemauser)|true|none|回复发送者|none|
|receiver_id|[User](#schemauser)|true|none|回复发送者|none|
|message_id|[Message](#schemamessage)|true|none|回复|none|

<h2 id="tocS_ANoticeB">ANoticeB</h2>

<a id="schemaanoticeb"></a>
<a id="schema_ANoticeB"></a>
<a id="tocSanoticeb"></a>
<a id="tocsanoticeb"></a>

```python
{
class ANoticeB(models.Model):
    sender_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Notice_sender', on_delete=models.CASCADE,
                                  db_column='sender_id')
    receiver_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Notice_receiver', on_delete=models.CASCADE,
                                    db_column='receiver_id')
    notice_id = models.ForeignKey('Notice', on_delete=models.CASCADE, db_column='notice_id')

    class Meta:
        db_table = 'A_notice_B'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|sender_id|[User](#schemauser)|true|none|回复发送者|none|
|receiver_id|[User](#schemauser)|true|none|回复发送者|none|
|notice_id|[Notice](#schemanotice)|true|none|消息|none|

<h2 id="tocS_ProjectManager">ProjectManager</h2>

<a id="schemaprojectmanager"></a>
<a id="schema_ProjectManager"></a>
<a id="tocSprojectmanager"></a>
<a id="tocsprojectmanager"></a>

```python
{
class ProjectManager(models.Model):
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE, db_column='project_id')
    manager_id = models.ForeignKey('Manager', on_delete=models.CASCADE, db_column='manager_id')

    class Meta:
        db_table = 'project_manager'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|project_id|[Project](#schemaproject)|true|none|签到所属项目|none|
|manager_id|[Manager](#schemamanager)|true|none|团队管理员|none|

<h2 id="tocS_TeamNotice">TeamNotice</h2>

<a id="schemateamnotice"></a>
<a id="schema_TeamNotice"></a>
<a id="tocSteamnotice"></a>
<a id="tocsteamnotice"></a>

```python
{
class TeamNotice(models.Model):
    team_id = models.ForeignKey('Team', on_delete=models.CASCADE, db_column='team_id')
    notice_id = models.ForeignKey('Notice', on_delete=models.CASCADE, db_column='notice_id')

    class Meta:
        db_table = 'team_notice'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|team_id|[Team](#schemateam)|true|none|团队|none|
|notice_id|[Notice](#schemanotice)|true|none|消息|none|

<h2 id="tocS_ProjectNotice">ProjectNotice</h2>

<a id="schemaprojectnotice"></a>
<a id="schema_ProjectNotice"></a>
<a id="tocSprojectnotice"></a>
<a id="tocsprojectnotice"></a>

```python
{
class ProjectNotice(models.Model):
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE, db_column='project_id')
    notice_id = models.ForeignKey('Notice', on_delete=models.CASCADE, db_column='notice_id')

    class Meta:
        db_table = 'project_notice'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|project_id|[Project](#schemaproject)|true|none|签到所属项目|none|
|notice_id|[Notice](#schemanotice)|true|none|消息|none|

<h2 id="tocS_ProjectTag">ProjectTag</h2>

<a id="schemaprojecttag"></a>
<a id="schema_ProjectTag"></a>
<a id="tocSprojecttag"></a>
<a id="tocsprojecttag"></a>

```python
{
class ProjectTag(models.Model):
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE, db_column='project_id')
    tag_name = models.CharField(max_length=1024, db_column='tag_name')

    class Meta:
        db_table = 'project_tag'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|project_id|[Project](#schemaproject)|true|none|签到所属项目|none|
|tag_name|string|true|none|标签名|none|

<h2 id="tocS_ProjectStudent">ProjectStudent</h2>

<a id="schemaprojectstudent"></a>
<a id="schema_ProjectStudent"></a>
<a id="tocSprojectstudent"></a>
<a id="tocsprojectstudent"></a>

```python
{
class ProjectStudent(models.Model):
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE, db_column='project_id')
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE, db_column='student_id')

    class Meta:
        db_table = 'project_student'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|project_id|[Project](#schemaproject)|true|none|签到所属项目|none|
|student_id|[Student](#schemastudent)|true|none|学生|none|

<h2 id="tocS_ManApplyTeam">ManApplyTeam</h2>

<a id="schemamanapplyteam"></a>
<a id="schema_ManApplyTeam"></a>
<a id="tocSmanapplyteam"></a>
<a id="tocsmanapplyteam"></a>

```python
{
class ManApplyTeam(models.Model):
    team_id = models.ForeignKey('Team', on_delete=models.CASCADE, db_column='team_id')
    manager_id = models.ForeignKey('Manager', on_delete=models.CASCADE, db_column='manager_id')
    status = models.BooleanField(db_column='status', default=False)  # 0代表申请加入, 1代表申请退出

    class Meta:
        db_table = 'manager_apply_team'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|team_id|[Team](#schemateam)|true|none|团队|none|
|manager_id|[Manager](#schemamanager)|true|none|团队管理员|none|
|status|boolean|true|none|加入/退出状态|none|

<h2 id="tocS_StuApplyProject">StuApplyProject</h2>

<a id="schemastuapplyproject"></a>
<a id="schema_StuApplyProject"></a>
<a id="tocSstuapplyproject"></a>
<a id="tocsstuapplyproject"></a>

```python
{
 class StuApplyProject(models.Model):
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE, db_column='project_id')
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE, db_column='student_id')
    status = models.BooleanField(db_column='status', default=False)  # 0代表申请加入, 1代表申请退出

    class Meta:
        db_table = 'student_apply_project'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|project_id|[Project](#schemaproject)|true|none|签到所属项目|none|
|student_id|[Student](#schemastudent)|true|none|学生|none|
|status|boolean|true|none|加入/退出状态|none|

<h2 id="tocS_StuApplyTeam">StuApplyTeam</h2>

<a id="schemastuapplyteam"></a>
<a id="schema_StuApplyTeam"></a>
<a id="tocSstuapplyteam"></a>
<a id="tocsstuapplyteam"></a>

```python
{
class StuApplyTeam(models.Model):
    team_id = models.ForeignKey('Team', on_delete=models.CASCADE, db_column='team_id')
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE, db_column='student_id')
    status = models.BooleanField(max_length=128, db_column='status', default=False)  # 0代表申请加入, 1代表申请退出

    class Meta:
        db_table = 'student_apply_team'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|team_id|[Team](#schemateam)|true|none|团队|none|
|student_id|[Student](#schemastudent)|true|none|学生|none|
|status|boolean|true|none|加入/退出状态|none|

<h2 id="tocS_TeamProject">TeamProject</h2>

<a id="schemateamproject"></a>
<a id="schema_TeamProject"></a>
<a id="tocSteamproject"></a>
<a id="tocsteamproject"></a>

```python
{
class TeamProject(models.Model):
    team_id = models.ForeignKey('Team', on_delete=models.CASCADE, db_column='team_id')
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE, db_column='project_id')

    class Meta:
        db_table = 'team_project'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|team_id|[Team](#schemateam)|true|none|团队|none|
|project_id|[Project](#schemaproject)|true|none|签到所属项目|none|

<h2 id="tocS_TeamManager">TeamManager</h2>

<a id="schemateammanager"></a>
<a id="schema_TeamManager"></a>
<a id="tocSteammanager"></a>
<a id="tocsteammanager"></a>

```python
{
class TeamManager(models.Model):
    team_id = models.ForeignKey('Team', on_delete=models.CASCADE, db_column='team_id')
    manager_id = models.ForeignKey('Manager', on_delete=models.CASCADE, db_column='manager_id')

    class Meta:
        db_table = 'team_manager'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|team_id|[Team](#schemateam)|true|none|团队|none|
|manager_id|[Manager](#schemamanager)|true|none|团队管理员|none|

<h2 id="tocS_TeamStudent">TeamStudent</h2>

<a id="schemateamstudent"></a>
<a id="schema_TeamStudent"></a>
<a id="tocSteamstudent"></a>
<a id="tocsteamstudent"></a>

```python
{
class TeamStudent(models.Model):
    team_id = models.ForeignKey('Team', on_delete=models.CASCADE, db_column='team_id')
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE, db_column='student_id')

    class Meta:
        db_table = 'team_student'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|team_id|[Team](#schemateam)|true|none|团队|none|
|student_id|[Student](#schemastudent)|true|none|学生|none|

<h2 id="tocS_FeedbackFile">FeedbackFile</h2>

<a id="schemafeedbackfile"></a>
<a id="schema_FeedbackFile"></a>
<a id="tocSfeedbackfile"></a>
<a id="tocsfeedbackfile"></a>

```python
{
  class FeedbackFile(models.Model):
    feedback_id = models.ForeignKey('Feedback', on_delete=models.CASCADE, db_column='feedback_id')
    file_id = models.ForeignKey('File', on_delete=models.CASCADE, db_column='file_id')
    post_time = models.CharField(max_length=1024, db_column='post_time')

    class Meta:
        db_table = 'feedback_file'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|feedback_id|[Feedback](#schemafeedback)|true|none|反馈|none|
|file_id|[File](#schemafile)|true|none|文件|none|
|post_time|string|true|none|发布时间|none|

<h2 id="tocS_FeedbackImage">FeedbackImage</h2>

<a id="schemafeedbackimage"></a>
<a id="schema_FeedbackImage"></a>
<a id="tocSfeedbackimage"></a>
<a id="tocsfeedbackimage"></a>

```python
{
 class FeedbackImage(models.Model):
    feedback_id = models.ForeignKey('Feedback', on_delete=models.CASCADE, db_column='feedback_id')
    image_id = models.ForeignKey('Image', on_delete=models.CASCADE, db_column='image_id')
    post_time = models.CharField(max_length=1024, db_column='post_time')

    class Meta:
        db_table = 'feedback_image'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|feedback_id|[Feedback](#schemafeedback)|false|none|反馈|none|
|image_id|[Image](#schemaimage)|true|none|图片|none|
|post_time|string|true|none|发布时间|none|

<h2 id="tocS_Feedback">Feedback</h2>

<a id="schemafeedback"></a>
<a id="schema_Feedback"></a>
<a id="tocSfeedback"></a>
<a id="tocsfeedback"></a>

```python
{
class Feedback(models.Model):
    ID = models.AutoField(primary_key=True, db_column='feedback_id')
    profile = models.CharField(max_length=1024, db_column='profile')
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE, db_column='student_id')
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE, db_column='project_id')

    def __str__(self):
        return self.ID

    class Meta:
        db_table = 'feedback'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|ID|string|true|none|反馈id|none|
|profile|string|true|none|反馈简介|none|
|student_id|[Student](#schemastudent)|true|none|学生|none|
|project_id|[Project](#schemaproject)|true|none|签到所属项目|none|

<h2 id="tocS_FileMessage">FileMessage</h2>

<a id="schemafilemessage"></a>
<a id="schema_FileMessage"></a>
<a id="tocSfilemessage"></a>
<a id="tocsfilemessage"></a>

```python
{
class FileMessage(models.Model):
    file_id = models.ForeignKey("File", on_delete=models.CASCADE, db_column="file_id")
    message_id = models.ForeignKey("Message", on_delete=models.CASCADE, db_column="message_id")

    class Meta:
        db_table = "file_message"
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|file_id|[File](#schemafile)|true|none|文件|none|
|message_id|[Message](#schemamessage)|true|none|回复|none|

<h2 id="tocS_FileNotice">FileNotice</h2>

<a id="schemafilenotice"></a>
<a id="schema_FileNotice"></a>
<a id="tocSfilenotice"></a>
<a id="tocsfilenotice"></a>

```python
{
class FileNotice(models.Model):
    file_id = models.ForeignKey("File", on_delete=models.CASCADE, db_column="file_id")
    notice_id = models.ForeignKey("Notice", on_delete=models.CASCADE, db_column="notice_id")

    class Meta:
        db_table = "file_notice"
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|file_id|[File](#schemafile)|true|none|文件|none|
|notice_id|[Notice](#schemanotice)|true|none|消息|none|

<h2 id="tocS_FileProject">FileProject</h2>

<a id="schemafileproject"></a>
<a id="schema_FileProject"></a>
<a id="tocSfileproject"></a>
<a id="tocsfileproject"></a>

```python
{
class FileProject(models.Model):
    file_id = models.ForeignKey("File", on_delete=models.CASCADE, db_column="file_id")
    project_id = models.ForeignKey("Project", on_delete=models.CASCADE, db_column="project_id")

    class Meta:
        db_table = "file_project"
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|file_id|[File](#schemafile)|true|none|文件|none|
|project_id|[Project](#schemaproject)|true|none|签到所属项目|none|

<h2 id="tocS_FileUser">FileUser</h2>

<a id="schemafileuser"></a>
<a id="schema_FileUser"></a>
<a id="tocSfileuser"></a>
<a id="tocsfileuser"></a>

```python
{
class FileUser(models.Model):
    file_id = models.ForeignKey("File", on_delete=models.CASCADE, db_column="file_id")
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="user_id")

    class Meta:
        db_table = "file_user"
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|file_id|[File](#schemafile)|true|none|文件|none|
|user_id|[User](#schemauser)|true|none|回复发送者|none|

<h2 id="tocS_File">File</h2>

<a id="schemafile"></a>
<a id="schema_File"></a>
<a id="tocSfile"></a>
<a id="tocsfile"></a>

```python
{
class File(models.Model):
    ID = models.AutoField(primary_key=True, db_column='file_id')
    url = models.TextField(max_length=4096, db_column='url')
    post_time = models.CharField(max_length=1024, db_column='post_time')

    def __str__(self):
        return self.ID

    class Meta:
        db_table = 'file'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|ID|string|true|none|文件id|none|
|url|string|true|none|文件地址|none|
|post_time|string|true|none|文件发布时间|none|

<h2 id="tocS_ImageMessage">ImageMessage</h2>

<a id="schemaimagemessage"></a>
<a id="schema_ImageMessage"></a>
<a id="tocSimagemessage"></a>
<a id="tocsimagemessage"></a>

```python
{
class ImageMessage(models.Model):
    image_id = models.ForeignKey("Image", on_delete=models.CASCADE, db_column="image_id")
    message_id = models.ForeignKey("Message", on_delete=models.CASCADE, db_column="message_id")

    class Meta:
        db_table = "image_message"
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|image_id|[Image](#schemaimage)|true|none|图片|none|
|message_id|[Message](#schemamessage)|true|none|回复|none|

<h2 id="tocS_ImageNotice">ImageNotice</h2>

<a id="schemaimagenotice"></a>
<a id="schema_ImageNotice"></a>
<a id="tocSimagenotice"></a>
<a id="tocsimagenotice"></a>

```python
{
class ImageNotice(models.Model):
    image_id = models.ForeignKey("Image", on_delete=models.CASCADE, db_column="image_id")
    notice_id = models.ForeignKey("Notice", on_delete=models.CASCADE, db_column="notice_id")

    class Meta:
        db_table = "image_notice"
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|image_id|[Image](#schemaimage)|true|none|图片|none|
|notice_id|[Notice](#schemanotice)|true|none|消息|none|

<h2 id="tocS_ImageProject">ImageProject</h2>

<a id="schemaimageproject"></a>
<a id="schema_ImageProject"></a>
<a id="tocSimageproject"></a>
<a id="tocsimageproject"></a>

```python
{
class ImageProject(models.Model):
    image_id = models.ForeignKey("Image", on_delete=models.CASCADE, db_column="image_id")
    project_id = models.ForeignKey("Project", on_delete=models.CASCADE, db_column="project_id")

    class Meta:
        db_table = "image_project"
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|image_id|[Image](#schemaimage)|false|none|图片|none|
|project_id|[Project](#schemaproject)|true|none|签到所属项目|none|

<h2 id="tocS_Image">Image</h2>

<a id="schemaimage"></a>
<a id="schema_Image"></a>
<a id="tocSimage"></a>
<a id="tocsimage"></a>

```python
{
class Image(models.Model):
    ID = models.AutoField(primary_key=True, db_column='image_id')
    url = models.TextField(max_length=4096, db_column='url')
    post_time = models.CharField(max_length=1024, db_column='post_time')

    def __str__(self):
        return self.ID

    class Meta:
        db_table = "image"
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|ID|string|true|none|图片id|none|
|url|string|true|none|图片地址|none|
|post_time|string|true|none|图片发布时间|none|

<h2 id="tocS_DiscussionMessage">DiscussionMessage</h2>

<a id="schemadiscussionmessage"></a>
<a id="schema_DiscussionMessage"></a>
<a id="tocSdiscussionmessage"></a>
<a id="tocsdiscussionmessage"></a>

```python
{
class DiscussionMessage(models.Model):
    discussion_id = models.ForeignKey('Discussion', on_delete=models.CASCADE, db_column='discussion_id')
    message_id = models.ForeignKey('Message', on_delete=models.CASCADE, db_column='message_id')

    class Meta:
        db_table = 'discussion_message'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|discussion_id|[Discussion](#schemadiscussion)|true|none|讨论|none|
|message_id|[Message](#schemamessage)|true|none|回复|none|

<h2 id="tocS_Message">Message</h2>

<a id="schemamessage"></a>
<a id="schema_Message"></a>
<a id="tocSmessage"></a>
<a id="tocsmessage"></a>

```python
{
class Message(models.Model):
    ID = models.AutoField(primary_key=True, db_column='message_id')
    post_time = models.CharField(max_length=1024, db_column='post_time')
    text = models.CharField(max_length=1024, db_column='text')

    def __str__(self):
        return self.ID

    class Meta:
        db_table = 'message'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|ID|string|true|none|回复id|none|
|post_time|string|true|none|回复发布时间|none|
|text|string|true|none|回复内容|none|

<h2 id="tocS_DiscussionProject">DiscussionProject</h2>

<a id="schemadiscussionproject"></a>
<a id="schema_DiscussionProject"></a>
<a id="tocSdiscussionproject"></a>
<a id="tocsdiscussionproject"></a>

```python
{
class DiscussionProject(models.Model):
    discussion_id = models.ForeignKey('Discussion', on_delete=models.CASCADE, db_column='discussion_id')
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE, db_column='project_id')

    class Meta:
        db_table = 'discussion_project'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|discussion_id|[Discussion](#schemadiscussion)|true|none|讨论|none|
|project_id|[Project](#schemaproject)|true|none|签到所属项目|none|

<h2 id="tocS_Discussion">Discussion</h2>

<a id="schemadiscussion"></a>
<a id="schema_Discussion"></a>
<a id="tocSdiscussion"></a>
<a id="tocsdiscussion"></a>

```python
{
class Discussion(models.Model):
    ID = models.AutoField(primary_key=True, db_column='discussion_id')
    time = models.CharField(max_length=1024, db_column='time')
    type = models.CharField(max_length=1024, db_column='type')
    title = models.CharField(max_length=1024, db_column='title')
    profile = models.TextField(max_length=1024, db_column='profile')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='author')

    def __str__(self):
        return self.ID

    class Meta:
        db_table = 'discussion'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|ID|string|true|none|讨论id|none|
|type|string|true|none|讨论类型|none|
|time|string|true|none|发起讨论的时间|none|
|title|string|true|none|讨论标题|none|
|profile|string|true|none|讨论简介|none|
|author|string|true|none|讨论发布者|none|

<h2 id="tocS_Notice">Notice</h2>

<a id="schemanotice"></a>
<a id="schema_Notice"></a>
<a id="tocSnotice"></a>
<a id="tocsnotice"></a>

```python
{
class Notice(models.Model):
    ID = models.AutoField(primary_key=True, db_column='notice_id')
    time = models.CharField(max_length=1024, db_column='time')
    type = models.CharField(max_length=1024, db_column='type')
    profile = models.TextField(max_length=4096, db_column='profile')

    def __str__(self):
        return self.ID

    class Meta:
        db_table = 'notice'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|ID|string|true|none|通知id|none|
|time|string|true|none|通知发布时间|none|
|type|string|true|none|通知类型|none|
|profile|string|true|none|通知内容简介|none|

<h2 id="tocS_Team">Team</h2>

<a id="schemateam"></a>
<a id="schema_Team"></a>
<a id="tocSteam"></a>
<a id="tocsteam"></a>

```python
{
class Team(models.Model):
    ID = models.AutoField(primary_key=True, db_column='team_id')
    name = models.CharField(max_length=128, db_column='name')
    profile = models.TextField(max_length=4096, db_column='profile')
    submit_time = models.CharField(max_length=128, db_column='submit_time')  # 提交申请队伍的时间
    image_id = models.CharField(max_length=1024, db_column="image_id")
    isCheck = models.BooleanField(db_column='isCheck', default=True)  # 是否在审核中

    def __str__(self):
        return self.ID

    class Meta:
        db_table = 'team'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|ID|string|true|none|团队id|none|
|name|string|true|none|团队姓名|none|
|profile|string|true|none|团队简介|none|
|submit_time|string|true|none|申请团队时间|none|
|image_id|string|true|none|团队头像id|none|
|isCheck|boolean|true|none|是否通过审核|none|

<h2 id="tocS_Project">Project</h2>

<a id="schemaproject"></a>
<a id="schema_Project"></a>
<a id="tocSproject"></a>
<a id="tocsproject"></a>

```python
{
class Project(models.Model):
    ID = models.AutoField(primary_key=True, db_column='project_id')
    name = models.CharField(max_length=128, db_column='name')
    time = models.CharField(max_length=128, db_column='time')
    place = models.CharField(max_length=128, db_column='place')
    profile = models.TextField(max_length=4096, db_column='profile')
    state = models.CharField(max_length=128, db_column='state')
    quest_url = models.CharField(max_length=1024, db_column='quest_url')
    private = models.BooleanField(db_column='private', default=False)  # 是否团体内私有
    isCheck = models.BooleanField(db_column='isCheck', default=True)  # 是否在审核中

    def __str__(self):
        return self.ID

    class Meta:
        db_table = 'project'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|ID|string|true|none|id|none|
|name|string|true|none|项目名|none|
|time|string|true|none|项目时间（开始-结束）|none|
|place|string|true|none|项目地点|none|
|profile|string|true|none|项目简介|none|
|state|boolean|true|none|项目状态|none|
|quest_url|string|true|none|问卷url|none|
|private|boolean|true|none|是否团队私有|none|
|isCheck|boolean|true|none|是否通过审核|none|

<h2 id="tocS_Adminstrator">Adminstrator</h2>

<a id="schemaadminstrator"></a>
<a id="schema_Adminstrator"></a>
<a id="tocSadminstrator"></a>
<a id="tocsadminstrator"></a>

```python
{
class Adminstrator(User):
    image_id = models.CharField(max_length=128, db_column='image_id')  # 头像信息

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'adminstrator'
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|username|string|true|none|学工号|none|
|password|string|true|none|密码|none|
|first_name|string|true|none|昵称|none|
|image_id|string|true|none|头像id|none|

<h2 id="tocS_Manager">Manager</h2>

<a id="schemamanager"></a>
<a id="schema_Manager"></a>
<a id="tocSmanager"></a>
<a id="tocsmanager"></a>

```python
{
class Manager(User):
    image_id = models.CharField(max_length=128, db_column='image_id')  # 头像信息

    def __str__(self):
        return self.username
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|username|string|true|none|学工号|none|
|password|string|true|none|密码|none|
|first_name|string|true|none|昵称|none|
|image_id|string|true|none|头像id|none|

<h2 id="tocS_Student">Student</h2>

<a id="schemastudent"></a>
<a id="schema_Student"></a>
<a id="tocSstudent"></a>
<a id="tocsstudent"></a>

```python
class Student(User):
    real_name = models.CharField(max_length=128, db_column='real_name')  # 真实姓名
    phone_id = models.CharField(max_length=128, db_column='phone_id')  # 电话号码
    id_number = models.CharField(max_length=128, db_column='id_number')  # 身份证号
    wx_id = models.CharField(max_length=128, db_column='wx_id')  # 微信号
    faculty_id = models.CharField(max_length=128, db_column='faculty_id')  # 学院系号
    image_id = models.CharField(max_length=128, db_column='image_id')  # 头像信息

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'student'

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|username|string|true|none|用户名|none|
|password|string|true|none|密码|none|
|first_name|string|true|none|昵称|none|
|real_name|string|true|none|真实姓名|none|
|phone_id|string|true|none|电话号码|none|
|id_number|string|true|none|身份证号|none|
|wx_id|string|true|none|微信号|none|
|faculty_id|string|true|none|学院号|none|
|image_id|string|true|none|头像id|none|

<h2 id="tocS_User">User</h2>

<a id="schemauser"></a>
<a id="schema_User"></a>
<a id="tocSuser"></a>
<a id="tocsuser"></a>

```json
{
  "username": "string",
  "password": "string",
  "first_name": "string"
}

```

### Attribute

|Name|Type|Required|Restrictions|Title|Description|
|---|---|---|---|---|---|
|username|string|true|none|学工号|none|
|password|string|true|none|密码|none|
|first_name|string|true|none|昵称|none|
