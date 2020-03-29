from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import courses
def courses(request):
    context = {
        'posts': courses.objects.all()
    }
    return render(request, 'courses/about.html', context)
class PostListView(ListView):
    model = courses
    template_name = 'courses/courses.html'
    context_object_name = 'posts'
    paginate_by = 6
class PostDetailView(DetailView):
    model = courses

class PostCreateView( LoginRequiredMixin, CreateView):
    model = courses
    fields = ['courses', 'detail']

    def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)




