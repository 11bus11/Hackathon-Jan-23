# Generated by Django 3.2.16 on 2023-01-21 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalcFunding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField()),
                ('savings', models.IntegerField()),
                ('salary_pre', models.IntegerField()),
                ('salary_post', models.IntegerField()),
                ('expences', models.IntegerField()),
            ],
            options={
                'ordering': ['cost'],
            },
        ),
    ]
