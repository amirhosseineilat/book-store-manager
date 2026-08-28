from django.urls import path
from . import views

urlpatterns = [
    path('List/',views.book_list_view,name='book-List'),
    path('Add/',views.book_add_view,name='book-Add'),
    path('Search/',views.book_search_view,name='book-Add'),
    path('Edit/',views.book_edit_view,name='book-Edit'),
    path('Delete/',views.book_delete_view,name='book-Delete'),
    path('Filter/',views.book_filter_view,name='book-Filter'),
]
