# Generated by Django 2.2.3 on 2019-07-18 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190717_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='sex',
            field=models.IntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV'), (5, 'V'), (6, 'VI'), (7, 'VII'), (8, 'VIII'), (9, 'IX'), (10, 'X'), (11, 'XI'), (12, 'XII'), (13, 'XIII'), (14, 'XIV'), (15, 'XV'), (16, 'T'), (17, '零'), (18, 'KH'), (19, '外伝'), (20, 'Job')], default=1, verbose_name='シリーズ'),
        ),
    ]
