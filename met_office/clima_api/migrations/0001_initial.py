# Generated by Django 3.2.13 on 2022-06-16 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Descripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_clima', models.IntegerField(choices=[[0, 'Soleado'], [1, 'Luvia'], [2, 'Nublado'], [3, 'Nieve']], default=0)),
                ('temperatura', models.FloatField()),
                ('crear_en', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-crear_en'],
            },
        ),
    ]