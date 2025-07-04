# Generated by Django 4.2.16 on 2025-02-08 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Vendor'), (2, 'Customer')], null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pin_code',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]
