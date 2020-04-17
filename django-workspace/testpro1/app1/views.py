from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    src = '''
    <marquee>
        <h1>Hello, world !!</h1>
    </marquee>
    '''
    return HttpResponse(src)

def ex01(request):
    # 템플릿 사용해서 데이터 전달하기
    name = '원종래'
    age = 27
    context = {
        'name' : name,
        'age' : age,
    }
    response = render(request, 'app1/ex01.html', context)
    return response

def ex02(request):
    return render(request, 'app1/ex02.html')

def ex03(request):
    name = request.GET['name']
    age = request.GET['age']
    context = {
        'name' : name,
        'age' : age,
    }
    return render(request, 'app1/ex03.html', context)
