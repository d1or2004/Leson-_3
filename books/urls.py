from django.urls import path
from .views import BookCreatesAPIView, BookDetailAPIView, BookDeleteAPIView, BookUpdateAPIView, \
    BookCreateAPIView

urlpatterns = [
    path('books/', BookCreatesAPIView.as_view()),
    path('books/<int:pk>/', BookDetailAPIView.as_view()),
    path('books/<int:pk>/delete/', BookDeleteAPIView.as_view()),
    path('books/<int:pk>/'
         ' h/', BookUpdateAPIView.as_view()),
    path('books/create/', BookCreateAPIView.as_view()),
]
