from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('ipo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipo',
            name='ipo_price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='IPO price', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='ipo',
            name='listing_price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Listing price', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='ipo',
            name='listing_gain',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Listing gain in %', max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='ipo',
            name='current_market_price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Current market price', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='ipo',
            name='current_return',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Current return in %', max_digits=5, null=True),
        ),
    ] 