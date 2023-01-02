from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db.models.signals import pre_save


# Create your models here.
class Shop_By_Categories(models.Model):
    category = models.CharField(max_length=200)
    
    def __str__(self):
        return self.category


class Shop_By_Brand1(models.Model):
    brand_name=models.CharField(max_length=200,blank=True, null=True)
    brand_logo = models.ImageField(upload_to = "media")
    
    def __str__(self):
        return self.brand_name


class Language(models.Model):
    language_name=models.CharField(max_length=200,blank=True, null=True)
    language_logo = models.ImageField(upload_to = "media")
    
    def __str__(self):
        return self.language_name


class Accessories(models.Model):
    accessories_name=models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return self.accessories_name


class Shopping_Bag(models.Model):
    title=models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return self.title


class Shopping_Bag_Items(models.Model):
    title=models.ForeignKey(Shopping_Bag,on_delete=models.CASCADE,null=True)
    heading=models.CharField(max_length=200,blank=True, null=True)
    price=models.CharField(max_length=200,blank=True, null=True)
    image=models.ImageField(upload_to = "media")

    def __str__(self):
        return self.heading


class slider(models.Model):
    product_heading=models.CharField(max_length=200,blank=True, null=True)
    animated_text_description=models.TextField(max_length=200,blank=True, null=True)
    small_animated_word=models.CharField(max_length=200,blank=True, null=True)
    product_price=models.FloatField()
    background_cover_image=models.ImageField(upload_to = "media")
    product_image=models.ImageField(upload_to = "media")
    
    def __str__(self):
        return self.product_heading


class Categoryall(models.Model):
    main_category = models.ForeignKey(Shop_By_Categories,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' __ ' + self.main_category.category


class Sub_Categoryall(models.Model):
    categori=models.ForeignKey(Categoryall,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.categori.main_category.category + ' __ ' + self.categori.name + '__ ' + self.name


class Section(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Color(models.Model):
    code=models.CharField(max_length=100)


    def __str__(self):
        return self.code




class Product(models.Model):
    total_quantity=models.IntegerField()
    Availability=models.IntegerField()
    image=models.ImageField(upload_to = "Featured Images",default=False)
    name=models.CharField(max_length=200,default=False)
    price=models.IntegerField()
    Discount=models.IntegerField()
    Product_information=RichTextField()
    model_Name=models.CharField(max_length=200)
    Category=models.ForeignKey(Categoryall,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True)
    Tags=models.CharField(max_length=200)
    Description=RichTextField()
    section=models.ForeignKey(Section,on_delete=models.DO_NOTHING)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product_detail", kwargs={'slug': self.slug})

    class Meta:
        db_table = "app_Product"

def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Product)

    

class Product_Image(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to = "Product Images",default=False)



class Additional_Information(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    specification=models.CharField(max_length=100)
    detail=RichTextField()


class Rating(models.Model):
    name=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    review=models.TextField()
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

    def __str__(self):
        return str(self.pk)

class Shipping_Addres(models.Model):
    f_name=models.CharField(max_length=200)
    l_name=models.CharField(max_length=200)
    company_name=models.CharField(max_length=200)
    area_code=models.CharField(max_length=200)
    primary_phone=models.CharField(max_length=200)
    street_address=models.CharField(max_length=200)
    street_address_2=models.CharField(max_length=200,default=False)
    zip_code=models.CharField(max_length=200)
    bussiness_type=models.BooleanField(default=False,null=True)
    

    def __str__(self):
        return str(self.f_name + " "+ self.l_name+ " " + self.zip_code)

class Payment_Type(models.Model):
    payment_type=models.ImageField(upload_to = "Payment_Type",default=False)

    def __str__(self):
        return self.id
    

class Payment_Method(models.Model):
    cardholder_name=models.CharField(max_length=200)
    cardnumber=models.CharField(max_length=200)
    payment_type=models.CharField(max_length=200)
    expiration_date_month=models.CharField(max_length=200)
    expiration_date_year=models.CharField(max_length=200)
    CSC_card=models.CharField(max_length=200)

    def __str__(self):
        return self.cardnumber
    



