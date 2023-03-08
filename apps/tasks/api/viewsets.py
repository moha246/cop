from core.viewsets import PartialModelViewSet
from tasks.api.serializers import TaskSerializer


class TaskViewSet(PartialModelViewSet):
    serializer_class = TaskSerializer
    queryset = TaskSerializer.Meta.model.objects.all()
    lookup_url_kwarg = "task_id"
