# Generated by Django 2.2.1 on 2019-12-19 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('REZERVAPP', '0003_auto_20191219_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='rest_admin_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]