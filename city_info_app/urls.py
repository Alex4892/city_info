from django.urls import path, re_path


from city_info_app.views import (view_home, view_news, view_management, 
                   view_facts, view_contacts, view_history, view_history_people, view_history_photos)

app_name = "app"

urlpatterns = [
    path('', view_home, name='home'),
    re_path(r'^home/.+$', view_home, name='home_fallback'),
    path('news/', view_news, name='news'),
    re_path(r'^news/.+$', view_news, name='news_fallback'),
    path('management/', view_management, name='management'),
    re_path(r'^management/.+$', view_management, name='management_fallback'),
    path('facts/', view_facts, name='facts'),
    re_path(r'^facts/.+$', view_facts, name='facts_fallback'),
    path('contacts/', view_contacts, name='contacts'),
    re_path(r'^contacts/.+$', view_contacts, name='contacts_fallback'),
    path('history/', view_history, name='history'),
    re_path(r'^history/.+$', view_history, name='history_fallback'),
    path('history/people/', view_history_people, name='history_people'),
    re_path(r'^history/people.+$', view_history_people, name='history_people_fallback'),
    path('history/photos/', view_history_photos, name='history_photos'),
    re_path(r'^history/photos/.+$', view_history_photos, name='history_photos_fallback'),
]