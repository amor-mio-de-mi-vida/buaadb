import time

from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import logout as dj_logout, login as dj_login

from .utils import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    password = request.POST.get('password')
    password_again = request.POST.get('password_again')
    if password_again != password:
        return JsonResponse({"status": 404})  # 两次密码不一致

    id = request.POST.get('id')
    first_name = request.POST.get('name')
    role = request.POST.get('role')
    print(role)
    if exist_id(id):
        return JsonResponse({"status": 402})  # 学工号重复

    if role == "0":
        Student.objects.create_user(
            username=id,
            password=password,
            first_name=first_name,
        )
        return JsonResponse({"status": 200})
    elif role == "1":
        Manager.objects.create_user(
            username=id,
            password=password,
            first_name=first_name,
        )
        return JsonResponse({"status": 200})
    elif role == "2":
        Adminstrator.objects.create_user(
            username=id,
            password=password,
            first_name=first_name,
        )
        return JsonResponse({"status": 200})
    else:
        return JsonResponse({"status": 401})  # 无权限注册


def login(request):
    if request.method != 'POST':
        return JsonResponse({"status": 500})  # 非POST请求

    id = request.POST.get('id')
    password = request.POST.get('password')
    role = request.POST.get('role')
    if role == "0":
        user = Student.objects.filter(username=id).first()
    elif role == "1":
        user = Manager.objects.filter(username=id).first()
    elif role == "2":
        user = Adminstrator.objects.filter(username=id).first()
    else:
        return JsonResponse({"status": 400})  # 未注册

    if user and user.check_password(password):
        dj_login(request, user)
        request.session['username'] = id
        request.session['role'] = role
        return JsonResponse({"status": 200})  # 登录成功
    elif user:
        return JsonResponse({"status": 300})  # 密码错误
    else:
        return JsonResponse({"status": 400})  # 未注册


def logout(request):
    dj_logout(request=request)
    return JsonResponse({"status": 200})


def change_password(request):
    if request.method != 'POST':
        return JsonResponse({"status": 500})  # 非POST请求

    user_id = request.session.get('username')
    print(user_id)
    user = User.objects.get(username=user_id)
    old_password = request.POST.get('old_password')
    new_password = request.POST.get('new_password')
    new_password_again = request.POST.get('new_password_again')
    if new_password != new_password_again:
        return JsonResponse({"status": 400})
    if user.check_password(old_password):
        user.set_password(new_password)
        user.save()
        return JsonResponse({"status": 200})
    else:
        return JsonResponse({"status": 401})


