# Generated by Django 3.2.18 on 2023-05-25 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20230525_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(),
        ),
    ]
