# Generated by Django 2.2 on 2019-05-25 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ContentId', models.IntegerField(verbose_name='内容ID')),
                ('Content', models.TextField(verbose_name='事项内容')),
                ('Title', models.CharField(default='未填写', max_length=256, verbose_name='事项标题')),
                ('DateCreated', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('TagId', models.IntegerField(verbose_name='事项类型')),
            ],
            options={
                'verbose_name': 'todo item content',
            },
        ),
        migrations.CreateModel(
            name='ItemInfo',
            fields=[
                ('ItemId', models.IntegerField(primary_key=True, serialize=False, verbose_name='事项ID')),
                ('Repeat', models.IntegerField(verbose_name='重复天数')),
                ('DateCreated', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('IsDeleted', models.BooleanField(default=False, verbose_name='是否被删除')),
                ('IsDone', models.BooleanField(default=False, verbose_name='已完成')),
            ],
            options={
                'verbose_name': '待办事项',
            },
        ),
    ]
