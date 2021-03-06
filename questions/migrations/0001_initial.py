# Generated by Django 3.2.12 on 2022-03-22 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id_question', models.AutoField(primary_key=True, serialize=False)),
                ('id_user', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('views', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
    ]
