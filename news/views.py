from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "base.html")

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