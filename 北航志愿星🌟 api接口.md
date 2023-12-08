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

> Body 请求参数

```yaml
id: "21371477"
name: amor_mio_di_mi_vida
password: "666666"
password_again: "666666"
role: "0"

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» id|body|string| 是 |none|
|» name|body|string| 是 |none|
|» password|body|string| 是 |none|
|» password_again|body|string| 是 |none|
|» role|body|string| 是 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|没有权限|Inline|
|402|[Payment Required](https://tools.ietf.org/html/rfc7231#section-6.5.2)|学工号重复|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|两次密码不一致|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|非POST请求|Inline|

### 返回数据结构

## POST 登录

POST /buaa_db/login/

> Body 请求参数

```yaml
id: "21371477"
password: "666666"
role: "0"

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» id|body|string| 否 |none|
|» password|body|string| 否 |none|
|» role|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|
|300|[Multiple Choices](https://tools.ietf.org/html/rfc7231#section-6.4.1)|密码错误|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|未注册|Inline|

### 返回数据结构

## POST 登出

POST /buaa_db/logout/

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 修改密码

POST /buaa_db/change_password/

> Body 请求参数

```yaml
old_password: string
new_password: string
new_password_again: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» old_password|body|string| 否 |none|
|» new_password|body|string| 否 |none|
|» new_password_again|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|两次密码不一致|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|旧密码错误|Inline|

### 返回数据结构

## POST 获取个人信息

POST /buaa_db/get_personal_profile/

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
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

> Body 请求参数

```yaml
real_name: string
phone_id: string
id_number: string
wx_id: string
faculty_id: string
image: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» real_name|body|string| 否 |none|
|» phone_id|body|string| 否 |none|
|» id_number|body|string| 否 |none|
|» wx_id|body|string| 否 |none|
|» faculty_id|body|string| 否 |none|
|» image|body|string(binary)| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 获取所有团队

POST /buaa_db/get_teams/

返回的为团队id的list
（需要返回团队{id, name}的list

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» teams|[object]|true|none||none|
|»» id|string|true|none||none|
|»» name|string|true|none||none|

## POST 获取团队信息

POST /buaa_db/get_team_profile/

> Body 请求参数

```yaml
team_id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» team_id|body|string| 否 |none|

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
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

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» projects|[object]|true|none||project_id 的list|
|»» id|string|true|none||none|
|»» name|string|true|none||none|
|»» time|string|true|none||none|

## POST 获取项目详情

POST /buaa_db/get_project_profile/

> Body 请求参数

```yaml
project_id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» project_id|body|string| 否 |none|

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
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

> Body 请求参数

```yaml
username: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» username|body|string| 否 |none|

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
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

> Body 请求参数

```yaml
text: string
images: string
files: string
reciever: string
type: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» text|body|string| 否 |通知文字内容|
|» images|body|string| 否 |none|
|» files|body|string| 否 |none|
|» reciever|body|string| 否 |接收方id（团队id或项目id或用户id）|
|» type|body|string| 否 |0: 团体内消息 1: 项目内消息 2: 某个用户的消息|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 删除通知

POST /buaa_db/delete_notice/

团体管理员/系统管理员删除通知

> Body 请求参数

```yaml
notice_id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» notice_id|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 获取已发布的通知

POST /buaa_db/get_send_notice/

团体管理员/系统管理员获取自己发布的通知

> 返回示例

> 200 Response

```json
{
  "notices": [
    "string"
  ]
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» notices|[string]|true|none|notice_id的list|none|

## POST 获取接收到的通知列表

POST /buaa_db/get_receive_notice_list/

团体管理员/学生获取接收到的通知
//或者项目通知和团队通知可以分开

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» senders|[object]|true|none||none|
|»» name|string|true|none|发送方名称|none|
|»» id|string|true|none|发送方id|none|
|»» type|string|true|none|发送方类别|0:团队 1:项目 2:系统管理员|

## POST 获取接收到的特定发送方的通知

POST /buaa_db/get_receive_notice/

> Body 请求参数

```yaml
type: string
id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» type|body|string| 否 |none|
|» id|body|string| 否 |none|

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» notices|[object]|true|none||none|
|»» text|string|true|none||none|
|»» time|string|true|none||none|

# 团体相关功能

## POST 查看申请加入团队的学生

POST /buaa_db/get_in_team/

查看申请加入团队的学生/管理员，当前用户为系统管理员时返回申请加入团队的团体管理员，当前用户为团体管理员时返回申请加入团队的学生

> Body 请求参数

```yaml
{}

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» applies|[object]|true|none||none|
|»» student_id|string|true|none||none|
|»» student_name|string|true|none||none|
|»» project_id|string|true|none||none|
|»» project_name|string|true|none||none|

## POST 团队管理员获取管理的团队

POST /buaa_db/get_manage_teams/

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» teams|[object]|true|none||none|
|»» id|string|true|none||none|
|»» name|string|true|none||none|

## POST 查看申请退出团队的学生

POST /buaa_db/get_out_team/

列出管理的所有团队的退出申请

> Body 请求参数

```yaml
{}

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
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

> Body 请求参数

```yaml
receiver_id: string
team_id: string
result: string
reason: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» receiver_id|body|string| 否 |none|
|» team_id|body|string| 否 |none|
|» result|body|string| 否 |none|
|» reason|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 申请加入团体

POST /buaa_db/apply_team_in/

> Body 请求参数

```yaml
team_id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» team_id|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 申请退出团体

POST /buaa_db/apply_team_out/

> Body 请求参数

```yaml
team_id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» team_id|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 团队管理员创建团队

POST /buaa_db/man_create_team/

> Body 请求参数

```yaml
name: string
profile: string
image: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» name|body|string| 否 |none|
|» profile|body|string| 否 |none|
|» image|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|团队名字重复|Inline|

### 返回数据结构

## POST 团队管理员修改团队信息

POST /buaa_db/man_modify_team_profile/

> Body 请求参数

```yaml
team_id: string
profile: string
image: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» team_id|body|string| 否 |none|
|» profile|body|string| 否 |none|
|» image|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 获得团队中的管理者信息

POST /buaa_db/get_team_managers/

> Body 请求参数

```yaml
team_id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» team_id|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{
  "managers": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» managers|string|true|none||manager_id 的 list|

## POST 获得团队中的项目信息

POST /buaa_db/get_team_projects/

> Body 请求参数

```yaml
team_id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» team_id|body|string| 否 |none|

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» projects|[object]|false|none||none|
|»» name|string|true|none||none|
|»» time|string|true|none||none|
|»» place|string|true|none||none|

## POST 获得团队中的学生信息

POST /buaa_db/get_team_students/

> Body 请求参数

```yaml
team_id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» team_id|body|string| 否 |none|

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» students|[object]|true|none||none|
|»» name|string|true|none|姓名|none|
|»» id|string|true|none|学工号|none|

# 项目相关功能

## POST 团队管理员获取管理的全部项目

POST /buaa_db/get_manage_projects/

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» teams|[object]|true|none||none|
|»» name|string|true|none||none|
|»» position|string|true|none||none|
|»» time|string|true|none||none|

## POST 获取feedback的详细信息

POST /buaa_db/get_feedback_profile/

> Body 请求参数

```yaml
feedback_id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» feedback_id|body|string| 否 |none|

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» student_id|string|true|none||none|
|» project_id|string|true|none||none|
|» profile|string|true|none||none|
|» file_profile|[string]|true|none||none|
|» image_profile|[string]|true|none||none|

## POST 学生申请加入项目

POST /buaa_db/stu_apply_project_in/

> Body 请求参数

```yaml
project_id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» project_id|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 学生申请退出项目

POST /buaa_db/stu_apply_project_out/

> Body 请求参数

```yaml
project_id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» project_id|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 学生发布项目反馈

POST /buaa_db/stu_pub_feedback/

> Body 请求参数

```yaml
project_id: string
profile: string
images: string
files: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» project_id|body|string| 否 |none|
|» profile|body|string| 否 |none|
|» images|body|string| 否 |none|
|» files|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 学生获取已发布的项目反馈

POST /buaa_db/stu_get_feedback/

> Body 请求参数

```yaml
project_id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» project_id|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{
  "feedbacks": [
    "string"
  ]
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» feedbacks|[string]|true|none|feedback_id 的list|none|

## POST 学生删除反馈

POST /buaa_db/stu_delete_feedback/

> Body 请求参数

```yaml
feedback_id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» feedback_id|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 团队管理员创建项目

POST /buaa_db/man_create_project/

> Body 请求参数

```yaml
name: string
time: string
place: string
profile: string
private: string
team_id: string
tags: string
quest_url: string
images: string
files: string
state: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» name|body|string| 否 |none|
|» time|body|string| 否 |none|
|» place|body|string| 否 |none|
|» profile|body|string| 否 |none|
|» private|body|string| 否 |none|
|» team_id|body|string| 否 |none|
|» tags|body|string| 否 |none|
|» quest_url|body|string| 否 |none|
|» images|body|string| 否 |none|
|» files|body|string| 否 |none|
|» state|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 团体管理员删除项目

POST /buaa_db/man_delete_project/

> Body 请求参数

```yaml
project_id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» project_id|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 团队管理员获取申请加入项目的学生

POST /buaa_db/man_get_stu_in_project/

获取管理员管理的*全部项目*的加入申请

> Body 请求参数

```yaml
{}

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» applies|[object]|true|none||none|
|»» student_id|string|true|none||none|
|»» student_name|string|true|none||none|
|»» project_id|string|true|none||none|
|»» project_name|string|true|none||none|

## POST 团队管理员获取申请退出项目的学生

POST /buaa_db/man_get_stu_out_project/

获取管理员管理的全部项目的退出申请

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» applies|[object]|true|none||none|
|»» student_id|string|true|none||none|
|»» student_name|string|true|none||none|
|»» project_id|string|true|none||none|
|»» project_name|string|true|none||none|

## POST 团队管理员处理学生申请项目信息

POST /buaa_db/man_check_stu_project/

> Body 请求参数

```yaml
receiver_id: string
project_id: string
result: string
reason: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» receiver_id|body|string| 否 |none|
|» project_id|body|string| 否 |none|
|» result|body|string| 否 |none|
|» reason|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 团队管理员获取反馈

POST /buaa_db/man_get_project_feedback/

> Body 请求参数

```yaml
project_id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» project_id|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{
  "feedback": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» feedback|string|true|none||只存在一个文件|

## POST 学生获取加入的团队

POST /buaa_db/stu_get_team/

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 学生获取加入的项目

POST /buaa_db/stu_get_project/

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

# 项目相关功能/讨论/评论相关功能 

## POST 发布评论

POST /buaa_db/pub_message/

> Body 请求参数

```yaml
receiver_id: string
discussion_id: string
text: string
images: string
files: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» receiver_id|body|string| 否 |none|
|» discussion_id|body|string| 否 |none|
|» text|body|string| 否 |none|
|» images|body|string| 否 |none|
|» files|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 创建讨论

POST /buaa_db/create_discussion/

学生/团体管理员创建讨论

> Body 请求参数

```yaml
project_id: "2"
profile: 这是一个讨论
type: 提问
title: 这是标题

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» project_id|body|string| 是 |none|
|» profile|body|string| 是 |none|
|» type|body|string| 是 |none|
|» title|body|string| 是 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 删除讨论

POST /buaa_db/delete_discussion/

> Body 请求参数

```yaml
discussion_id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» discussion_id|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 获取讨论

POST /buaa_db/get_discussion/

学生/团体管理员获取项目中的discussion

> Body 请求参数

```yaml
project_id: "1"

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» project_id|body|string| 是 |none|

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
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

> Body 请求参数

```yaml
discussion_id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» discussion_id|body|string| 是 |none|

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» replies|[object]|true|none||none|
|»» student_name|string|true|none||none|
|»» student_id|string|true|none||none|
|»» time|string|true|none||none|
|»» text|string|true|none||none|

## POST 删除评论

POST /buaa_db/delete_message/

> Body 请求参数

```yaml
id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|id|query|string| 否 |message的id|
|body|body|object| 否 |none|
|» id|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

# 系统管理员相关

## POST 系统管理员处理待审核团体

POST /buaa_db/admin_check_apply_team/

> Body 请求参数

```yaml
team_id: string
result: string
reason: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» team_id|body|string| 否 |none|
|» result|body|string| 否 |none|
|» reason|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 系统管理员查看待审核团体

POST /buaa_db/admin_get_apply_team/

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» teams|[object]|true|none||team_id的list|
|»» name|string|true|none|团体名|none|
|»» id|string|true|none|团体id|none|
|»» time|string|false|none|提交申请时间|none|

## POST 系统管理员查看待审核项目

POST /buaa_db/admin_get_apply_project/

> 返回示例

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

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» projects|[object]|true|none||project_id的array|
|»» name|string|true|none|项目名称|none|
|»» id|string|true|none|项目id|none|
|»» time_start|string|true|none||none|
|»» time_end|string|true|none||none|
|»» location|string|true|none||none|

## POST 系统管理员处理待审核项目

POST /buaa_db/admin_check_apply_project/

> Body 请求参数

```yaml
project_id: string
result: string
reason: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» project_id|body|string| 否 |none|
|» result|body|string| 否 |none|
|» reason|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

# 新功能

## POST 团体管理员发布签到

POST /buaa_db/man_pub_sign/

> Body 请求参数

```yaml
project_id: string
name: string
latitude: string
longitude: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» project_id|body|string| 否 |要发布签到的项目|
|» name|body|string| 否 |签到的名字|
|» latitude|body|string| 否 |经度|
|» longitude|body|string| 否 |纬度|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 团队管理员查看发布的签到列表

POST /buaa_db/man_get_signList/

> Body 请求参数

```yaml
project_id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» project_id|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{
  "sign_id": "string",
  "name": "string",
  "time": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» sign_id|string|true|none||none|
|» name|string|true|none||none|
|» time|string|true|none||none|

## POST 团体管理员修改某次签到的状态

POST /buaa_db/man_modify_sign/

> Body 请求参数

```yaml
sign_id: string
student_username: string
state: string
message: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» sign_id|body|string| 否 |none|
|» student_username|body|string| 否 |none|
|» state|body|string| 否 |none|
|» message|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 团体管理员查看签到的具体信息

POST /buaa_db/man_get_signprofile/

> Body 请求参数

```yaml
sign_id: string
project_id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» sign_id|body|string| 否 |none|
|» project_id|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{
  "student_username": "string",
  "student_name": "string",
  "state": "string",
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» student_username|string|true|none||none|
|» student_name|string|true|none||none|
|» state|string|true|none||none|
|» message|string|true|none||none|

## POST 学生获取某个项目的签到列表

POST /buaa_db/stu_get_signlist/

> Body 请求参数

```yaml
project_id: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» project_id|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{
  "sign_id": "string",
  "sign_name": "string",
  "state": "string",
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» sign_id|string|true|none||none|
|» sign_name|string|true|none||none|
|» state|string|true|none||none|
|» message|string|true|none||none|

## POST 学生签到

POST /buaa_db/stu_signin/

> Body 请求参数

```yaml
sign_id: string
latitude: string
longitude: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» sign_id|body|string| 否 |none|
|» latitude|body|string| 否 |经度|
|» longitude|body|string| 否 |纬度|

> 返回示例

> 200 Response

```json
{}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

## POST 按照指定标签搜索项目

POST /buaa_db/search_project_tag/

> Body 请求参数

```yaml
tag: string

```

### 请求参数

|名称|位置|类型|必选|说明|
|---|---|---|---|---|
|body|body|object| 否 |none|
|» tag|body|string| 否 |none|

> 返回示例

> 200 Response

```json
{
  "project_id": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» project_id|string|true|none||none|

# 数据模型

