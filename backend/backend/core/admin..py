from django.contrib import admin
from .models import Artists, Playlists, UserInteractions, RecentlyListened, Users, UserFollowInteractions, Albums, Tracks

admin.site.register(Artists)
admin.site.register(Tracks)
admin.site.register(Albums)
admin.site.register(Playlists)
admin.site.register(UserInteractions)
admin.site.register(RecentlyListened)
admin.site.register(Users)
admin.site.register(UserFollowInteractions)