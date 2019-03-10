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
      if self.kwargs['lang'] == 'ko':
         # Korean
         catId = 27
      else:
         # English
         catId = 28

      return CksdaContent.objects.raw('SELECT cc.*, (SELECT fv.value FROM cksda_fields_values as fv WHERE fv.field_id = 1 AND fv.item_id = cc.id) as speakerName, (SELECT fv.value FROM cksda_fields_values as fv WHERE fv.field_id = 2 AND fv.item_id = cc.id) as url FROM cksda_content as cc WHERE catId = ' + str(catId))
      #return CksdaContent.objects.all().filter(catid=catId)
   
   def get_fields(self):

      return CksdaFieldsValues

class SermonRetrieveView(generics.RetrieveAPIView):
   lookup_field = 'id'
   serializer_class = SermonSerializer
   #queryset = CksdaContent.objects.all()
   def get_queryset(self):
      return CksdaContent.objects.all()
