# Generated by Django 4.1.6 on 2023-04-29 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='ExpensesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_category', models.CharField(max_length=100)),
                ('amount_of_money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('entry_date', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('dr', models.FloatField(default=0)),
                ('cr', models.FloatField(default=0)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expense.account')),
            ],
        ),
    ]
