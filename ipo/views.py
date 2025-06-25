from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Company, IPO, Document, CustomUser
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework import viewsets, permissions
from .serializers import CompanySerializer, IPOSerializer, DocumentSerializer
from .forms import CustomUserCreationForm, IPOForm

# Create your views here.

def is_approved(user):
    return user.is_approved

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_approved or user.is_superuser:
                    login(request, user)
                    return redirect('admin_dashboard')
                else:
                    messages.error(request, 'Your account is pending approval from an administrator.')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    # Add Bootstrap classes to form fields
    form.fields['username'].widget.attrs.update({'class': 'form-control'})
    form.fields['password'].widget.attrs.update({'class': 'form-control'})
    return render(request, 'ipo/login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('custom_login')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        # Add Bootstrap classes to form fields
        form.fields['username'].widget.attrs.update({'class': 'form-control'})
        form.fields['password1'].widget.attrs.update({'class': 'form-control'})
        form.fields['password2'].widget.attrs.update({'class': 'form-control'})
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully. Please wait for admin approval before logging in.')
            return redirect('custom_login')
    else:
        form = CustomUserCreationForm()
        # Add Bootstrap classes to form fields
        form.fields['username'].widget.attrs.update({'class': 'form-control'})
        form.fields['password1'].widget.attrs.update({'class': 'form-control'})
        form.fields['password2'].widget.attrs.update({'class': 'form-control'})
    return render(request, 'ipo/register.html', {'form': form})

@login_required
@user_passes_test(is_approved)
def admin_dashboard(request):
    return render(request, 'ipo/admin_dashboard.html')

# Update all class-based views to include approval check
class ApprovedUserRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_approved and not request.user.is_superuser:
            messages.error(request, 'Your account is pending approval from an administrator.')
            return redirect('custom_login')
        return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class CompanyListView(ApprovedUserRequiredMixin, ListView):
    model = Company
    template_name = 'ipo/company_list.html'
    context_object_name = 'companies'

@method_decorator(login_required, name='dispatch')
class CompanyCreateView(ApprovedUserRequiredMixin, CreateView):
    model = Company
    fields = ['company_name', 'company_logo']
    template_name = 'ipo/company_form.html'
    success_url = reverse_lazy('company_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'
        return form

@method_decorator(login_required, name='dispatch')
class CompanyUpdateView(ApprovedUserRequiredMixin, UpdateView):
    model = Company
    fields = ['company_name', 'company_logo']
    template_name = 'ipo/company_form.html'
    success_url = reverse_lazy('company_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'
        return form

@method_decorator(login_required, name='dispatch')
class CompanyDeleteView(ApprovedUserRequiredMixin, DeleteView):
    model = Company
    template_name = 'ipo/company_confirm_delete.html'
    success_url = reverse_lazy('company_list')

@method_decorator(login_required, name='dispatch')
class IPOListView(ApprovedUserRequiredMixin, ListView):
    model = IPO
    template_name = 'ipo/ipo_list.html'
    context_object_name = 'ipos'
    queryset = IPO.objects.select_related('company')

@method_decorator(login_required, name='dispatch')
class IPOCreateView(ApprovedUserRequiredMixin, CreateView):
    model = IPO
    form_class = IPOForm
    template_name = 'ipo/ipo_form.html'
    success_url = reverse_lazy('ipo_list')

@method_decorator(login_required, name='dispatch')
class IPOUpdateView(ApprovedUserRequiredMixin, UpdateView):
    model = IPO
    form_class = IPOForm
    template_name = 'ipo/ipo_form.html'
    success_url = reverse_lazy('ipo_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'
        return form

@method_decorator(login_required, name='dispatch')
class IPODeleteView(ApprovedUserRequiredMixin, DeleteView):
    model = IPO
    template_name = 'ipo/ipo_confirm_delete.html'
    success_url = reverse_lazy('ipo_list')

@method_decorator(login_required, name='dispatch')
class DocumentListView(ApprovedUserRequiredMixin, ListView):
    model = Document
    template_name = 'ipo/document_list.html'
    context_object_name = 'documents'
    queryset = Document.objects.select_related('ipo')

@method_decorator(login_required, name='dispatch')
class DocumentCreateView(ApprovedUserRequiredMixin, CreateView):
    model = Document
    fields = ['ipo', 'rhp_pdf', 'drhp_pdf']
    template_name = 'ipo/document_form.html'
    success_url = reverse_lazy('document_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'
        return form

@method_decorator(login_required, name='dispatch')
class DocumentUpdateView(ApprovedUserRequiredMixin, UpdateView):
    model = Document
    fields = ['ipo', 'rhp_pdf', 'drhp_pdf']
    template_name = 'ipo/document_form.html'
    success_url = reverse_lazy('document_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'
        return form

@method_decorator(login_required, name='dispatch')
class DocumentDeleteView(ApprovedUserRequiredMixin, DeleteView):
    model = Document
    template_name = 'ipo/document_confirm_delete.html'
    success_url = reverse_lazy('document_list')

# Public IPO List View with search and filter

def public_ipo_list(request):
    query = request.GET.get('q', '')
    status = request.GET.get('status', '')
    ipos = IPO.objects.select_related('company').all()
    if query:
        ipos = ipos.filter(company__company_name__icontains=query)
    if status:
        ipos = ipos.filter(status=status)
    paginator = Paginator(ipos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    statuses = IPO.STATUS_CHOICES
    return render(request, 'ipo/public_ipo_list.html', {
        'page_obj': page_obj,
        'query': query,
        'status': status,
        'statuses': statuses,
    })

# Public IPO Detail View

def public_ipo_detail(request, pk):
    ipo = IPO.objects.select_related('company').get(pk=pk)
    documents = ipo.documents.all()
    return render(request, 'ipo/public_ipo_detail.html', {
        'ipo': ipo,
        'documents': documents,
    })

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdminOrReadOnly]

class IPOViewSet(viewsets.ModelViewSet):
    queryset = IPO.objects.select_related('company').all()
    serializer_class = IPOSerializer
    permission_classes = [IsAdminOrReadOnly]

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.select_related('ipo').all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAdminOrReadOnly]

def home(request):
    return render(request, 'ipo/home.html')
