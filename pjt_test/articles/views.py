from django.shortcuts import render

# Create your views here.
def hello(request):
    print('hello')
    print(request)
    return render(request, 'articles/index.html')