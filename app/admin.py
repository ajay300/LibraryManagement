from django.contrib import admin

from app.models import Book , IssuedBook ,Member


# # admin.site.register()

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','isbn','category']

@admin.register(IssuedBook)
class IssuedBookAdmin(admin.ModelAdmin):
    list_display = ['student_id','isbn']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['user','first_name','last_name','std','roll_no','phone','branch']