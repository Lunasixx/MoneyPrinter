# Generated by Django 3.2.4 on 2021-06-12 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin', models.CharField(blank=True, max_length=255, null=True)),
                ('symbol', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('platform1', models.CharField(blank=True, max_length=50, null=True)),
                ('platform2', models.CharField(blank=True, max_length=50, null=True)),
                ('platform3', models.CharField(blank=True, max_length=50, null=True)),
                ('contract1', models.CharField(blank=True, max_length=32, null=True)),
                ('contract2', models.CharField(blank=True, max_length=32, null=True)),
                ('contract3', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
    ]
