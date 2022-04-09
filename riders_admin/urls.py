from . import views
from django.urls import path

urlpatterns = [
    path('', views.login,name='login'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('add-expense',views.add_expense),
    path('view-expense',views.view_expense,name='exp_view'),
    path('add-sales',views.add_sales),
    path('view-sales',views.view_sales,name='sales_view'),
    path('profit',views.Profit),
    path('del-exp/<int:id>',views.del_exp),
    path('del-sale/<int:id>',views.del_sale),
    path('logout',views.logout,name='')
]
