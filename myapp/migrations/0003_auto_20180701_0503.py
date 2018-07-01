# Generated by Django 2.0.1 on 2018-07-01 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_vote_connect'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='choice_text',
        ),
        migrations.AddField(
            model_name='question',
            name='choice_text1',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_text2',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
