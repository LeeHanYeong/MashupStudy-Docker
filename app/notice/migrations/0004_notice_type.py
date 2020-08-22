# Generated by Django 2.2.7 on 2019-12-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notice", "0003_auto_20190923_1813"),
    ]

    operations = [
        migrations.AddField(
            model_name="notice",
            name="type",
            field=models.CharField(
                choices=[("all", "전체 공지"), ("team", "팀별 공지"), ("project", "프로젝트 공지")],
                default="all",
                max_length=10,
                verbose_name="공지유형",
            ),
            preserve_default=False,
        ),
    ]
