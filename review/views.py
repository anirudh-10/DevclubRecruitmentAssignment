from django.shortcuts import render,  get_object_or_404
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
from .models import review
from courses.models import courses

# Create your views here.

@login_required
def home(request):
    context = {
        'posts': review.objects.all()
    }
    return render(request, 'review/home.html', context)

class PostListView(ListView):
    model = review
    template_name = 'review/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

class PostDetailView(DetailView):
    model = review

class PostCreateView( LoginRequiredMixin, CreateView):
    model = review
    fields = ['instructor', 'Paper_Difficulty_out_of_10','content_covered_during_lectures_out_of_10','teaching_method_out_of_10', 'comments', 'course']

    def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)

class UserPostListView(ListView):
    model = review
    template_name = 'review/user_reviews.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return review.objects.filter(author=user).order_by('-date_posted')

class PostUpdateView( LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = review
    fields = ['instructor', 'Paper_Difficulty_out_of_10','content_covered_during_lectures_out_of_10','teaching_method_out_of_10', 'comments', 'course',]

    def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = review
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
class SearchView(ListView):
    model = review.instructor
    template_name = 'home.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = review.objects.filter(instructor__contanis=query)
          result = postresult
       else:
           result = None
       return result     