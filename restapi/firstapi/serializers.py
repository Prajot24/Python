from rest_framework import serializers

class studentSerializer(serializers.Serializer):
    name = serializers.CharField( max_length=50)
    Roll_no = serializers.IntegerField()
    city = serializers.CharField( max_length=50)