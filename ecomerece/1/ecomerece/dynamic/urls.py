from operator import index
from dynamic import views
from .views import ProfileView, SignUpView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from dynamic.views import SignUpView, ProfileView

urlpatterns = [
    path('', views.home, name="home"),
    path('base', views.base, name='base'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('about_us', views.about_us, name='about_us'),
    path('checkout_cart', views.cart, name='checkout_cart'),
    
    path('checkout_complete', views.checkout_complete, name='checkout_complete'),
    path('checkout_info', views.checkout_info, name='checkout_info'),
    path('checkout_payment', views.checkout_payment, name='checkout_payment'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('faq', views.faq, name='faq'),
    path('index_fixed_header', views.index_fixed_header, name='index_fixed_header'),
    path('index_inverse_header', views.index_inverse_header, name='index_inverse_header'),
    path('my_account', views.my_account, name='my_account'),
    path('product_detail/<slug:slug>', views.product_detail, name='product_detail'),
    path('404', views.error_404, name='404'),
    path('product/', views.product, name='product'),
    path('product/filter-data',views.filter_data,name="filter-data"),
    path('search_results', views.search_results, name='search_results'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
