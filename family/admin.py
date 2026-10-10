from django.contrib import admin
from .models import FamilyMember

@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "relationship", "active", "created_at")
    search_fields = ("name", "relationship")
    list_filter = ("active", "relationship")
