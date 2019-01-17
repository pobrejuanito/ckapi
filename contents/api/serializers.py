# converts to json
from rest_framework import serializers
from django.contrib.auth.models import User
from contents.models import CksdaContent

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
      model = User
      fields = ('url', 'username', 'email', 'is_staff')

class SermonSerializer(serializers.ModelSerializer):
   class Meta:
      model = CksdaContent
      fields = ('title','created')