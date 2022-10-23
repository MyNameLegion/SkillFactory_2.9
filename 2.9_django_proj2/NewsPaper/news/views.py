from django.views.generic import ListView, DetailView
from .models import Post, Category
from django.shortcuts import render


class ListPost(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-date_time'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'

class ListCategory(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Category
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'category'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'post.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'cate'

class DetailPost(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


def show_all_category(request):
    categories = Category.objects.all()
    return render(request, 'post.html', {
        'categories': categories
    })
