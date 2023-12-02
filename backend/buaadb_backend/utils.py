import random

from backend import settings
from .models import *


def exist_id(id):
    res = User.objects.filter(username=id).count()
    if res == 0:
        return False
    else:
        return True


def delete_file():
    pass


def store_file(file, fn, type):
    # 图片扩展名
    suffix = file.name.rsplit(".")[1]
    # 重新定义图片名
    file_name = fn + '_%d' % random.randint(0, 10000)
    # 储存图片在本地
    if type == 0:
        addr = settings.IMAGE_DIR + str(file_name) + '.' + suffix
        URL = settings.IMAGE_PATH + str(file_name) + '.' + suffix
    else:
        addr = settings.FILE_DIR + str(file_name) + '.' + suffix
        URL = settings.FILE_PATH + str(file_name) + '.' + suffix
    destination = open(addr, 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()

    if type == 0:
        result = Image.objects.create(url=URL, post_time=fn)
    else:
        result = File.objects.create(url=URL, post_time=fn)

    return result


def send_notice(time, type, profile, sender_id, receiver_id):
    sender = User.objects.get(username=sender_id)
    notice = Notice.objects.create(time=time, type=type, profile=profile)
    receiver = User.objects.get(username=receiver_id)
    ANoticeB.objects.create(sender_id=sender, receiver_id=receiver, notice_id=notice)
    print("successfully send notice")


def get_notice(username, is_sender):
    user = User.objects.get(username=username)
    if is_sender:
        notice_ids = ANoticeB.objects.filter(sender_id=user).values_list('notice_id', flat=True)
        notices = []
        for notice_id in notice_ids:
            notice = Notice.objects.get(ID=notice_id)
            notices.append({
                "id": notice_id,
                "time": notice.time,
                "type": notice.type,
                "profile": notice.profile
            })
    else:
        notice_ids = ANoticeB.objects.filter(receiver_id=user).values_list('notice_id', flat=True)
        notices = []
        for notice_id in notice_ids:
            notice = Notice.objects.get(ID=notice_id)
            notices.append({
                "id": notice_id,
                "time": notice.time,
                "type": notice.type,
                "profile": notice.profile
            })
    return notices

def exist_team_name(name):
    count = Team.objects.filter(name=name).count()

    if count == 0:
        return False
    else:
        return True

def get_role(username):
    count = Student.objects.filter(username=username).count()
    if count != 0:
        return 0
    else:
        count = Manager.objects.filter(username=username).count()
        if count != 0:
            return 1
        else:
            return 2
