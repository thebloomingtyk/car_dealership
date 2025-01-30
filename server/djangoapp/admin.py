from django.contrib import admin
from .models import CarMake, CarModel

# Inline model for CarModel
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of empty forms to show (you can change this)
    fields = ('name', 'type', 'year')  # Display these fields in the inline form

# Admin class for CarMake
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]  # Embed CarModelInline within CarMakeAdmin
    list_display = ('name', 'description')  # Display name and description in the list
    search_fields = ('name',)  # Search by the name of the CarMake
    list_filter = ('name',)  # Filter by car make

# Admin class for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')  # Display these fields in the list
    search_fields = ('name', 'car_make__name')  # Search by CarModel name or CarMake name
    list_filter = ('type', 'year')  # Filter by car type or year

# Registering the models with the custom admin classes
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
