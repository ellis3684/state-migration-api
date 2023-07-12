from django.core.management.base import BaseCommand
from statemigrations.models import StateMigration
import pandas as pd


class Command(BaseCommand):
    """
    Django custom command to import census data from CSVs and
    create new StateMigration object for each row in migration CSV.
    """
    def handle(self, *args, **options):
        # If user has already run 'importdata' command, raise error and do not repeat write to database.
        object_count = StateMigration.objects.count()
        if object_count != 0:
            self.stderr.write(
                'Import failed: you have already created StateMigration objects. '
                'There must be zero currently existing StateMigration objects to run \'importdata\'.'
            )
        else:
            classification_df = pd.read_csv('census_classification.csv')
            migration_df = pd.read_csv('census_migration_data.csv')

            nc_df = migration_df[migration_df['current_state'] == 'NC']

            for index, row in nc_df.iterrows():
                # Get division ID from classification DF
                division_id = classification_df[classification_df['abbrv'] == row['previous_state']]['parent_id'].values[0]

                # Create new StateMigration object with values parsed from migration DF and division ID parsed above
                StateMigration.objects.create(
                    year=row['year'],
                    previous_state=row['previous_state'],
                    previous_division=division_id,
                    estimate=row['estimate'],
                    margin_of_error=row['margin_of_error']
                )
