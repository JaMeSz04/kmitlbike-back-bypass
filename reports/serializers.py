from rest_framework import serializers

from reports.models import Feedback, Report


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ("like", "comment")

    def create(self, validated_data):
        return Feedback.objects.create(**validated_data)


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ("report_type", "detail")

    def create(self, validated_data):
        return Report.objects.create(**validated_data)

    def validate_report_type(self, instance):
        if instance in [report_type[0] for report_type in Report.get_type()]:
            return instance
        raise serializers.ValidationError("Report type does not exist.")
