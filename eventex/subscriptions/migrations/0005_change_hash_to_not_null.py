# Generated by Django 2.0.5 on 2021-04-05 11:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_populate_uuid_values'),
    ]

    operations = [
     migrations.AlterField(
            model_name='subscription',
            name='hashid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='hash'),
        ),
    ]
