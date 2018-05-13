from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from django.views import generic

from .models import User, Education, Work

class IndexView(generic.DetailView):
    model = User
    template_name = 'exp3/index.html'

class EducationView(generic.DetailView):
    model = User
    template_name = 'exp3/education.html'

class WorkView(generic.DetailView):
    model = User
    template_name = 'exp3/work.html'

class UserForm(forms.Form):
    email = forms.CharField(label='邮箱')
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

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

def login(request):
    if request.method == 'POST':
        ##获取表单信息
        uf = UserForm(request.POST)
        if uf.is_valid():
            email = uf.cleaned_data['email']
            password = uf.cleaned_data['password']

            ##判断用户密码是否匹配
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