from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("article/<int:id>/", views.article, name="article"),
    path("search/", views.search, name="search"),
    path("bookmarks/", views.bookmarks, name="bookmarks"),
    path("register/", views.register, name="register")
]
