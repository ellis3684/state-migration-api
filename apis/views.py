from rest_framework import generics
from statemigrations.models import StateMigration
from .serializers import StateMigrationSerializer


class StateMigrationAPIView(generics.ListAPIView):
    serializer_class = StateMigrationSerializer

    # Override queryset to parse URL args
    def get_queryset(self):
        if self.kwargs.get('state'):
            if self.kwargs.get('year'):
                return StateMigration.objects.filter(
                    previous_state=self.kwargs['state'].upper(),
                    year=self.kwargs['year']
                )
            else:
                return StateMigration.objects.filter(previous_state=self.kwargs['state'].upper())

        elif self.kwargs.get('div'):
            if self.kwargs.get('year'):
                return StateMigration.objects.filter(
                    previous_division=self.kwargs['div'].upper(),
                    year=self.kwargs['year']
                )
            else:
                return StateMigration.objects.filter(previous_division=self.kwargs['div'].upper())
