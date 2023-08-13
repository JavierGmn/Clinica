from django.contrib import admin
from .models import *

class PacienteAdmin(admin.ModelAdmin):
   list_display = ('nombre', 'apellido', 'email', 'telefono')
   search_fields =  ['nombre', 'apellido']

class ClinicaAdmin(admin.ModelAdmin):
   list_display = ( 'direccion','nombre','telefono')
   search_fields =  ['nombre', 'telefono']
 

class MedicoAdmin(admin.ModelAdmin):
   list_display = ('nombre', 'apellido', 'email','especialidad', 'telefono', 'fk_clinica')
   search_fields =  ['nombre', 'apellido', 'email']
 

class AdministradorAdmin(admin.ModelAdmin):
   list_display = ('nombre', 'apellido', 'email','fk_clinica')
   search_fields =  ['nombre', 'apellido', 'email']
 

class JornadaAdmin(admin.ModelAdmin):
   list_display = ('fecha', 'horaEntrada', 'horaSalida','horasExtras', 'fk_clinica')
   search_fields =  ['fecha']



 
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Clinica, ClinicaAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Adminostrador, AdministradorAdmin)
admin.site.register(Jornada, JornadaAdmin)