import sqlparse

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import Q, Count
# from django.db import connection

from .models import User, Education, Work, Diary

# ------------------------------
# Login
# ------------------------------


class IndexView(generic.DetailView):
    model = User
    template_name = 'exp3/index.html'


class UserForm(forms.Form):
    email = forms.CharField(label='邮箱')
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


def login(request):
    if request.method == 'POST':
        # 获取表单信息
        uf = UserForm(request.POST)
        if uf.is_valid():
            email = uf.cleaned_data['email']
            password = uf.cleaned_data['password']

            # 判断用户密码是否匹配
            try:
                user = User.objects.get(email=email)
            except(KeyError, User.DoesNotExist):
                return render(request, 'exp3/login.html', {
                    'uf': uf,
                    'error_message': "用户名错误.",
                })
            else:
                if password==user.password:
                    info = '登录成功！'
                    return HttpResponseRedirect(reverse('exp3:index', args=(user.id,)))
                else:
                    info = '请检查密码是否正确!'
                    return render(request, 'exp3/login.html', {
                        'uf': uf,
                        'error_message': "密码错误.",
                    })

    uf = UserForm()
    return render(request, 'exp3/login.html', {'uf': uf})

# ------------------------------
# About work
# ------------------------------

class WorkView(generic.DetailView):
    model = User
    template_name = 'exp3/work.html'

def newWorkInfo(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.work_set.create(
        company=request.POST['company'],
        position=request.POST['position'],
        begin=request.POST['begin'],
        end=request.POST['end']
    )
    return HttpResponseRedirect(reverse('exp3:work', args=(user.id,)))

def deleteWorkInfo(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    work.delete()
    return HttpResponseRedirect(reverse('exp3:work', args=(work.user.id,)))

def changeWorkInfo(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    try:
        work.company = request.POST['company']
        work.position = request.POST['position']
        work.begin = request.POST['begin']
        work.end = request.POST['end']
        work.save()
    except:
        return HttpResponseRedirect(reverse('exp3:work', args=(work.user.id,)))
    else:
        return HttpResponseRedirect(reverse('exp3:work', args=(work.user.id,)))


# ------------------------------
# About Education
# ------------------------------

class EducationView(generic.DetailView):
    model = User
    template_name = 'exp3/education.html'

def newEducationInfo(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.education_set.create(
        school=request.POST['school'],
        level=request.POST['level'],
        begin=request.POST['begin'],
        end=request.POST['end']
    )
    return HttpResponseRedirect(reverse('exp3:education', args=(user.id,)))

def deleteEducationInfo(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    education.delete()
    return HttpResponseRedirect(reverse('exp3:education', args=(education.user.id,)))

def changeEducationInfo(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    try:
        education.school = request.POST['school']
        education.level = request.POST['level']
        education.begin = request.POST['begin']
        education.end = request.POST['end']
        education.save()
    except:
        return HttpResponseRedirect(reverse('exp3:education', args=(education.user.id,)))
    else:
        return HttpResponseRedirect(reverse('exp3:education', args=(education.user.id,)))

# ------------------------------
# About Info
# ------------------------------

def changeInfo(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    try:
        user.name = request.POST['name']
        user.sex = request.POST['sex']
        user.birth = request.POST['birth']
        user.address = request.POST['address']
        user.save()
    except:
        return HttpResponseRedirect(reverse('exp3:index', args=(user.id,)))
    else:
        return HttpResponseRedirect(reverse('exp3:index', args=(user.id,)))

# ------------------------------
# About diary
# ------------------------------

def diaryList(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    diarys = Diary.objects.filter(Q(author__in=user.follow.all()) | Q(author__exact=user)).order_by('-date')
    stat = sqlparse.format(str(diarys.query).replace('`', ''), reindent=True, keyword_case='upper')
    return render(request, 'exp3/diaryList.html', {'diarys' : diarys, 'user' : user, 'stat' : stat})

def diarypage(request, user_id, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'exp3/diary.html', {'diary': diary, 'user' : user })

def editDiary(request, user_id, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'exp3/editDiary.html', {'diary': diary, 'user': user})

def pushEditDiary(request, user_id, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    try:
        diary.author = User.objects.get(pk=user_id)
        diary.title = request.POST['title']
        diary.content = request.POST['content']
        diary.date = timezone.now()
        diary.save()
    except:
        return HttpResponseRedirect(reverse('exp3:diary', args=(user_id, diary_id,)))
    else:
        return HttpResponseRedirect(reverse('exp3:diary', args=(user_id, diary_id,)))

def deleteEditDiary(request, user_id, diary_id):
    diary = get_object_or_404(Diary, pk=diary_id)
    diary.delete()
    return HttpResponseRedirect(reverse('exp3:diaryList', args=(user_id,)))

class NewDiaryView(generic.DetailView):
    model = User
    template_name = 'exp3/newDiary.html'

def pushNewDiary(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    diary = user.diary_set.create(
        author=user,
        title=request.POST['title'],
        content=request.POST['content'],
        date=timezone.now()
    )
    return render(request, 'exp3/diary.html', {'diary': diary, 'user' : user })

# ------------------------------
# About diary
# ------------------------------

def follow(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    users = user.follow.all().annotate(num_diary=Count('diary')).values('name','num_diary','id')
    stat = sqlparse.format(str(users.query).replace('`', ''), reindent=True, keyword_case='upper')
    return render(request, 'exp3/follow.html', {'user': user, 'users': users, 'stat': stat})

def addFollow(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    ppp = user.follow.all()
    users = User.objects.exclude(pk__in=ppp.values_list('pk', flat=True)).annotate(num_diary=Count('diary')).values('name','num_diary','id')
    stat = sqlparse.format(str(users.query).replace('`', ''), reindent=True, keyword_case='upper')
    return render(request, 'exp3/addFollow.html', {'user': user, 'users': users, 'stat': stat})

def unfollow(request, user_id, u_id):
    user = get_object_or_404(User, pk=user_id)
    u = get_object_or_404(User, pk=u_id)
    user.follow.remove(u)
    return HttpResponseRedirect(reverse('exp3:follow', args=(user_id,)))

def doAddFollow(request, user_id, u_id):
    user = get_object_or_404(User, pk=user_id)
    u = get_object_or_404(User, pk=u_id)
    user.follow.add(u)
    return HttpResponseRedirect(reverse('exp3:follow', args=(user_id,)))