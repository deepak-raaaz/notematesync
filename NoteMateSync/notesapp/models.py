from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title=models.CharField(max_length=50)
    pages=models.IntegerField()
    img=models.ImageField(upload_to='Notes',blank=True,null=True)
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    liked=models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='author')

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
        value=models.CharField(choices=LIKE_CHOICES,default='LIKE',max_length=10)

        def __str__(self):
            return str(self.note)

    

