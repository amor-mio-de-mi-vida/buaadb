from django.urls import path
from .views import *

urlpatterns = [
    path("register/", register),  # 注册 # finish
    path("login/", login),  # 登陆 # finish
    path("logout/", logout),  # 登出 # finish
    path("change_password/", change_password),  # 修改密码 # finish
    path("get_personal_profile/", get_personal_profile),  # 获取个人信息 # finish
    path("modify_personal_profile/", modify_personal_profile),  # 修改个人信息 # finish
    path("get_teams/", get_teams),  # 获取所有团体 # finish
    path("get_team_profile/", get_team_profile),  # 获取团体信息 # finish
    path("get_project/", get_project),  # 获取所有项目 # finish
    path("get_project_profile/", get_project_profile),  # 获取项目信息 # finish
    path("create_discussion/", create_discussion),  # 发起讨论 # finish
    path("delete_discussion/", delete_discussion),  # 删除讨论 # finish
    path("get_discussion/", get_discussion),  # 获得项目中的讨论 # finish
    path("get_discussion_profile", get_discussion_profile),  # 获得讨论详情 # finish
    path("pub_notice/", pub_notice),  # 发布通知 # finish
    path("delete_notice/", delete_notice),  # 删除通知 # finish
    path("get_send_notice/", get_send_notice),  # 获得已发出的通知 # finish
    path("get_receive_notice_list/", get_receive_notice_list),  # 获得收到的通知 # finish
    path("get_receive_notice/", get_receive_notice), # 获得特定发送方的notice
    path("pub_message/", pub_message),  # 发布评论 # finish
    path("delete_message/", delete_message),  # 删除评论 # finish
    path("get_in_team/", get_in_team),  # 查看申请加入团队的学生/管理员 # finish
    path("get_out_team/", get_out_team),  # 查看申请退出团队的学生/管理员 # finish
    path("check_team_in/", check_team_in),  # 审核申请加入团队信息 # finish
    path("check_team_out/", check_team_out),  # 审核申请退出团队信息 # finish
    path("apply_team_in/", apply_team_in),  # 申请加入团队 # finish
    path("apply_team_out/", apply_team_out),  # 申请退出团队
    path("get_team_projects/", get_team_projects),  # 获得团队中的项目信息 # finish
    path("get_team_students/", get_team_students),  # 获得团队中的学生信息 # finish
    path("get_team_managers/", get_team_managers),  # 获得团队中的管理者信息 # finish
    path("get_feedback_profile/", get_feedback_profile),  # 获取feedback的详细信息 # finish
    path("get_other_profile/", get_other_profile),  # 获得他人的信息 #
    path("get_discussion_replies/", get_discussion_replies), #获得讨论下的回复
    # ---------上面是通用的功能-/--------下面是学生端功能----------------- #
    path("stu_apply_project_in/", stu_apply_project_in),  # 学生申请加入项目 # finish
    path("stu_apply_project_out/", stu_apply_project_out), # 学生申请退出项目 # finish
    path("stu_pub_feedback/", stu_pub_feedback),  # 学生发布项目反馈 # finish
    path("stu_get_feedback/", stu_get_feedback),  # 学生获取已发布的项目反馈 # finish
    path("stu_delete_feedback/", stu_delete_feedback),  # 学生删除反馈 # finish
    path("stu_get_team/", stu_get_team),
    path("stu_get_project/", stu_get_project),
    # ---------上面是学生端功能-----------下面是团体管理员功能------------ #
    path("man_create_team/", man_create_team),  # 团队管理员创建团队 # finish
    path("man_modify_team_profile/", man_modify_team_profile),  # 团队管理员修改团队信息 # finish
    path("man_create_project/", man_create_project),  # 团队管理员创建项目 # finish
    path("man_delete_project/", man_delete_project),  # 团队管理员删除项目 # finish
    path("man_get_stu_in_project/", man_get_stu_in_project), # 团队管理员获取申请加入项目的学生 # finish
    path("man_get_stu_out_project/", man_get_stu_out_project), # 团队管理员获取申请退出项目的学生 # finish
    path("man_check_stu_project_in/", man_check_stu_project_in), # 团队管理员处理学生申请项目信息 # finish
    path("man_check_stu_project_out/", man_check_stu_project_out), # 团队管理员处理学生申请项目信息 # finish
    path("man_get_project_feedback/", man_get_project_feedback), # 团队管理员获取反馈 # finish
    path("get_manage_teams/", get_manage_teams), #团体管理员获取管理的团队
    path("get_manage_projects/", get_manage_projects), #团体管理员获取管理的团队
    # ---------上面是团体管理员功能--------下面是系统管理员功能------------ #
    path("admin_get_apply_team/", admin_get_apply_team),  # 系统管理员查看待审核团体 # finish
    path("admin_get_apply_project/", admin_get_apply_project),  # 系统管理员审核团体 # finish
    path("admin_check_apply_team/", admin_check_apply_team),  # 系统管理员处理待审核团体 # finish
    path("admin_check_apply_project/", admin_check_apply_project),  # 系统管理员审核项目 # finish
]
