# Generated by Django 2.2.7 on 2019-12-01 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0012_auto_20191201_1356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ('id', 'user__first_name', 'user__last_name')},
        ),
        migrations.AlterModelOptions(
            name='membership',
            options={'ordering': ('valid_from', 'member')},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ('since', 'position', 'member')},
        ),
        migrations.AlterField(
            model_name='membership',
            name='fee_amount',
            field=models.FloatField(choices=[(20, 'General'), (10, 'Estudiante y/o Desempleado'), (0, 'Exento')], default=20),
        ),
    ]
