# Generated by Django 2.2.4 on 2019-08-31 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20190831_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='branch',
            field=models.CharField(choices=[('Mechanical', 'Mechanical'), ('Computer Science', 'Computer Science'), ('Information science', 'Information science'), ('Electrical', 'Electrical'), ('Civil', 'Civil'), ('Biotechnology', 'Biotechnology'), ('Chemical', 'Chemical'), ('Electronics and Communication', 'Electronics and Communication'), ('Industrial and Management', 'Industrial and Management'), ('Medical Electronics', 'Medical Electronics'), ('All', 'All')], max_length=40),
        ),
    ]
