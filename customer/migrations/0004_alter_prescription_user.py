# Generated by Django 3.2.4 on 2022-04-17 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_prescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
    ]
