import logging
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        logger.info('Starting to populate the database...')

        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(id=ObjectId(), email='thundergod@mhigh.edu', name='Thor', password='password123'),
            User(id=ObjectId(), email='metalgeek@mhigh.edu', name='Tony Stark', password='password123'),
            User(id=ObjectId(), email='zerocool@mhigh.edu', name='Steve Rogers', password='password123'),
            User(id=ObjectId(), email='crashoverride@mhigh.edu', name='Natasha Romanoff', password='password123'),
            User(id=ObjectId(), email='sleeptoken@mhigh.edu', name='Bruce Banner', password='password123'),
        ]
        logger.info(f'Creating users: {[user.email for user in users]}')
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(id=ObjectId(), name='Blue Team', members=[str(users[0].id), str(users[1].id)]),
            Team(id=ObjectId(), name='Gold Team', members=[str(users[2].id), str(users[3].id), str(users[4].id)]),
        ]
        logger.info(f'Creating teams: {[team.name for team in teams]}')
        Team.objects.bulk_create(teams)

        # Create activities
        activities = [
            Activity(id=ObjectId(), user=users[0], activity_type='Cycling', duration=60),
            Activity(id=ObjectId(), user=users[1], activity_type='Crossfit', duration=120),
            Activity(id=ObjectId(), user=users[2], activity_type='Running', duration=90),
            Activity(id=ObjectId(), user=users[3], activity_type='Strength', duration=30),
            Activity(id=ObjectId(), user=users[4], activity_type='Swimming', duration=75),
        ]
        logger.info(f'Creating activities: {[activity.activity_type for activity in activities]}')
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(id=ObjectId(), team=teams[0], score=100),
            Leaderboard(id=ObjectId(), team=teams[1], score=90),
        ]
        logger.info(f'Creating leaderboard entries: {[entry.score for entry in leaderboard_entries]}')
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(id=ObjectId(), name='Cycling Training', description='Training for a road cycling event', duration=60),
            Workout(id=ObjectId(), name='Crossfit', description='Training for a crossfit competition', duration=120),
            Workout(id=ObjectId(), name='Running Training', description='Training for a marathon', duration=90),
            Workout(id=ObjectId(), name='Strength Training', description='Training for strength', duration=30),
            Workout(id=ObjectId(), name='Swimming Training', description='Training for a swimming competition', duration=75),
        ]
        logger.info(f'Creating workouts: {[workout.name for workout in workouts]}')
        Workout.objects.bulk_create(workouts)

        logger.info('Database population completed successfully.')
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
