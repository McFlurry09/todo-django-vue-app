from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .models import TODO
from .serializers import TODOserializer



class TODOViewSet(viewsets.ModelViewSet):
    
    queryset = TODO.objects.all()
    serializer_class = TODOserializer
    filter_backends = [
        DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ("title", "is_complete")
    search_fields = ("title")
    ordering_fields = ("is_complete", "created_at", "updated_at")
