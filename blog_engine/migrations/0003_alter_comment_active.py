# Generated by Django 4.0.5 on 2022-06-18 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_engine', '0002_rename_comments_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
