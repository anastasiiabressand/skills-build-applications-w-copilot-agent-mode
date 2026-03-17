from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Suppression des anciennes données (contournement bug Djongo)
        for model in [User, Team, Activity, Leaderboard, Workout]:
            for obj in model.objects.all():
                obj.delete()

        # Création des équipes
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Création des utilisateurs super-héros
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        spiderman = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Création d’activités
        Activity.objects.create(user=ironman, type='Course', duration=30, date=date.today())
        Activity.objects.create(user=spiderman, type='Natation', duration=45, date=date.today())
        Activity.objects.create(user=batman, type='Cyclisme', duration=60, date=date.today())
        Activity.objects.create(user=superman, type='Course', duration=50, date=date.today())

        # Création de workouts
        Workout.objects.create(name='HIIT', description='Entraînement intensif', suggested_for='Marvel')
        Workout.objects.create(name='Yoga', description='Souplesse et récupération', suggested_for='DC')

        # Création du leaderboard
        Leaderboard.objects.create(user=ironman, score=100, week=1)
        Leaderboard.objects.create(user=spiderman, score=90, week=1)
        Leaderboard.objects.create(user=batman, score=95, week=1)
        Leaderboard.objects.create(user=superman, score=110, week=1)

        self.stdout.write(self.style.SUCCESS('octofit_db peuplée avec des données de test Marvel/DC !'))
