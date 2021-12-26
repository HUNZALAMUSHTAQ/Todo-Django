# Generated by Django 4.0 on 2021-12-25 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('complete', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
