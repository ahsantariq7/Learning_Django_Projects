
from logging.config import valid_ident
from unicodedata import category
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView
from .models import  Section, Shipping_Addres, Shop_By_Categories,Shopping_Bag,slider,Product,Categoryall,Color,Payment_Method
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'commons/signup.html'


# Edit Profile View
class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'commons/profile.html'


def home(request):
    
    all7=slider.objects.all()
    categories=Categoryall.objects.all()
    products = Product.objects.all()
    
    catid=request.GET.get('categories')
    if catid:
        products=Product.objects.filter(Category=catid)
    else:
        products=Product.objects.all()
    
    exclusive_promotions=Product.objects.filter(section__name="Exclusive Promotions")
    paginator = Paginator(exclusive_promotions, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    trending_items=Product.objects.filter(section__name="Trending Items")
    paginator = Paginator(trending_items, 6)

    page_number1 = request.GET.get('page1')
    page_obj1 = paginator.get_page(page_number1)

    tablet=Product.objects.filter(section__name="Tablet")
    paginator = Paginator(tablet, 6)

    page_number2 = request.GET.get('page2')
    page_obj2 = paginator.get_page(page_number2)
  

    if 'q' in request.GET:
        q=request.GET['q']
        products=Product.objects.filter(name__icontains=q)
    else:
        products=Product.objects.all()
        
    context={'all7':all7,'categories':categories,'products':products,'page1':page_obj1,'page':page_obj,'page2':page_obj2}
    return render(request, 'index.html',context)

def about_us(request):
    return render(request, 'about_us.html')

def base(request):
    all5=Shopping_Bag.objects.all()
    categories=Shop_By_Categories.objects.all()
   
    

    
    context={'all5':all5,'categories':categories,}
    return render(request, 'base.html',context)

def checkout_cart(request):
    return render(request, 'checkout_cart.html')

def cart(request):
    if request.method == 'POST':
        return redirect('checkout_info')
    return render(request, 'cart/cart.html')

def checkout_complete(request):
    if request.method == 'POST':
        return redirect('product')
    return render(request, 'checkout_complete.html')

def checkout_info(request):
    if request.method == 'POST':
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        company_name=request.POST.get('company_name')
        area_code=request.POST.get('area_code')
        primary_phone = request.POST.get('primary_phone')
        street_address=request.POST.get('street_address')
        zip_code=request.POST.get('zip_code')
        bussiness_type=request.POST.get('bussiness_type')
        form=Shipping_Addres(f_name=f_name, l_name=l_name,company_name=company_name,zip_code=zip_code,area_code=area_code,primary_phone=primary_phone,street_address=street_address,bussiness_type=bussiness_type)
         
        form.save()

        
        return redirect('checkout_payment')
    else:
        return render(request,"checkout_info.html")

def checkout_payment(request):
    if request.method == 'POST':
        cardholder_name=request.POST.get('cardholder_name')
        cardnumber=request.POST.get('cardnumber')
        payment_type=request.POST.get('payment_type')
        expiration_date_month=request.POST.get('expiration_date_month')
        expiration_date_year=request.POST.get('expiration_date_year')
        CSC_card=request.POST.get('CSC_card')

        form=Payment_Method(cardholder_name=cardholder_name,cardnumber=cardnumber,payment_type=payment_type,expiration_date_month=expiration_date_month,expiration_date_year=expiration_date_year,CSC_card=CSC_card)
        form.save()
        return redirect('checkout_complete')
    else:

        return render(request, 'checkout_payment.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def faq(request):
    return render(request, 'faq.html')

def index_fixed_header(request):
    return render(request, 'index_fixed_header.html')

def index_inverse_header(request):
    return render(request, 'index_inverse_header.html')

def my_account(request):
    return render(request, 'my_account.html')

@login_required(login_url='/login/')
def product_detail(request,slug):
    products=Product.objects.filter(slug=slug)
    if products.exists():
        products=Product.objects.filter(slug=slug)
    else:
        return redirect('404')


    context={
        'products':products,
    }

    return render(request, 'product_detail.html',context)


def error_404(request):
    return render(request, 'errors/404.html')


def product(request):
    categories=Categoryall.objects.all()
    products=Product.objects.all()
    sections=Section.objects.all()
    color=Color.objects.all()
    """
    catid=request.GET.get('categories')
    if catid:
        cat=Product.objects.filter(Category=catid)
    else:
        cat=Product.objects.all()

    
    
    paginator = Paginator(cat, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    """
    

    COLORID=request.GET.get('colorID')
    if COLORID:
        products=Product.objects.filter(color=COLORID)
    else:
        products=Product.objects.all()

    catid1=request.GET.get('ahsan')
    if catid1:
        products=Product.objects.filter(section=catid1)
        
    else:
        products=Product.objects.all()

    
    if 'q' in request.GET:
        q=request.GET['q']
        products=Product.objects.filter(name__icontains=q)
    else:
        products=Product.objects.all()
  
    context={
        'categories':categories,
        'products':products,
        
        #'page_obj':page_obj,
        'sections':sections,
        'color':color,
    }
    return render(request, 'product.html',context)

def filter_data(request):
    categories = request.GET.getlist('category[]')
    #brands = request.GET.getlist('brand[]')

    allProducts = Product.objects.all().order_by('-id').distinct()
    if len(categories) > 0:
        allProducts = allProducts.filter(Category__id__in=categories).distinct()

    #if len(brands) > 0:
     #   allProducts = allProducts.filter(Brand__id__in=brands).distinct()


    t = render_to_string('ajax/product.html', {'page_obj': allProducts})

    return JsonResponse({'data': t})




def search_results(request):
    return render(request, 'search_results.html')

@login_required(login_url='/login/')
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url='/login/')
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url='/login/')
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url='/login/')
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url='/login/')
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url='/login/')
def cart_detail(request):
    return render(request, 'cart/cart.html')



