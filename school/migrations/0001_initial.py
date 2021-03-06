# Generated by Django 2.2.3 on 2019-07-21 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('area', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('roll_no', models.IntegerField(max_length=20, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=30)),
                ('school_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.School')),
            ],
        ),
    ]
