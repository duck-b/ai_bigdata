# Generated by Django 4.0.3 on 2022-03-19 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_mitem_delete_useritem'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='mitem',
            table='m_item',
        ),
    ]