# Generated by Django 3.2 on 2022-02-07 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['commentcreated_on']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_at']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='active',
            new_name='commentactive',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='commentbody',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_on',
            new_name='commentcreated_on',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='email',
            new_name='commentemail',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='commentname',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='commentpost',
        ),
    ]
