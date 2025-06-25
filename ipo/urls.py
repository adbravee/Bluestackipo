from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('login/', views.custom_login, name='custom_login'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('register/', views.register, name='register'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/companies/', views.CompanyListView.as_view(), name='company_list'),
    path('admin-dashboard/companies/add/', views.CompanyCreateView.as_view(), name='company_add'),
    path('admin-dashboard/companies/<int:pk>/edit/', views.CompanyUpdateView.as_view(), name='company_edit'),
    path('admin-dashboard/companies/<int:pk>/delete/', views.CompanyDeleteView.as_view(), name='company_delete'),
    path('admin-dashboard/ipos/', views.IPOListView.as_view(), name='ipo_list'),
    path('admin-dashboard/ipos/add/', views.IPOCreateView.as_view(), name='ipo_add'),
    path('admin-dashboard/ipos/<int:pk>/edit/', views.IPOUpdateView.as_view(), name='ipo_edit'),
    path('admin-dashboard/ipos/<int:pk>/delete/', views.IPODeleteView.as_view(), name='ipo_delete'),
    path('admin-dashboard/documents/', views.DocumentListView.as_view(), name='document_list'),
    path('admin-dashboard/documents/add/', views.DocumentCreateView.as_view(), name='document_add'),
    path('admin-dashboard/documents/<int:pk>/edit/', views.DocumentUpdateView.as_view(), name='document_edit'),
    path('admin-dashboard/documents/<int:pk>/delete/', views.DocumentDeleteView.as_view(), name='document_delete'),
    path('ipos/', views.public_ipo_list, name='public_ipo_list'),
    path('ipos/<int:pk>/', views.public_ipo_detail, name='public_ipo_detail'),
    path('', views.home, name='home'),
]

router = DefaultRouter()
router.register(r'companies', views.CompanyViewSet, basename='api-companies')
router.register(r'ipos', views.IPOViewSet, basename='api-ipos')
router.register(r'documents', views.DocumentViewSet, basename='api-documents')

urlpatterns += router.urls 