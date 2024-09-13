from django.shortcuts import render

# Create your views here.
def index(request): # 위치 인자 필수
    # 메인페이지를 응답
    return render(request, 'articles/index.html') # render의 첫번째 인자를 request로 받아야 함
                                         # render: 페이지를 렌더링하는 함수