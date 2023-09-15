from PIL import Image

from django.db import models

from django.contrib.auth.models import User


def compress_and_optimize_image(image_field):

    img = Image.open(image_field.path)

    img.save(image_field.path, quality=80, optimize=True)



class Book(models.Model):

    title = models.CharField(max_length=200)

    year = models.PositiveSmallIntegerField()

    cover_photo = models.ImageField(upload_to='book_covers/')



    def __str__(self):

        return self.title



    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        if self.cover_photo:

            compress_and_optimize_image(self.cover_photo)



class BookPage(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='pages')

    keywords = models.CharField(max_length=800)

    page_photo = models.ImageField(upload_to='book_pages/')



    def __str__(self):

        return f"Page {self.pk} of {self.book.title}"



    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        if self.page_photo:

            compress_and_optimize_image(self.page_photo)



class Post(models.Model):

    title = models.CharField(max_length=255)

    video_file = models.FileField(upload_to='blog_videos/')

    thumbnail = models.ImageField(upload_to='thumbnails/')

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    body = models.TextField()

    date = models.DateField()



    def __str__(self):

        return self.title + '|' + str(self.author)



    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        if self.thumbnail:

            compress_and_optimize_image(self.thumbnail)



class WebImgs(models.Model):

    title = models.CharField(max_length=25)

    thumbnail = models.ImageField(upload_to='web_imgs/')



    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        if self.thumbnail:

            compress_and_optimize_image(self.thumbnail)









    
    

