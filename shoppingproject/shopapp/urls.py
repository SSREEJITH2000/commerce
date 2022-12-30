from django.urls import path
from .import views
app_name='shopapp'
urlpatterns = [

    path('',views.all_product_category,name='all_product_category'),
    path('<slug:category_slug>/',views.all_product_category,name='product_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_category_detail'),

]