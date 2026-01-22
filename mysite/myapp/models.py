from django.db import models

# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.item_name
    
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=1000)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default='https://imgs.search.brave.com/ly6q72bVHFGys1gJtrLNOkcfdZdZbZuIpJg36gF3bdA/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly91cy4x/MjNyZi5jb20vNDUw/d20veXVwaXJhbW9z/L3l1cGlyYW1vczE0/MDcveXVwaXJhbW9z/MTQwNzAyNDE0LzMw/MjE4ODMzLWZvb2Qt/ZGVzaWduLW92ZXIt/YmVpZ2UtYmFja2dy/b3VuZC12ZWN0b3It/aWxsdXN0cmF0aW9u/LmpwZz92ZXI9Ng')