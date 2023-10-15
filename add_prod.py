import subprocess



# Define the command you want to run in the Heroku shell

heroku_command = 'print("Hello from the Django shell!")'




# Run the Heroku CLI command to open the Heroku shell and execute the command

subprocess.run(['heroku', 'run', 'python', 'manage.py', 'shell'])



