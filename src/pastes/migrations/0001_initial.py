# Generated by Django 2.0.7 on 2019-03-12 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('title', models.CharField(blank=True, max_length=30)),
                ('syntax', models.IntegerField(choices=[(3, 'SQL'), (5, 'CSS'), (2, 'HTML'), (1, 'Python'), (4, 'Javascript'), (0, 'Plain')], default=0)),
                ('poster', models.CharField(blank=True, max_length=30)),
                ('timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
    ]
