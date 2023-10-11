from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Article, User, Comment, Bookmark

# Create your views here.
def index(request):
    articles = Article.objects.all()[:10]
    return render(request, "index.html", {"articles": articles})

def login_user(request):
    if request.method == "POST":
        name = request.POST["user_name"]
        password = request.POST["password"]
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "login.html", {"authenticated": False})
    else:
        return render(request, "login.html")

# www.newsportal.com/article/5/
# www.newsportal.com/article/?article_id=5
def article(request, id):
    article = Article.objects.get(id=id)
    in_bookmarks = False
    for bookmark in request.user.bookmarks.all():
        if article == bookmark.article:
            in_bookmarks = True
    return render(request, "article.html", {"article": article, "in_bookmarks": in_bookmarks})

def comment(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            content = request.POST["content"]
            article = Article.objects.get(id=id)
            user = request.user
            comment = Comment(content=content, article=article, user=user)
            comment.save()
            return redirect("article", id)
        else:
            return render(request, "comment.html")
    else:
        return redirect("article", id)

def search(request):
    return render(request, "base.html")

def bookmarks(request):
    if request.user.is_authenticated:
        return render(request, "bookmarks.html")
    else:
        return redirect("index")

def add_bookmark(request, id):
    article = Article.objects.get(id=id)
    
    for bookmark in request.user.bookmarks.all():
        if article == bookmark.article:
            bookmark.delete()
            return redirect("article", id)
        
    bookmark = Bookmark(article=article, user=request.user)
    bookmark.save()
    return redirect("article", id)

def register(request):
    if request.method == "POST":
        # name = request.POST["first_name"]
        # lastname = request.POST["last_name"]
        username = request.POST["user_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if password != password2:
            return render(request, "register.html", {"invalid_password": True})
        else:
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            return redirect("index")
    else:
        return render(request, "register.html")

def logout_user(request):
    logout(request)
    return redirect("index")