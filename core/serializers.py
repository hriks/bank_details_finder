from rest_framework import serializers
from core.models import Bank


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = (
            "ifsc_code", "bank_name", "branch", "address",
            "city", "distict", "state"
        )
