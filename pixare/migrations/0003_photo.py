# Generated by Django 2.1.2 on 2018-12-17 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pixare', '0002_auto_20181211_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=32)),
                ('caption', models.TextField(blank=True)),
                ('view_count', models.IntegerField(default=0)),
                ('like_count', models.IntegerField(default=0)),
                ('comment_count', models.IntegerField(default=0)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('square_loc', models.CharField(default='', max_length=128)),
                ('thumb_loc', models.CharField(default='', max_length=128)),
                ('middle_loc', models.CharField(default='', max_length=128)),
                ('original_loc', models.CharField(default='', max_length=128)),
                ('middle_width', models.IntegerField(default=0)),
                ('middle_height', models.IntegerField(default=0)),
                ('original_width', models.IntegerField(default=0)),
                ('original_height', models.IntegerField(default=0)),
                ('score', models.FloatField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
    ]