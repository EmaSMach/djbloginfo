# Generated by Django 4.0.6 on 2022-08-26 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_views_number_alter_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='categories',
        ),
    ]
