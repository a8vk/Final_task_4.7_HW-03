# Generated by Django 4.2 on 2023-04-15 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_new_data_pub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]