# Generated by Django 4.0 on 2022-01-07 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('height', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Range',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mysite.group')),
            ],
        ),
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='t_user', to='mysite.user')),
            ],
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField()),
                ('range', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.range')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('segments', models.ManyToManyField(to='mysite.Segment')),
                ('tourist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.tourist')),
            ],
        ),
        migrations.CreateModel(
            name='DefinedSegment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('name', models.CharField(max_length=100, unique=True)),
                ('end_point', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='end_point', to='mysite.point')),
                ('segment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='defined_segment', to='mysite.segment')),
                ('start_point', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='start_point', to='mysite.point')),
            ],
        ),
        migrations.CreateModel(
            name='CustomSegment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elevation', models.IntegerField()),
                ('start_name', models.CharField(max_length=50)),
                ('end_name', models.CharField(max_length=50)),
                ('start_height', models.IntegerField()),
                ('end_height', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('segment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_segment', to='mysite.segment')),
            ],
        ),
    ]
