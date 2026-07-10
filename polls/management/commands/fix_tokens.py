from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
import secrets

User = get_user_model()

class Command(BaseCommand):
    help = 'Aggiorna i token senza modificare le password esistenti'

    def handle(self, *args, **options):
        USERS_DATA = {
            'user-demo': '93a112a22924466021713a6e7dc2016fff56ccbd',
            'admin_demo': 'c08108e69ea2e55aa269766ebcc347ce606b829c',
        }

        for username, key in USERS_DATA.items():
            user = User.objects.filter(username=username).first()
            
            if not user:
                user = User.objects.create_user(username=username, password=secrets.token_urlsafe(16))
                self.stdout.write(f"Creato nuovo utente: {username}")
            
            Token.objects.filter(user=user).delete()
            Token.objects.create(user=user, key=key)
            self.stdout.write(f"Token forzato per: {username}")

        self.stdout.write(self.style.SUCCESS("Sincronizzazione completata!"))