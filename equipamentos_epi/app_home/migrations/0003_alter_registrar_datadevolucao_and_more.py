# Generated by Django 5.1.7 on 2025-04-09 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0002_epi_registrar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrar',
            name='datadevolucao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registrar',
            name='observacao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='registrar',
            name='status',
            field=models.CharField(choices=[('emprestado', 'Emprestado'), ('em_uso', 'Em uso'), ('fornecido', 'Fornecido'), ('devolvido', 'Devolvido'), ('danificado', 'Danificado'), ('perdido', 'Perdido')], max_length=100),
        ),
    ]
