# Generated by Django 4.1.7 on 2024-04-15 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_book', '0002_alter_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
