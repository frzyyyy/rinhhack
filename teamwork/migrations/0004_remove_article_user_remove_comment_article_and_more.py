# Generated by Django 4.2.6 on 2023-11-25 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teamwork', '0003_customer_movies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Movies',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]