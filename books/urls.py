from django.urls import path
from .views import BookListAPIView, BookCreateAPIView, MyBooksAPIView, UpdateBookAPIView

app_name = 'books'

urlpatterns = [
    path("create", BookCreateAPIView.as_view(), name="create"),
    path("my_books", MyBooksAPIView.as_view(), name="my_books"),
    path("update/<int:id>", UpdateBookAPIView.as_view(), name="my_books"),
    path("<str:college_name>/<str:branch>/<str:sem>/",
         BookListAPIView.as_view(), name="book_list"),

]
