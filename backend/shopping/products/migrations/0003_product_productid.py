# Generated by Django 2.2.9 on 2020-01-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productId',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]