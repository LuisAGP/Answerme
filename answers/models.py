from django.db import models
from questions.models import Question

# Create your models here.
class Answer(models.Model):
    id_answer   = models.AutoField(primary_key=True)
    id_user     = models.IntegerField()
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    description = models.TextField()
    votes       = models.IntegerField()
    is_solution = models.BooleanField(default=False)
    user_name   = models.CharField(max_length=255)

