from django.shortcuts import render, get_object_or_404
from django.views import generic
from polls.models import Image, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'image_list'

    def get_queryset(self):
        return Image.objects.all

class DetailView(generic.DetailView):
    model = Image
    template_name = 'polls/detail.html'

def upvote(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    image.votes += 1
    image.save()
    return HttpResponseRedirect(reverse("polls:index"))

def downvote(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    image.votes -= 1
    image.save()
    return HttpResponseRedirect(reverse("polls:index"))
    

def cast_vote(request, image_id, score):
    image = get_object_or_404(Image, pk=image_id)
    if image.votes > 0:
        image.votes += score
        image.save()
    return HttpResponseRedirect(reverse('polls:index'))

#def index(request):
    #return render(request, 'polls/index.html')


