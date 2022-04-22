from django.contrib import admin
from dagracemarketapp.models import(Category,
                                    Product,
                                    Slideimg,
                                            )    
           
           


# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Slideimg)