from django.db import models

# Create your models here.
class Question(models.Model):

    class Status(models.IntegerChoices):
        NEW = 1, "NEW"
        UNS = 2, "UNSOLVED"
        SOL = 3, "SOLVED"
        CLO = 4, "CLOSED"
    
    id_question = models.AutoField(primary_key=True)
    id_user     = models.IntegerField()
    id_solution = models.IntegerField(null=True, blank=True)
    title       = models.CharField(max_length=255)
    description = models.TextField()
    views       = models.IntegerField()
    status      = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.NEW)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    deleted_at  = models.DateTimeField(null=True, blank=True)

    def get_status(self):
        for i in self.Status.choices:
            if int(self.status) == (i[0]):
                return i[1]




class Label(models.Model):
    id_label    = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    deleted_at  = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.id_label}.- {self.name}"




class LabelsQuestion(models.Model):
    id_labels_question = models.AutoField(primary_key=True)
    id_question        = models.ForeignKey(Question, on_delete=models.CASCADE)
    id_label           = models.ForeignKey(Label, on_delete=models.CASCADE)
    label              = models.CharField(max_length=255)
    created_at         = models.DateTimeField(auto_now_add=True)
    updated_at         = models.DateTimeField(auto_now=True)
    deleted_at         = models.DateTimeField(null=True, blank=True)
