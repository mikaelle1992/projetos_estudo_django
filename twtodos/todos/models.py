from django.db import models
from datetime import date

class Todo(models.Model):
    title = models.CharField(verbose_name="Título", max_length=255, unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data de entrega",null=False, blank=False)
    finished_at = models.DateField(null=True, blank=False)


    class Meta:
        ordering = ["deadline"]
        #ordenação

    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()
