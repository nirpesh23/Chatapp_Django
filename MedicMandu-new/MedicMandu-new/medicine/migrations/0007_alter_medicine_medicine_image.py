# Generated by Django 3.2.4 on 2022-04-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0006_alter_medicine_medicine_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='medicine_image',
            field=models.ImageField(blank=True, null=True, upload_to='medicine/'),
        ),
    ]
