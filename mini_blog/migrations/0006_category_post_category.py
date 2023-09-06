# Generated by Django 4.2.4 on 2023-08-27 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_blog', '0005_alter_post_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='uncategorized', max_length=255),
        ),
    ]
