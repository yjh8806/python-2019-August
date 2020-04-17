from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# 서브앱의 views.py는 직접 HttpResponse를 반환하거나 (간단한 내용일 경우에만)

# render() 함수를 이용하여 template(HTML)으로 연결한다

# 템플릿은 서브앱/templates/서브앱/***.html 의 형식으로 준비한다

def index(request):
    # return HttpResponse('<script>alert("Hello, world !!");</script>')
    return render(request, 'index/index.html')

def ex01(request):
    return render(request, 'index/ex01.html')

# 클래스 뷰를 사용하기 위해, 모든 내용을 작성할 필요 없이
# 미리 만들어진 View클래스를 상속받는 자식클래스를 작성하면 된다

from django.views.generic import View

class Ex02(View):
    # 만약 요청이 GET방식으로 전달되면, get함수가 처리한다
    def get(self, request):
        return render(request, 'index/ex02_form.html')

    # 만약 요청이 POST방식으로 전달되면 post함수가 처리한다
    def post(self, request):
        userid = request.POST['userid']
        userpw = request.POST['userpw']

        if userid == 'itbank' and userpw == 'it':
            return render(request, 'index/ex02_result.html', {'msg' : '로그인 성공'})
        else:
            return render(request, 'index/ex02_result.html')


class Ex03(View):
    def get(self, request):
        return render(request, 'index/ex03_form.html')

    def post(self, request):
        n1 = int(request.POST['n1'])    # 사용자 입력값을 파이썬 변수에 저장
        n2 = int(request.POST['n2'])
        oper = request.POST['oper']

        if oper == '+': answer = n1 + n2    # 연산자에 따라서 answer 변수의 값을 결정
        if oper == '-': answer = n1 - n2
        if oper == '*': answer = n1 * n2
        if oper == '/': answer = n1 / n2
        
        context = {     # 템플릿에게 전달할 데이터를 변수이름 : 값의 형식으로 묶어서 전달
            'n1' : n1,
            'n2' : n2,
            'oper' : oper,
            'answer' : answer,
        }

        return render(request, 'index/ex03_result.html', context)


