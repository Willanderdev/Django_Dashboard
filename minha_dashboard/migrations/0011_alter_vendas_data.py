# Generated by Django 4.1.5 on 2023-01-20 21:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minha_dashboard', '0010_alter_vendas_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 18, 38, 44, 585812)),
        ),
    ]
