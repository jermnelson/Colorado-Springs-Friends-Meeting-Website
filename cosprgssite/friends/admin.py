__author__ = "Jeremy Nelson"

from django.contrib import admin
from friends.models import Category, Committee, CommitteeMembership
from friends.models import Friend, OfficeHolder, PhoneNumber, PostalAddress

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CommitteeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('number',)

def full_address(obj):
    return ("{0}, {1} {2}".format(
        obj.streetAddress,
        obj.addressLocality,
        obj.addressRegion))

class PostalAddressAdmin(admin.ModelAdmin):
    list_display = (full_address,)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Committee, CommitteeAdmin)
admin.site.register(CommitteeMembership)
admin.site.register(Friend)
admin.site.register(OfficeHolder)
admin.site.register(PhoneNumber, PhoneNumberAdmin)
admin.site.register(PostalAddress, PostalAddressAdmin)

