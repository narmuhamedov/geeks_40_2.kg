# Generated by Django 3.2.10 on 2024-06-07 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_blog', '0006_alter_reviewsemployees_stars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True)),
                ('price', models.PositiveIntegerField(default=110)),
                ('tags', models.ManyToManyField(to='news_blog.Tag')),
            ],
        ),
    ]
