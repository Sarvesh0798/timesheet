from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.signup, name='signup'),
    path('login/register/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('add/', views.add, name='add'),
    path('logout/', views.logout, name='logout'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterec/<int:id>', views.updaterec, name='update'),
       ]