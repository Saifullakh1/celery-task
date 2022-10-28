# Generated by Django 4.0.5 on 2022-06-19 19:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=200)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_reference', models.UUIDField(default=uuid.uuid4)),
                ('address', models.CharField(max_length=250)),
                ('owner_name', models.CharField(max_length=250)),
                ('owner_email', models.EmailField(max_length=250)),
                ('shipment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('shipped', 'shipped')], default='pending', max_length=200)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orderApp.order')),
            ],
        ),
    ]