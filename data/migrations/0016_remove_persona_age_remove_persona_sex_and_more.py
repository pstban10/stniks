# Generated by Django 5.1.1 on 2024-11-14 14:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0015_remove_prdata_user_records'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='age',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='user',
        ),
        migrations.RemoveField(
            model_name='prdata',
            name='name',
        ),
        migrations.AddField(
            model_name='persona',
            name='name',
            field=models.CharField(default='zooro', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prdata',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='data.persona'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('U', 'UNDEFINED')], max_length=1)),
                ('age', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.persona')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]
