from django.db import models



class FamilyMember(models.Model):
    name = models.CharField(max_length=80)
    relationship = models.CharField(max_length=40)
    notes = models.CharField(max_length=200, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.relationship})"