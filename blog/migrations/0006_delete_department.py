# Generated by Django 4.0.2 on 2022-02-14 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_department_hod'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Department',
        ),
    ]