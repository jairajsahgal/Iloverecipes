
from .models import Book, Post, BookPage

from django.shortcuts import render

from django.views.generic import ListView, DetailView


from django.views import generic
from django.urls import reverse_lazy

from django.views.generic import DetailView 


def Main(request):

    recent5 = Book.objects.all()[:5]

    pages=BookPage.objects.all()


    context = {
        'recent': recent5,
        'pages': pages,
    }
   
    return render(request, 'home.html', context)


def base(request):

        #books = Book.objects.all()
        recent5 = Book.objects.all()[:5]
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



