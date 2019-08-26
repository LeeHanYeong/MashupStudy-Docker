# Generated by Django 2.2.4 on 2019-08-26 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import members.models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20190826_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAdminProxy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('members.user',),
            managers=[
                ('objects', members.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='period',
            name='is_current',
            field=models.BooleanField(default=False, verbose_name='현재 기수여부'),
        ),
        migrations.CreateModel(
            name='UserPeriodOutcount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.DecimalField(decimal_places=2, default=0, max_digits=3, verbose_name='아웃카운트')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_period_outcount_set', related_query_name='user_period_outcount', to='members.Period', verbose_name='기수')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_period_outcount_set', related_query_name='user_period_outcount', to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
            options={
                'verbose_name': '사용자 활동기수별 아웃카운트 정보',
                'verbose_name_plural': '사용자 활동기수별 아웃카운트 정보 목록',
                'unique_together': {('user', 'period')},
            },
        ),
    ]
