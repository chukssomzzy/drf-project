from rest_framework import serializers, validators
from watchlist_app.models import Movie
"""Defines different serializers for models"""


def name_validate(value):
    """Validate len of name"""
    if len(value) < 3:
        raise validators.ValidationError("Too short name")
    else:
        return value


class MovieSerializers(serializers.Serializer):
    """Defines the types of different fields in Movies"""
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_validate])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, movie_data):
        """Create a new movie object"""
        return Movie.objects.create(**movie_data)

    def update(self, movie_inst, movie_data):
        """Update a part of movie data"""
        movie_inst.name = movie_data.get("name", movie_inst.name)
        movie_inst.description = movie_data.get("description",
                                                movie_inst.description)
        movie_inst.active = movie_data.get("active",
                                           movie_inst.active)
        movie_inst.save()
        return movie_inst
# Validators

    # def validate_name(self, name):
    #     """Text name field if it passes  a particular condition"""
    #     if len(name) < 3:
    #         raise validators.\
    #             ValidationError("Your name field must be > 3 chars")
    #     else:
    #         return name

    def validate(self, movie_data):
        """Validate the entire movie data"""
        if movie_data['name'] == movie_data['description']:
            raise validators.ValidationError(
                "Unique field name and description")
        else:
            return movie_data
