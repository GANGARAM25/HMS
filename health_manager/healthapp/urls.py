from django.urls import path
from . import views

urlpatterns = [
    path('d/',views.Signup_FDO,name='Signup_FDO'),
    path('a/',views.Signup_DBA,name='Signup_DBA'),
    path('b/',views.Signup_DEO,name='Signup_DEO'),
    path('c/',views.Signup_DOC,name='Signup_DOC'),
    path('',views.Signin,name='Signin'),
    path('e/',views.menu_fdo,name='menu_fdo'),
    path('f/',views.menu_dba,name='menu_dba'),
    path('g/',views.menu_deo,name='menu_deo'),
    path('h/',views.menu_doc,name='menu_doc'),
    path('i/',views.home_fdo,name='home_fdo'),
    path('j/',views.home_dba,name='home_dba'),
    path('k/',views.home_deo,name='home_deo'),
    path('l/',views.home_doc,name='home_doc'),
    path('m/',views.account_doc,name='account_doc'),
    path('n/',views.account_deo,name='account_deo'),
    path('o/',views.account_dba,name='account_dba'),
    path('p/',views.account_fdo,name='account_fdo'),
    path('q/',views.logout_,name='logout'),
]