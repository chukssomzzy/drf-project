from rest_framework import serializers
"""Defines different serializers for models"""


class MovieSerializers(serializers.Serializer):
    """Defines the types of different fields in Movies"""
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
