# Generated by Django 3.2.4 on 2022-04-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medname', models.CharField(max_length=55)),
                ('medtype', models.CharField(choices=[('l', 'Liquid'), ('tab', 'Tablet'), ('cap', 'Capsules'), ('drops', 'Drops'), ('ins', 'Insulin'), ('Topical', 'Topical medicines'), ('Imp', 'Implants')], default='Liquid', max_length=10, null=True)),
                ('medmanufacturdate', models.DateField(null=True)),
                ('medexpirydate', models.DateField(null=True)),
                ('manufacturer', models.CharField(max_length=150, null=True)),
                ('description', models.CharField(max_length=40, null=True)),
                ('medicine_image', models.ImageField(blank=True, null=True, upload_to='images/Medicine')),
                ('slug', models.SlugField(max_length=150, null=True)),
                ('price', models.PositiveIntegerField(null=True)),
                ('in_stock', models.BooleanField(default=True, null=True)),
                ('is_active', models.BooleanField(default=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
