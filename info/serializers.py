from rest_framework import serializers

from info.models import Credit


class CreditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credit
        fields = ("name", "position")

    def to_representation(self, instance):
        credit = super(CreditSerializer, self).to_representation(instance)
        credit.pop("position")
        credit["position"] = instance.position.name
        return credit
