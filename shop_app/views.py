from django.shortcuts import render

# Create your views here.
# импортируем из стандартной сборки Django
from django.http import HttpResponse
# импортируем модель для CBV            
from django.views import generic 
from .models import Product,  Category

class ProductListView(generic.ListView): 
    template_name = 'products_list.html' # подключаем наш Темплейт
    context_object_name = 'products' # под каким именем передадутся данные в Темплейт
    model = Product # название Модели

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        # передаем в словарь контекста список всех категорий 
        context['categories'] = Category.objects.all()
        return context

class ProductDetail(generic.DetailView): 
    template_name = 'product_detail.html' 
    model = Product

class CategoryDetail(generic.DetailView): 
    template_name = 'category.html' 
    context_object_name = 'category'
    model = Category


def index(request):
    request_method = request.method
    
    ip_address = request.META['REMOTE_ADDR']
    browser_info = request.META['HTTP_USER_AGENT']
    
    response_text = "Тип запроса: {}. IP-адрес: {}. ЮзерАгент: {}".format(request_method, ip_address, browser_info)
    return HttpResponse(response_text)