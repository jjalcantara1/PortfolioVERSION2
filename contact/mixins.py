from django.forms.utils import ErrorList

from django import forms
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from django.shortcuts import redirect

class FormUserNeededMixin(object):
    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(
                ["User must be logged in to continue"])
            return self.form_invalid(form)


class UserOwnerFormMixin(FormUserNeededMixin, object):
    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(UserOwnerFormMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(
                ["This user is not allowed to change this data."])
            return self.form_invalid(form)

# def admin_user_required(view_func):
#     """
#     Decorator for views that checks if the user is an admin.
#     If the user is an admin, the view is displayed; otherwise,
#     the user is redirected to the login page.
#     """
#     actual_decorator = user_passes_test(
#         lambda u: u.is_active and u.is_admin,
#         login_url='admin:login',
#         redirect_field_name=None
#     )
#
#     if isinstance(view_func, (list, tuple)):
#         return [actual_decorator(view) for view in view_func]
#     else:
#         return actual_decorator(view_func)
#
# class AdminRequiredMixin:
#     """
#     Mixin for views that require admin authentication.
#     """
#     @classmethod
#     def as_view(cls, **initkwargs):
#         view = super().as_view(**initkwargs)
#         return admin_user_required(view)