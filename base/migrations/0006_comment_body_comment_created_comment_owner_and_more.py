# Generated by Django 4.0 on 2022-05-11 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0005_alter_post_likes_delete_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(blank=True, default='Test', null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, default='TEST', max_length=200, null=True),
        ),
    ]
