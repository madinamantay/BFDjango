# Generated by Django 2.2.10 on 2020-04-19 19:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_on', models.DateTimeField(default=None, null=True)),
                ('is_done', models.BooleanField(default=False)),
                ('notes', models.CharField(blank=True, default='', max_length=255)),
            ],
            options={
                'verbose_name': 'Task item',
                'verbose_name_plural': 'Task items',
            },
        ),
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Task list',
                'verbose_name_plural': 'Tasks list',
            },
        ),
    ]