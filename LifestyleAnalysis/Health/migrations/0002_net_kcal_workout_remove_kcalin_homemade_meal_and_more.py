# Generated by Django 5.0.7 on 2024-07-31 03:35

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Health', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Net_kcal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('cal_in', models.PositiveIntegerField()),
                ('cal_out_apple', models.PositiveIntegerField()),
                ('cal_out_app', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='kcalin',
            name='homemade_meal',
        ),
        migrations.RemoveField(
            model_name='recipeingredient',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='kcalin',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='kcalin',
            name='premade_meal',
        ),
        migrations.RemoveField(
            model_name='kcalin',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='recipeingredient',
            name='recipe',
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('duration_min', models.PositiveIntegerField()),
                ('kcal_out', models.PositiveIntegerField()),
                ('miles', models.PositiveSmallIntegerField()),
                ('workout_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Health.workout')),
            ],
        ),
        migrations.DeleteModel(
            name='HomemadeMeal',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='PremadeMeal',
        ),
        migrations.DeleteModel(
            name='KcalIn',
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
        migrations.DeleteModel(
            name='RecipeIngredient',
        ),
    ]