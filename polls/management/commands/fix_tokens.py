from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class Command(BaseCommand):
    help = 'Assicura che gli utenti abbiano i token predefiniti'

    def handle(self, *args, **options):
        
        FIXED_TOKENS = {
            'user-demo': '93a112a22924466021713a6e7dc2016fff56ccbd',
            'carmine': '387112285bbbd5c3f8428de46969c314d458ded0',
            'admin_demo': 'c08108e69ea2e55aa269766ebcc347ce606b829c',
        }

        count = 0
        for username, key in FIXED_TOKENS.items():
            user = User.objects.filter(username=username).first()
            if user:
                
                token, created = Token.objects.get_or_create(user=user)
                
                
                if token.key != key:
                    token.key = key
                    token.save()
                    self.stdout.write(self.style.SUCCESS(f"Token forzato per: {username}"))
                    count += 1
                else:
                    self.stdout.write(f"Token già corretto per: {username}")
        
        if count == 0:
            self.stdout.write("Tutti i token sono già configurati correttamente.")
        else:
            self.stdout.write(self.style.SUCCESS(f"Operazione completata: aggiornati {count} token."))