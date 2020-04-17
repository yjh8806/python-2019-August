from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    src = '''
    <div style="font-size:40pt;
                font-weight:bolder;
                text-align:center;
                font-family:궁서;
                color:chocolate;">
                첫번째 페이지 테스트
                </div>
    '''
    return HttpResponse(src)