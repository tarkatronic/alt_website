#!/usr/bin/env python
import os
import sys

# Set up our pythonpath, assuming we are in [project]/bin/manage.py
PROJECT_DIR, PROJECT_MODULE_NAME = os.path.split(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.join(PROJECT_DIR, PROJECT_MODULE_NAME, 'alt_website/alt_website'))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alt_website.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
