# Generated by Django 3.0.2 on 2020-04-26 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='id',
        ),
        migrations.AddField(
            model_name='question',
            name='prob_link',
            field=models.CharField(default='', max_length=500, primary_key=True, serialize=False),
        ),
    ]
