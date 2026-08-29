from django.shortcuts import render, redirect , get_object_or_404
from django.db.models import Q
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'book/home.html')

def book_list_view(request):
    books = Book.objects.all()

    context = {"books": books}

    return render(request, "book/book_list.html", context)


def book_detail_view(request, book_id):

    try:
        book = Book.objects.get(pk=book_id)

        if request.user.is_authenticated:
            is_favorite = book.favorites.filter(id=request.user.id).exists()

        else:
            is_favorite = False

        context = {"book": book,'is_favorite':is_favorite}

        return render(request, "book/book_detail.html", context)

    except Book.DoesNotExist:
        context = {"message": "this book does not avaiable"}

        return render(request, "book/404.html", context)

@login_required
def book_add_genre_view(request):
    if request.method == "POST":
        genre = request.POST.get("genre")
        

        book = Category.objects.create(
            name=name,
            
        )

        return redirect("book-List")

    return render(request, "book/add_genre_book.html")

@login_required
def book_add_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        isbn = request.POST.get("isbn")
        publisher = request.POST.get("publisher")
        publish_date = request.POST.get("publish_date")
        price = request.POST.get("price")
        page = request.POST.get("page")
        genre = request.POST.getlist("genre")
        

        book = Book.objects.create(
            title=title,
            author=author,
            isbn=isbn,
            publisher=publisher,
            publish_date=publish_date,
            price=price,
            page=page,
        )

        book.genre.set(genre)
        

        return redirect("book-List")

    return render(request, "book/add_book.html")


def book_search_view(request):

    books = Book.objects.all()
    categories = Category.objects.all()

    search = request.GET.get("search")
    min_publish_date = request.GET.get("min_publish_date")
    max_publish_date = request.GET.get("max_publish_date")
    category = request.GET.get("category")


    if search:
        books = books.filter(
            Q(title__icontains=search) |
            Q(author__icontains=search)
        )

    if min_publish_date:
        books = books.filter(
            publish_date__gte=min_publish_date
        )

    if max_publish_date:
        books = books.filter(
            publish_date__lte=max_publish_date
        )

    if category:
        books = books.filter(
            categories__id=category
        )

    return render(
        request,
        "book/search.html",
        {
            "books": books
            "categories":categories
        }
    )

@login_required
def book_edit_view(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)

        if request.method == "POST":

            title = request.POST.get("title")
            author = request.POST.get("author")
            isbn = request.POST.get("isbn")
            publisher = request.POST.get("publisher")
            publish_date = request.POST.get("publish_date")
            price = request.POST.get("price")
            page = request.POST.get("page")
            genre = request.POST.getlist("genre")

            book.title = title
            book.author = author
            book.isbn = isbn
            book.publisher = publisher
            book.publish_date = publish_date
            book.price = price
            book.page = page
            book.genre.set(genre)

            book.save()

            return redirect("book-List")

        return render(request, "book/edit_book.html", {"book": book})

    except Book.DoesNotExist:
        context = {"message": "this book does not avaiable"}

        return render(request, "book/404.html", context)

@login_required
def book_delete_view(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)

        if request.method == "POST":

            book.delete()

            return redirect("book-List")

        return redirect("book-List")

    except Book.DoesNotExist:
        context = {"message": "this book does not avaiable"}

        return render(request, "book/404.html", context)

@login_required
def book_filter_delete_view(request):

    books = Book.objects.all()

    if request.method == "POST":
        search = request.POST.get("search")
        max_publish_date = request.POST.get("max_publish_date")
        min_publish_date = request.POST.get("min_publish_date")

    else:
        search = request.GET.get("search")
        max_publish_date = request.GET.get("max_publish_date")
        min_publish_date = request.GET.get("min_publish_date")

    if search:

        books = books.filter(Q(title__icontains=search) | Q(author__icontains=search))

    if max_publish_date:

        books = books.filter(publish_date__lte=max_publish_date)

    if min_publish_date:

        books = books.filter(publish_date__gte=min_publish_date)

    if request.method == "POST":

        books.delete()

        return redirect("book-List")
    return render(request, "book/filter_delete.html", {"books": books})

@login_required
def toggle_favorite(request, book_id):
    book = get_object_or_404(Book,pk=book_id)

    if request.method == "POST":

        if book.favorites.filter(id=request.user.id).exists():
           
            book.favorites.remove(request.user)

          else:
            
            book.favorites.add(request.user)

    return redirect("book-detail", book_id=book_id)
    

def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password1")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")

        if User.objects.filter(username=username).exists():
            return render(
                request,
                'book/register.html',
                { 'message' : 'you already registered please login' })

        User.objects.create_user(
            username=username,
            password=password,
            first_name=firstname,
            last_name=lastname,
            email=email)

        return redirect("Login")

    return render(
        request,
        'book/register.html')


def login_veiw(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
                username=username,
                password=password
            )

        if user is not None:

            login(request,user)

            return redirect('book-List')

        return render(
            request,
            'book/login.html',
            { 'message' : 'your username or password is not valid' }
        )
    
    return render(
            request,
            'book/login.html',
        )


def logout_view(request):

    logout(request)

    return redirect('book-List')

def my_favorite_view(request):

    fav_books = request.user.favorites.all()

    return render(
        request,
        "book/my_favorite.html",
        {
        "fav_books":fav_books
        })
    