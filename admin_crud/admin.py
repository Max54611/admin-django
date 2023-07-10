from django.contrib import admin

# Register your models here.
from .models import * 

@admin.register(Section)
class Section(admin.ModelAdmin):
    list_display=("section_id","section_name")


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display=("category_id","category_name","image_url","section_section")

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display=("product_id","description","image_url","marked_price","product_name","review_count","selling_price","total_rating","category_category")
    


