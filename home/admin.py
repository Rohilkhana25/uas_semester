from django.contrib import admin
from home.models import Rohildb
# Register your models here.
class RohilAdmin(admin.ModelAdmin):
    list_display = ['npm','nama','alamat','tetala', 'kelas']
    search_fields = ['npm','nama','alamat','tetala', 'kelas']
    list_display = ['npm','nama','alamat','tetala', 'kelas']
    list_per_page =9
    
admin.site.register(Rohildb,RohilAdmin)