from django.urls import path, include
from . import views  

urlpatterns = [
    path('', views.employee_form),  
    path('list', views.employee_list),  # Add a comma here
    path('list/', views.employee_list, name='employee_list'),
    path('insert/', views.employee_form, name='employee_insert'),  # POST for insert
    path('update/<int:id>/', views.employee_form, name='employee_update'),  # POST for update
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
]
