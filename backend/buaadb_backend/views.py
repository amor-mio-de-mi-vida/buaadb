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
    role = request.POSt.get('role')

    if exist_id(id):
        return JsonResponse({"status": 402})  # 学工号重复

    if role == 0:
        Student.objects.create_user(
            username=id,
            password=password,
            first_name=first_name,
            role=0
        )
        return JsonResponse({"status": 200})
    elif role == 1:
        Manager.objects.create_user(
            username=id,
            password=password,
            first_name=first_name,
            role=1
        )
        return JsonResponse({"status": 200})
    elif role == 2:
        Adminstrator.objects.create_user(
            username=id,
            password=password,
            first_name=first_name,
            role=2
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
    if role == 0:
        user = Student.objects.filter(username=id).first()
    elif role == 1:
        user = Manager.objects.filter(username=id).first()
    elif role == 2:
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
    role = request.session.get('role')
    res = User.objects.get(username=username)

    res_real_name = ""
    res_phone_id = ""
    res_id_number = ""
    res_wx_id = ""
    res_faculty_id = ""

    if role == 0:
        res_stu = Student.objects.get(username=res)
        res_real_name = res_stu.real_name
        res_phone_id = res_stu.phone_id
        res_id_number = res_stu.id_number
        res_wx_id = res_stu.wx_id
        res_faculty_id = res_stu.faculty_id
        res_image_id = res_stu.image_id
    elif role == 1:
        res_man = Manager.objects.get(username=res)
        res_image_id = res_man.image_id
    else:
        res_admin = Adminstrator.objects.get(username=res)
        res_image_id = res_admin.image_id

    return JsonResponse({
        'status': 200,
        'profile': {
            'user_id': username,
            'name': res.first_name,
            'real_name': res_real_name,
            'phone_id': res_phone_id,
            'id_number': res_id_number,
            'wx_id': res_wx_id,
            'faculty_id': res_faculty_id,
            'image_id': res_image_id
        }
    })


def get_other_profile(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    role = request.session.get('role')
    username = request.POST.get('username')

    if role == 0:
        try:
            user = Manager.objects.get(username=username)
        except models.ObjectDoesNotExist:
            user = Student.objects.get(username=username)
        firstname = user.first_name
        image_id = user.image_id
        image = Image.objects.get(ID=image_id)
        return JsonResponse({
            "status": 200,
            "username": username,
            "name": firstname,
            "image_url": image.url
        })
    elif role == 1 or role == 2:
        try:
            user = Manager.objects.get(username=username)
            firstname = user.first_name
            image_id = user.image_id
            image = Image.objects.get(ID=image_id)
            return JsonResponse({
                "status": 200,
                "username": username,
                "name": firstname,
                "image_url": image.url
            })
        except models.ObjectDoesNotExist:
            user = Student.objects.get(username=username)
            image_id = user.image_id
            image = Image.objects.get(ID=image_id)
            return JsonResponse({
                "status": 200,
                "username": username,
                "name": user.first_name,
                "image_url": image.url,
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

    if role == 0:
        res_stu = Student.objects.get(username=res)
        res_stu.real_name = request.POST.get("real_name")
        res_stu.phone_id = request.POST.get("phone_id")
        res_stu.id_number = request.POST.get("id_number")
        res_stu.wx_id = request.POST.get("wx_id")
        res_stu.faculty_id = request.POST.get("faculty_id")
        image = request.FILES.get("image")
        fn = time.strftime('%Y%m%d%H%M%S')
        res_stu.image_id = store_file(image, fn, 0)
        res_stu.save()
        return JsonResponse({"status": 200})
    elif role == 1:
        res_man = Manager.objects.get(username=res)
        image = request.FILES.get("image")
        fn = time.strftime('%Y%m%d%H%M%S')
        res_man.image_id = store_file(image, fn, 0)
        res_man.save()
        return JsonResponse({"status": 200})
    else:
        res_admin = Adminstrator.objects.get(username=res)
        image = request.FILES.get("image")
        fn = time.strftime('%Y%m%d%H%M%S')
        res_admin.image_id = store_file(image, fn, 0)
        res_admin.save()
        return JsonResponse({"status": 200})


def get_teams(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    teams = list(Team.objects.filter(check=False).values_list('ID', flat=True))
    return JsonResponse({"status": 200, "teams": teams})


def get_team_profile(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    team_id = request.POST.get("team_id")
    team = Team.objects.get(ID=team_id)

    name = team.name
    profile = team.profile
    image_id = team.image_id
    image = Image.objects.get(ID=image_id)
    image_url = image.url
    image_post_time = image.post_time
    projects = TeamProject.objects.filter(team_id=team).all()
    students = TeamStudent.objects.filter(team_id=team).all()
    managers = TeamManager.objects.filter(team_id=team).all()

    return JsonResponse({
        "status": 200,
        "name": name,
        "profile": profile,
        "image_id": image_id,
        "image_url": image_url,
        "image_post_time": image_post_time,
        "projects": projects,
        "students": students,
        "managers": managers
    })


def pub_notice(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    sender_id = request.session.get('username')
    sender = User.objects.get(username=sender_id)

    receiver_id = request.POST.get("receiver_id")
    receiver = User.objects.get(username=receiver_id)
    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)
    type = request.POST.get("type")
    profile = request.POST.get("text")
    images = request.FILES.get("images")
    files = request.FILES.get("files")
    fn = time.strftime('%Y%m%d%H%M%S')
    notice = Notice.objects.create(time=fn, type=type, profile=profile)
    ANoticeB.objects.create(sender_id=sender, receiver_id=receiver, notice_id=notice)
    ProjectNotice.objects.create(project_id=project, notice_id=notice)

    for image in images:
        image_id = store_file(image, fn, 0)
        # 写数据库
        ImageNotice.objects.create(image_id=image_id, notice_id=notice)

    for file in files:
        file_id = store_file(file, fn, 1)
        # 写数据库
        FileNotice.objects.create(file_id=file_id, notice_id=notice)

    return JsonResponse({"status": 200})


def delete_notice(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    notice_id = request.POST.get("notice_id")
    try:
        notice = Notice.objects.get(notice_id)
        notice.delete()
    except models.ObjectDoesNotExist:
        return JsonResponse({"status": 400})  # 不存在此通知


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
    notices = get_notice(username=username, is_sender=False)

    return JsonResponse({"status": 200, "notices": notices})


def get_project(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    username = request.session.get('username')
    role = request.session.get('role')
    result = []

    if role == 0:
        projects = list(Project.objects.filter(check=False).values_list('ID', flat=True))
        student = Student.objects.get(username=username)
        for project_id in projects:
            project = Project.objects.get(ID=project_id)
            if project.private:
                try:
                    ProjectStudent.objects.get(student_id=student, project_id=project)
                    result.append(project_id)
                except models.ObjectDoesNotExist:
                    continue
            else:
                result.append(project_id)
        return JsonResponse({"status": 200, "projects": result})
    elif role == 1:
        projects = list(Project.objects.filter(check=False).values_list('ID', flat=True))
        manager = Manager.objects.get(username=username)
        for project_id in projects:
            project = Project.objects.get(ID=project_id)
            if project.private:
                try:
                    ProjectManager.objects.get(manager_id=manager, project_id=project)
                    result.append(project_id)
                except models.ObjectDoesNotExist:
                    continue
            else:
                result.append(project_id)
        return JsonResponse({"status": 200, "projects": result})
    elif role == 2:
        projects = list(Project.objects.values_list('ID', flat=True))
        return JsonResponse({"status": 200, "projects": projects})
    else:
        return JsonResponse({"status": 400})


def get_project_profile(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)

    tags = ProjectTag.objects.filter(project_id=project).all()
    managers = ProjectManager.objects.filter(project_id=project).all()
    students = ProjectStudent.objects.filter(project_id=project).all()

    return JsonResponse({
        "status": 200,
        "project_id": project.ID,
        "name": project.name,
        "time": project.time,
        "place": project.place,
        "profile": project.profile,
        "state": project.state,
        "quest_url": project.quest_url,
        "check": project.check,
        "private": project.private,
        "tags": tags,
        "managers": managers,
        "students": students
    })


def create_discussion(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    username = request.session.get('username')
    fn = time.strftime('%Y%m%d%H%M%S')
    type = request.POST.get("type")
    title = request.POST.get("title")
    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)
    user = User.objects.get(username=username)
    discussion = Discussion.objects.create(time=fn, type=type, title=title, author=user)
    DiscussionProject.objects.create(discussion_id=discussion, project_id=project)

    return JsonResponse({"status": 200})


def delete_discussion(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    discussion_id = request.POST.get('discussion_id')
    discussion = Discussion.objects.get(ID=discussion_id)
    discussion.delete()

    return JsonResponse({"status": 200})


def get_discussion(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    project_id = request.POST.get("project_id")
    project = Project.objects.get(ID=project_id)

    discussions = DiscussionProject.objects.filter(project_id=project).all()

    return JsonResponse({"status": 200, "discussions": discussions})


def get_discussion_profile(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    discussion_id = request.POST.get('discussion_id')
    discussion = Discussion.objects.get(ID=discussion_id)
    messages = DiscussionMessage.objects.filter(discussion_id=discussion).all()
    project = DiscussionProject.objects.filter(discussion_id=discussion).first()

    return JsonResponse({
        "status": 200,
        "id": discussion.ID,
        "time": discussion.time,
        "type": discussion.type,
        "title": discussion.title,
        "author": discussion.author,
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
    AMessageB(sender_id=sender, receiver_id=receiver, message_id=message)

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

    projects = TeamProject.objects.filter(team_id=team).values_list('ID', flat=True).all()

    return JsonResponse({"status": 200, 'projects': projects})


def get_team_students(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    team_id = request.POST.get('team_id')
    team = Team.objects.get(ID=team_id)

    students = TeamStudent.objects.filter(team_id=team).values_list('ID', flat=True).all()

    return JsonResponse({"status": 200, 'students': students})


def get_team_managers(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    team_id = request.POST.get('team_id')
    team = Team.objects.get(ID=team_id)

    managers = TeamManager.objects.filter(team_id=team).values_list('ID', flat=True).all()

    return JsonResponse({"status": 200, 'managers': managers})


def get_in_team(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    role = request.session.get('role')
    team_id = request.POST.get('team_id')
    team = Team.objects.get(ID=team_id)

    if role == 1:  # manager获取申请加入team的学生
        students = StuApplyTeam.objects.filter(team_id=team, status=False).values_list('ID', flat=True).all()
        return JsonResponse({"status": 200, "ids": students})
    elif role == 2:  # admin获取申请加入team的manager
        managers = ManApplyTeam.objects.filter(team_id=team, status=False).values_list('ID', flat=True).all()
        return JsonResponse({"status": 200, "ids": managers})
    else:
        return JsonResponse({"status": 400})


def get_out_team(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    role = request.session.get('role')
    team_id = request.POST.get('team_id')
    team = Team.objects.get(ID=team_id)

    if role == 1:  # manager获取申请加入team的学生
        students = StuApplyTeam.objects.filter(team_id=team, status=True).values_list('ID', flat=True).all()
        return JsonResponse({"status": 200, "ids": students})
    elif role == 2:  # admin获取申请加入team的manager
        managers = ManApplyTeam.objects.filter(team_id=team, status=True).values_list('ID', flat=True).all()
        return JsonResponse({"status": 200, "ids": managers})
    else:
        return JsonResponse({"status": 400})


def check_team(request):
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

    if role == 1:  # manager获取申请加入team的学生
        student = Student.objects.get(username=receiver_id)
        if result:
            StuApplyTeam.objects.get(student_id=student, team_id=team).delete()
            TeamStudent.objects.create(team_id=team, student_id=student)
            type = "success"
            send_notice(fn, type, profile, sender_id, receiver_id)
        else:
            profile = reason
            type = "fail"
            send_notice(fn, type, profile, sender_id, receiver_id)
        return JsonResponse({"status": 200})
    elif role == 2:  # admin获取申请加入team的manager
        manager = Manager.objects.get(username=receiver_id)
        if result:
            ManApplyTeam.objects.get(manager_id=manager, team_id=team).delete()
            TeamManager.objects.create(team_id=team, manager_id=manager)
            type = "success"
            send_notice(fn, type, profile, sender_id, receiver_id)
        else:
            profile = reason
            type = "fail"
            send_notice(fn, type, profile, sender_id, receiver_id)
        return JsonResponse({"status": 200})
    else:
        return JsonResponse({"status": 400})


def apply_team(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    username = request.session.get('username')
    role = request.session.get('role')
    team_id = request.POST.get('team_id')
    team = Team.objects.get(ID=team_id)
    status = request.POST.get('status')  # result为False时申请加入,result为True时申请退出

    if role == 0:
        student = Student.objects.get(username=username)
        StuApplyTeam.objects.create(student_id=student, team_id=team, status=status)
        return JsonResponse({"status": 200})
    elif role == 1:
        manager = Manager.objects.get(username=username)
        ManApplyTeam.objects.create(manager_id=manager, team_id=team, status=status)
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
            "file_id": file.file_id,
            "post_time": file.post_time,
        })

    for image in images:
        image_profile.append({
            "image_id": image.image_id,
            "post_time": image.post_time,
        })

    return JsonResponse({
        "status": 200,
        "student_id": student_id,
        "project_id": project_id,
        "profile": feedback.profile,
        "file_profile": file_profile,
        "image_profile": image_profile
    })


def stu_apply_project(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    username = request.session.get('username')
    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)
    status = request.POST.get('status')  # result为False时申请加入,result为True时申请退出

    student = Student.objects.get(username=username)
    StuApplyProject.objects.create(student_id=student, project_id=project, status=status)
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
    for image in images:
        image_id = store_file(image, fn, 0)
        FeedbackImage.objects.create(image_id=image_id, feedback_id=feedback, post_time=fn)

    for file in files:
        file_id = store_file(file, fn, 1)
        FeedbackFile.objects.create(file_id=file_id, feedback_id=feedback, post_time=fn)


def stu_get_feedback(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    username = request.session.get('username')
    student = Student.objects.get(usernamstu_get_feedbacke=username)
    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)

    feedbacks = Feedback.objects.filter(student_id=student, project_id=project).values_list('ID', flat=True).all()

    return JsonResponse({"status": 200, "feedbacks": feedbacks})


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
    try:
        Team.objects.get(name=name)
        return JsonResponse({"status": 400})
    except models.ObjectDoesNotExist:
        profile = request.POST.get('profile')
        image = request.FILES.get('image')
        fn = time.strftime('%Y%m%d%H%M%S')
        image_id = store_file(image, fn, 0)
        team = Team.objects.create(name=name, profile=profile, image_id=image_id, check=True)
        TeamManager.objects.create(team_id=team, manager_id=manager, check=False)  # check为false代表此man自动管理team不用申请

        send_notice(time=fn, type='', profile='apply for team', sender_id=username, receiver_id='66666666')
        return JsonResponse({"status": 200})


def man_modify_team_profile(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    team_id = request.POST.get('team_id')
    team = Team.objects.get(ID=team_id)

    team.profile = request.POST.get('profile')
    image = request.FILES.get("image")
    fn = time.strftime('%Y%m%d%H%M%S')
    team.image_id = store_file(image, fn, 0)
    team.save()

    return JsonResponse({"status": 200})


def man_create_project(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    manager_id = request.session.get('username')
    manager = Manager.objects.get(username=manager_id)
    team_id = request.POST.get('team_id')
    team = Team.objects.get(ID=team_id)
    name = request.POST.get('name')
    time = request.POST.get('time')
    place = request.POST.get('place')
    profile = request.POST.get('profile')
    state = request.POST.get('state')
    quest_url = request.POST.get('quest_url')
    private = request.POST.get('private')
    tags = request.POST.get('tags')
    images = request.FILES.get('images')
    files = request.FILES.get('files')
    fn = time.strftime('%Y%m%d%H%M%S')

    project = Project.objects.create(name=name, time=time, place=place, profile=profile, state=state,
                                     quest_url=quest_url, private=private)

    TeamProject.objects.create(team_id=team, project_id=project)
    ProjectManager.objects.create(project_id=project, manager_id=manager)
    for tag in tags:
        ProjectTag.objects.create(project_id=project, tag_name=tag)
    for image in images:
        image_id = store_file(image, fn, 0)
        ImageProject.objects.create(image_id=image_id, project_id=project)
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

    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)

    students = StuApplyProject.objects.filter(project_id=project, status=False).values_list('ID', flat=True).all()
    return JsonResponse({"status": 200, "ids": students})


def man_get_stu_out_project(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)

    students = StuApplyProject.objects.filter(project_id=project, status=True).values_list('ID', flat=True).all()
    return JsonResponse({"status": 200, "ids": students})


def man_check_stu_project(request):
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

    student = Student.objects.get(username=receiver_id)
    if result:
        StuApplyProject.objects.get(student_id=student, project_id=project).delete()
        ProjectStudent.objects.create(project_id=project, student_id=student)
        type = "success"
        send_notice(fn, type, profile, sender_id, receiver_id)
    else:
        profile = reason
        type = "fail"
        send_notice(fn, type, profile, sender_id, receiver_id)
    return JsonResponse({"status": 200})


def man_get_project_feedback(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    project_id = request.POST.get('project_id')
    project = Project.objects.get(ID=project_id)

    feedbacks = Feedback.objects.filter(project_id=project).values_list('feedback_id', flat=True).all()

    return JsonResponse({"status": 200, "feedbacks": feedbacks})


def admin_get_apply_team(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    teams = Team.objects.filter(check=True).values_list('ID', flat=True)

    return JsonResponse({"status": 200, "teams": teams})


def admin_get_apply_project(request):
    if request.method != "POST":
        return JsonResponse({"status": 500})  # 非POST请求

    projects = Project.objects.filter(check=True).values_list('ID', flat=True)

    return JsonResponse({"status": 200, "projects": projects})


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
    receiver_ids = TeamManager.objects.filter(team_id=team).values_list('manager_id', flat=True).all

    if result:
        team.check = True
        team.save()
        type = "success"
        for receiver_id in receiver_ids:
            send_notice(fn, type, profile, sender_id, receiver_id)
    else:
        team.delete()
        profile = reason
        type = "fail"
        for receiver_id in receiver_ids:
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
    receiver_id = ProjectManager.objects.filter(project_id=project).values_list('manager_id', flat=True)

    if result:
        project.check = True
        project.save()
        type = "success"
        send_notice(fn, type, profile, sender_id, receiver_id)
        return JsonResponse({"status": 200})
    else:
        project.delete()
        profile = reason
        type = "fail"
        send_notice(fn, type, profile, sender_id, receiver_id)

    return JsonResponse({"status": 200})
