from django.contrib import admin

from car_manager.models import CarModel, CommentModel

class CarAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'updated_at',)
    fields = ('id', 'make', 'model', 'year', 'description', 'created_at', 'updated_at', 'owner')


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at')
    fields = ('id', 'content', 'created_at', 'car', 'author')


admin.site.register(CarModel, CarAdmin)
admin.site.register(CommentModel, CommentAdmin)

