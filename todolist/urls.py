from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns


from .views import TasklistCreateView, TasklistDetailsView, TaskCreateView, TaskDetailsView, RegisterFormView, \
    LoginFormView

urlpatterns = {
    # url(r'^login/$', auth_views.login, name="login"),
    # url(r'^logout/$', auth_views.logout, name="logout"),
    # url(r'^signup/$', signup, name="signup"),
    url(r'^register/$', RegisterFormView.as_view()),
    url(r'^login/$', LoginFormView.as_view()),
    url(r'^todolists/$', TasklistCreateView.as_view(), name="lists"),
    url(r'^todolists/(?P<pk>[0-9]+)/$', TasklistDetailsView.as_view(), name="list-detail"),
    url(r'^todolists/(?P<list_id>[0-9]+)/tasks/$', TaskCreateView.as_view(), name="tasks"),
    url(r'^todolists/(?P<list_id>[0-9]+)/tasks/(?P<pk>[0-9]+)', TaskDetailsView.as_view(), name="task-detail"),

}

urlpatterns = format_suffix_patterns(urlpatterns)