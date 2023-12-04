from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import settings


# 学生
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


# 团体管理员
class Manager(User):
    image_id = models.CharField(max_length=128, db_column='image_id')  # 头像信息

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'manager'


# 系统管理员
class Adminstrator(User):
    image_id = models.CharField(max_length=128, db_column='image_id')  # 头像信息

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'adminstrator'


# 项目
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


# 团体
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


# 通知
class Notice(models.Model):
    ID = models.AutoField(primary_key=True, db_column='notice_id')
    time = models.CharField(max_length=1024, db_column='time')
    type = models.CharField(max_length=1024, db_column='type')
    profile = models.TextField(max_length=4096, db_column='profile')

    def __str__(self):
        return self.ID

    class Meta:
        db_table = 'notice'


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


class DiscussionProject(models.Model):
    discussion_id = models.ForeignKey('Discussion', on_delete=models.CASCADE, db_column='discussion_id')
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE, db_column='project_id')

    class Meta:
        db_table = 'discussion_project'


class DiscussionMessage(models.Model):
    discussion_id = models.ForeignKey('Discussion', on_delete=models.CASCADE, db_column='discussion_id')
    message_id = models.ForeignKey('Message', on_delete=models.CASCADE, db_column='message_id')

    class Meta:
        db_table = 'discussion_message'


class Image(models.Model):
    ID = models.AutoField(primary_key=True, db_column='image_id')
    url = models.TextField(max_length=4096, db_column='url')
    post_time = models.CharField(max_length=1024, db_column='post_time')

    def __str__(self):
        return self.ID

    class Meta:
        db_table = "image"


class ImageUser(models.Model):
    image_id = models.ForeignKey("Image", on_delete=models.CASCADE, db_column="image_id")
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="user_id")

    class Meta:
        db_table = "image_user"


class ImageProject(models.Model):
    image_id = models.ForeignKey("Image", on_delete=models.CASCADE, db_column="image_id")
    project_id = models.ForeignKey("Project", on_delete=models.CASCADE, db_column="project_id")

    class Meta:
        db_table = "image_project"


class ImageNotice(models.Model):
    image_id = models.ForeignKey("Image", on_delete=models.CASCADE, db_column="image_id")
    notice_id = models.ForeignKey("Notice", on_delete=models.CASCADE, db_column="notice_id")

    class Meta:
        db_table = "image_notice"


class ImageMessage(models.Model):
    image_id = models.ForeignKey("Image", on_delete=models.CASCADE, db_column="image_id")
    message_id = models.ForeignKey("Message", on_delete=models.CASCADE, db_column="message_id")

    class Meta:
        db_table = "image_message"


class File(models.Model):
    ID = models.AutoField(primary_key=True, db_column='file_id')
    url = models.TextField(max_length=4096, db_column='url')
    post_time = models.CharField(max_length=1024, db_column='post_time')

    def __str__(self):
        return self.ID

    class Meta:
        db_table = 'file'


class FileUser(models.Model):
    file_id = models.ForeignKey("File", on_delete=models.CASCADE, db_column="file_id")
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="user_id")

    class Meta:
        db_table = "file_user"


class FileProject(models.Model):
    file_id = models.ForeignKey("File", on_delete=models.CASCADE, db_column="file_id")
    project_id = models.ForeignKey("Project", on_delete=models.CASCADE, db_column="project_id")

    class Meta:
        db_table = "file_project"


class FileNotice(models.Model):
    file_id = models.ForeignKey("File", on_delete=models.CASCADE, db_column="file_id")
    notice_id = models.ForeignKey("Notice", on_delete=models.CASCADE, db_column="notice_id")

    class Meta:
        db_table = "file_notice"


class FileMessage(models.Model):
    file_id = models.ForeignKey("File", on_delete=models.CASCADE, db_column="file_id")
    message_id = models.ForeignKey("Message", on_delete=models.CASCADE, db_column="message_id")

    class Meta:
        db_table = "file_message"


class Feedback(models.Model):
    ID = models.AutoField(primary_key=True, db_column='feedback_id')
    profile = models.CharField(max_length=1024, db_column='profile')
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE, db_column='student_id')
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE, db_column='project_id')

    def __str__(self):
        return self.ID

    class Meta:
        db_table = 'feedback'


class FeedbackImage(models.Model):
    feedback_id = models.ForeignKey('Feedback', on_delete=models.CASCADE, db_column='feedback_id')
    image_id = models.ForeignKey('Image', on_delete=models.CASCADE, db_column='image_id')
    post_time = models.CharField(max_length=1024, db_column='post_time')

    class Meta:
        db_table = 'feedback_image'


