# Generated by Django 2.2.9 on 2020-01-02 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='value',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]