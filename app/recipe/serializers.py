"""
Serializers for recipe APIs
"""
from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializers for recipes."""
    class Meta:
        model = Recipe
        fields = ['id','title','time_minutes','price','link']
        read_only_fields =['id']

class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe Detail view."""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id','name']
        read_only_fields = ['id']
