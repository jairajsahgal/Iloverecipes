from django.contrib import admin

from .models import Book, BookPage, Post, WebImgs

from django.forms import Textarea



from OCR import perform_ocr

from django.db import models

from django.contrib import admin

from .models import Book, Post, WebImgs



class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'year','cover_photo')



    search_fields = ('title', 'year')

    prepopulated_fields = {'title': ('title',)}

    actions = ['compress_cover_photos']



    def compress_cover_photos(self, request, queryset):

        for book in queryset:

            book.compress_and_optimize_image(book.cover_photo)

        self.message_user(request, "Cover photos compressed and optimized successfully.")



admin.site.register(Book, BookAdmin)



class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'date')

    list_filter = ('author', 'date')

    search_fields = ('title', 'author__username')

    date_hierarchy = 'date'

    actions = ['compress_thumbnails']



    def compress_thumbnails(self, request, queryset):

        for post in queryset:

            post.compress_and_optimize_image(post.thumbnail)

        self.message_user(request, "Thumbnails compressed and optimized successfully.")



admin.site.register(Post, PostAdmin)



class WebImgsAdmin(admin.ModelAdmin):

    list_display = ('title',)

    search_fields = ('title',)

    actions = ['compress_images']



    def compress_images(self, request, queryset):

        for web_img in queryset:

            web_img.compress_and_optimize_image(web_img.thumbnail)

        self.message_user(request, "Images compressed and optimized successfully.")



admin.site.register(WebImgs, WebImgsAdmin)


class BookPageAdmin(admin.ModelAdmin):


    list_display=('book','keywords','page_photo')



    def save_model(self, request, obj, form, change):

        custom_keywords = form.cleaned_data.get('keywords')  # Replace with the actual field name from your form

        print(custom_keywords)



        # Get the image field itself
    
        image_field = form.cleaned_data.get('page_photo')  # Replace 'image_field_name' with the actual field name from your form


        if image_field:


            try:

                path = image_field.path
                print("file name", path)


                ocrtext = perform_ocr(path)

                print(ocrtext)

                length=len(obj.keywords)

                if length > 1000:
                    obj.keywords=(ocrtext,custom_keywords)
                else:
                    obj.keywords += f"{ocrtext}"
            except:
                obj.keywords = custom_keywords



        super().save_model(request, obj, form, change)


admin.site.register(BookPage, BookPageAdmin)



#class BookPagesAdmin(admin.ModelAdmin):
#
#    list_display = ['book', 'keywords', 'page_photo']
#
#    list_filter = ['book']
#
#    search_fields = ['keywords']
#
#    fieldsets = [
#
#        ('Book Info', {'fields': ['book', 'keywords', 'page_photo']}),
#
#
#
#    ]
#
#    formfield_overrides = {
#
#        models.CharField: {'widget': Textarea(attrs={'rows': 4, 'cols': 3})},  # Customize the Textarea widget
#
#
#
#    }
#
#
#
#admin.site.register(BookPage, BookPagesAdmin)










