from django.conf.urls import url
from webapp.views import index, ConsultaList, consulta_view, ConsultaDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^consulta',consulta_view, name='consulta_crear'),
    url(r'^listar', ConsultaList.as_view(), name='consulta_listar'),
    url(r'^eliminar/(?P<pk>\d+)/$', ConsultaDelete.as_view(), name='consulta_eliminar'),
]
