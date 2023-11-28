from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView


urlpatterns = [
    path("", PostListView.as_view(), name="list"),   #just post/ as defined in our config urls.py patterns. 
    path("new/", PostCreateView.as_view(), name="new"),
    path("<int:pk>/", PostDetailView.as_view(), name="detail"),
]