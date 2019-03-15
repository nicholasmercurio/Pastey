# Generated by Django 2.0.7 on 2019-03-12 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastes', '0003_auto_20190312_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='syntax',
            field=models.IntegerField(choices=[(0, 'Plain'), (3, 'SQL'), (2, 'HTML'), (4, 'Javascript'), (1, 'Python'), (5, 'CSS')], default=0),
        ),
    ]
