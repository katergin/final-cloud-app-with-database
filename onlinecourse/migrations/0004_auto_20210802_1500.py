# Generated by Django 3.1.3 on 2021-08-02 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_auto_20210801_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='points',
        ),
        migrations.AddField(
            model_name='question',
            name='grade',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(),
        ),
    ]
