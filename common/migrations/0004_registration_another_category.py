# Generated by Django 5.0.4 on 2024-10-21 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_alter_registration_date_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='another_category',
            field=models.CharField(max_length=256, null=True),
        ),
    ]