class FeedbackFile(models.Model):
    feedback_id = models.ForeignKey('Feedback', on_delete=models.CASCADE, db_column='feedback_id')
    file_id = models.ForeignKey('File', on_delete=models.CASCADE, db_column='file_id')
    post_time = models.CharField(max_length=1024, db_column='post_time')

    class Meta:
        db_table = 'feedback_file'


class Message(models.Model):
    ID = models.AutoField(primary_key=True, db_column='message_id')
    post_time = models.CharField(max_length=1024, db_column='post_time')
    text = models.CharField(max_length=1024, db_column='text')

    def __str__(self):
        return self.ID

    class Meta:
        db_table = 'message'


class TeamStudent(models.Model):
    team_id = models.ForeignKey('Team', on_delete=models.CASCADE, db_column='team_id')
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE, db_column='student_id')

    class Meta:
        db_table = 'team_student'


class TeamManager(models.Model):
    team_id = models.ForeignKey('Team', on_delete=models.CASCADE, db_column='team_id')
    manager_id = models.ForeignKey('Manager', on_delete=models.CASCADE, db_column='manager_id')

    class Meta:
        db_table = 'team_manager'


class TeamProject(models.Model):
    team_id = models.ForeignKey('Team', on_delete=models.CASCADE, db_column='team_id')
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE, db_column='project_id')

    class Meta:
        db_table = 'team_project'


class StuApplyTeam(models.Model):
    team_id = models.ForeignKey('Team', on_delete=models.CASCADE, db_column='team_id')
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE, db_column='student_id')
    status = models.BooleanField(max_length=128, db_column='status', default=False)  # 0代表申请加入, 1代表申请退出

    class Meta:
        db_table = 'student_apply_team'


class StuApplyProject(models.Model):
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE, db_column='project_id')
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE, db_column='student_id')
    status = models.BooleanField(db_column='status', default=False)  # 0代表申请加入, 1代表申请退出

    class Meta:
        db_table = 'student_apply_project'


class ManApplyTeam(models.Model):
    team_id = models.ForeignKey('Team', on_delete=models.CASCADE, db_column='team_id')
    manager_id = models.ForeignKey('Manager', on_delete=models.CASCADE, db_column='manager_id')
    status = models.BooleanField(db_column='status', default=False)  # 0代表申请加入, 1代表申请退出

    class Meta:
        db_table = 'manager_apply_team'


class ProjectStudent(models.Model):
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE, db_column='project_id')
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE, db_column='student_id')

    class Meta:
        db_table = 'project_student'


class ProjectTag(models.Model):
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE, db_column='project_id')
    tag_name = models.CharField(max_length=1024, db_column='tag_name')

    class Meta:
        db_table = 'project_tag'


class ProjectNotice(models.Model):
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE, db_column='project_id')
    notice_id = models.ForeignKey('Notice', on_delete=models.CASCADE, db_column='notice_id')

    class Meta:
        db_table = 'project_notice'


class TeamNotice(models.Model):
    team_id = models.ForeignKey('Team', on_delete=models.CASCADE, db_column='team_id')
    notice_id = models.ForeignKey('Notice', on_delete=models.CASCADE, db_column='notice_id')

    class Meta:
        db_table = 'team_notice'


class ProjectManager(models.Model):
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE, db_column='project_id')
    manager_id = models.ForeignKey('Manager', on_delete=models.CASCADE, db_column='manager_id')

    class Meta:
        db_table = 'project_manager'


class ANoticeB(models.Model):
    sender_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Notice_sender', on_delete=models.CASCADE,
                                  db_column='sender_id')
    receiver_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Notice_receiver', on_delete=models.CASCADE,
                                    db_column='receiver_id')
    notice_id = models.ForeignKey('Notice', on_delete=models.CASCADE, db_column='notice_id')

    class Meta:
        db_table = 'A_notice_B'


class AMessageB(models.Model):
    sender_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Message_sender', on_delete=models.CASCADE,
                                  db_column='sender_id')
    receiver_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Message_receiver', on_delete=models.CASCADE,
                                    db_column='receiver_id')
    message_id = models.ForeignKey('Message', on_delete=models.CASCADE, db_column='message_id')

    class Meta:
        db_table = 'A_message_B'


class Sign(models.Model):
    id = models.AutoField(primary_key=True, db_column='sign_ID')
    name = models.CharField(max_length=255, db_column='name')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, db_column='class_id')
    latitude = models.CharField(max_length=255, db_column='latitude')
    longitude = models.CharField(max_length=255, db_column='longitude')
    time = models.CharField(max_length=255, db_column='time')

    class Meta:
        db_table = 'Sign'


class StudentSign(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, db_column='student_ID')
    sign = models.ForeignKey('Sign', on_delete=models.CASCADE, db_column='sign_ID')
    state = models.BooleanField(db_column='state', default=False)
    message = models.TextField(max_length=4096, db_column='message', default="未签到")

    class Meta:
        db_table = 'StudentSign'
