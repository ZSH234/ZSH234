from django.urls import path
from .views import contact,index,trainer,why

urlpatterns = [
    path(''contact,name='contact'),
    path(''index,name='index'),
    path(''trainer,name='trainer'),
    path(''why,name='name')
    
 
]
