from django.urls import path

from .views import PostList, PostDetail, AuthorList, AuthorDetail,\
    CategoryList, CategoryDetail  # импортируем наше представление

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам
    # у нас останется пустым, позже станет ясно, почему
    path('', PostList.as_view()),
    # т. к. сам по себе это класс, то нам надо представить этот
    # класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', PostDetail.as_view()),
    # pk — это первичный ключ статьи, который будет выводиться у нас в шаблон
    path('', AuthorList.as_view()),
    path('<int:pk>', AuthorDetail.as_view()),
    path('', CategoryList.as_view()),
    path('<int:pk>', CategoryDetail.as_view()),
]
