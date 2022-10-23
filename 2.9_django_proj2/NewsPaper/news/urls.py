from django.urls import path
from .views import ListPost, DetailPost, show_all_category, ListCategory

urlpatterns = [
    path('', ListPost.as_view()),
    path('<int:pk>', DetailPost.as_view()),
    path('<int:pk>', show_all_category),
    path('<int:pk>', ListCategory.as_view())

    ]
