# Generated by Django 5.1.1 on 2024-10-10 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_remove_rm_skater_squat_rm_paralel_dips_weight_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rm',
            name='date_of_medition',
            field=models.DateField(default='2024-10-04'),
            preserve_default=False,
        ),
    ]
