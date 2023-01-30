from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product'),
    path('products/new/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', delete_product, name='product_delete'),
    path('',main,name='main'),
    path('suppliers/', SupplierListView.as_view(), name='supplier'),
    path('suppliers/create/', SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/<int:pk>/update/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/<int:pk>/delete/', delete_supplier, name='supplier_delete'),
    path('manager/', ManagerListView.as_view(), name='manager'),
    path('manager/create/', ManagerCreateView.as_view(), name='create_manager'),
    path('manager/<int:pk>/update/', ManagerUpdateView.as_view(), name='update_manager'),
    path('manager/<int:pk>/delete/', delete_manager, name='delete_manager'),
    path('stock/', StockListView.as_view(), name='stock'),
    path('stock/create/', StockCreateView.as_view(), name='create_stock'),
    path('stock/<int:pk>/update/', StockUpdateView.as_view(), name='update_stock'),
    path('stock/<int:pk>/delete/', delete_stock, name='delete_stock'),
    path('cookers/', CookerListView.as_view(), name='cooker'),
    path('cookers/create/', CookerCreateView.as_view(), name='cooker_create'),
    path('cookers/<int:pk>/update/', CookerUpdateView.as_view(), name='cooker_update'),
    path('cookers/<int:pk>/delete/', delete_cooker, name='cooker_delete'),
    path('supplies/', SuppliesListView.as_view(), name='supplies'),
    path('suplies/<int:suplie_id>/realise', realise_suplie, name='realise_suplie'),
    path('supplier/<int:supplier_id>/supplies_create/', supplie_create_view, name='create_supplies'),
    path("supplier/<int:supplier_id>/supplies_create/add_product", supplies_product_view, name='add_create_supplies'),
    path('supplies/update/<int:pk>/', SuppliesUpdateView.as_view(), name='update_supplies'),
    path('supplies/delete/<int:pk>/', delete_supplies, name='delete_supplies'),
    path('cooker/', CookerSelectView.as_view(), name='cooker_select'),
    path('cooker/product/', CookerProductView.as_view(), name='cooker_product'),
    path('cooker/history/', CookerProductHistoryView.as_view(), name='cooker_product_history'),
    path('download/pdf/', download_pdf, name='download_pdf'),
     ]
