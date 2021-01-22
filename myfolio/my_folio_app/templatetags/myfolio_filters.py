from django import template


register = template.Library()

@register.filter
def in_skill_category(obj,category_name):
    return obj.filter(skill__category__category_name=category_name)

@register.filter
def single_count_in_skill_category(obj,category_name):
    return obj.filter(skill__category__category_name=category_name).count() == 1