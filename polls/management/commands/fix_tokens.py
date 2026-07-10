from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class Command(BaseCommand):
    help = 'Crea o aggiorna i token per gli utenti specificati'

    def handle(self, *args, **options):
        FIXED_TOKENS = {
            'user-demo': '93a112a22924466021713a6e7dc2016fff56ccbd',
            'admin_demo': 'c08108e69ea2e55aa269766ebcc347ce606b829c',
        }

        for username, key in FIXED_TOKENS.items():
            user = User.objects.filter(username=username).first()
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                if token.key != key:
                    token.key = key
                    token.save()
                    self.stdout.write(f"Token aggiornato per: {username}")
                else:
                    self.stdout.write(f"Token già corretto per: {username}")
            else:
                self.stdout.write(self.style.WARNING(f"Utente non trovato nel database: {username}"))

        self.stdout.write(self.style.SUCCESS("Operazione completata!"))