# Generated by Django 4.1.6 on 2023-04-24 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0005_servico_identificador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriamanutencao',
            name='titulo',
            field=models.CharField(choices=[('TO', 'TROCAR ÓLEO'), ('TPF', 'TROCAR PASTILHAS DE FREIO'), ('B', 'BALENCEAMENTO'), ('S', 'SUSPENSAO')], max_length=3),
        ),
    ]