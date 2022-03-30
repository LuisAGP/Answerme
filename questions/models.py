from django.db import models

# Create your models here.
class Question(models.Model):
    id_question = models.AutoField(primary_key=True)
    id_user     = models.IntegerField()
    title       = models.CharField(max_length=255)
    description = models.TextField()
    views       = models.IntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    deleted_at  = models.DateTimeField(null=True, blank=True)




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
