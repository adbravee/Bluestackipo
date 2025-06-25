from rest_framework import serializers
from .models import Company, IPO, Document

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_id', 'company_name', 'company_logo']

class IPOSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), source='company', write_only=True)
    class Meta:
        model = IPO
        fields = [
            'ipo_id', 'company', 'company_id', 'price_band', 'open_date', 'close_date', 'issue_size', 'issue_type',
            'listing_date', 'status', 'ipo_price', 'listing_price', 'listing_gain', 'current_market_price', 'current_return'
        ]

class DocumentSerializer(serializers.ModelSerializer):
    ipo = IPOSerializer(read_only=True)
    ipo_id = serializers.PrimaryKeyRelatedField(queryset=IPO.objects.all(), source='ipo', write_only=True)
    class Meta:
        model = Document
        fields = ['document_id', 'ipo', 'ipo_id', 'rhp_pdf', 'drhp_pdf'] 