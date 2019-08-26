# Generated by Django 2.2.4 on 2019-08-26 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_auto_20190826_1548'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='period',
            options={'ordering': ('-number', '-pk', 'is_current'), 'verbose_name': '기수정보', 'verbose_name_plural': '기수정보 목록'},
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='이메일'),
        ),
    ]
