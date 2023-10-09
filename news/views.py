from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()[:10]
    return render(request, "index.html", {"articles": articles})

def login(request):
    return render(request, "base.html")

# www.newsportal.com/article/5/
# www.newsportal.com/article/?article_id=5
def article(request, id):
    return render(request, "base.html")

def search(request):
    return render(request, "base.html")

def bookmarks(request):
    return render(request, "base.html")

def register(request):
    return render(request, "base.html")