# Generated by Django 2.2.8 on 2020-01-31 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_user_birth_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('-id', 'name'), 'verbose_name': '사용자', 'verbose_name_plural': '사용자 목록'},
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['name'], name='members_use_name_af6d2f_idx'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['birth_date'], name='members_use_birth_d_38ac34_idx'),
        ),
    ]
