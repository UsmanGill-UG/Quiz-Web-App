# Generated by Django 4.2.5 on 2023-09-25 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_rename_quiz_name_quiz_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_text',
            new_name='choice',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='question',
        ),
    ]
