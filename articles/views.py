from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormMixin
from django.urls import reverse_lazy 
from .models import Article, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm
class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'



class ArticleDetailView(DetailView, FormMixin):
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'
    form_class = CommentForm
    success_url = reverse_lazy('article_list')

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk':self.get_object().id})


    def post(self,request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView): 
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url = 'login'


class ArticleDeleteView(LoginRequiredMixin, DeleteView): 
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment_new.html'
    fields = ('comment', )
    login_url = 'login'
