# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-22 00:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_servicos', '0001_initial'),
        ('app_base', '0001_initial'),
        ('app_contrato', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalRecebe_Contrato_Nutri',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('value_received_total', models.FloatField()),
                ('value_received_in_Credit', models.FloatField(blank=True)),
                ('value_received_in_Debit', models.FloatField(blank=True)),
                ('value_received_in_Money', models.FloatField(blank=True)),
                ('value_received_in_Ticket', models.FloatField(blank=True)),
                ('value_received_in_Check', models.FloatField(blank=True)),
                ('value_received_in_Promissory', models.FloatField(blank=True)),
                ('remaining_value', models.FloatField(blank=True, help_text='Valor que falta ser pago pelo m\xeas de tratamento, caso haja.')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('client', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='app_contrato.Contrato_Nutricional')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical recebe_ contrato_ nutri',
            },
        ),
        migrations.CreateModel(
            name='HistoricalRecebe_Contrato_Odonto',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('value_received_total', models.FloatField()),
                ('value_received_in_Credit', models.FloatField(blank=True)),
                ('value_received_in_Debit', models.FloatField(blank=True)),
                ('value_received_in_Money', models.FloatField(blank=True)),
                ('value_received_in_Ticket', models.FloatField(blank=True)),
                ('value_received_in_Check', models.FloatField(blank=True)),
                ('value_received_in_Promissory', models.FloatField(blank=True)),
                ('remaining_value', models.FloatField(blank=True, help_text='Valor que falta ser pago pelo m\xeas de tratamento, caso haja.')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('client', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='app_contrato.Contrato_Odontologico')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical recebe_ contrato_ odonto',
            },
        ),
        migrations.CreateModel(
            name='HistoricalRecebe_Contrato_Psico',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('value_received_total', models.FloatField()),
                ('value_received_in_Credit', models.FloatField(blank=True)),
                ('value_received_in_Debit', models.FloatField(blank=True)),
                ('value_received_in_Money', models.FloatField(blank=True)),
                ('value_received_in_Ticket', models.FloatField(blank=True)),
                ('value_received_in_Check', models.FloatField(blank=True)),
                ('value_received_in_Promissory', models.FloatField(blank=True)),
                ('remaining_value', models.FloatField(blank=True, help_text='Valor que falta ser pago pelo m\xeas de tratamento, caso haja.')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('client', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='app_contrato.Contrato_Psicologicos')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical recebe_ contrato_ psico',
            },
        ),
        migrations.CreateModel(
            name='HistoricalRecebe_sem_contrato_nutri',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('velue_attendance', models.FloatField()),
                ('value_received_total', models.FloatField()),
                ('value_received_in_Credit', models.FloatField(blank=True)),
                ('value_received_in_Debit', models.FloatField(blank=True)),
                ('value_received_in_Money', models.FloatField(blank=True)),
                ('value_received_in_Ticket', models.FloatField(blank=True)),
                ('value_received_in_Check', models.FloatField(blank=True)),
                ('value_received_in_Promissory', models.FloatField(blank=True)),
                ('remaining_value', models.FloatField(blank=True, help_text='Valor que falta ser pago pelo servi\xe7o, caso haja.')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('client', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='app_base.Cliente')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical recebe_sem_contrato_nutri',
            },
        ),
        migrations.CreateModel(
            name='HistoricalRecebe_sem_contrato_odonto',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('velue_attendance', models.FloatField()),
                ('value_received_total', models.FloatField()),
                ('value_received_in_Credit', models.FloatField(blank=True)),
                ('value_received_in_Debit', models.FloatField(blank=True)),
                ('value_received_in_Money', models.FloatField(blank=True)),
                ('value_received_in_Ticket', models.FloatField(blank=True)),
                ('value_received_in_Check', models.FloatField(blank=True)),
                ('value_received_in_Promissory', models.FloatField(blank=True)),
                ('remaining_value', models.FloatField(blank=True, help_text='Valor que falta ser pago pelo servi\xe7o, caso haja.')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('client', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='app_base.Cliente')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical recebe_sem_contrato_odonto',
            },
        ),
        migrations.CreateModel(
            name='HistoricalRecebe_sem_contrato_Psicologico',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('velue_attendance', models.FloatField()),
                ('value_received_total', models.FloatField()),
                ('value_received_in_Credit', models.FloatField(blank=True)),
                ('value_received_in_Debit', models.FloatField(blank=True)),
                ('value_received_in_Money', models.FloatField(blank=True)),
                ('value_received_in_Ticket', models.FloatField(blank=True)),
                ('value_received_in_Check', models.FloatField(blank=True)),
                ('value_received_in_Promissory', models.FloatField(blank=True)),
                ('remaining_value', models.FloatField(blank=True, help_text='Valor que falta ser pago pelo servi\xe7o, caso haja.')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('client', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='app_base.Cliente')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical recebe_sem_contrato_ psicologico',
            },
        ),
        migrations.CreateModel(
            name='Recebe_Contrato_Nutri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_received_total', models.FloatField()),
                ('value_received_in_Credit', models.FloatField(blank=True)),
                ('value_received_in_Debit', models.FloatField(blank=True)),
                ('value_received_in_Money', models.FloatField(blank=True)),
                ('value_received_in_Ticket', models.FloatField(blank=True)),
                ('value_received_in_Check', models.FloatField(blank=True)),
                ('value_received_in_Promissory', models.FloatField(blank=True)),
                ('remaining_value', models.FloatField(blank=True, help_text='Valor que falta ser pago pelo m\xeas de tratamento, caso haja.')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_contrato.Contrato_Nutricional')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Recebe dos contratos Nutricionais',
            },
        ),
        migrations.CreateModel(
            name='Recebe_Contrato_Odonto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_received_total', models.FloatField()),
                ('value_received_in_Credit', models.FloatField(blank=True)),
                ('value_received_in_Debit', models.FloatField(blank=True)),
                ('value_received_in_Money', models.FloatField(blank=True)),
                ('value_received_in_Ticket', models.FloatField(blank=True)),
                ('value_received_in_Check', models.FloatField(blank=True)),
                ('value_received_in_Promissory', models.FloatField(blank=True)),
                ('remaining_value', models.FloatField(blank=True, help_text='Valor que falta ser pago pelo m\xeas de tratamento, caso haja.')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_contrato.Contrato_Odontologico')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Recebe dos contratos odontol\xf3gicos',
            },
        ),
        migrations.CreateModel(
            name='Recebe_Contrato_Psico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_received_total', models.FloatField()),
                ('value_received_in_Credit', models.FloatField(blank=True)),
                ('value_received_in_Debit', models.FloatField(blank=True)),
                ('value_received_in_Money', models.FloatField(blank=True)),
                ('value_received_in_Ticket', models.FloatField(blank=True)),
                ('value_received_in_Check', models.FloatField(blank=True)),
                ('value_received_in_Promissory', models.FloatField(blank=True)),
                ('remaining_value', models.FloatField(blank=True, help_text='Valor que falta ser pago pelo m\xeas de tratamento, caso haja.')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_contrato.Contrato_Psicologicos')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Recebe dos contratos psicol\xf3gicos',
            },
        ),
        migrations.CreateModel(
            name='Recebe_sem_contrato_nutri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('velue_attendance', models.FloatField()),
                ('value_received_total', models.FloatField()),
                ('value_received_in_Credit', models.FloatField(blank=True)),
                ('value_received_in_Debit', models.FloatField(blank=True)),
                ('value_received_in_Money', models.FloatField(blank=True)),
                ('value_received_in_Ticket', models.FloatField(blank=True)),
                ('value_received_in_Check', models.FloatField(blank=True)),
                ('value_received_in_Promissory', models.FloatField(blank=True)),
                ('remaining_value', models.FloatField(blank=True, help_text='Valor que falta ser pago pelo servi\xe7o, caso haja.')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_base.Cliente')),
                ('serices', models.ManyToManyField(to='app_servicos.Servicos_Nutricional')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Recebe os clientes sem contrato na clinica',
            },
        ),
        migrations.CreateModel(
            name='Recebe_sem_contrato_odonto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('velue_attendance', models.FloatField()),
                ('value_received_total', models.FloatField()),
                ('value_received_in_Credit', models.FloatField(blank=True)),
                ('value_received_in_Debit', models.FloatField(blank=True)),
                ('value_received_in_Money', models.FloatField(blank=True)),
                ('value_received_in_Ticket', models.FloatField(blank=True)),
                ('value_received_in_Check', models.FloatField(blank=True)),
                ('value_received_in_Promissory', models.FloatField(blank=True)),
                ('remaining_value', models.FloatField(blank=True, help_text='Valor que falta ser pago pelo servi\xe7o, caso haja.')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_base.Cliente')),
                ('serices', models.ManyToManyField(to='app_servicos.Servicos_Odonto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Recebe os clientes sem contrato na clinica',
            },
        ),
        migrations.CreateModel(
            name='Recebe_sem_contrato_Psicologico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('velue_attendance', models.FloatField()),
                ('value_received_total', models.FloatField()),
                ('value_received_in_Credit', models.FloatField(blank=True)),
                ('value_received_in_Debit', models.FloatField(blank=True)),
                ('value_received_in_Money', models.FloatField(blank=True)),
                ('value_received_in_Ticket', models.FloatField(blank=True)),
                ('value_received_in_Check', models.FloatField(blank=True)),
                ('value_received_in_Promissory', models.FloatField(blank=True)),
                ('remaining_value', models.FloatField(blank=True, help_text='Valor que falta ser pago pelo servi\xe7o, caso haja.')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_base.Cliente')),
                ('serices', models.ManyToManyField(to='app_servicos.Servicos_Psicologicos')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Recebe os clientes sem contrato na clinica',
            },
        ),
    ]
