from rest_framework import serializers
from app.models import QuoteModel

class quoteSerializer(serializers.ModelSerializer):
    class Meta():
        model = QuoteModel
        fields = '__all__'