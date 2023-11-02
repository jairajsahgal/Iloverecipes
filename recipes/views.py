
from django.views.generic import ListView, DetailView
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import DetailView 
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.views import View 
from .models import Book, Post, BookPage,UserProfile,UserBook, UserBookPage, BookPage

from django.shortcuts import render

from django.http import HttpResponse

from .models import UserBook, UserBookPage

def Main(request):

    recent5 = Book.objects.order_by('-id')[:5]  # Order by id in descending order to get the latest 5 books

    all_books = Book.objects.all()

    pages = BookPage.objects.all()

    context = {

        'recent': recent5,

        'pages': pages,

        'all': all_books,

    }

    return render(request, 'home.html', context)


def base(request):
        

        recent5 = Book.objects.order_by('-id')[:5]
        
        all= Book.objects.all()
        
        pages=BookPage.objects.all()

        context = {
        'all'   : all,
        'recent': recent5,
        'pages' : pages,
    }
        return render(request, 'recipes/base.html',context)


def link_view(request): 
    a = Book.objects.filter(title__istartswith='a').order_by('title')
    b = Book.objects.filter(title__istartswith='b').order_by('title')
    c = Book.objects.filter(title__istartswith='c').order_by('title')
    d = Book.objects.filter(title__istartswith='d').order_by('title')
    e = Book.objects.filter(title__istartswith='e').order_by('title')
    f = Book.objects.filter(title__istartswith='f').order_by('title')
    g = Book.objects.filter(title__istartswith='g').order_by('title')
    h = Book.objects.filter(title__istartswith='h').order_by('title')
    i = Book.objects.filter(title__istartswith='i').order_by('title')
    j = Book.objects.filter(title__istartswith='j').order_by('title')
    k = Book.objects.filter(title__istartswith='k').order_by('title')
    l = Book.objects.filter(title__istartswith='l').order_by('title')
    m = Book.objects.filter(title__istartswith='m').order_by('title')
    n = Book.objects.filter(title__istartswith='n').order_by('title')
    o = Book.objects.filter(title__istartswith='o').order_by('title')
    p = Book.objects.filter(title__istartswith='p').order_by('title')
    q = Book.objects.filter(title__istartswith='q').order_by('title') 
    r = Book.objects.filter(title__istartswith='r').order_by('title')
    s = Book.objects.filter(title__istartswith='s').order_by('title')
    t = Book.objects.filter(title__istartswith='t').order_by('title')
    u = Book.objects.filter(title__istartswith='u').order_by('title')
    v = Book.objects.filter(title__istartswith='v').order_by('title')
    w = Book.objects.filter(title__istartswith='w').order_by('title')
    x = Book.objects.filter(title__istartswith='x').order_by('title')
    y = Book.objects.filter(title__istartswith='y').order_by('title')
    z = Book.objects.filter(title__istartswith='z').order_by('title')


    context = { 'a': a,
               'b': b,
               'c': c,
               'd':d,
               'e' :e, 
               'f' :f, 
               'g' :g, 
               'h' :h, 
               'i' :i, 
               'j' :j, 
               'k' :k, 
               'l' :l, 
               'm' :m,
               'n' :n, 
               'o' :o, 
               'p' :p,   
               'q' :q, 
               'r' :r, 
               's' :s, 
               't' :t, 
               'u' :u, 
               'v' :v, 
               'w' :w, 
               'x' :x, 
               'y' :y, 
               'z' :z, 
               } 
    return render(request, 'recipes/links.html', context)

def search_results(request):

    search_term = request.GET.get('search_term')
    if search_term:
        search_results = BookPage.objects.filter(keywords__contains=search_term)
    else:
        search_results = None
    
    context = {'search_results': search_results}
    return render(request, 'search_results.html', context)

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

class blogview(ListView):
    model = Post
    template_name = 'another_template.html'

class videopage(DetailView):
    model = Post
    template_name = 'videoclass.html'

def search_results(request):

    search_term = request.GET.get('search_term')

    search_results = []

    if search_term:

        search_results = BookPage.objects.filter(keywords__contains=search_term)

        MEDIA_UR='https://d17usxoyp786nd.cloudfront.net/'
        

    context = {'search_results': search_results, 'MEDIA_URL': MEDIA_UR}

    return render(request, 'search_results.html', context)

def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            recent5 = Book.objects.order_by('-id')[:5]  # Order by id in descending order to get the latest 5 books

            all_books = Book.objects.all()
            pages = BookPage.objects.all()
            context = {

                    'recent': recent5,

                    'pages': pages,

                    'all': all_books,

                    }

            return render(request, 'home.html', context)

        else:

            # Display an error message

            error_message = "Invalid credentials"

            return render(request, 'Error.html', {'error_message': error_message})

    else:

        return render(request, 'login.html')

def register_view(request):

    if request.method == 'POST':

        form = RegistrationForm(request.POST)

        if form.is_valid():

            # Create a new user account using Django's User model

            user_data = form.cleaned_data

            new_user = User.objects.create_user(

                username=user_data['username'],

                email=user_data['email'],

                password=user_data['password'],

            )

            try:

                send_mail(
                    f"Welcome {new_user.username}",
                    "Thank you for joining I love cookbooks",
                    "admin@ilovecookbooks.org",
                    [new_user.email],
                    fail_silently=False,
                )

            except:

                print("sending an email failed")
            

            return redirect('recipes:login')

    else:

        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


def UserProfileView(request, pk):

    try:
        print("trying to get user info")

        user_profile = UserProfile.objects.get(pk=pk)

        print("user has profile")

        user_books = UserBook.objects.filter(user=user_profile.user)

        print("user has books")

        context = {

            'user_profile': user_profile,

            'user_books': user_books,

        }

    except:

        context={}
        print("You dont have a profile looooooser!!!")

    return render(request, 'User_Profile.html', context)


def user_book_pages(request, user_book_id):

    try:

        user_book = UserBook.objects.get(id=user_book_id, user=request.user)

        user_book_pages = UserBookPage.objects.filter(user_book=user_book).order_by('order')

        book_pages = [user_book_page.book_page for user_book_page in user_book_pages]



        context = {

            'user_book': user_book,

            'user_book_pages': user_book_pages,

            'book_pages': book_pages,

        }



        return render(request, 'user_books.html', context)

    except UserBook.DoesNotExist:

        return HttpResponse("User Book not found or unauthorized", status=404)



def page_view(request, page_id, book_id):

    page = get_object_or_404(BookPage, pk=page_id)

    book = get_object_or_404(Book, pk=book_id)

    context = {

        'page': page,

        'book': book,

    }

    return render(request, 'page_view.html', context)
