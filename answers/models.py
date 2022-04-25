from django.db import models
from questions.models import Question

# Create your models here.
class Answer(models.Model):
    id_answer   = models.AutoField(primary_key=True)
    id_user     = models.IntegerField()
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    description = models.TextField()
    total_votes = models.IntegerField()
    is_solution = models.BooleanField(default=False)
    user_name   = models.CharField(max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    deleted_at  = models.DateTimeField(null=True, blank=True)


    def recalculate_votes(self):
        votes = Vote.objects.filter(id_answer__id_answer=self.id_answer, deleted_at=None)
        cont = 0

        for i in votes:
            if i.positive_vote:
                cont += 1
            elif i.negative_vote:
                cont -= 1

        self.total_votes = cont
        self.save()




class Vote(models.Model):
    id_vote       = models.AutoField(primary_key=True)
    id_answer     = models.ForeignKey(Answer, on_delete=models.CASCADE)
    id_user       = models.IntegerField()
    positive_vote = models.BooleanField(default=False)
    negative_vote = models.BooleanField(default=False)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    deleted_at    = models.DateTimeField(null=True, blank=True)