# Generated by Django 4.2 on 2023-05-20 09:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wheater", "0002_alter_city_name_alter_currentweather_dt_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="currentweather",
            name="dt",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="dailyweather",
            name="dt",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="hourlyweather",
            name="dt",
            field=models.DateTimeField(),
        ),
        migrations.AlterUniqueTogether(
            name="currentweather",
            unique_together={("city", "dt")},
        ),
        migrations.AlterUniqueTogether(
            name="dailyweather",
            unique_together={("city", "dt")},
        ),
        migrations.AlterUniqueTogether(
            name="hourlyweather",
            unique_together={("city", "dt")},
        ),
    ]