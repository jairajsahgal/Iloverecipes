from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField()
    cover_photo = models.ImageField(upload_to='book_covers/')

    def __str__(self):
        return self.title

class BookPage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='pages')
    keywords = models.CharField(max_length=800)
    page_photo = models.ImageField(upload_to='book_pages/')

    def __str__(self):
        return f"Page {self.pk} of {self.book.title}"
    

class Post(models.Model):
    title= models. CharField(max_length=255)
    video_file= models.FileField(upload_to='blog_videos/')
    thumbnail= models.ImageField(upload_to='thumbnails/')
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    body= models.TextField()
    date= models.DateField()

    def __str__(self):
        return self.title + '|' + str(self.author)
    
class WebImgs(models.Model):
    title= models.CharField(max_length=25)
    thumbnail= models.ImageField(upload_to='web_imgs/')

    
    

