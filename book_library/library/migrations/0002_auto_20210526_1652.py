# Generated by Django 3.1.1 on 2021-05-26 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='მომხმარებელი'),
        ),
        migrations.AddField(
            model_name='quantity',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book', verbose_name='წიგნის სახელი'),
        ),
        migrations.AddField(
            model_name='quantity',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.branch', verbose_name='ფილიალი'),
        ),
        migrations.AddField(
            model_name='order',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book', verbose_name='წიგნი'),
        ),
        migrations.AddField(
            model_name='order',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.branch', verbose_name='ფილიალი'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='მომხმარებელი'),
        ),
        migrations.AddField(
            model_name='history',
            name='return_book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.order', verbose_name='რომელი წიგნი დააბრუნა'),
        ),
        migrations.AddField(
            model_name='history',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='მომხმარებელი'),
        ),
        migrations.AddField(
            model_name='branch',
            name='book',
            field=models.ManyToManyField(through='library.Quantity', to='library.Book'),
        ),
    ]
