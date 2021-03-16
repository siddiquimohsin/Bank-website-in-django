from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('add_new',views.add_new,name='add'),
    path('show',views.login,name='Show_All_Record'),
    path('check',views.check,name='Check'),
    path('deposit',views.deposit,name='deposit'),
    path('comment',views.comment,name='comment'),

]