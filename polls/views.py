from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action 
from rest_framework.response import Response
from .models import Poll, Choice
from .serializers import PollSerializer
from polls.permission import IsOwnerOrReadOnly 

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def vote(self, request, pk=None):
        poll = self.get_object()
        
        
        if not poll.is_active:
            return Response({'error': 'Il sondaggio è chiuso'}, status=status.HTTP_400_BAD_REQUEST)
        
        choice_id = request.data.get('choice_id')
        try:
            choice = poll.choices.get(id=choice_id)
        except Choice.DoesNotExist:
            return Response({'error': 'Opzione non trovata'}, status=status.HTTP_404_NOT_FOUND)
        
        choice.votes += 1
        choice.save()
        
        return Response({'status': 'voto registrato', 'total_votes': choice.votes}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def results(self, request, pk=None):
        poll = self.get_object()
        results = [{"choice": choice.text, "votes": choice.votes} for choice in poll.choices.all()]
        return Response(results, status=status.HTTP_200_OK)
# Create your views here.
