from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from polls.models import Image
from django.urls import reverse
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'image_list'

    def get_queryset(self):
        return Image.objects.all

class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Image

def upvote(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    image.votes += 1
    image.save()
    return HttpResponseRedirect(reverse('polls:index'))


def downvote(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    image.votes -= 1
    image.save()
    return HttpResponseRedirect(reverse('polls:index'))


