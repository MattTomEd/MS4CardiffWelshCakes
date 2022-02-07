# Generated by Django 3.2 on 2022-02-07 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220207_2204'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='commentactive',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='commentbody',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='commentcreated_on',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='commentemail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='commentname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='commentpost',
            new_name='post',
        ),
    ]
