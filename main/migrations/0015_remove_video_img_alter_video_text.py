# Generated by Django 5.1 on 2024-09-13 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_pdf_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='img',
        ),
        migrations.AlterField(
            model_name='video',
            name='text',
            field=models.TextField(verbose_name='Nima haqida'),
        ),
    ]
