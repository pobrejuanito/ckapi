# genetic view
from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from contents.models import CksdaContent
from .serializers import SermonSerializer, UserSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SermonListView(generics.ListAPIView):
   lookup_field = 'id'
   serializer_class = SermonSerializer

   def get_queryset(self):
      return CksdaContent.objects.all()
      
class SermonRetrieveView(generics.RetrieveAPIView):
   lookup_field = 'id'
   serializer_class = SermonSerializer
   #queryset = CksdaContent.objects.all()
   def get_queryset(self):
      return CksdaContent.objects.all()
