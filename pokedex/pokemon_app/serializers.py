# pokemon_app/serializers.py
from rest_framework import serializers # import serializers from DRF
from .models import Pokemon # import Pokemon model from models.py
from move_app.serializers import MoveSerializer

class PokemonSerializer(serializers.ModelSerializer):
    moves = serializers.SerializerMethodField()

    class Meta:
        model = Pokemon # specify what model this serializer is for
        fields = ['id', 'name', 'level', 'moves', 'type'] # specify the fields you would like this serializer to return

    def get_moves(self, instance):
        moves = instance.moves.all()
        return MoveSerializer(moves, many=True).data