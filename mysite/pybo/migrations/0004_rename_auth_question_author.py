# Generated by Django 4.0.3 on 2024-08-13 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0003_answer_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='auth',
            new_name='author',
        ),
    ]
