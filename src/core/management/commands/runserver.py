import os

from os import path
from configparser import ConfigParser
from configparser import ParsingError
from configparser import NoOptionError
from configparser import NoSectionError

from django.core.management.commands.runserver import Command as RunserverCommand
from django.conf import settings

class Command(RunserverCommand):
    """
    Assign $env, command when you do $python manage.py runserver

    file: django/core/management/commands/runserver.py

    Add ´main´ app to the last of the installed apps
    """
    def add_arguments(self, parser):
        parser.add_argument(
            '--profile', 
            nargs='?',
            dest='aws_profile',
            help='Specify the aws profile in the environment.',
            )
        
        super().add_arguments(parser)

    def handle(self, *args, **options):
        if options['aws_profile']:
            env = options['aws_profile']
            self.aws_profile = options.get('aws_profile')
            self.stdout.write(f'[aws-profile] Use {env} profile.')
            aws_access_key_id, aws_secret_access_key = get_profile_credentials(env)
            os.environ['AWS_ACCESS_KEY_ID'] = aws_access_key_id
            os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_access_key
            print(aws_access_key_id, aws_secret_access_key)

        super().handle(*args, **options)

def get_profile_credentials(profile_name):
    config = ConfigParser()
    config.read([path.join(path.expanduser("~"),'.aws/credentials')])
    try:
        aws_access_key_id = config.get(profile_name, 'aws_access_key_id')
        aws_secret_access_key = config.get(profile_name, 'aws_secret_access_key')
    except ParsingError:
        print('Error parsing config file')
        raise
    except (NoSectionError, NoOptionError):
        try:
            aws_access_key_id = config.get('default', 'aws_access_key_id')
            aws_secret_access_key = config.get('default', 'aws_secret_access_key')
        except (NoSectionError, NoOptionError):
            print('Unable to find valid AWS credentials')
            raise
    return aws_access_key_id, aws_secret_access_key