# Generated by Django 4.1.1 on 2022-09-22 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0002_disciplina'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boletim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrega', models.DateField()),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.aluno')),
            ],
        ),
        migrations.CreateModel(
            name='NotasBoletim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField(max_length=10)),
                ('boletim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.boletim')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escola.disciplina')),
            ],
        ),
    ]
