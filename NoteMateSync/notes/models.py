from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title=models.CharField(max_length=150)
    course=models.TextField()
    liked=models.ManyToManyField(User,default=None,blank=True,related_name='Liked')
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField( auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='author')
    img=models.ImageField(upload_to='note_img',blank=True,null=True)

    def __str__(self):
        return str(self.title)
    
    @property
    def num_likes(self):
        return self.liked.all().count()
    
LIKE_CHOICES=(
    ('LIKE','LIKE'),
    ('UNLIKE','UNLIKE')
)

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    note=models.ForeignKey(Note,on_delete=models.CASCADE)
    value=models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)

    def __str__(self):
        return str(self.note)