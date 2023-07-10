from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Product,Category
# Create your views here.
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = 'El nombre de usuario debe ser menor a 150 caracteres y no puede contener caracteres especiales'
        self.fields['password1'].help_text = 'La contraseña debe tener al menos 3 caracteres'
        self.fields['password2'].help_text = 'La contraseña debe tener al menos 3 caracteres'
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_crud:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'autenticacion/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'autenticacion/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url='admin_crud:login')
def index(request):
    productListado=Product.objects.all()
    categoryListado=Category.objects.all()
    context={
        'products':productListado,
        'categorys':categoryListado,
    }
    return render(request,"index.html",context)

def registrarproduct(request):
    product_id = request.POST["txtcodigo"]
    description=request.POST["txtdescr"]
    image_url = request.POST["txturl"]
    marked_price=request.POST["numprecio"]
    product_name=request.POST["txtname"]
    review_count=0
    selling_price=request.POST["numprecio"]
    total_rating=0
    cat=request.POST["categ"]
    category_category=Category.objects.get(pk=cat)

    product=Product.objects.filter(product_id=product_id).create(product_id=product_id,description=description,image_url=image_url,marked_price=marked_price,product_name=product_name,review_count=review_count,selling_price=selling_price,total_rating=total_rating,category_category=category_category)
    return redirect('/')

def eliminarproduct(request,product_id):
    product=Product.objects.get(product_id=product_id)
    product.delete()
    return redirect('/')