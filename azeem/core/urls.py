from xml.dom.minidom import Document
from django.urls import path
from core.views import SignUpView, ProfileView
from core import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path("contact",views.contact, name='contact'),
    path('startcontract', views.UploadFile, name='startcontract'),
    path("showcontact",views.show_contact, name='showcontact'),
    path("showcontract",views.show_contract, name='showcontract'),
    path("pin",views.pin, name='pin'),
    path("employee",views.employee, name='employee'),
    path("dashboard",views.dashboard, name='dashboard'),
    path("order_history",views.order_history, name='order_history'),
    path("tourism",views.tourism, name='tourism'),
    path("show_tourism",views.show_tourism, name='show_tourism'),
    path("tourism_page",views.tourism_page, name='tourism_page'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)