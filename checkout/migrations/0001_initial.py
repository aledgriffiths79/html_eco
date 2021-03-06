# Generated by Django 2.2.6 on 2019-10-31 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0004_remove_product_sold_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('full_name', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=64)),
                ('postcode', models.CharField(blank=True, max_length=20)),
                ('city_or_town', models.CharField(max_length=128)),
                ('address2', models.CharField(max_length=128)),
                ('address1', models.CharField(max_length=128)),
                ('county', models.CharField(max_length=128)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='checkout.Order')),
                ('product', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='products.Product')),
            ],
        ),
    ]
