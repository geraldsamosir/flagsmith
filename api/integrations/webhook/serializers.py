from rest_framework import serializers

from integrations.webhook.models import WebhookConfiguration


class WebhookConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebhookConfiguration
        fields = ("id", "base_url")
