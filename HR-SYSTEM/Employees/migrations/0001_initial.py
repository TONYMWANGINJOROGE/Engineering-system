# Generated by Django 5.0.2 on 2024-02-29 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('emp_code', models.CharField(max_length=5)),
                ('MobileNumber', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=50)),
            ],
        ),
    ]
