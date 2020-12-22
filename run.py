from app.models import Todo
from app.serializers import TodoSerializer

todo = Todo.objects.first()
serializer = TodoSerializer(todo)
serializer.data