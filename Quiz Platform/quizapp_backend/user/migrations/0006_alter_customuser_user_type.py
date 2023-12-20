# Generated by Django 4.2.5 on 2023-09-25 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'Student'), (2, 'Teacher'), (3, 'Admin')], max_length=10),
        ),
    ]
