# Generated by Django 4.2.14 on 2024-07-26 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_alter_projectmodel_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='proj_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to='taskapp.projectmodel'),
        ),
    ]
