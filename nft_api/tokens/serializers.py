from rest_framework import serializers
from .models import NFT


class NFTSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = NFT
        fields = ['id', 'unique_hash', 'tx_hash','media_url', 'owner']
