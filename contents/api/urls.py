from django.urls import path
from .views import SermonListView, SermonRetrieveView

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
   path('', SermonListView.as_view(), name='sermons_list'),
   path('<int:id>', SermonRetrieveView.as_view(), name='sermons_read')
]
