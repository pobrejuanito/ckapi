# Generated by Django 2.1.5 on 2019-01-17 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CksdaContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_id', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=255)),
                ('introtext', models.TextField()),
                ('fulltext', models.TextField()),
                ('state', models.IntegerField()),
                ('catid', models.PositiveIntegerField()),
                ('created', models.DateTimeField()),
                ('urls', models.TextField()),
                ('attribs', models.CharField(max_length=5120)),
            ],
            options={
                'db_table': 'cksda_content',
                'managed': False,
            },
        ),
    ]