from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_django_admin_config'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='hashid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True, verbose_name='hash'),
        ),
    ]
  

