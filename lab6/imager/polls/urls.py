from django.urls import path
from . import views

app_name="polls"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    #post: /polls/1/upvote,
    path('<int:image_id>/upvote', views.upvote, name='upvote'),
    path('<int:image_id>/downvote', views.downvote, name='downvote'),
]