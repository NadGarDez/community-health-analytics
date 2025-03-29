from django.contrib import admin
from .models import UsuarioPersonalizado, Doctor
# Register your models here.


admin.site.register([UsuarioPersonalizado, Doctor])
