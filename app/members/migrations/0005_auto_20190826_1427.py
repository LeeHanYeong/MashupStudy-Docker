# Generated by Django 2.2.4 on 2019-08-26 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0004_auto_20190813_0407"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True, verbose_name="이메일"),
        ),
    ]
