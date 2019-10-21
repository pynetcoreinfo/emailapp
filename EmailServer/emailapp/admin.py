from django.contrib import admin

from emailapp.models import EMailCompose

class EmailAdmin(admin.ModelAdmin):
    list_display = ('id','author','subject','message','date_sented')

admin.site.register(EMailCompose,EmailAdmin)
