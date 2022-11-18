from django.contrib import admin

from .models import Case, CaseItem


class CaseItemInline(admin.TabularInline):
    model = CaseItem


class CaseAdmin(admin.ModelAdmin):
    inlines = [CaseItemInline]


admin.site.register(Case, CaseAdmin)
