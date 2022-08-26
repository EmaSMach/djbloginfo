# Generated by Django 4.0.6 on 2022-08-26 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, related_name='posts', to='blog.category'),
        ),
    ]
