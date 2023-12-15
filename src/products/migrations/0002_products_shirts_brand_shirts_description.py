# Generated by Django 4.2 on 2023-12-14 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(max_length=150)),
                ('category', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('brand', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='shirts',
            name='brand',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='shirts',
            name='description',
            field=models.CharField(max_length=150, null=True),
        ),
    ]