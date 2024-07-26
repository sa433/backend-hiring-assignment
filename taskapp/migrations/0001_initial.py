# Generated by Django 4.2.14 on 2024-07-25 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=255)),
                ('pdesc', models.TextField()),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskapp.clientmodel')),
            ],
        ),
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=255)),
                ('tdesc', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('To Do', 'To Do'), ('WIP', 'WIP'), ('On Hold', 'On Hold'), ('Done', 'DOne')], default='To Do', max_length=10)),
                ('proj_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskapp.projectmodel')),
            ],
        ),
    ]
