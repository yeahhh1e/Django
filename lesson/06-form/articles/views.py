from django.shortcuts import render, redirect
# 모델 클래스 가져오기
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    # url로부터 전달받은 pk를 활용해 데이터를 조회
    # article = Article.objects.get(id=pk)
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)



def create(request):
    # 요청 메서드가 POST일 때
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    # 요청 메서드가 POST가 아닐 때 (GET, PUT, DELETE 등 다른 메서드)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
   


def delete(request, pk):
    # 어떤 게시글 삭제할지 조회
    article = Article.objects.get(pk=pk)

    # 조회한 게시글 삭제
    article.delete()
    return redirect('articles:index')



def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article) # 수정할 때 원래 내용 보이게 하기
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)


# 과거 코드
# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     # 게시글 작성 페이지 응답
#     return render(request, 'articles/create.html', context)

# 과거 코드 
# def create(request):
#     # 1. 모델폼 인스턴스 생성 (+ 사용자 입력 데이터를 통째로 인자로 작성)
#     form = ArticleForm(request.POST)
    
#     # 2. 유효성 검사
#     if form.is_valid():
#         article = form.save()
#         return redirect('articles:detail', article.pk)
    
#     # 유효성 검사 실패 시 context로 넘겨주기
#     # 실패한 이유와 함께 넘겨줌
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)

#     # 3. 저장
    
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
#     # article = Article(title=title, content=content)

 # 과거 코드
# def edit(request, pk):
#     # 어떤 게시글을 수정할지 조회
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article) # 수정할 때 원래 내용 보이게 하기
#     context = {
#         'article': article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)   

# 과거 코드
# def update(request, pk):
#     article = Article.objects.get(pk=pk)
#     # 1. 모델폼 인스턴스 생성(+사용자 입력 데이터 & 기존 데이터)
#     form = ArticleForm(request.POST, instance=article)
#     # 2. 유효성 검사
#     if form.is_valid():
#         form.save()
#         return redirect('articles:detail', article.pk)
#     context = {
#         'article' : article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article.title = title
    # article.content = content
    # article.save()

    

