from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def home(request):
    return render(request, 'blog/home.html', {'title': 'Home', 'posts': Article.objects.all()})

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/home.html'
    context_object_name ='posts'
    ordering = ['-date_posted']
    paginate_by = 2

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article.html'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model= Article
    template_name = 'blog/article_form.html'
    fields = ['title','content']

    def form_valid(self, form): #dzieki temu możemy przypisywać artykuł do aktualnie zalogowanego użytkownika
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'blog/article.form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): # sprawdzamy, czy użytkownik jest autorem postu i może wprowadzać zmiany
        article = self.get_object()
        return self.request.user == article.author #sprawdzanie czy osoba zalogowana to autor artykułu


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'blog/delete.html'

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author