from re import search
from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path("", blog_view, name="blog"),
    path("<int:pid>/", single_view, name="single"),
    path("category/<str:cat_name>/", blog_view, name="category"),
    path("author/<str:author_username>/", blog_view, name="author"),
    path("date/<str:datetime>/", blog_view, name="date"),
    path("search/", blog_search, name="search"),
]
