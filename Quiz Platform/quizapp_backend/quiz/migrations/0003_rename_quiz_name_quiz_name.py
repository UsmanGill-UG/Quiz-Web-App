# Generated by Django 4.2.5 on 2023-09-25 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_remove_choice_text_remove_question_text_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='quiz_name',
            new_name='name',
        ),
    ]
