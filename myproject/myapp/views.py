from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'myapp/index.html')

def load(req):
    return render(req, 'myapp/load.html')

def inference(req):
    return render(req, 'myapp/inference.html')

def test1(req):
    return render(req, 'myapp/test_1.html')

def register(req):
    return render(req, 'myapp/register.html')
