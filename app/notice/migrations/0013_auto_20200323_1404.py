# Generated by Django 2.2.11 on 2020-03-23 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("notice", "0012_auto_20200323_1223"),
    ]

    operations = [
        migrations.RemoveField(model_name="attendance", name="created",),
        migrations.RemoveField(model_name="attendance", name="modified",),
        migrations.RemoveField(model_name="historicalattendance", name="created",),
        migrations.RemoveField(model_name="historicalattendance", name="modified",),
        migrations.RemoveField(model_name="historicalnotice", name="created",),
        migrations.RemoveField(model_name="historicalnotice", name="modified",),
        migrations.RemoveField(model_name="notice", name="created",),
        migrations.RemoveField(model_name="notice", name="modified",),
    ]
