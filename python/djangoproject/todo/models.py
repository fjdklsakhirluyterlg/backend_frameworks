from django.db import models
from django.utils.timezone import now

# Create your models here.


class TodoList(models.Model):
    name = models.CharField(max_length=350)

    def items(self):
        todos = self.objects.all()

class Todo(models.Model):
    title = models.CharField(max_length=350)
    done = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=now)
    todolist = models.ForeignKey(TodoList, on_delete="CASCADE")

