# Generated by Django 3.0.3 on 2020-08-06 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='eemail',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]