from django.shortcuts import render

# Create your views here.

from django.views.generic import View

from .models import Member

class Index(View):
    def get(self, request):
        return render(request, 'index/index.html')  # templates

    def post(self, request):
        userid = request.POST['userid']
        userpw = request.POST['userpw']

        login = Member.objects.all().filter(userid=userid)    
        # 여러 개 중에서 조건에 맞는 결과를 반환
        
        # login = Member.objects.get(userid=userid)
        # 제시한 조건에 대해서 반드시 결과가 있는 경우에만 사용
        
        if len(login) != 0 and login[0].userpw == userpw:
            # 세션에 계정 이름과 사용자 이름을 저장 (개별 문자열을 저장)
            request.session['userid'] = login[0].userid
            request.session['username'] = login[0].username
            
            return render(request, 'index/check.html', {'result' : True})
        else:
            return render(request, 'index/check.html', {'result' : False})

from django.http import HttpResponseRedirect    # redirect : 클라이언트에게 지정한 주소로 이동해라
from django.contrib.sessions.models import Session

def logout(request):
    Session.objects.all().delete()  # 세션이 DB에 저장되는 형식이므로, DB와 동일하게 삭제함수를 호출
    return HttpResponseRedirect('/')    # 파일이름이 없으니까 index를 요청한다