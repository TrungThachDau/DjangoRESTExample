
from django.urls import path,include
from . import views
from rest_framework import routers

from .views import BookUpdateView, GetAllTypeBook

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
urlpatterns = [
    # path('books/', views.books, name='books'),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),

    path('books/<int:id>/', BookUpdateView.as_view(), name='book-update'),

    path('type_book/', views.TypeBookList.as_view()),
    path('typebooks/', GetAllTypeBook, name='typebooks-list'),
]