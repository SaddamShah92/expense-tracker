from django.urls import path
from . import views
urlpatterns = [
    path('', views.expense_list, name = 'expense_list'),
    path('add/', views.add_expense, name = 'add_expnese'),
    path('delete/<int:pk>/', views.delete_expense, name = 'delete_expense'),
    path('expense_detail/<int:pk>' , views.expense_detail, name = 'expense_detail'),
]