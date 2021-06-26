from django.urls import path
from homepage import views as hview
urlpatterns = [
    path('',hview.home,name='home'),
    path('contact/',hview.contact,name='contact_dh'),
    path('django/',hview.django,name='django'),
    path('java/',hview.java,name='java'),
    path('mobile_application/',hview.mobile_application,name='mobile_application'),
    path('pythonpage/',hview.pythonpage,name='pythonpage'),
    path('web_application/',hview.web_application,name='web_application'),
    
]
