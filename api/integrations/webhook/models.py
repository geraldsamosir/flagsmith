from django.db import models

from environments.models import Environment
from integrations.common.models import IntegrationsModel


class WebhookConfiguration(IntegrationsModel):
    environment = models.OneToOneField(
        Environment, related_name="webhook_config", on_delete=models.CASCADE
    )
