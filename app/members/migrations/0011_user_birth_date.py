# Generated by Django 2.2.8 on 2020-01-31 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_auto_20190914_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='생일'),
        ),
    ]
