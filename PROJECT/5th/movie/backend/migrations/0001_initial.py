# Generated by Django 4.0.3 on 2022-03-07 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MCast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cast_actor', models.CharField(max_length=45)),
                ('cast_cast', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'm_cast',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_userid', models.IntegerField(db_column='comment_userId')),
                ('comment_username', models.CharField(db_column='comment_userName', max_length=45)),
                ('comment_point', models.IntegerField()),
                ('comment_contents', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'm_comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MMovie',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('movie_title', models.CharField(max_length=45)),
                ('movie_url', models.TextField()),
                ('movie_aud', models.FloatField(blank=True, null=True)),
                ('movie_net', models.FloatField(blank=True, null=True)),
                ('movie_rep', models.FloatField(blank=True, null=True)),
                ('movie_poster', models.TextField()),
                ('movie_genre', models.IntegerField()),
                ('movie_country', models.IntegerField()),
                ('movie_runtime', models.IntegerField()),
                ('movie_release', models.DateField()),
                ('movie_director', models.CharField(blank=True, max_length=45, null=True)),
                ('movie_age', models.IntegerField()),
                ('movie_content', models.TextField()),
            ],
            options={
                'db_table': 'm_movie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MAge',
            fields=[
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='backend.mmovie')),
                ('age_view10', models.IntegerField()),
                ('age_view20', models.IntegerField()),
                ('age_view30', models.IntegerField()),
                ('age_view40', models.IntegerField()),
                ('age_view50', models.IntegerField()),
                ('age_sati10', models.FloatField()),
                ('age_sati20', models.FloatField()),
                ('age_sati30', models.FloatField()),
                ('age_sati40', models.FloatField()),
                ('age_sati50', models.FloatField()),
            ],
            options={
                'db_table': 'm_age',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MGender',
            fields=[
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='backend.mmovie')),
                ('gender_man', models.IntegerField()),
            ],
            options={
                'db_table': 'm_gender',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MPoint',
            fields=[
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='backend.mmovie')),
                ('point_dir', models.IntegerField()),
                ('point_act', models.IntegerField()),
                ('point_sto', models.IntegerField()),
                ('point_vis', models.IntegerField()),
                ('point_ost', models.IntegerField()),
            ],
            options={
                'db_table': 'm_point',
                'managed': False,
            },
        ),
    ]