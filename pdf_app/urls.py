from django.urls import path
from . import views
from .views import CustomerListView

app_name = 'pdf_app'

urlpatterns = [
    path('',CustomerListView.as_view(),name='customer-list-view'),
    path('pdf/<pk>',views.customer_render_pdf_view,name='customer-pdf-view'),
]