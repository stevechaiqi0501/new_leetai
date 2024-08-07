# Generated by Django 5.0.6 on 2024-07-20 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leetai_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='datetime',
            field=models.DateField(auto_now_add=True, verbose_name='投稿日時'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True, max_length=500, null=True)),
                ('datetime', models.DateField(auto_now_add=True, verbose_name='投稿日時')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='参考画像')),
                ('bestanswer', models.BooleanField(default=False)),
                ('Question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Leetai_app.question')),
            ],
            options={
                'verbose_name_plural': 'Answer',
            },
        ),
    ]
