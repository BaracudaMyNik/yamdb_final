# Generated by Django 3.2 on 2023-02-02 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_alter_comment_pub_date'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='unique_title_author'),
        ),
    ]