from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class Command(BaseCommand):
    help = 'Assicura che gli utenti abbiano i token predefiniti senza errori'

    def handle(self, *args, **options):
        FIXED_TOKENS = {
            'user-demo': '93a112a22924466021713a6e7dc2016fff56ccbd',
            'admin_demo': 'c08108e69ea2e55aa269766ebcc347ce606b829c',
        }

        for username, key in FIXED_TOKENS.items():
            user = User.objects.filter(username=username).first()
            if user:
                
                token = Token.objects.filter(user=user).first()
                
                if token:
                    if token.key != key:
                        token.key = key
                        token.save()
                        self.stdout.write(f"Token aggiornato per: {username}")
                else:
                    Token.objects.create(user=user, key=key)
                    self.stdout.write(f"Token creato per: {username}")
        
        self.stdout.write(self.style.SUCCESS("Operazione completata con successo!"))