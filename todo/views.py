from rest_framework import viewsets, permissions
from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Todos to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('id')
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
