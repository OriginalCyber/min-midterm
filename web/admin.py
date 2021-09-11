from django.contrib import admin
from web.models import Physisian, Category, Patient


@admin.register(Physisian)
class PhysisianAdmin(admin.ModelAdmin):
    list_display = ["physisian_code", "first_name", "last_name"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ["patient_code", "patient_name_th", "patient_name_en", "category"]
