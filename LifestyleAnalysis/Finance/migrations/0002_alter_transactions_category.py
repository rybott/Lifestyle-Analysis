# Generated by Django 5.0.7 on 2024-08-07 04:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Finance.categories'),
        ),
    ]
