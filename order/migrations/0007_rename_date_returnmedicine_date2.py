# Generated by Django 3.2.4 on 2022-04-16 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_alter_returnmedicine_medicine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='returnmedicine',
            old_name='date',
            new_name='date2',
        ),
    ]