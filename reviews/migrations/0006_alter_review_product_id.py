# Generated by Django 4.0.3 on 2022-04-04 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('reviews', '0005_review_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
