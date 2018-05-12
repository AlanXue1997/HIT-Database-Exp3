from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from django.views import generic

from .models import User

class IndexView(generic.DetailView):
    model = User
    template_name = 'exp3/detail.html'

class UserForm(forms.Form):
    email = forms.CharField(label='邮箱')
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

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