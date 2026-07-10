from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()
class Command(BaseCommand):
    help = 'Crea i token mancanti per tutti gli utenti esistenti'

    def handle(self, *args, **options):
        users = User.objects.all()
        count = 0
        for user in users:
            
            token, created = Token.objects.get_or_create(user=user)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Creato token per: {user.username}"))
                count += 1
        
        if count == 0:
            self.stdout.write("Tutti gli utenti hanno già un token.")
        else:
            self.stdout.write(self.style.SUCCESS(f"Operazione completata: creati {count} nuovi token."))