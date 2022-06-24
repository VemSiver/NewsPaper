from django.views.generic import ListView, DetailView  # импортируем класс, который говорит нам о том, что в этом представлении
# мы будем выводить список объектов из БД
from .models import Author, Category, Post, PostCategory, Comment
from datetime import datetime

# Create your views here.
class PostList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'newspost.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все
    # инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'newspost'  # это имя списка, в котором будут лежать все объекты, его надо указать,
    # чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-id')

    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон.
    # В возвращаемом словаре context будут храниться все переменные. Ключи этого словаря и есть переменные,
    # к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context[
            'value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере
                              # посмотреть работу другого фильтра
        return context

# создаём представление, в котором будут детали конкретного отдельного поста
class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного поста
    template_name = 'newspostdet.html'  # название шаблона будет newspostdet.html
    context_object_name = 'newspost'  # название объекта. в нём будет

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context[
            'value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере
                              # посмотреть работу другого фильтра
        return context

class AuthorList(ListView):
    model = Author  # указываем модель, объекты которой мы будем выводить
    template_name = 'newsauthor.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все
    # инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'newsauthor'  # это имя списка, в котором будут лежать все объекты, его надо указать,
    # чтобы обратиться к самому списку объектов через HTML-шаблон

# создаём представление, в котором будут детали конкретного отдельного товара
class AuthorDetail(DetailView):
    model = Author  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'newsauthor.html'  # название шаблона будет newsauthor.html
    context_object_name = 'newsauthor'  # название объекта. в нём будет

class CategoryList(ListView):
    model = Category  # указываем модель, объекты которой мы будем выводить
    template_name = 'newscategory.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все
    # инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'newscategory'  # это имя списка, в котором будут лежать все объекты, его надо указать,
    # чтобы обратиться к самому списку объектов через HTML-шаблон

class CategoryDetail(DetailView):
    model = Author  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'newscategory.html'  # название шаблона будет product.html
    context_object_name = 'newscategory'  # название объекта. в нём будет
