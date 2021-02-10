
from django.contrib import admin
from django.urls import path
from django.conf import settings
from Home import views as home_views
urlpatterns = [
    path('', home_views.home, name="home"),
    path('home/', home_views.home, name="home"),
    path('admin/', admin.site.urls),
    path('list_courses', home_views.list_courses, name="list_courses"),
    path('delete_course/<int:id>',
         home_views.delete_course, name="delete_course"),
    path('save_course/', home_views.save_course, name="save_course"),
    path('create_course/', home_views.create_course, name="create_course"),

    path('list_careers', home_views.list_careers, name="list_careers"),
    path('delete_career/<int:id>',
         home_views.delete_career, name="delete_career"),
    path('save_career/', home_views.save_career, name="save_career"),
    path('create_career/', home_views.create_career, name="create_career"),

]


# Configuración para la carga de imágenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
