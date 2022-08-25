# Generated by Django 4.0.6 on 2022-08-25 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_counter', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='login_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número de logueos'),
        ),
    ]