from django.shortcuts import render, redirect, get_object_or_404
import psycopg2
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import NewContent
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from aiogram.utils.mixins import DataMixin
from django.contrib.postgres.search import SearchVector
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from django.views.generic import TemplateView
from django.db.models import F

connection = psycopg2.connect(
        host='127.0.0.1',
        user='bigbosadmin',
        password='admin',
        database='shop_db',
    )

connection.autocommit = True

# form to add product
def create_post(request):
    error = ''
    form = CreateForm(request.POST)
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Ошибка"
            form = CreateForm()
    data = {
        "title": "Добавить",
        "head": "Форма добавления",
        "form": form,
        "error": error,
    }
    return render(request, 'shop/createform.html', data)

# create views of all product
def show_all(request):
    base = NewContent.objects.all()
    data = {
        'test': request.build_absolute_uri(),
        'story': base,
        'title': "Список товаров",
        'head': 'Список товаров',
    }
    return render(request, 'shop/content.html', data)



def search(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('q')
        minprice = int(request.GET.get('a'))
        maxprice = int(request.GET.get('b'))

        if query == '':
            query = 'None'
        results = NewContent.objects.filter(Q(product__icontains=query))
    return render(request, 'shop/searchresults.html', {'query': query,
                                                'results': results,
                                                'maxprice': maxprice,
                                                'minprice': minprice})



#create detail view
# class ContentView(DetailView):
#     model = NewContent
#     template_name = 'shop/detailview.html'
#     content_object_name ='newcontent'

class ProductDetailView(DetailView):
    model = NewContent
    template_name = 'shop/detailview.html'
    context_object_name = 'newcontent'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        view, created = ProductView.objects.get_or_create(product=obj)
        if not created:
            view.count += 1
            view.save()
        return obj


    



# def post_detail(request, slug, pk):
#
#     # Проверяем есть ли пост с запрашиваемым слагом
#     post = get_object_or_404(NewContent, slug__iexact=slug)
#
#     if not request.session.session_key:
#         request.session.save()
#     # получаем сессию
#     session_key = request.session.session_key
#
#     is_views = PostCountViews.objects.filter(postId=post.id, sesId=session_key)
#
#     # если нет информации о просмотрах создаем ее
#     if is_views.count() == 0 and str(session_key) != 'None':
#
#         views = PostCountViews()
#         views.sesId = session_key
#         views.postId = post
#         views.save()
#
#         post.count_views += 1
#         post.save()
#
#     return render(request, 'shop/detailview.html', context={'new': post})

#create registration
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            #new_user.save()
            return redirect('success')
    else:
        print('invalid form')

    form = SignUpForm()
    data = {
        "form": form,
        "title": "Sign up",
    }
    return render(request, 'shop/signup.html', data)

def success(request):
    return render(request, 'shop/success.html')

#create profile view

@login_required
def profile(request):
    return render(request, 'shop/profile.html')

# create basket

connection = psycopg2.connect(
        host='127.0.0.1',
        user='bigbosadmin',
        password='admin',
        database='shop_db',
    )

connection.autocommit = True

def into_basket(user:str, product:str, id_product:int):
    if user != '' and product != '' and id_product != '':
        with connection.cursor() as cursor:
            requests_to_db = "INSERT INTO shop_basket (username, product, id_product) VALUES(%s, %s, %s)"
            cursor.execute(requests_to_db, (user, product, id_product))

def get_id_product(user:str):
    with connection.cursor() as cursor:
        r = """SELECT id_product FROM shop_basket WHERE username=%s"""
        cursor.execute(r, (user,))
        return cursor.fetchall()

def basket(request):
    auth_user = ''
    product = ''
    id_product = ''
    auth_user = request.user.username
    if request.method == "GET":
        id_product = int(request.GET.get('q'))
    if id_product != '':
        with connection.cursor() as cursor:
            req = """SELECT product FROM shop_newcontent WHERE id=%s"""
            cursor.execute(req, (str(id_product)))
            product = cursor.fetchone()[0]
    into_basket(str(auth_user), str(product), int(id_product))

    data = {
        'id': id_product,
        'product': product,
        'auth_user': auth_user,
    }
    return render(request, 'shop/basket.html', data)

def view_basket(request):

    auth_user = request.user.username

    results = Basket.objects.filter(Q(username__icontains=auth_user))

    v = get_id_product(str(auth_user))
    data_to_web = []
    for el in v:
        data_to_web.append(el[0])

    data = {
        'products': results,
        'user': auth_user,
        'id': data_to_web,
    }

    return render(request, 'shop/mybasket.html', data)


# create search view

# connection = psycopg2.connect(
#         host='127.0.0.1',
#         user='bigbosadmin',
#         password='admin',
#         database='shop_db',
#     )
#
# connection.autocommit = True
#
# def search_function(product, price_1, price_2):
#     with connection.cursor() as cursor:
#         cd = """SELECT id FROM shop_newcontent WHERE (product=%s AND (price>=%s AND price<=%s))"""
#         cursor.execute(cd, (product, price_1, price_2))
#         all_data = cursor.fetchall()
#         return all_data

# def search_request(request):
#     # here i get data
#
#
#
#
#     all_data = search_function(product, price_1, price_2)
#     data = []
#     for i in range(len(all_data)):
#         data.append(all_data[i][0])



# its not active now

#login view

def login_request(request):
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = 'u are login'
                    return redirect('home')
                else:
                    message = 'error'
                    return redirect('signup')
            else:
                message = 'error'
                return redirect('main')
    else:
        form = LoginForm()
    data = {
        'head': message,
        'form': form,
    }
    return render(request, 'shop/login.html', data)

#logout form
def logout_request(request):
    logout(request)

    return render(request, 'shop/logout.html')

