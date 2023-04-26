from rest_framework import serializers
from .models import Movie, Actor, Review


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     opening_date = serializers.DateField()    # opening_date = serializers.DateField(format="%Y/%m/%d")
#     running_time = serializers.IntegerField()
#     overview = serializers.CharField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.opening_date = validated_data.get(
#             'opening_date', instance.opening_date)
#         instance.running_time = validated_data.get(
#             'running_time', instance.running_time)
#         instance.overview = validated_data.get('overview', instance.overview)
#         instance.save()
#         return instance

from django.core.validators import MaxLengthValidator, MinLengthValidator
from rest_framework.validators import UniqueValidator
from rest_framework.validators import UniqueTogetherValidator


# class MovieSerializer(serializers.ModelSerializer):
#     # name = serializers.CharField(validators=[UniqueValidator(
#     #     queryset=Movie.objects.all(),
#     #     message='이미 존재하는 영화 이름입니다.',
#     # )])
#     overview = serializers.CharField(validators=[MinLengthValidator(
#         limit_value=10), MaxLengthValidator(limit_value=300)])
#     movie_reviews = serializers.PrimaryKeyRelatedField(
#         source='reviews', many=True, read_only=True)
#     actors = serializers.StringRelatedField(many=True, read_only=True)

#     class Meta:
#         model = Movie
#         fields = ['id', 'name', 'movie_reviews', 'actors'
#                   'opening_date', 'running_time', 'overview']
#         # read_only_fields = ['reviews']
#         validators = [
#             UniqueTogetherValidator(
#                 queryset=Movie.objects.all(),
#                 fields=['name', 'overview'],
#             )
#         ]

# fields = '__all__'

# exclude = ['overview']

# fields = ['id', 'name', 'opening_date', 'running_time', 'overview']
# read_only_fields = ['name']

# fields = ['id', 'name', 'opening_date', 'running_time', 'overview']
# extra_kwargs = {
#     'overview': {'write_only': True},
# }

# from rest_framework.serializers import ValidationError

# class MovieSerializer(serializers.ModelSerializer):
#     # ...
#     def overview_validator(value):
#         if value > 300:
#             raise ValidationError('소개 문구는 최대 300자 이하로 작성해야 합니다.')
#         elif value < 10:
#             raise ValidationError('소개 문구는 최소 10자 이상으로 작성해야 합니다.')
#         return value

# class MovieSerializer(serializers.ModelSerializer):
#     overview = serializers.CharField(validators=[overview_validator])
#     class Meta:
#         model = Movie
#         fields = ['id', 'name', 'opening_date', 'running_time', 'overview']

# class MovieSerializer(serializers.ModelSerializer):
#     # ...

#     def validate_overview(self, value):
#         if 10 <= len(value) and len(value) <= 300:
#             return value
#         raise ValidationError('영화 소개는 10자 이상, 300자 이하로 작성해주세요.')

# class MovieSerializer(serializers.ModelSerializer):
#     # ...

#     def validate(self, attrs):
#         if 10 > len(attrs['overview']) or len(attrs['overview']) > 300:
#             raise ValidationError('영화 소개는 10자 이상, 300자 이하로 작성해주세요.')
#         if len(attrs['name']) > 50:
#             raise ValidationError('영화 이름은 50자 이하로 작성해주세요.')
#         return attrs


# class ActorSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     gender = serializers.CharField()
#     birth_date = serializers.DateField()

#     def create(self, validated_data):
#         return Actor.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.gender = validated_data.get('gender', instance.gender)
#         instance.birth_date = validated_data.get(
#             'birth_date', instance.birth_date)
#         instance.save()
#         return instance

class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'name', 'reviews', 'actors',
                  'opening_date', 'running_time', 'overview']
        read_only_fields = ['reviews']


class ActorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ['id', 'name', 'gender', 'birth_date', 'movies']


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'movie', 'username', 'star', 'comment', 'created']
