import glob
import os

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Command to rename a Django project.

    This command will search for all Python files within the project directory
    and replace occurrences of the old project name 'piasweb' with the new one.
    It also renames the main project folder to match the new name.

    Usage:
        python manage.py rename <new_project_name>

    Example:
        python manage.py rename my_new_project
    """

    help = 'Renames the Django project from "piasweb" to a new name.'

    def add_arguments(self, parser):
        """
        Add command arguments to specify the new project name.

        Args:
            new: The new name of the project (string).
        """
        parser.add_argument("new", type=str, help="The new project name.")

    def handle(self, *args, **options):
        """
        The main logic to handle the renaming process.

        It searches through all Python files in the project, replacing occurrences of
        'piasweb' with the new project name. The project directory is also renamed.

        Args:
            new: The new project name (str).
        """
        old_name = "piasweb"
        new_name = options["new"]

        base_dir = str(settings.BASE_DIR)
        project_files = []

        # Add manage.py to the list of files to process
        manage_file = os.path.join(base_dir, "manage.py")
        project_files.append(manage_file)

        # Add all Python files within the project directory
        project_files += glob.glob(os.path.join(base_dir, old_name, "*.py"))
        project_files += glob.glob(os.path.join(base_dir, old_name, "**", "*.py"))

        # Replace occurrences of 'piasweb' with the new name
        for python_file in project_files:
            with open(python_file, "r") as file:
                file_data = file.read()

            updated_data = file_data.replace(old_name, new_name)

            with open(python_file, "w") as file:
                file.write(updated_data)

        # Rename the project folder
        old_project_dir = os.path.join(base_dir, old_name)
        new_project_dir = os.path.join(base_dir, new_name)

        try:
            os.rename(old_project_dir, new_project_dir)
            self.stdout.write(self.style.SUCCESS(f'Successfully renamed project from "{old_name}" to "{new_name}".'))
        except OSError as e:
            self.stdout.write(self.style.ERROR(f"Error renaming project folder: {e}"))
