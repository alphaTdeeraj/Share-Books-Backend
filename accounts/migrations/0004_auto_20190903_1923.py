# Generated by Django 2.2.4 on 2019-09-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_college'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
