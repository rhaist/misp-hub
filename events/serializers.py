from rest_framework import serializers

class AttributeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeType
