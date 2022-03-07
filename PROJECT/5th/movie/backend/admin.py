from django.contrib import admin
from .models import MMovie, MAge, MCast, MComment, MGender, MPoint
# Register your models here.

admin.site.register(MMovie)
admin.site.register(MAge)
admin.site.register(MCast)
admin.site.register(MComment)
admin.site.register(MGender)
admin.site.register(MPoint)