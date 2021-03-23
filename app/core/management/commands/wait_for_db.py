import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        """Handle the command"""
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                self.stdout.write('Trying DB connection...')
                db_conn = connections['default']
                msg = 'Connection complete waiting for other '\
                      'dependencies to start...'
                self.stdout.write(msg)
                time.sleep(5)
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
