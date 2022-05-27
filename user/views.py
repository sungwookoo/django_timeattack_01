import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from user.models import UserModel


def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/index.html')
    elif request.method == 'POST':
        data = json.loads(request.body)
        email = data['email']
        password = data['password']
        if "@" not in email:
            return HttpResponse("이메일 형식 에러")
        if len(password) < 8:
            return HttpResponse("비밀번호 길이 에러")
        UserModel.objects.create_user(username=email, email=email, password=password)
        return HttpResponse("회원가입 완료")

