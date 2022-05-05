from django.contrib import admin

from petshop.models import Customer, Shop, Pet, Item, POrder, Contains


admin.site.register(Customer)
admin.site.register(Shop)
admin.site.register(Pet)
admin.site.register(Item)
admin.site.register(POrder)
admin.site.register(Contains)
