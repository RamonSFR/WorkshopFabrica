# Generated by Django 4.1.7 on 2023-03-30 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videogame_store', '0002_loja'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=100)),
            ],
        ),
    ]
