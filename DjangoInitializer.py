'''
Django Initializer
Created by Fransiscus Emmanuel Bunaren
https://bunaren.com
'''

import os

project_name = input("Project Name : ")
app_name = input("App Name : ")

# Create Project and App
def init_project_app():
    # Start Project and App
    cmd_str = "django-admin startproject " + project_name + " & cd " + project_name + " & python manage.py startapp " + app_name
    os.popen(cmd_str).read()

    # Make Static Folder
    os.mkdir(project_name + "/static")

# Configuration For settings.py file
def config_settings():
    # Configure settings.py
    with open(project_name + "/" + project_name + "/settings.py","r") as f:
        settings = f.read().split("\n")

    # Add ALLOWED HOST
    settings.insert(27,"ALLOWED_HOSTS = ['*']")

    # Add APP to INSTALLED APP
    settings.insert(40,"'{}'".format(app_name) + ",")

    # Add Whitenoise to Middleware
    settings.insert(51,"'whitenoise.middleware.WhiteNoiseMiddleware',")

    # Add STATIC FILE Configuration
    settings = "\n".join(settings)
    settings += "\n" + '''STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]'''

    #Save File
    with open(project_name + "/" + project_name + "/settings.py","w+") as f:
        f.write(settings)

# Configure project/urls.py
def config_project_urls():
    with open(project_name + "/" + project_name + "/urls.py","r") as f:
        settings = f.read().split("\n")
    settings.insert(20,"path('', include('{}.urls')),".format(app_name))

# Do CollectStatic
def do_collectstatic():
    os.popen("cd " + project_name + " & python manage.py collectstatic").read()

# Apply Configurations
init_project_app()
config_settings()
do_collectstatic()

print("Finished")
