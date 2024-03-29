# Generated by Django 4.0.5 on 2022-08-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_alter_post_options_alter_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='intro',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
