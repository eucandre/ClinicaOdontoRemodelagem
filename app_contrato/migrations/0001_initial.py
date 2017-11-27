# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-22 00:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_orcamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato_Nutricional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sign', models.DateField(auto_now=True)),
                ('contract_value', models.FloatField()),
                ('contract_duration', models.DateField(help_text='Data poss\xedvel para finalizar o contrato.')),
                ('client_orcament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_orcamento.Orcamento_Nutri')),
            ],
            options={
                'verbose_name_plural': 'Contratos nutricionais cadastrados na cl\xednica',
            },
        ),
        migrations.CreateModel(
            name='Contrato_Odontologico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sign', models.DateField(auto_now=True)),
                ('contract_value', models.FloatField()),
                ('contract_duration', models.DateField(help_text='Data poss\xedvel para finalizar o contrato.')),
                ('client_orcament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_orcamento.Orcamento_Odonto')),
            ],
            options={
                'verbose_name_plural': 'Contratos odontol\xf3gicos cadastrados na cl\xednica',
            },
        ),
        migrations.CreateModel(
            name='Contrato_Psicologicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sign', models.DateField(auto_now=True)),
                ('contract_value', models.FloatField()),
                ('contract_duration', models.DateField(help_text='Data poss\xedvel para finalizar o contrato.')),
                ('client_orcament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_orcamento.Orcamento_Psico')),
            ],
            options={
                'verbose_name_plural': 'Contratos psicol\xf3gicos cadastrados na cl\xednica',
            },
        ),
        migrations.CreateModel(
            name='HistoricalContrato_Nutricional',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('date_sign', models.DateField(blank=True, editable=False)),
                ('contract_value', models.FloatField()),
                ('contract_duration', models.DateField(help_text='Data poss\xedvel para finalizar o contrato.')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('client_orcament', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='app_orcamento.Orcamento_Nutri')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical contrato_ nutricional',
            },
        ),
        migrations.CreateModel(
            name='HistoricalContrato_Odontologico',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('date_sign', models.DateField(blank=True, editable=False)),
                ('contract_value', models.FloatField()),
                ('contract_duration', models.DateField(help_text='Data poss\xedvel para finalizar o contrato.')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('client_orcament', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='app_orcamento.Orcamento_Odonto')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical contrato_ odontologico',
            },
        ),
        migrations.CreateModel(
            name='HistoricalContrato_Psicologicos',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('date_sign', models.DateField(blank=True, editable=False)),
                ('contract_value', models.FloatField()),
                ('contract_duration', models.DateField(help_text='Data poss\xedvel para finalizar o contrato.')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('client_orcament', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='app_orcamento.Orcamento_Psico')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical contrato_ psicologicos',
            },
        ),
        migrations.CreateModel(
            name='HistoricalResponsavel',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('responsible', models.CharField(max_length=150)),
                ('cpf', models.CharField(blank=True, max_length=11)),
                ('cnpj', models.CharField(blank=True, max_length=22)),
                ('rg', models.CharField(blank=True, max_length=30)),
                ('rua', models.CharField(max_length=150)),
                ('bairro', models.CharField(max_length=150)),
                ('cidade', models.CharField(max_length=150)),
                ('celular', models.CharField(max_length=11)),
                ('watsapp', models.CharField(max_length=11)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical responsavel',
            },
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsible', models.CharField(max_length=150)),
                ('cpf', models.CharField(blank=True, max_length=11)),
                ('cnpj', models.CharField(blank=True, max_length=22)),
                ('rg', models.CharField(blank=True, max_length=30)),
                ('rua', models.CharField(max_length=150)),
                ('bairro', models.CharField(max_length=150)),
                ('cidade', models.CharField(max_length=150)),
                ('celular', models.CharField(max_length=11)),
                ('watsapp', models.CharField(max_length=11)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Respons\xe1vel por clientes cadastrados na cl\xednica',
            },
        ),
        migrations.AddField(
            model_name='historicalcontrato_psicologicos',
            name='responsible',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='app_contrato.Responsavel'),
        ),
        migrations.AddField(
            model_name='historicalcontrato_psicologicos',
            name='user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalcontrato_odontologico',
            name='responsible',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='app_contrato.Responsavel'),
        ),
        migrations.AddField(
            model_name='historicalcontrato_odontologico',
            name='user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalcontrato_nutricional',
            name='responsible',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='app_contrato.Responsavel'),
        ),
        migrations.AddField(
            model_name='historicalcontrato_nutricional',
            name='user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contrato_psicologicos',
            name='responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_contrato.Responsavel'),
        ),
        migrations.AddField(
            model_name='contrato_psicologicos',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contrato_odontologico',
            name='responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_contrato.Responsavel'),
        ),
        migrations.AddField(
            model_name='contrato_odontologico',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contrato_nutricional',
            name='responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_contrato.Responsavel'),
        ),
        migrations.AddField(
            model_name='contrato_nutricional',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
