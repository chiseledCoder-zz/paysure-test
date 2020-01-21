# Generated by Django 3.0.2 on 2020-01-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ext_id', models.CharField(max_length=20, unique=True)),
                ('benefits', models.PositiveIntegerField(choices=[(1, 'dentist'), (2, 'optician'), (3, 'gynecologist'), (4, 'orthopedic')], default=1)),
                ('currency', models.CharField(max_length=3)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ext_id', models.CharField(max_length=20, unique=True)),
                ('benefits', models.PositiveIntegerField(choices=[(1, 'dentist'), (2, 'optician'), (3, 'gynecologist'), (4, 'orthopedic')], default=1)),
                ('currency', models.CharField(max_length=3)),
                ('total_max_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
