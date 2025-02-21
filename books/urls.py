
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
urlpatterns = [
    # path('books/', views.books, name='books'),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]