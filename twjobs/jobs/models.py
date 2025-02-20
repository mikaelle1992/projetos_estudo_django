from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.DecimalField(decimal_places=2, max_digits=10)
    Skills = models.ManyToManyField("skills.Skill", related_name="jobs")

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return f"<Job: {self.title}>"