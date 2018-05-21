from django.core.management.base import CommandError
from django.core.management.templates import TemplateCommand
from django.conf import settings
import os

BASE_DIR = settings.PROJECT_ROOT

class Command(TemplateCommand):
    help = (
        "Creates a Django app directory structure for the given app name in "
        "apps direcotry."
    )
    missing_args_message = "You must provide an application name."

    def handle(self, **options):
        app_name = options.pop('name')
        target = os.path.join(BASE_DIR, 'apps', app_name)
        self.validate_name(app_name, 'app')
        if not os.path.exists(target):
            os.makedirs(target)
        super().handle('app', app_name, target, **options)


