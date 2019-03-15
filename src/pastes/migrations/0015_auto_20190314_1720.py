# Generated by Django 2.0.7 on 2019-03-14 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastes', '0014_auto_20190314_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paste',
            name='generated_url',
            field=models.CharField(db_index=True, default='blyuy6', max_length=6),
        ),
        migrations.AlterField(
            model_name='paste',
            name='syntax',
            field=models.IntegerField(choices=[(0, 'Plain'), (2, 'HTML'), (4, 'Javascript'), (1, 'Python'), (3, 'SQL'), (5, 'CSS')], default=0),
        ),
    ]