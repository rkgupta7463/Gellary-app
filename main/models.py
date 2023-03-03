from django.db import models
from django.conf import settings
# Create your models here.


##user rishu
##Pass :- Rishu@7463

###model for image
class uploadImg(models.Model):
    image=models.FileField(upload_to="media")
    created_img=models.DateTimeField(auto_created=True,auto_now=True)   
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name = 'uploadImg')

    def __str__(self):
        return f'{self.author}+{self.image}'