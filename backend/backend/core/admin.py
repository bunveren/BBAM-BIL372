from django.contrib import admin
from .models import Artists, Playlists, User_Interactions, Recently_Listened, Users, User_Follow_Interactions, Albums, Tracks

admin.site.register(Artists)
admin.site.register(Tracks)
admin.site.register(Albums)
admin.site.register(Playlists)
admin.site.register(User_Interactions)
admin.site.register(Recently_Listened)
admin.site.register(Users)
admin.site.register(User_Follow_Interactions)
