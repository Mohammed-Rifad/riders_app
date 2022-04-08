from . import views
from django.urls import path

urlpatterns = [
    path('', views.login,name='login'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('add-expense',views.add_expense),
    path('view-expense',views.view_expense),
    path('add-sales',views.add_sales),
    path('view-sales',views.view_sales),
    path('profit',views.Profit),
    path('logout',views.logout,name='')
]
