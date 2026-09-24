from django.core.management import BaseCommand
from django.contrib.auth.models import User
from decouple import config

class Command(BaseCommand):
    help = "This helps to create the default admin for a project launched on remote server"

    admin_username = config("DEFAULT_ADMIN_USERNAME")
    admin_password = config("DEFAULT_ADMIN_PASSWORD")

    def handle(self, *args, **kwargs):
        if not(self.admin_username and self.admin_password):
            self.stdout.write(self.style.ERROR("Credentials are important"))

        if User.objects.filter(username = self.admin_username).exists():
            self.stdout.write(self.style.ERROR("Username already exists"))
        else:
            User.objects.create_superuser(username=self.admin_username, password=self.admin_password, email=None)
            self.stdout.write(self.style.SUCCESS(f"Admin with the username {self.admin_username} has been created"))

        
