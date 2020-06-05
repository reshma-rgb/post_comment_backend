from django.contrib import admin
from postcomment.models import Post,Comment,UserPost

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserPost)
