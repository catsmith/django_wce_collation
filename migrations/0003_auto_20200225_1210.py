# Generated by Django 2.2 on 2020-02-25 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collation', '0002_auto_20190602_1722'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collation',
            options={'ordering': ['chapter_number', 'stanza_number', 'line_number']},
        ),
    ]