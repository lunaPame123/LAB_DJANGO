from django.urls import path # type: ignore
from django.views.generic import RedirectView # type: ignore
from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='index', permanent=False)),
    path('index', views.index, name='index'),
    path('customer_edit/<int:id>', views.customer_edit, name='customer_edit'),
    path('customer_delete/<int:id>', views.customer_delete, name='customer_delete'),
]