# Generated by Django 4.2.5 on 2023-10-25 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_modelwords_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modelcatswords',
            options={'verbose_name': 'Categories', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='modelwords',
            options={'verbose_name': 'Words', 'verbose_name_plural': 'Words'},
        ),
        migrations.AddField(
            model_name='modelcatswords',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='modelwords',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.modelcatswords'),
        ),
    ]
