# Generated by Django 5.1.4 on 2025-01-12 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departement', '0007_professeurmodel_nom_prof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professeurmodel',
            name='chef_departement',
            field=models.ManyToManyField(blank=True, to='departement.departementmodel'),
        ),
    ]
