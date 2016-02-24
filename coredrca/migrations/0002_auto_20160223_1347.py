# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coredrca', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coredrca.Curso'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='disciplinas',
            field=models.ManyToManyField(to='coredrca.Disciplina'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='secretaria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coredrca.Departamento'),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coredrca.Curso'),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='disc_pre',
            field=models.ManyToManyField(to='coredrca.Disciplina'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coredrca.Departamento'),
        ),
        migrations.AlterField(
            model_name='secretaria',
            name='departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coredrca.Departamento'),
        ),
    ]
