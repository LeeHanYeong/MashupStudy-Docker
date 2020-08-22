# Generated by Django 2.2.8 on 2019-12-17 12:31

from django.db import migrations
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ("notice", "0004_notice_type"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="notice",
            options={
                "ordering": (
                    django.db.models.expressions.OrderBy(
                        django.db.models.expressions.F("start_at"),
                        descending=True,
                        nulls_last=True,
                    ),
                    "-id",
                ),
                "verbose_name": "공지",
                "verbose_name_plural": "공지 목록",
            },
        ),
    ]
