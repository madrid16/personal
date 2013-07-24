from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.mantenimiento', name='index_view'),
    url(r'^inicio$', 'app.views.inicio', name='inicio'),
    url(r'^contacto$', 'app.views.contact', name='contact'),
    url(r'^contact$', 'app.views.contactValid', name='contactValid'),
    url(r'^nosotros$', 'app.views.nosotrosView', name='nosotrosView'),
    url(r'^proyectos$', 'app.views.proyectosView', name='proyectosView'),
    url(r'^servicios$', 'app.views.serviceView', name='serviceView'),
    url(r'^mantenimiento$', 'app.views.mantenimiento', name='mantenimientoView'),
    url(r'^index$', 'app.views.index_view', name='index'),
    url(r'^contact_mantenimiento$', 'app.views.contact_mantenimiento', name='contact_mantenimiento'),
    url(r'^sitemap$', 'app.views.sitemap', name='sitemap'),
    # url(r'^personal/', include('personal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))