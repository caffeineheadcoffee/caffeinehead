"""
Management utility to create default superusers.
"""
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Used to create a default superuser."
    requires_migrations_checks = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.User = get_user_model()

    def handle(self, *args, **options):
        data = {
            'full_name': 'Caffeine Head Admin',
            'is_staff': True,
            'is_active': True,
            'is_superuser': True
        }

        user, _created = self.User.objects.update_or_create(
            email=settings.DJANGO_ADMIN.get('EMAIL'),
            defaults=data
        )
        user.set_password(settings.DJANGO_ADMIN.get('PASSWORD'))
        user.save()
