# Generated by Django 3.2.3 on 2021-06-13 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210611_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='body',
            new_name='body_img',
        ),
        migrations.AddField(
            model_name='product',
            name='body_info',
            field=models.URLField(default='o'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='body_size',
            field=models.URLField(default='o'),
            preserve_default=False,
        ),
    ]