# Generated by Django 4.2.6 on 2023-11-25 10:58

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Adminstrator",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("image_id", models.CharField(db_column="image_id", max_length=128)),
            ],
            options={
                "db_table": "adminstrator",
            },
            bases=("auth.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Discussion",
            fields=[
                (
                    "ID",
                    models.AutoField(
                        db_column="discussion_id", primary_key=True, serialize=False
                    ),
                ),
                ("time", models.CharField(db_column="time", max_length=1024)),
                ("type", models.CharField(db_column="type", max_length=1024)),
                ("title", models.CharField(db_column="title", max_length=1024)),
                ("profile", models.TextField(db_column="profile", max_length=1024)),
                (
                    "author",
                    models.ForeignKey(
                        db_column="author",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "discussion",
            },
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "ID",
                    models.AutoField(
                        db_column="feedback_id", primary_key=True, serialize=False
                    ),
                ),
                ("profile", models.CharField(db_column="profile", max_length=1024)),
            ],
            options={
                "db_table": "feedback",
            },
        ),
        migrations.CreateModel(
            name="File",
            fields=[
                (
                    "ID",
                    models.AutoField(
                        db_column="file_id", primary_key=True, serialize=False
                    ),
                ),
                ("url", models.TextField(db_column="url", max_length=4096)),
                ("post_time", models.CharField(db_column="post_time", max_length=1024)),
            ],
            options={
                "db_table": "file",
            },
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "ID",
                    models.AutoField(
                        db_column="image_id", primary_key=True, serialize=False
                    ),
                ),
                ("url", models.TextField(db_column="url", max_length=4096)),
                ("post_time", models.CharField(db_column="post_time", max_length=1024)),
            ],
            options={
                "db_table": "image",
            },
        ),
        migrations.CreateModel(
            name="Manager",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("image_id", models.CharField(db_column="image_id", max_length=128)),
            ],
            options={
                "db_table": "manager",
            },
            bases=("auth.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "ID",
                    models.AutoField(
                        db_column="message_id", primary_key=True, serialize=False
                    ),
                ),
                ("post_time", models.CharField(db_column="post_time", max_length=1024)),
                ("text", models.CharField(db_column="text", max_length=1024)),
            ],
            options={
                "db_table": "message",
            },
        ),
        migrations.CreateModel(
            name="Notice",
            fields=[
                (
                    "ID",
                    models.AutoField(
                        db_column="notice_id", primary_key=True, serialize=False
                    ),
                ),
                ("time", models.CharField(db_column="time", max_length=1024)),
                ("type", models.CharField(db_column="type", max_length=1024)),
                ("profile", models.TextField(db_column="profile", max_length=4096)),
            ],
            options={
                "db_table": "notice",
            },
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "ID",
                    models.AutoField(
                        db_column="class_id", primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(db_column="name", max_length=128)),
                ("time", models.CharField(db_column="time", max_length=128)),
                ("place", models.CharField(db_column="place", max_length=128)),
                ("profile", models.TextField(db_column="profile", max_length=4096)),
                ("state", models.CharField(db_column="state", max_length=128)),
                ("quest_url", models.CharField(db_column="quest_url", max_length=1024)),
                ("private", models.BooleanField(db_column="private", default=False)),
                ("isCheck", models.BooleanField(db_column="isCheck", default=True)),
            ],
            options={
                "db_table": "project",
            },
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("real_name", models.CharField(db_column="real_name", max_length=128)),
                ("phone_id", models.CharField(db_column="phone_id", max_length=128)),
                ("id_number", models.CharField(db_column="id_number", max_length=128)),
                ("wx_id", models.CharField(db_column="wx_id", max_length=128)),
                (
                    "faculty_id",
                    models.CharField(db_column="faculty_id", max_length=128),
                ),
                ("image_id", models.CharField(db_column="image_id", max_length=128)),
            ],
            options={
                "db_table": "student",
            },
            bases=("auth.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "ID",
                    models.AutoField(
                        db_column="team_id", primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(db_column="name", max_length=128)),
                ("profile", models.TextField(db_column="profile", max_length=4096)),
                ("image_id", models.CharField(db_column="image_id", max_length=1024)),
                ("isCheck", models.BooleanField(db_column="isCheck", default=True)),
            ],
            options={
                "db_table": "team",
            },
        ),
        migrations.CreateModel(
            name="TeamStudent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "student_id",
                    models.ForeignKey(
                        db_column="student_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.student",
                    ),
                ),
                (
                    "team_id",
                    models.ForeignKey(
                        db_column="team_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.team",
                    ),
                ),
            ],
            options={
                "db_table": "team_student",
            },
        ),
        migrations.CreateModel(
            name="TeamProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "project_id",
                    models.ForeignKey(
                        db_column="project_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.project",
                    ),
                ),
                (
                    "team_id",
                    models.ForeignKey(
                        db_column="team_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.team",
                    ),
                ),
            ],
            options={
                "db_table": "team_project",
            },
        ),
        migrations.CreateModel(
            name="TeamManager",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "manager_id",
                    models.ForeignKey(
                        db_column="manager_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.manager",
                    ),
                ),
                (
                    "team_id",
                    models.ForeignKey(
                        db_column="team_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.team",
                    ),
                ),
            ],
            options={
                "db_table": "team_manager",
            },
        ),
        migrations.CreateModel(
            name="StuApplyTeam",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.BooleanField(db_column="status", default=False)),
                (
                    "student_id",
                    models.ForeignKey(
                        db_column="student_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.student",
                    ),
                ),
                (
                    "team_id",
                    models.ForeignKey(
                        db_column="team_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.team",
                    ),
                ),
            ],
            options={
                "db_table": "student_apply_team",
            },
        ),
        migrations.CreateModel(
            name="StuApplyProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.BooleanField(db_column="status", default=False)),
                (
                    "project_id",
                    models.ForeignKey(
                        db_column="project_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.project",
                    ),
                ),
                (
                    "student_id",
                    models.ForeignKey(
                        db_column="student_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.student",
                    ),
                ),
            ],
            options={
                "db_table": "student_apply_project",
            },
        ),
        migrations.CreateModel(
            name="ProjectTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tag_name", models.CharField(db_column="tag_name", max_length=1024)),
                (
                    "project_id",
                    models.ForeignKey(
                        db_column="project_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.project",
                    ),
                ),
            ],
            options={
                "db_table": "project_tag",
            },
        ),
        migrations.CreateModel(
            name="ProjectStudent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "project_id",
                    models.ForeignKey(
                        db_column="project_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.project",
                    ),
                ),
                (
                    "student_id",
                    models.ForeignKey(
                        db_column="student_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.student",
                    ),
                ),
            ],
            options={
                "db_table": "project_student",
            },
        ),
        migrations.CreateModel(
            name="ProjectNotice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "notice_id",
                    models.ForeignKey(
                        db_column="notice_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.notice",
                    ),
                ),
                (
                    "project_id",
                    models.ForeignKey(
                        db_column="project_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.project",
                    ),
                ),
            ],
            options={
                "db_table": "project_notice",
            },
        ),
        migrations.CreateModel(
            name="ProjectManager",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "manager_id",
                    models.ForeignKey(
                        db_column="manager_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.manager",
                    ),
                ),
                (
                    "project_id",
                    models.ForeignKey(
                        db_column="project_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.project",
                    ),
                ),
            ],
            options={
                "db_table": "project_manager",
            },
        ),
        migrations.CreateModel(
            name="ManApplyTeam",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.BooleanField(db_column="status", default=False)),
                (
                    "manager_id",
                    models.ForeignKey(
                        db_column="manager_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.manager",
                    ),
                ),
                (
                    "team_id",
                    models.ForeignKey(
                        db_column="team_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.team",
                    ),
                ),
            ],
            options={
                "db_table": "manager_apply_team",
            },
        ),
        migrations.CreateModel(
            name="ImageUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image_id",
                    models.ForeignKey(
                        db_column="image_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.image",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        db_column="user_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "image_user",
            },
        ),
        migrations.CreateModel(
            name="ImageProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image_id",
                    models.ForeignKey(
                        db_column="image_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.image",
                    ),
                ),
                (
                    "project_id",
                    models.ForeignKey(
                        db_column="project_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.project",
                    ),
                ),
            ],
            options={
                "db_table": "image_project",
            },
        ),
        migrations.CreateModel(
            name="ImageNotice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image_id",
                    models.ForeignKey(
                        db_column="image_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.image",
                    ),
                ),
                (
                    "notice_id",
                    models.ForeignKey(
                        db_column="notice_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.notice",
                    ),
                ),
            ],
            options={
                "db_table": "image_notice",
            },
        ),
        migrations.CreateModel(
            name="ImageMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image_id",
                    models.ForeignKey(
                        db_column="image_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.image",
                    ),
                ),
                (
                    "message_id",
                    models.ForeignKey(
                        db_column="message_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.message",
                    ),
                ),
            ],
            options={
                "db_table": "image_message",
            },
        ),
        migrations.CreateModel(
            name="FileUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "file_id",
                    models.ForeignKey(
                        db_column="file_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.file",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        db_column="user_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "file_user",
            },
        ),
        migrations.CreateModel(
            name="FileProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "file_id",
                    models.ForeignKey(
                        db_column="file_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.file",
                    ),
                ),
                (
                    "project_id",
                    models.ForeignKey(
                        db_column="project_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.project",
                    ),
                ),
            ],
            options={
                "db_table": "file_project",
            },
        ),
        migrations.CreateModel(
            name="FileNotice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "file_id",
                    models.ForeignKey(
                        db_column="file_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.file",
                    ),
                ),
                (
                    "notice_id",
                    models.ForeignKey(
                        db_column="notice_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.notice",
                    ),
                ),
            ],
            options={
                "db_table": "file_notice",
            },
        ),
        migrations.CreateModel(
            name="FileMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "file_id",
                    models.ForeignKey(
                        db_column="file_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.file",
                    ),
                ),
                (
                    "message_id",
                    models.ForeignKey(
                        db_column="message_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.message",
                    ),
                ),
            ],
            options={
                "db_table": "file_message",
            },
        ),
        migrations.CreateModel(
            name="FeedbackImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("post_time", models.CharField(db_column="post_time", max_length=1024)),
                (
                    "feedback_id",
                    models.ForeignKey(
                        db_column="feedback_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.feedback",
                    ),
                ),
                (
                    "image_id",
                    models.ForeignKey(
                        db_column="image_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.image",
                    ),
                ),
            ],
            options={
                "db_table": "feedback_image",
            },
        ),
        migrations.CreateModel(
            name="FeedbackFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("post_time", models.CharField(db_column="post_time", max_length=1024)),
                (
                    "feedback_id",
                    models.ForeignKey(
                        db_column="feedback_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.feedback",
                    ),
                ),
                (
                    "file_id",
                    models.ForeignKey(
                        db_column="file_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.file",
                    ),
                ),
            ],
            options={
                "db_table": "feedback_file",
            },
        ),
        migrations.AddField(
            model_name="feedback",
            name="project_id",
            field=models.ForeignKey(
                db_column="project_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="buaadb_backend.project",
            ),
        ),
        migrations.AddField(
            model_name="feedback",
            name="student_id",
            field=models.ForeignKey(
                db_column="student_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="buaadb_backend.student",
            ),
        ),
        migrations.CreateModel(
            name="DiscussionProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "discussion_id",
                    models.ForeignKey(
                        db_column="discussion_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.discussion",
                    ),
                ),
                (
                    "project_id",
                    models.ForeignKey(
                        db_column="project_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.project",
                    ),
                ),
            ],
            options={
                "db_table": "discussion_project",
            },
        ),
        migrations.CreateModel(
            name="DiscussionMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "discussion_id",
                    models.ForeignKey(
                        db_column="discussion_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.discussion",
                    ),
                ),
                (
                    "message_id",
                    models.ForeignKey(
                        db_column="message_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.message",
                    ),
                ),
            ],
            options={
                "db_table": "discussion_message",
            },
        ),
        migrations.CreateModel(
            name="ANoticeB",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "notice_id",
                    models.ForeignKey(
                        db_column="notice_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.notice",
                    ),
                ),
                (
                    "receiver_id",
                    models.ForeignKey(
                        db_column="receiver_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Notice_receiver",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sender_id",
                    models.ForeignKey(
                        db_column="sender_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Notice_sender",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "A_notice_B",
            },
        ),
        migrations.CreateModel(
            name="AMessageB",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "message_id",
                    models.ForeignKey(
                        db_column="message_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="buaadb_backend.message",
                    ),
                ),
                (
                    "receiver_id",
                    models.ForeignKey(
                        db_column="receiver_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Message_receiver",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sender_id",
                    models.ForeignKey(
                        db_column="sender_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Message_sender",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "A_message_B",
            },
        ),
    ]