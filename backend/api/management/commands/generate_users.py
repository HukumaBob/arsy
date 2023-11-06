from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from mixer.backend.django import mixer

from threedmodels.models import ThreeDModel

class Command(BaseCommand):
    """
    The Command class inherits from BaseCommand to create a custom Django command.
    This command generates test data by creating users and 3D models.
    """
    help = 'Generate test data'

    def add_arguments(self, parser):
        """
        The add_arguments method adds command line arguments.
        """
        parser.add_argument('num_users', type=int, help='The number of users to create')

    def handle(self, *args, **options):
        """
        The handle method performs the main logic of the command.
        It creates a specified number of users and 3D models.
        """
        num_users = options['num_users']  # Get the number of users from the command line arguments

        try:
            # Create users and 3D models
            for i in range(num_users):
                user = mixer.blend(User)  # Create and save a new user
                self.stdout.write(self.style.NOTICE(f'Created user #{i}'))

                mixer.blend(ThreeDModel, owner=user)  # Create and save a new 3D model for the user
                self.stdout.write(self.style.NOTICE(f'Created 3d model #{i} for user #{user}'))

            self.stdout.write(self.style.SUCCESS('Users generation complete.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {e}'))
