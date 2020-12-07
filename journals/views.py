from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Journal


class JournalView(LoginRequiredMixin, ListView):
    """
    Класс для отображения набора журналов
    """
    model = Journal
    template_name = 'journals/list.html'
    context_object_name = 'journals'
    login_url = 'login'


class JournalDetailView(LoginRequiredMixin, DetailView):
    """
    Класс для детального отображения журнала
    """
    model = Journal
    template_name = 'journals/detail.html'
    context_object_name = 'journal'
    login_url = 'login'


class JournalReversedView(LoginRequiredMixin, ListView):
    """
    Класс для отображения набора журналов, отсортированный
    в порядке убывания количества страниц
    """
    model = Journal
    queryset = Journal.objects.all().order_by('-page_count')
    template_name = 'journals/list.html'
    context_object_name = 'journals'
    login_url = 'login'


class JournalEditView(LoginRequiredMixin, UpdateView):
    """
    Класс для редактирования журнала. Поля: title, editor, page_count
    """
    model = Journal
    template_name = "journals/edit.html"
    fields = ("title", "editor", "page_count")
    context_object_name = "journal"
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        """
        Метод для проверки прав доступа на возможность редактирования журнала
        Редактировать может только тот, кто ее создал
        """
        journal_object = self.get_object()
        if journal_object.owner != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class JournalDeleteView(LoginRequiredMixin, DeleteView):
    """
    Класс для удаления журнала
    """
    model = Journal
    template_name = "journals/delete.html"
    success_url = reverse_lazy("journals")
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        """
        Метод для проверки прав доступа на возможность удаления журнала
        Удалять может только тот, кто ее создал
        """
        journal_object = self.get_object()
        if journal_object.owner != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class JournalCreateView(LoginRequiredMixin, CreateView):
    """
    Класс для создания нового журнала
    """
    model = Journal
    template_name = "journals/new.html"
    fields = ("title", "editor", "page_count")
    login_url = 'login'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
