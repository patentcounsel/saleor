# Generated by Django 3.2.18 on 2023-03-20 08:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0021_app_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="app",
            name="brand_logo_default",
            field=models.ImageField(blank=True, null=True, upload_to="app-logos"),
        ),
        migrations.AddField(
            model_name="appinstallation",
            name="brand_logo_default",
            field=models.ImageField(blank=True, null=True, upload_to="app-logos"),
        ),
    ]