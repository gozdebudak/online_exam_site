# Generated by Django 3.1.6 on 2021-02-20 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinexam', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='student_answer',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
