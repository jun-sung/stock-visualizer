# Generated by Django 3.2.9 on 2021-12-04 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.TextField(null=True)),
                ('data', models.TextField(null=True)),
            ],
        ),
    ]
