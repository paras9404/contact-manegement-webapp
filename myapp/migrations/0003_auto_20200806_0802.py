# Generated by Django 3.0.3 on 2020-08-06 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_employee_eemail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='econtact',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='eid',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='ename',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
