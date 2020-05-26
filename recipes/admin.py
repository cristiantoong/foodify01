from django.contrib import admin
from recipes.models import Recipe, Comment, Like
from accounts.models import UserProfile





# admin.site.register(Ingredient)
# admin.site.register(Instruction)
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Like)





