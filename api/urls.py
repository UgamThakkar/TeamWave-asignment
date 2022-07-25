from . views import All_questions_View, Query_ques_View, Advance_search_View, Detail_View
from django.conf.urls import url
app_name = 'api'
urlpatterns = [
    url('questions/$',All_questions_View.as_view(),name='all_ques'),
    url('queryques/$',Query_ques_View.as_view(),name='queryques'),
   	url('advsearch/$',Advance_search_View.as_view(),name='advsearch'),
   	url('answerdetails/$',Detail_View.as_view(),name='answerdetails'),
]