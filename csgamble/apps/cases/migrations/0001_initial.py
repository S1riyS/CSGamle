# Generated by Django 4.1.3 on 2022-11-17 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=1000)),
            ],
        ),
        migrations.CreateModel(
            name='CaseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cases.case')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.item')),
                ('wear_level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.wearlevel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='case',
            name='items',
            field=models.ManyToManyField(through='cases.CaseItem', to='core.item'),
        ),
    ]
