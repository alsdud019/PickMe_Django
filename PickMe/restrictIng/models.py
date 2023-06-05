from django.db import models

# Create your models here.
class restrictList(models.Model):
    class Meta:
        db_table='restrictList'

    # restrict_id=models.CharField(max_length=20,null=False)
    restrict_regulate_type=models.CharField(max_length=10,null=True)
    restrict_name_ko=models.CharField(max_length=200,null=False)
    restrict_name_en=models.CharField(max_length=200,null=True)
    restrict_country=models.CharField(max_length=10, null=True)
    restrict_limit=models.TextField(null=True)

class allIngredientList(models.Model):
    class Meta:
        db_table='allIngredientList'
    ingredient_ko_name=models.CharField(max_length=2000,null=False,default='')
    ingredient_en_name=models.CharField(max_length=2000,null=True,default='')

class ingredeintList(models.Model):
    class Meta:
        db_table='ingredientList'
    #ingredient_id=models.ImageField()
    ingredient_ko_name=models.CharField(max_length=2000)
    ingredient_en_name=models.CharField(max_length=2000)
    restrict_type=models.BooleanField(default=False)
    restrict_regulate_type=models.CharField(max_length=10,null=True)     
    restrict_limit=models.TextField(null=True)
    restrict_country=models.CharField(max_length=10, null=True)

class imgpost(models.Model):
    image=models.ImageField(upload_to='images')   
    def _str__(self):
        return str(self.title)
    



