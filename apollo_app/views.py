from django.shortcuts import render,HttpResponse

# Create your views here.

def login(request):
    return HttpResponse("login")

def index(request):
    return HttpResponse("index")

def safe_a(request):
    print("输出A等级安全的算法")
    return HttpResponse("实现了A等级安全级别")

def safe_b(request):
    return HttpResponse("实现B级别的安全等级")

def reg(request):
    return HttpResponse("增加了注册功能")