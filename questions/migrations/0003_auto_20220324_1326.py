# Generated by Django 3.2.12 on 2022-03-24 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_label_labelsquestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='labelsquestion',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
