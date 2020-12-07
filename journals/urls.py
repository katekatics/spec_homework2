from django.urls import path

from .views import (
    JournalView,
    JournalDetailView,
    JournalReversedView,
    JournalCreateView,
    JournalEditView,
    JournalDeleteView
)


urlpatterns = [
    path('', JournalView.as_view(), name='journals'),
    path('<int:pk>/', JournalDetailView.as_view(), name='detail_journal'),
    path(
        'journals_reversed/',
        JournalReversedView.as_view(),
        name='journals_reversed'),
    path('new/', JournalCreateView.as_view(), name='new_journal'),
    path('<int:pk>/edit/', JournalEditView.as_view(), name='edit_journal'),
    path(
        '<int:pk>/delete/',
        JournalDeleteView.as_view(),
        name='delete_journal')
]