def get_personal_profile(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    username = request.session.get('username')
    print(username)
    role = request.session.get('role')
    res = User.objects.get(username=username)

    res_real_name = ""
    res_phone_id = ""
    res_id_number = ""
    res_wx_id = ""
    res_faculty_id = ""

    if role == "0":
        res_stu = Student.objects.get(username=res)
        res_real_name = res_stu.real_name
        res_phone_id = res_stu.phone_id
        res_id_number = res_stu.id_number
        res_wx_id = res_stu.wx_id
        res_faculty_id = res_stu.faculty_id
        res_image_id = res_stu.image_id
        res_image_url = ''
        if res_image_id:
            image = Image.objects.get(ID=res_image_id)
            res_image_url = image.url
    elif role == "1":
        res_man = Manager.objects.get(username=res)
        res_image_id = res_man.image_id
        image = Image.objects.get(ID=res_image_id)
        res_image_url = image.url
    else:
        res_admin = Adminstrator.objects.get(username=res)
        res_image_id = res_admin.image_id
        image = Image.objects.get(ID=res_image_id)
        res_image_url = image.url

    return JsonResponse({
        'status': 200,
        'username': username,
        'name': res.first_name,
        'real_name': res_real_name,
        'phone_id': res_phone_id,
        'id_number': res_id_number,
        'wx_id': res_wx_id,
        'faculty_id': res_faculty_id,
        # 'image_id': res_image_id,
        'image_url': res_image_url,
        'role': role
    })


def get_other_profile(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    role = request.session.get('role')
    username = request.POST.get('username')
    print(username)

    if role == "0":
        if get_role(username) == 1:
            user = Manager.objects.get(username=username)
        else:
            user = Student.objects.get(username=username)
        firstname = user.first_name
        #image_id = user.image_id
        #image = Image.objects.get(ID=image_id)
        #image_url = image.url
        return JsonResponse({
            "status": 200,
            "username": username,
            "name": firstname,
            #"image_url": image_url
        })
    elif role == "1" or role == "2":
        if get_role(username) == 1:
            user = Manager.objects.get(username=username)
            firstname = user.first_name
            image_id = user.image_id
            image = Image.objects.get(ID=image_id)
            image_url = image.url
            return JsonResponse({
                "status": 200,
                "username": username,
                "name": firstname,
                "image_url": image_url
            })
        else:
            user = Student.objects.get(username=username)
            image_id = user.image_id
            image_url = ''
            if image_id:
                image = Image.objects.get(ID=image_id)
                image_url = image.url
            return JsonResponse({
                "status": 200,
                "username": username,
                "name": user.first_name,
                "image_url": image_url,
                "real_name": user.real_name,
                "phone_id": user.phone_id,
                "id_number": user.id_number,
                "wx_id": user.wx_id,
                "faculty_id": user.faculty_id
            })
    else:
        return JsonResponse({"status": 400})


# TODO
def modify_personal_profile(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    user_id = request.session.get('username')
    role = request.session.get('role')
    res = User.objects.get(username=user_id)

    if role == "0":
        res_stu = Student.objects.get(username=res)
        res_stu.real_name = request.POST.get("real_name")
        res_stu.phone_id = request.POST.get("phone_id")
        res_stu.id_number = request.POST.get("id_number")
        res_stu.wx_id = request.POST.get("wx_id")
        res_stu.faculty_id = request.POST.get("faculty_id")
        image = request.FILES.get("image")
        fn = time.strftime('%Y%m%d%H%M%S')
        if image is not None:
            res_stu.image_id = store_file(image, fn, 0).ID
        else:
            res_stu.image_id = ""

        res_stu.save()
        return JsonResponse({"status": 200})
    elif role == "1":
        res_man = Manager.objects.get(username=res)
        image = request.FILES.get("image")
        fn = time.strftime('%Y%m%d%H%M%S')
        if image is not None:
            res_man.image_id = store_file(image, fn, 0).ID
        else:
            res_man.image_id = ""
        res_man.save()
        return JsonResponse({"status": 200})
    else:
        res_admin = Adminstrator.objects.get(username=res)
        image = request.FILES.get("image")
        fn = time.strftime('%Y%m%d%H%M%S')
        if image is not None:
            res_admin.image_id = store_file(image, fn, 0).ID
        else:
            res_admin.image_id = ""
        res_admin.save()
        return JsonResponse({"status": 200})


def get_teams(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    result = []
    teams = Team.objects.filter(isCheck=False).all()

    for team in teams:
        image = team.image_id
        image_url = Image.objects.get(ID=image).url
        result.append({
            "id": team.ID,
            "name": team.name,
            "image_url": image_url
        })

    return JsonResponse({"status": 200, "teams": result})


def get_team_profile(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    team_id = request.POST.get("team_id")
    team = Team.objects.get(ID=team_id)

    name = team.name
    profile = team.profile
    image_id = team.image_id
    image_url = ''
    image_post_time = ''
    if image_id:
        image = Image.objects.get(ID=image_id)
        image_url = image.url
        image_post_time = image.post_time
    result1 = []
    projects = TeamProject.objects.filter(team_id=team).all()
    for relation in projects:
        project = relation.project_id
        result1.append({
            "id": project.ID,
            "name": project.name,
            "time": project.time,
            "position": project.place
        })

    result2 = []
    students = TeamStudent.objects.filter(team_id=team).all()
    for relation in students:
        student_id = relation.student_id
        student = Student.objects.get(username=student_id)
        result2.append({
            "name": student.first_name,
            "id": student.username
        })

    result3 = []
    managers = TeamManager.objects.filter(team_id=team).all()
    for relation in managers:
        manager_id = relation.manager_id
        manager = Manager.objects.get(username=manager_id)
        result3.append({
            "name": manager.first_name,
            "id": manager.username
        })

    return JsonResponse({
        "status": 200,
        "name": name,
        "profile": profile,
        "image_id": image_id,
        "image_url": image_url,
        "image_post_time": image_post_time,
        "projects": result1,
        "students": result2,
        "managers": result3
    })


def pub_notice(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    sender_id = request.session.get('username')
    sender = User.objects.get(username=sender_id)
    receiver_id = request.POST.get("receiver")
    type = request.POST.get("type")
    fn = time.strftime('%Y%m%d%H%M%S')
    profile = request.POST.get("text")
    images = request.FILES.get("images")
    files = request.FILES.get("files")

    notice = Notice.objects.create(time=fn, profile=profile)

    if type == "0":
        team = Team.objects.get(ID=receiver_id)
        TeamNotice.objects.create(team_id=team, notice_id=notice)

    elif type == "1":
        project = Project.objects.get(ID=receiver_id)
        ProjectNotice.objects.create(project_id=project, notice_id=notice)

    elif type == "2":
        receiver = User.objects.get(username=receiver_id)
        ANoticeB.objects.create(sender_id=sender, receiver_id=receiver, notice_id=notice)

    if images:
        for image in images:
            image_id = store_file(image, fn, 0)
            # 写数据库
            ImageNotice.objects.create(image_id=image_id, notice_id=notice)

    if files:
        for file in files:
            file_id = store_file(file, fn, 1)
            # 写数据库
            FileNotice.objects.create(file_id=file_id, notice_id=notice)

    return JsonResponse({"status": 200})


def delete_notice(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    notice_id = request.POST.get("notice_id")
    notice = Notice.objects.get(ID=notice_id)
    notice.delete()
    return JsonResponse({"status": 200})


def get_send_notice(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    username = request.session.get('username')
    notices = get_notice(username=username, is_sender=True)

    return JsonResponse({"status": 200, "notices": notices})


def get_receive_notice(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    username = request.session.get('username')
    receiver = User.objects.get(username=username)
    type = request.POST.get("type")
    id = request.POST.get("id")
    print(id)

    notices = []

    if type == "0":
        team = Team.objects.get(ID=id)
        relations = TeamNotice.objects.filter(team_id=team).all()
        for relation in relations:
            notices.append({
                "id": relation.notice_id.ID,
                "time": relation.notice_id.time,
                "profile": relation.notice_id.profile
            })
    elif type == "1":
        project = Project.objects.get(ID=id)
        relations = ProjectNotice.objects.filter(project_id=project).all()
        for relation in relations:
            notices.append({
                "id": relation.notice_id.ID,
                "time": relation.notice_id.time,
                "profile": relation.notice_id.profile
            })
    elif type == "2":
        sender = User.objects.get(username=id)
        relations = ANoticeB.objects.filter(sender_id=sender, receiver_id=receiver).all()
        for relation in relations:
            notices.append({
                "id": relation.notice_id.ID,
                "time": relation.notice_id.time,
                "profile": relation.notice_id.profile
            })

    return JsonResponse({"status": 200, "notices": notices})


def get_receive_notice_list(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    username = request.session.get('username')
    role = request.session.get('role')
    receiver = User.objects.get(username=username)

    person = []
    relations = ANoticeB.objects.filter(receiver_id=receiver).all()
    for relation in relations:
        sender = relation.sender_id
        list1 = {"id": sender.username, "name": sender.first_name}
        if list1 not in person:
            person.append({
                "id": sender.username,
                "name": sender.first_name
            })

    teams = []
    projects = []

    if role == "0":
        student = Student.objects.get(username=username)
        relations = TeamStudent.objects.filter(student_id=student).all()
        for relation in relations:
            teams.append({
                "id": relation.team_id.ID,
                "name": relation.team_id.name
            })
        relations = ProjectStudent.objects.filter(student_id=student).all()
        for relation in relations:
            projects.append({
                "id": relation.project_id.ID,
                "name": relation.project_id.name,
                "time": relation.project_id.time
            })
    elif role == "1":
        manager = Manager.objects.get(username=username)
        relations = TeamManager.objects.filter(manager_id=manager).all()
        for relation in relations:
            teams.append({
                "id": relation.team_id.ID,
                "name": relation.team_id.name
            })
        relations = ProjectManager.objects.filter(manager_id=manager).all()
        for relation in relations:
            projects.append({
                "id": relation.project_id.ID,
                "name": relation.project_id.name,
                "time": relation.project_id.time
            })

    return JsonResponse({
        "status": 200,
        "person": person,
        "teams": teams,
        "projects": projects
    })


def get_project(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    username = request.session.get('username')
    role = request.session.get('role')
    result = []

    if role == "0":
        projects = Project.objects.filter(isCheck=False).all()
        student = Student.objects.get(username=username)
        for project in projects:
            if project.private:
                try:
                    team = TeamProject.objects.get(project_id=project).team_id
                    TeamStudent.objects.get(student_id=student, team_id=team)
                    image = ImageProject.objects.get(project_id=project).image_id
                    result.append({
                        "id": project.ID,
                        "name": project.name,
                        "time": project.time,
                        "url": image.url
                    })
                except models.ObjectDoesNotExist:
                    continue
            else:
                image = ImageProject.objects.get(project_id=project).image_id
                result.append({
                    "id": project.ID,
                    "name": project.name,
                    "time": project.time,
                    "url": image.url
                })
        return JsonResponse({"status": 200, "projects": result})
    elif role == "1":
        projects = Project.objects.filter(isCheck=False).all()
        manager = Manager.objects.get(username=username)
        for project in projects:
            if project.private:
                try:
                    team = TeamProject.objects.get(project_id=project).team_id
                    TeamManager.objects.get(manager_id=manager, team_id=team)
                    image = ImageProject.objects.get(project_id=project).image_id
                    result.append({
                        "id": project.ID,
                        "name": project.name,
                        "time": project.time,
                        "url": image.url
                    })
                except models.ObjectDoesNotExist:
                    continue
            else:
                image = ImageProject.objects.get(project_id=project).image_id
                result.append({
                    "id": project.ID,
                    "name": project.name,
                    "time": project.time,
                    "url": image.url
                })
        return JsonResponse({"status": 200, "projects": result})
    elif role == "2":
        result = []
        projects = Project.objects.all()
        for project in projects:
            image = ImageProject.objects.get(project_id=project).image_id
            result.append({
                "id": project.ID,
                "name": project.name,
                "time": project.time,
                "url": image.url
            })
        return JsonResponse({"status": 200, "projects": result})
    else:
        return JsonResponse({"status": 400})


def get_project_profile(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    role = request.session.get('role')
    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)

    tags = []
    relations = ProjectTag.objects.filter(project_id=project).all()
    for relation in relations:
        tags.append(relation.tag_name)
    managers = []
    relations = ProjectManager.objects.filter(project_id=project).all()
    for relation in relations:
        manager = relation.manager_id
        managers.append({
            "username": manager.username,
            "name": manager.first_name,
        })
    students = []
    relations = ProjectStudent.objects.filter(project_id=project).all()
    for relation in relations:
        student = relation.student_id
        students.append({
            "username": student.username,
            "name": student.first_name
        })
    team_name = ''
    if project.private:
        relation = TeamProject.objects.get(project_id=project)
        team = relation.team_id
        team_name = team.name

    image = ImageProject.objects.get(project_id=project).image_id

    return JsonResponse({
        "status": 200,
        "name": project.name,
        "time": project.time,
        "place": project.place,
        "profile": project.profile,
        "state": project.state,
        "quest_url": project.quest_url,
        "check": project.isCheck,
        "private": project.private,
        "team_name": team_name,
        "tags": tags,
        "managers": managers,
        "students": students,
        "url": image.url,
        "role": role
    })


def create_discussion(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    username = request.session.get('username')
    fn = time.strftime('%Y%m%d%H%M%S')
    type = request.POST.get("type")
    title = request.POST.get("title")
    project_id = request.POST.get('project_id')
    profile = request.POST.get('profile')
    project = Project.objects.get(ID=project_id)
    user = User.objects.get(username=username)
    discussion = Discussion.objects.create(time=fn, type=type, title=title, profile=profile, author=user)
    DiscussionProject.objects.create(discussion_id=discussion, project_id=project)

    return JsonResponse({"status": 200})


def delete_discussion(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    discussion_id = request.POST.get('discussion_id')
    discussion = Discussion.objects.get(ID=discussion_id)
    discussion.delete()

    return JsonResponse({"status": 200})


def stu_get_team(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    username = request.session.get('username')
    student = Student.objects.get(username=username)
    teams = []
    relations = TeamStudent.objects.filter(student_id=student).all()
    for relation in relations:
        teams.append({
            "id": relation.team_id.ID,
            "name": relation.team_id.name,
            "profile": relation.team_id.profile
        })
    return JsonResponse({"status": 200, "teams": teams})


def stu_get_project(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    username = request.session.get('username')
    student = Student.objects.get(username=username)
    projects = []
    relations = ProjectStudent.objects.filter(student_id=student).all()
    for relation in relations:
        projects.append({
            "id": relation.project_id.ID,
            "name": relation.project_id.name,
            "time": relation.project_id.time,
            "position": relation.project_id.place,
            "dialogVisible": False
        })

    return JsonResponse({"status": 200, "projects": projects})


def get_discussion(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    project_id = request.POST.get("project_id")
    project = Project.objects.get(ID=project_id)

    discussions = []
    relations = DiscussionProject.objects.filter(project_id=project).all()
    for relation in relations:
        discussion = relation.discussion_id
        if get_role(discussion.author.username) == 0:
            stu = Student.objects.get(username=discussion.author.username)
            image = Image.objects.get(ID=stu.image_id)
        else:
            man = Manager.objects.get(username=discussion.author.username)
            image = Image.objects.get(ID=man.image_id)
        discussions.append({
            "id": discussion.ID,
            "title": discussion.title,
            "time": discussion.time,
            "author_name": discussion.author.first_name,
            "author_id": discussion.author.username,
            "author_url": image.url
        })
    return JsonResponse({"status": 200, "discussions": discussions})


def get_discussion_profile(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    discussion_id = request.POST.get('discussion_id')
    discussion = Discussion.objects.get(ID=discussion_id)
    messages = DiscussionMessage.objects.filter(discussion_id=discussion).all()
    project = DiscussionProject.objects.filter(discussion_id=discussion).first()

    if get_role(discussion.author.username) == 0:
        stu = Student.objects.get(username=discussion.author.username)
        image = Image.objects.get(ID=stu.image_id)
    else:
        man = Manager.objects.get(username=discussion.author.username)
        image = Image.objects.get(ID=man.image_id)

    return JsonResponse({
        "status": 200,
        "id": discussion.ID,
        "time": discussion.time,
        "type": discussion.type,
        "title": discussion.title,
        "author": discussion.author,
        "author_url": image.url,
        "project_id": project,
        "messsages": messages
    })


def pub_message(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    sender_id = request.session.get('username')
    sender = User.objects.get(username=sender_id)

    receiver_id = request.POST.get('receiver_id')
    receiver = User.objects.get(username=receiver_id)
    discussion_id = request.POST.get('discussion_id')
    discussion = Discussion.objects.get(ID=discussion_id)
    text = request.POST.get("text")
    fn = time.strftime('%Y%m%d%H%M%S')
    images = request.FILES.get("images")
    files = request.FILES.get("files")
    message = Message.objects.create(post_time=fn, text=text)
    DiscussionMessage.objects.create(discussion_id=discussion, message_id=message)
    AMessageB.objects.create(sender_id=sender, receiver_id=receiver, message_id=message)

    for image in images:
        addr = store_file(image, fn, 0)
        # 写数据库
        img = Image.objects.create(url=addr, post_time=fn)
        ImageMessage.objects.create(image_id=img, message_id=message)

    for file in files:
        addr = store_file(file, fn, 1)
        # 写数据库
        file = File.objects.create(url=addr, post_time=fn)
        FileMessage.objects.create(file_id=file, message_id=message)

    return JsonResponse({"status": 200})


def get_discussion_replies(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    discussion_id = request.POST.get("discussion_id")
    relations = DiscussionMessage.objects.filter(discussion_id=discussion_id).all()

    messages = []
    for relation in relations:
        message = relation.message_id
        message_image = ImageMessage.objects.get(message_id=message).image_id
        amessageb = AMessageB.objects.get(message_id=relation.message_id)
        sender = amessageb.sender_id
        from_image = ImageUser.objects.get(user_id=sender).image_id
        from_name = sender.first_name
        receiver = amessageb.receiver_id
        to_name = receiver.first_name
        messages.append({
            "id": relation.message_id.ID,
            "message_url": message_image.url,
            "post_time": relation.message_id.post_time,
            "text": relation.message_id.text,
            "from_name": from_name,
            "from_id": sender.username,
            "from_url": from_image.url,
            "to_name": to_name,
            "to_id": receiver.username,
            "visible": False
        })

    return JsonResponse({"status": 200, "messages": messages})


def delete_message(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    id = request.POST.get('id')
    message = Message.objects.get(ID=id)

    message.delete()

    return JsonResponse({"status": 200})


def get_team_projects(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    team_id = request.POST.get('team_id')
    team = Team.objects.get(ID=team_id)

    projects = []
    relations = TeamProject.objects.filter(team_id=team).all()
    for relation in relations:
        projects.append({
            "id": relation.project_id.ID,
            "name": relation.project_id.name,
            "time": relation.project_id.time,
            "place": relation.project_id.place
        })

    return JsonResponse({"status": 200, 'projects': projects})


def get_team_students(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    team_id = request.POST.get('team_id')
    team = Team.objects.get(ID=team_id)

    students = []
    relations = TeamStudent.objects.filter(team_id=team).all()
    for relation in relations:
        students.append({
            "id": relation.student_id.username,
            "name": relation.student_id.first_name
        })

    return JsonResponse({"status": 200, 'students': students})


def get_team_managers(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    team_id = request.POST.get('team_id')
    team = Team.objects.get(ID=team_id)

    managers = []
    relations = TeamManager.objects.filter(team_id=team).all()
    for relation in relations:
        managers.append({
            "username": relation.manager_id.username,
            "name": relation.manager_id.first_name
        })

    return JsonResponse({"status": 200, 'managers': managers})


def get_in_team(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    role = request.session.get('role')
    # team_id = request.POST.get('team_id')
    # team = Team.objects.get(ID=team_id)

    if role == "1":  # manager获取申请加入team的学生
        students = []
        relations = StuApplyTeam.objects.filter(status=False).all()
        for relation in relations:
            students.append({
                "student_id": relation.student_id.username,
                "student_name": relation.student_id.first_name,
                "team_id": relation.team_id.ID,
                "team_name": relation.team_id.name
            })
        return JsonResponse({"status": 200, "applies": students})
    elif role == "2":  # admin获取申请加入team的manager
        managers = []
        relations = ManApplyTeam.objects.filter(status=False).all()
        for relation in relations:
            managers.append({
                "username": relation.manager_id.username,
                "name": relation.manager_id.first_name
            })
        return JsonResponse({"status": 200, "applies": managers})
    else:
        return JsonResponse({"status": 400})


def get_out_team(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    role = request.session.get('role')
    # team_id = request.POST.get('team_id')
    # team = Team.objects.get(ID=team_id)

    if role == "1":  # manager获取申请加入team的学生
        students = []
        relations = StuApplyTeam.objects.filter(status=True).all()
        for relation in relations:
            students.append({
                "username": relation.student_id.username,
                "name": relation.student_id.first_name,
                "team_id": relation.team_id.ID,
                "team_name": relation.team_id.name
            })
        return JsonResponse({"status": 200, "ids": students})
    elif role == "2":  # admin获取申请加入team的manager
        managers = []
        relations = ManApplyTeam.objects.filter(status=True).all()
        for relation in relations:
            managers.append({
                "username": relation.manager_id.username,
                "name": relation.manager_id.first_name
            })
        return JsonResponse({"status": 200, "ids": managers})
    else:
        return JsonResponse({"status": 400})


def check_team_in(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    sender_id = request.session.get('username')
    role = request.session.get('role')
    receiver_id = request.POST.get('receiver_id')
    team_id = request.POST.get('team_id')
    team = Team.objects.get(ID=team_id)
    result = request.POST.get('result')
    reason = request.POST.get('reason')

    fn = time.strftime('%Y%m%d%H%M%S')
    profile = ""
    type = "2"

    print(receiver_id)
    if role == "1":  # manager获取申请加入team的学生
        student = Student.objects.get(username=receiver_id)
        if result:
            StuApplyTeam.objects.get(student_id=student, team_id=team).delete()
            TeamStudent.objects.create(team_id=team, student_id=student)
            profile = "success"
            send_notice(fn, type, profile, sender_id, receiver_id)
        else:
            profile = "fail:" + reason
            send_notice(fn, type, profile, sender_id, receiver_id)
        return JsonResponse({"status": 200})
    elif role == "2":  # admin获取申请加入team的manager
        manager = Manager.objects.get(username=receiver_id)
        if result:
            ManApplyTeam.objects.get(manager_id=manager, team_id=team).delete()
            TeamManager.objects.create(team_id=team, manager_id=manager)
            profile = "success"
            send_notice(fn, type, profile, sender_id, receiver_id)
        else:
            profile = "fail:" + reason
            send_notice(fn, type, profile, sender_id, receiver_id)
        return JsonResponse({"status": 200})
    else:
        return JsonResponse({"status": 400})


def check_team_out(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    sender_id = request.session.get('username')
    role = request.session.get('role')
    receiver_id = request.POST.get('receiver_id')
    team_id = request.POST.get('team_id')
    team = Team.objects.get(ID=team_id)
    result = request.POST.get('result')
    reason = request.POST.get('reason')

    fn = time.strftime('%Y%m%d%H%M%S')
    profile = ""
    type = "2"

    print(receiver_id)
    if role == "1":  # manager获取申请加入team的学生
        student = Student.objects.get(username=receiver_id)
        if result:
            StuApplyTeam.objects.get(student_id=student, team_id=team).delete()
            TeamStudent.objects.get(team_id=team, student_id=student).delete()
            profile = "success"
            send_notice(fn, type, profile, sender_id, receiver_id)
        else:
            profile = "fail:" + reason
            send_notice(fn, type, profile, sender_id, receiver_id)
        return JsonResponse({"status": 200})
    elif role == "2":  # admin获取申请加入team的manager
        manager = Manager.objects.get(username=receiver_id)
        if result:
            ManApplyTeam.objects.get(manager_id=manager, team_id=team).delete()
            TeamManager.objects.get(team_id=team, manager_id=manager).delete()
            profile = "success"
            send_notice(fn, type, profile, sender_id, receiver_id)
        else:
            profile = "fail:" + reason
            send_notice(fn, type, profile, sender_id, receiver_id)
        return JsonResponse({"status": 200})
    else:
        return JsonResponse({"status": 400})


def apply_team_in(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    username = request.session.get('username')
    role = request.session.get('role')
    team_id = request.POST.get('team_id')
    team = Team.objects.get(ID=team_id)

    if role == "0":
        student = Student.objects.get(username=username)
        count = StuApplyTeam.objects.filter(student_id=student, team_id=team).count()
        if count == 0:
            StuApplyTeam.objects.create(student_id=student, team_id=team, status=False)
        return JsonResponse({"status": 200})
    elif role == "1":
        manager = Manager.objects.get(username=username)
        count = ManApplyTeam.objects.filter(manager_id=manager, team_id=team).count()
        if count == 0:
            ManApplyTeam.objects.create(manager_id=manager, team_id=team, status=False)
        return JsonResponse({"status": 200})
    else:
        return JsonResponse({"status": 400})


def apply_team_out(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    username = request.session.get('username')
    role = request.session.get('role')
    team_id = request.POST.get('team_id')
    team = Team.objects.get(ID=team_id)

    if role == "0":
        student = Student.objects.get(username=username)
        count = StuApplyTeam.objects.filter(student_id=student, team_id=team).count()
        if count == 0:
            StuApplyTeam.objects.create(student_id=student, team_id=team, status=True)
        return JsonResponse({"status": 200})
    elif role == "1":
        manager = Manager.objects.get(username=username)
        count = ManApplyTeam.objects.filter(manager_id=manager, team_id=team).count()
        if count == 0:
            ManApplyTeam.objects.create(manager_id=manager, team_id=team, status=True)
        return JsonResponse({"status": 200})
    else:
        return JsonResponse({"status": 400})


def get_feedback_profile(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    feedback_id = request.POST.get('feedback_id')
    feedback = Feedback.objects.get(ID=feedback_id)

    student_id = feedback.student_id
    project_id = feedback.project_id
    file_profile = []
    image_profile = []
    files = FeedbackFile.objects.filter(feedback_id=feedback).all()
    images = FeedbackImage.objects.filter(feedback_id=feedback).all()

    for file in files:
        file_profile.append({
            "file_id": file.file_id.ID,
            "post_time": file.file_id.post_time,
            "url": file.file_id.url
        })

    '''for image in images:
        image_profile.append({
            "image_id": image.image_id.ID,
            "post_time": image.image_id.post_time,
            "url": image.image_id.url
        })'''

    return JsonResponse({
        "status": 200,
        "student_username": student_id.username,
        "project_id": project_id.ID,
        "profile": feedback.profile,
        "file_profile": file_profile,
        "image_profile": image_profile
    })


def stu_apply_project_in(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    username = request.session.get('username')
    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)

    student = Student.objects.get(username=username)
    count = StuApplyProject.objects.filter(student_id=student, project_id=project).count()
    if count == 0:
        StuApplyProject.objects.create(student_id=student, project_id=project, status=False)
    return JsonResponse({"status": 200})


def stu_apply_project_out(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    username = request.session.get('username')
    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)

    student = Student.objects.get(username=username)

    count = StuApplyProject.objects.filter(student_id=student, project_id=project).count()
    if count == 0:
        StuApplyProject.objects.create(student_id=student, project_id=project, status=True)
    return JsonResponse({"status": 200})


def stu_pub_feedback(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    username = request.session.get('username')
    student = Student.objects.get(username=username)
    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)
    profile = request.POST.get('profile')
    images = request.FILES.get('images')
    files = request.FILES.get('files')
    fn = time.strftime('%Y%m%d%H%M%S')

    feedback = Feedback.objects.create(profile=profile, student_id=student, project_id=project)
    if images:
        for image in images:
            image_id = store_file(image, fn, 0)
            FeedbackImage.objects.create(image_id=image_id, feedback_id=feedback, post_time=fn)

    #if files:
    #    for file in files:
    file_id = store_file(files, fn, 1)
    FeedbackFile.objects.create(file_id=file_id, feedback_id=feedback, post_time=fn)
    return JsonResponse({"status": 200})


def stu_get_feedback(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    username = request.session.get('username')
    student = Student.objects.get(username=username)
    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)

    result = []
    feedbacks = Feedback.objects.filter(student_id=student, project_id=project).all()
    for feedback in feedbacks:
        result.append({
            "id": feedback.ID,
            "profile": feedback.profile
        })

    return JsonResponse({"status": 200, "feedbacks": result})


def stu_delete_feedback(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    feedback_id = request.POST.get('feedback_id')
    feedback = Feedback.objects.get(ID=feedback_id)

    feedback.delete()

    return JsonResponse({"status": 200})


def man_create_team(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    username = request.session.get('username')
    manager = Manager.objects.get(username=username)
    name = request.POST.get('name')
    if exist_team_name(name):
        return JsonResponse({"status": 400})
    else:
        profile = request.POST.get('profile')
        image = request.FILES.get('image')
        fn = time.strftime('%Y%m%d%H%M%S')
        img_id = ""
        if image is not None:
            image_id = store_file(image, fn, 0)
            img_id = image_id.ID
        team = Team.objects.create(name=name, profile=profile, isCheck=True, submit_time=fn, image_id=img_id)
        TeamManager.objects.create(team_id=team, manager_id=manager)  # check为false代表此man自动管理team不用申请

        send_notice(time=fn, type='', profile='apply for team', sender_id=username, receiver_id='21373236')
        return JsonResponse({"status": 200})


def man_modify_team_profile(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    team_id = request.POST.get('team_id')
    team = Team.objects.get(ID=team_id)

    team.profile = request.POST.get('profile')
    image = request.FILES.get("image")
    fn = time.strftime('%Y%m%d%H%M%S')
    if image is not None:
        team.image_id = store_file(image, fn, 0).ID
    team.save()

    return JsonResponse({"status": 200})


def get_manage_teams(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    manager_id = request.session.get('username')
    manager = Manager.objects.get(username=manager_id)

    teams = []
    relations = TeamManager.objects.filter(manager_id=manager).all()
    for relation in relations:
        teams.append({
            "id": relation.team_id.ID,
            "name": relation.team_id.name,
            "profile": relation.team_id.profile,
            "isCheck": relation.team_id.isCheck
        })

    return JsonResponse({"status": 200, "teams": teams})


def get_manage_projects(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    manager_id = request.session.get('username')
    manager = Manager.objects.get(username=manager_id)

    projects = []
    relations = ProjectManager.objects.filter(manager_id=manager).all()
    for relation in relations:
        projects.append({
            "id": relation.project_id.ID,
            "name": relation.project_id.name,
            "place": relation.project_id.place,
            "time": relation.project_id.time,
            "isCheck": relation.project_id.isCheck
        })

    return JsonResponse({"status": 200, "projects": projects})

def man_create_project(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    manager_id = request.session.get('username')
    manager = Manager.objects.get(username=manager_id)
    team_id = request.POST.get('team_id')
    private = request.POST.get('private')
    name = request.POST.get('name')
    time1 = request.POST.get('time')
    place = request.POST.get('place')
    profile = request.POST.get('profile')
    state = request.POST.get('state')
    quest_url = request.POST.get('quest_url')
    tag = request.POST.get('tag')
    images = request.FILES.get('images')
    files = request.FILES.get('files')
    fn = time.strftime('%Y%m%d%H%M%S')

    project = Project.objects.create(name=name, time=time1, place=place, profile=profile, state=state,
                                     quest_url=quest_url, private=private)

    if private == '1':
        team = Team.objects.get(ID=team_id)
        TeamProject.objects.create(team_id=team, project_id=project)
    ProjectManager.objects.create(project_id=project, manager_id=manager)

    ProjectTag.objects.create(project_id=project, tag_name=tag)

    if images:
        for image in images:
            image_id = store_file(image, fn, 0)
            ImageProject.objects.create(image_id=image_id, project_id=project)
    if files:
        for file in files:
            file_id = store_file(file, fn, 0)
            FileProject.objects.create(file_id=file_id, project_id=project)

    return JsonResponse({"status": 200})


def man_delete_project(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)

    project.delete()

    return JsonResponse({"status": 200})


def man_get_stu_in_project(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    # project_id = request.POST.get('project_id')
    # project = Project.objects.get(ID=project_id)

    students = []
    relations = StuApplyProject.objects.filter(status=False).all()
    for relation in relations:
        students.append({
            "student_id": relation.student_id.username,
            "student_name": relation.student_id.first_name,
            "project_id": relation.project_id.ID,
            "project_name": relation.project_id.name
        })
    return JsonResponse({"status": 200, "applies": students})


def man_get_stu_out_project(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    # project_id = request.POST.get('project_id')
    # project = Project.objects.get(ID=project_id)

    students = []
    relations = StuApplyProject.objects.filter(status=True).all()
    for relation in relations:
        students.append({
            "student_id": relation.student_id.username,
            "student_name": relation.student_id.first_name,
            "project_id": relation.project_id.ID,
            "project_name": relation.project_id.name
        })
    return JsonResponse({"status": 200, "applies": students})


def man_check_stu_project_in(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    sender_id = request.session.get('username')
    receiver_id = request.POST.get('receiver_id')
    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)
    result = request.POST.get('result')
    reason = request.POST.get('reason')

    fn = time.strftime('%Y%m%d%H%M%S')
    profile = ""
    type = "1"
    student = Student.objects.get(username=receiver_id)
    if result == "1":
        StuApplyProject.objects.get(student_id=student, project_id=project).delete()
        ProjectStudent.objects.create(project_id=project, student_id=student)
        profile = "项目加入成功: " + project.name + "。"
        send_notice(fn, type, profile, sender_id, receiver_id)
    else:
        profile = "项目加入失败: " + project.name + "。 (原因: " + reason + ")"
        send_notice(fn, type, profile, sender_id, receiver_id)
    return JsonResponse({"status": 200})


def man_check_stu_project_out(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    sender_id = request.session.get('username')
    receiver_id = request.POST.get('receiver_id')
    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)
    result = request.POST.get('result')
    reason = request.POST.get('reason')

    fn = time.strftime('%Y%m%d%H%M%S')
    profile = ""
    type = "1"
    student = Student.objects.get(username=receiver_id)
    if result == "1":
        StuApplyProject.objects.get(student_id=student, project_id=project).delete()
        ProjectStudent.objects.get(project_id=project, student_id=student).delete()
        profile = "项目退出成功: " + project.name + "。"
        send_notice(fn, type, profile, sender_id, receiver_id)
    else:
        profile = "项目加入失败: " + project.name + "。 (原因: " + reason + ")"
        send_notice(fn, type, profile, sender_id, receiver_id)
    return JsonResponse({"status": 200})


def man_get_project_feedback(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)

    result = []
    feedbacks = Feedback.objects.filter(project_id=project).all()
    for feedback in feedbacks:
        result.append({
            "id": feedback.ID,
            "profile": feedback.profile
        })

    return JsonResponse({"status": 200, "feedbacks": result})


def admin_get_apply_team(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    teams = Team.objects.filter(isCheck=True).all()
    result = []
    for team in teams:
        result.append({
            "name": team.name,
            "id": team.ID,
            "time": team.submit_time
        })

    return JsonResponse({"status": 200, "teams": result})


def admin_get_apply_project(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    projects = Project.objects.filter(isCheck=True).all()
    result = []
    for project in projects:
        result.append({
            "id": project.ID,
            "name": project.name,
            "time": project.time
        })

    return JsonResponse({"status": 200, "projects": result})


def admin_check_apply_team(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    sender_id = request.session.get("username")
    team_id = request.POST.get("team_id")
    team = Team.objects.get(ID=team_id)
    result = request.POST.get("result")
    reason = request.POST.get("reason")

    fn = time.strftime('%Y%m%d%H%M%S')
    profile = ""
    relations = TeamManager.objects.filter(team_id=team).all()
    type = "2"

    if result != "0":
        team.isCheck = False
        team.save()
        profile = "success"
        for relation in relations:
            receiver_id = relation.manager_id.username
            send_notice(fn, type, profile, sender_id, receiver_id)
    else:
        team.delete()
        profile = "fail:" + reason
        for relation in relations:
            receiver_id = relation.manager_id.username
            send_notice(fn, type, profile, sender_id, receiver_id)

    return JsonResponse({"status": 200})


def admin_check_apply_project(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    sender_id = request.session.get("username")
    project_id = request.POST.get("project_id")
    project = Project.objects.get(ID=project_id)
    result = request.POST.get("result")
    reason = request.POST.get("reason")

    fn = time.strftime('%Y%m%d%H%M%S')
    profile = ""
    receiver_id = ProjectManager.objects.get(project_id=project).manager_id
    type = "2"

    if result == '1':
        project.isCheck = False
        project.save()
        profile = "审核通过: " + project.name + "。"
        send_notice(fn, type, profile, sender_id, receiver_id)
        return JsonResponse({"status": 200})
    else:
        print("refuse!")
        project.delete()
        profile = "审核不通过: " + project.name + "。 (" + "原因:" + reason + ")"
        send_notice(fn, type, profile, sender_id, receiver_id)

    return JsonResponse({"status": 200})


def man_pub_sign(request):
    if request.method != 'POST':
        return JsonResponse({"status": 500})

    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)
    name = request.POST.get('name')
    fn = time.strftime('%Y%m%d%H%M%S')
    latitude = request.POST.get('latitude')
    longitude = request.POST.get('longitude')

    count = Sign.objects.filter(name=name).count()
    if count == 0:
        sign = Sign.objects.create(project=project, name=name, time=fn, latitude=latitude, longitude=longitude)
        relations = ProjectStudent.objects.filter(project_id=project).all()

        for relation in relations:
            student = relation.student_id
            StudentSign.objects.create(student=student, sign=sign)

    return JsonResponse({"status": 200})


def man_get_signList(request):
    if request.method != 'POST':
        return JsonResponse({"status": 500})

    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)
    signs = Sign.objects.filter(project=project).all()

    result = []
    for sign in signs:
        result.append({
            "sign_id": sign.id,
            "name": sign.name,
            "time": sign.time
        })

    return JsonResponse({"status": 200, "result": result})


def man_get_signprofile(request):
    if request.method != 'POST':
        return JsonResponse({"status": 500})

    sign_id = request.POST.get('sign_id')
    sign = Sign.objects.get(id=sign_id)
    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)

    relations = ProjectStudent.objects.filter(project_id=project).all()

    result = []
    for relation in relations:
        student = relation.student_id
        studentSign = StudentSign.objects.get(student=student, sign=sign)
        result.append({
            "student_username": student.username,
            "student_name": student.name,
            "state": studentSign.state,
            "message": studentSign.message
        })

    return JsonResponse({"status": 200, "result": result})


def man_modify_sign(request):
    if request.method != 'POST':
        return JsonResponse({"status": 500})

    sign_id = request.POST.get('sign_id')
    sign = Sign.objects.get(id=sign_id)
    student_username = request.POST.get('student_username')
    student = Student.objects.get(username=student_username)
    state = request.POST.get('state')
    message = request.POST.get('message')

    studentSign = StudentSign.objects.get(student=student, sign=sign)
    studentSign.state = state
    studentSign.message = message
    studentSign.save()

    return JsonResponse({"status": 200})


def stu_get_signlist(request):
    if request.method != 'POST':
        return JsonResponse({"status": 500})

    username = request.session.get('username')
    student = Student.objects.get(username=username)
    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)
    signs = Sign.objects.filter(project=project).all()
    result = []

    for sign in signs:
        relation = StudentSign.objects.get(sign=sign, student=student)
        result.append({
            "sign_id": sign.id,
            "name": sign.name,
            "state": relation.state,
            "message": relation.message
        })

    return JsonResponse({"status": 200, "signs": result})


def stu_signin(request):
    if request.method != 'POST':
        return JsonResponse({"status": 500})

    student_id = request.session.get('username')
    student = Student.objects.get(username=student_id)
    sign_id = request.POST.get('sign_id')
    sign = Sign.objects.get(id=sign_id)
    latitude = request.POST.get('latitude')
    longitude = request.POST.get('longitude')
    fn = time.strftime('%Y%m%d%H%M%S')

    if True:
        relation = StudentSign.objects.get(student=student, sign=sign)
        relation.state = True
        relation.message = "已签到"
        relation.save()
        return JsonResponse({"status": 200})
    else:
        return JsonResponse({"status": 400})


def search_project_tag(request):
    if request.method != 'POST':
        return JsonResponse({"status": 500})

    tag_name = request.POST.get("tag")
    print(tag_name)
    relations = ProjectTag.objects.filter(tag_name=tag_name).all()
    result = []
    for relation in relations:
        result.append({
            "id": relation.project_id.ID,
            "name": relation.project_id.name,
            "time": relation.project_id.time
        })

    return JsonResponse({"status": 200, "projects": result})
