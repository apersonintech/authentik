# Generated by Django 5.0.2 on 2024-02-29 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "authentik_providers_oauth2",
            "0017_accesstoken_session_id_authorizationcode_session_id_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="accesstoken",
            name="expires",
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name="authorizationcode",
            name="expires",
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name="devicetoken",
            name="expires",
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name="refreshtoken",
            name="expires",
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
