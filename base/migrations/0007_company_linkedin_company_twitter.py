# Generated by Django 4.0 on 2022-05-11 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_comment_body_comment_created_comment_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='linkedin',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='twitter',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
