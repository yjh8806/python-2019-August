from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'subapp1/index.html')

from subapp1.models import Member

def ex01(request):
    q = Member.objects.all()
    context = {
        'memberlist' : q ,
    }
    return render(request, 'subapp1/ex01_memberlist.html', context)

from django.views.generic import View

class Ex02(View):
    def get(self, request):   # 주소창을 통한 입력
        return render(request, 'subapp1/ex02_form.html')

    def post(self, request):  # <form> 태그의 method속성이 post인 경우
        name = request.POST['name']             # 사용자가 입력한 검색어를 전달받고
        q = Member.objects.all().filter()    # 검색어로 DB에서 검색
        context = {     # 결과를 memberlist라는 이름으로 context에 추가
            'memberlist' : q ,
        }
        return render(request, 'subapp1/ex02_result.html', context)

from subapp1.models import Account

class Ex03(View):
    def get(self, request):
        return render(request, 'subapp1/login.html')

    def post(self, request):
        userid = request.POST['userid']
        userpw = request.POST['userpw']
        q = Account.objects.all().filter(userid=userid)
        context = {
            'msg' : '로그인 실패',
        }
        for account in q:
            if userid == account.userid:
                if userpw == account.userpw:
                    context = {
                        'msg' : account.username + ', 로그인 성공',
                    }
        return render(request, 'subapp1/check.html', context)