from django.contrib import admin
from django.contrib.admin import sites as admin_sites

from django.apps import apps


def list_all_fields(model, excluded_fields=None):
  """Creates a custom admin list display showing all the model's fields.

  Args
  ----
  model : django.db.models.Model
      The model to create the admin interface for.
  excluded_fields : Iterable[str]
      An iterable of field name strings to exclude.

  Returns
  -------
  Tuple[django.db.models.Model, django.contrib.admin.ModelAdmin]
      A 2 tuple containing the model and the generated admin interface.

  """
  if excluded_fields:
    excluded_fields = set(excluded_fields)
    fields = [f.name for f in model._meta.fields if f not in excluded_fields]
  else:
    fields = [f.name for f in model._meta.fields]

  class Admin(admin.ModelAdmin):
    list_display = fields

  return (model, Admin)


def register(model, admin_class=None, **options):
  """Register a Model and optional ModelAdmin.

  Args
  ----
  model : django.db.models.Model
      The model to register.
  admin_class : Optional[django.contrib.admin.ModelAdmin]
      The admin class to use.
  **options
      Keyword arguments passed to the admin_class.

  """
  try:
    admin.site.register(model, admin_class, **options)
  except admin_sites.AlreadyRegistered:
    pass


def register_all_models(app_name):
  """Register all Models for a given app.

  Args
  ----
  app_name : str
      The name of the app to register.

  """
  app = apps.get_app_config(app_name)
  models = app.get_models()

  for model in models:
    register(*list_all_fields(model))


# Register the models
register_all_models('api')