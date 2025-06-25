from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    company_logo = models.ImageField(upload_to='company_logos/')

    def __str__(self):
        return self.company_name

class IPO(models.Model):
    STATUS_CHOICES = [
        ('Upcoming', 'Upcoming'),
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('Listed', 'Listed'),
    ]
    ipo_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='ipos')
    price_band = models.CharField(max_length=50, help_text='Price band for the IPO')
    open_date = models.DateField(help_text='IPO open date')
    close_date = models.DateField(help_text='IPO close date')
    issue_size = models.CharField(max_length=100, help_text='Total issue size')
    issue_type = models.CharField(max_length=50, help_text='Type of issue')
    listing_date = models.DateField(help_text='IPO listing date')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, help_text='IPO status')
    ipo_price = models.DecimalField(max_digits=10, decimal_places=2, help_text='IPO price', blank=True, null=True)
    listing_price = models.DecimalField(max_digits=10, decimal_places=2, help_text='Listing price', blank=True, null=True)
    listing_gain = models.DecimalField(max_digits=5, decimal_places=2, help_text='Listing gain in %', blank=True, null=True)
    current_market_price = models.DecimalField(max_digits=10, decimal_places=2, help_text='Current market price', blank=True, null=True)
    current_return = models.DecimalField(max_digits=5, decimal_places=2, help_text='Current return in %', blank=True, null=True)

    def __str__(self):
        return f"{self.company.company_name} IPO ({self.open_date})"

class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
    ipo = models.ForeignKey(IPO, on_delete=models.CASCADE, related_name='documents')
    rhp_pdf = models.FileField(upload_to='documents/rhp/')
    drhp_pdf = models.FileField(upload_to='documents/drhp/')

    def __str__(self):
        return f"Documents for {self.ipo}"
