# Generated by Django 5.1.1 on 2024-10-13 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_alter_rmdata_paralel_dips_weight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rmdata',
            name='user_weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
