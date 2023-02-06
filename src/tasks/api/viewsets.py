from rest_framework.viewsets import ModelViewSet

from tasks.api.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = TaskSerializer.Meta.model.objects.all()
    lookup_url_kwarg = "task_id"
