# Generated by Django 4.1.5 on 2023-01-19 23:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minha_dashboard', '0008_alter_vendas_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 19, 20, 35, 58, 329009)),
        ),
    ]
