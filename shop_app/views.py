from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# импортируем из стандартной сборки Django
from django.http import HttpResponse
# импортируем модель для CBV 
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy           
from django.views import generic 
from .models import Product,  Category , Order

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

class ProductCreate(generic.CreateView): 
	model = Product 
	# название нашего шаблона с формой
	template_name = 'product_new.html' 
	# какие поля будут в форме 
	fields = '__all__'

class OrderFormView(LoginRequiredMixin,generic.CreateView): 
  model = Order 
  template_name = 'order_form.html' 
  success_url = '/' 
  # выведем только поля, которые нужно заполнить самому человеку
  fields = ['customer_name', 'customer_phone']
  
  def form_valid(self, form):
      # получаем ID из ссылки и передаем в ORM для фильтрации
      product = Product.objects.get(id=self.kwargs['pk']) 
      # передаем в поле товара нашей формы отфильтрованный товар
      form.instance.product = product 
      # super — перезагружает форму, нужен для работы
      return super().form_valid(form)

class SignUpView(generic.CreateView): 
    form_class = UserCreationForm 
    success_url = reverse_lazy('login') 
    template_name = 'signup.html'

def index(request):
    request_method = request.method
    
    ip_address = request.META['REMOTE_ADDR']
    browser_info = request.META['HTTP_USER_AGENT']
    
    response_text = "Тип запроса: {}. IP-адрес: {}. ЮзерАгент: {}".format(request_method, ip_address, browser_info)
    return HttpResponse(response_text)