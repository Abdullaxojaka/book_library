# Generated by Django 5.1.3 on 2024-11-22 17:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='available',
            new_name='is_available',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AlterField(
            model_name='borrowrecord',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrow_records', to='library.book'),
        ),
        migrations.AlterField(
            model_name='borrowrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_books', to=settings.AUTH_USER_MODEL),
        ),
    ]
