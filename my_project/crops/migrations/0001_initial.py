# Generated by Django 5.1.3 on 2024-12-02 06:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='作物名')),
                ('variety', models.CharField(max_length=100, verbose_name='品種')),
                ('planting_date', models.DateField(verbose_name='播種日')),
                ('expected_harvest_date', models.DateField(verbose_name='収穫予定日')),
                ('current_stage', models.CharField(choices=[('seedling', '苗'), ('growing', '生育中'), ('flowering', '開花'), ('fruiting', '結実'), ('ready', '収穫期')], default='seedling', max_length=20, verbose_name='生育段階')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GrowthRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='記録日')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='growth_photos/')),
                ('notes', models.TextField(verbose_name='備考')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crops.crop')),
            ],
        ),
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harvest_date', models.DateField(verbose_name='収穫日')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='収穫量')),
                ('unit', models.CharField(max_length=20, verbose_name='単位')),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='収益')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='備考')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crops.crop')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='資材名')),
                ('item_type', models.CharField(choices=[('seed', '種子'), ('fertilizer', '肥料'), ('pesticide', '農薬'), ('tool', '道具')], max_length=20, verbose_name='種類')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='数量')),
                ('unit', models.CharField(max_length=20, verbose_name='単位')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]