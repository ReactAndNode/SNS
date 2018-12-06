from django.contrib import admin

from .models import Profile
# Register your models here.


# Here is the stuff help you to display the tables better
class PAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'email_confirmed',
                    'date_joined', 'publisher'
                    ]


admin.site.register(Profile, PAdmin)
