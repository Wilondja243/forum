# Generated by Django 5.1.2 on 2024-10-15 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_django', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study', models.CharField(choices=[('FR', 'Freshman'), ('SP', 'Sophomore')], max_length=50)),
            ],
        ),
    ]
