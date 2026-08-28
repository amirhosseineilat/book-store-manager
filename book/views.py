from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from .models import *


def book_list_view(request):
    books = Book.objects.all()

    context = { 'books' : books }

    return render(
        request,
        'book_list.html',
        context)


def book_detail_view(request,book_id):
    
    try:
        book = get_object_or_404(pk=book_id)

        context = { 'books' : books }

        return render(
            request,
            'book_list.html',
            context)

    except Book.DoesNotExist:
        context = { 'message' : 'this book does not avaiable' }

        return render(
            request,
            '404.html',
            context)


def book_add_view(request):
    
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        publisher = request.POST.get('publisher')
        publish_date = request.POST.get('publish_date')
        price = request.POST.get('price')
        page = request.POST.get('page')
        favorites = request.POST.get('favorites')
        genre = request.POST.get('genre')

        Book.objects.create(
            title,
            author,
            isbn,
            publisher,
            publish_date,
            price,
            page,
            favorites,
            genre)

        return redirect('book-List')

    return render(request,'add_book.html')


def book_search_view(request):
    
    books.objects.all()

    search = request.GET.get('search')

    if search:

        books = Books.filter(
            Q(title__icontains=search)|
            Q(author__icontains=search))

    return render(
        request,
        'search.html'
        { 'books' : books })


def book_edit_view(request,book_id):
    try:
        book = get_object_or_404(pk=book_id)

        if request.method == "POST":

            title = request.POST.get('title')
            author = request.POST.get('author')
            isbn = request.POST.get('isbn')
            publisher = request.POST.get('publisher')
            publish_date = request.POST.get('publish_date')
            price = request.POST.get('price')
            page = request.POST.get('page')
            favorites = request.POST.get('favorites')
            genre = request.POST.get('genre')

            book.title = title
            book.author = author
            book.isbn = isbn
            book.publisher = publisher
            book.publish_date = publish_date
            book.price = price
            book.page = page
            book.favorites = favorites
            book.genre = genre

            book.save()

            return redirect('book-List')

        return render(
        request,
        "edit_book.html",
        {"book": book}
    )

        

    except Book.DoesNotExist:
        context = { 'message' : 'this book does not avaiable' }

        return render(
            request,
            '404.html',
            context)


def book_delete_view(request):
    try:
        book = get_object_or_404(pk=book_id)

        if request.method == "POST":
            
            book.delete()

            return redirect('book-List')

        return redirect('book-List')

    except Book.DoesNotExist:
        context = { 'message' : 'this book does not avaiable' }

        return render(
            request,
            '404.html',
            context)


def book_filter_view(request):

    books = Book.objects.all()

    max_publish_date = request.GET.get('max_publish_date')
    min_publish_date = request.GET.get('min_publish_date')

    if max_publish_date:

        books = books.filter(publish_date__lte=max_publish_date)

    if min_publish_date:

        books = books.filter(publish_date__gte=min_publish_date)

    return render(
        request,
        'search.html'
        { 'books' : books })

def book_filter_delete_view(request):
    
    books = Book.objects.all()

    search = request.GET.get('search')
    max_publish_date = request.GET.get('max_publish_date')
    min_publish_date = request.GET.get('min_publish_date')

    if search:

        books = Books.filter(
            Q(title__icontains=search)|
            Q(author__icontains=search))

    if max_publish_date:

        books = books.filter(publish_date__lte=max_publish_date)

    if min_publish_date:

        books = books.filter(publish_date__gte=min_publish_date)

    book.delete()

    return render(
        request,
        'filter_delete.html'
        )
