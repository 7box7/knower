from django.contrib import admin
from .models import *


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "explore_name", "console_name", "photo")


@admin.register(ChildTopic)
class ChildTopicAdmin(admin.ModelAdmin):
    list_display = ("id", "external_id", "lvl_id", "id_topic", "importance", "redirect")


@admin.register(Way)
class WayAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(HistoryPeriodDate)
class HistoryPeriodDateAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "start_date", "end_date")


@admin.register(HistoryEventDate)
class HistoryEventDateAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "without_md", "date", "country", "period_id")


@admin.register(HistoryHumanDate)
class HistoryHumanDateAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date", "country", "who")


@admin.register(HistoryKingDate)
class HistoryKingDateAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date", "country")


@admin.register(Formula)
class FormulaAdmin(admin.ModelAdmin):
    list_display = ("id", "formul", "defin")


@admin.register(Definition)
class DefinitionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "text", "topic")


@admin.register(AllForms)
class AllFormsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "typee", "topic_id")


@admin.register(FormType)
class FormTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "fields", "names")
