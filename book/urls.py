from django.urls import path
from . import views

urlpatterns = [
    path("List/", views.book_list_view, name="book-List"),
    path("Detail/<int:book_id>/", views.book_detail_view, name="book-Detail"),
    path("Add/", views.book_add_view, name="book-Add"),
    path("Add/Genre", views.book_add_gerne_view, name="book-Add-Genre"),
    path("Search/", views.book_search_view, name="book-Search"),
    path("Edit/<int:book_id>/", views.book_edit_view, name="book-Edit"),
    path("Delete/<int:book_id>", views.book_delete_view, name="book-Delete"),
    path("Filter/Delete", views.book_filter_delete_view, name="book-Filter-Delete"),
    path("Favorite/<int:book_id>/", views.toggle_favorite, name="book-Favorite"),
    path("MyFavorites/",my_favorite_view,name"book-MyFavorites")
]
