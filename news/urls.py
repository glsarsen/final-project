from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_user, name="login"),
    path("article/<int:id>/", views.article, name="article"),
    path("article/<int:id>/comment/", views.comment, name="comment"),
    path("search/", views.search, name="search"),
    path("bookmarks/", views.bookmarks, name="bookmarks"),
    path("article/<int:id>/bookmark/", views.add_bookmark, name="add_bookmark"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_user, name="logout"),
]
