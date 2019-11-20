from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('slika/<int:pk>/', views.DetailView.as_view(), name='detail'),
    #localhost:8000/slika/3/upvote
    path('slika/<int:image_id, pk>/upvote', views.upvote, name="upvote"),
    path('slika/<int:image id, pk>/upvote', views.downvote, name="downvote"),
]