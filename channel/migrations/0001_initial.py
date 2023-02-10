# Generated by Django 4.1.3 on 2023-02-06 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channeldata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribers', models.IntegerField(blank=True, null=True)),
                ('videos', models.IntegerField(blank=True, null=True)),
                ('likes', models.IntegerField(blank=True, null=True)),
                ('comments', models.IntegerField(blank=True, null=True)),
                ('playlists', models.IntegerField(blank=True, null=True)),
                ('channel_level', models.IntegerField(blank=True, null=True)),
                ('total_views', models.IntegerField(blank=True, null=True)),
                ('followers', models.IntegerField(blank=True, null=True)),
                ('shares', models.IntegerField(blank=True, null=True)),
                ('total_uploads', models.IntegerField(blank=True, null=True)),
                ('total_comments', models.IntegerField(blank=True, null=True)),
                ('avg_views_per_video', models.FloatField(blank=True, null=True)),
                ('avg_engagement_per_video', models.FloatField(blank=True, null=True)),
                ('demographics', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ChannelData',
                'managed': False,
            },
        ),
    ]