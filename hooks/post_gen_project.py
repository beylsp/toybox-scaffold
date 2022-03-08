import subprocess


subprocess.call(["git", "init"])
subprocess.call(["git", "config", "user.name", "{{ cookiecutter.git_user_name }}"])
subprocess.call(["git", "config", "user.email", "{{ cookiecutter.git_user_email }}"])
subprocess.call(["git", "remote", "add", "origin", "{{ cookiecutter.git_user_email }}"])