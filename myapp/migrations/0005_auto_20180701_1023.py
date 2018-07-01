# Generated by Django 2.0.1 on 2018-07-01 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_question_the_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='choice_text3',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='vote',
            name='vote_total',
            field=models.IntegerField(default=0),
        ),
    ]