# Generated by Django 5.0.1 on 2024-01-19 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0005_delete_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('value', models.DecimalField(decimal_places=1, max_digits=4)),
            ],
        ),
    ]
