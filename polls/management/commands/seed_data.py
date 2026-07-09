from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model 
from polls.models import Poll

User = get_user_model() 

class Command(BaseCommand):
    help = 'Popola il database con dati demo'

    def handle(self, *args, **kwargs):
        
        admin, _ = User.objects.get_or_create(username='admin_demo')
        admin.set_password('admin12345')
        admin.is_staff = True
        admin.is_superuser = True
        admin.save()

        user, _ = User.objects.get_or_create(username='user_demo')
        user.set_password('user12345')
        user.save()

        self.stdout.write(self.style.SUCCESS('Database popolato correttamente con il tuo CustomUser!'))
        
        
        s1 = Poll.objects.create(title="Sondaggio Chiuso - Test Voto", created_by=admin, is_active=False)
        s1.choices.create(text="Sì") 
        s1.choices.create(text="No") 


        s2 = Poll.objects.create(title="Sondaggio di Admin - Test Sicurezza", created_by=admin, is_active=True)
        s2.choices.create(text="Opzione A") 


        s3 = Poll.objects.create(title="Sondaggio di User - Test OK", created_by=user, is_active=True)
        s3.choices.create(text="Django") 
        s3.choices.create(text="Flask")  