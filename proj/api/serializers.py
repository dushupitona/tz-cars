from rest_framework import serializers

from car_manager.models import CarModel, CommentModel


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id']


class CarSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='username', read_only=True)  

    class Meta:
        model = CarModel
        fields = ['make', 'model', 'year', 'description', 'created_at', 'updated_at', 'owner']

    def get_queryset(self):
        return CarModel.objects.select_related('owner')


class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['make', 'model', 'year', 'description']


class UpdateCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['make', 'model', 'year', 'description']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)  

    class Meta:
        model = CommentModel
        fields = ['content', 'created_at', 'car', 'author']

    def get_queryset(self):
        return CarModel.objects.select_related('author')
    

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ['content']