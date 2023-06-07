from django.urls import path
from .views import *


urlpatterns = [

    path(route='', view=index, name="index"),
    path(route='hakkimizda', view=about, name="about"),
    path(route='menü', view=menü, name="menü"),
    path(route='rezervasyon-yap', view=reservation, name="reservation"),
    path(route='ekibimiz', view=team_view, name="team"),
    path(route='iletisim', view=contact, name="contact"),
    path(route='hizmetlerimiz', view=services_view, name="service"),
    path(route='müsteri-yorumlari', view=user_comments, name="comment"),
    path(route='services/query/reservation-query', view=reservation_query, name='query')
]