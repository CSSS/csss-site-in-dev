"""
Django settings for csss project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mndb=kgytc4+ap(^var_w0o-dlo@j7@6e9_#964jhd3m*vk+2v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if 'ip_addr' not in os.environ:
    print(" no environment variable \"ip_addr\" seems to exist....please specify the ip address attached to the network interface of the server like so:");
    print(" export ip_addr = '<ipaddr>'");

ALLOWED_HOSTS = [os.environ['ip_addr']]


# Application definition

INSTALLED_APPS = [
	'csss',
	'announcements',
	'about',
	'documents',
    'events',
    '750_project',
    'comp_sci_guide',
    'bursaries_and_awards',
    'associated_dsus_and_clubs',
    'blog',
    'personal',
    'django_mailbox',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'django_file_form',
    'file_uploads',
    'django_file_form.ajaxuploader',
    'django_bootstrap3_form',
    'django_pony_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'csss.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'csss.wsgi.application'


LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/done/'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Vancouver'

USE_I18N = True

USE_L10N = True

USE_TZ = False

#STATICFILES_DIRS = [
#    'static_files/',
#]
#This is list of full paths your project should look fotr static files, beside standard apps. Namely, 
#Django will automatically look for static files in your installed apps. If app has dir called static 
#(app/static) all files and folders will be copied once you run collectstatic command. STATICFILES_DIRS 
#defines additional paths where your staticfiles can be found

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

import environ
ROOT_DIR = environ.Path(__file__) - 3

STATIC_URL = '/STATIC_URL/' 
#is the URL on your website where these collected files will be accessible. IE: mysite.com/ static/
#This is something that tells your browser where to look for JavaScript and CSS files



STATIC_ROOT = str(ROOT_DIR('STATIC_ROOT'))
#This is destination directory for your static files. This should be absolute path in yor file system, 
#for example: "/var/www/project/static" If you run 'python manage.py collectstatic' it will collect all 
#static files from your project and copy them into STATIC_ROOT dir

MEDIA_URL = '/MEDIA_URL/'
#URL that handles the media served from MEDIA_ROOT, used for managing stored files. It must end in a slash 
#if set to a non-empty value. You will need to configure these files to be served in both development and production environments.


MEDIA_ROOT = str(ROOT_DIR('MEDIA_ROOT'))
#Absolute filesystem path to the directory that will hold user-uploaded files.


FILE_FORM_MASTER_DIR = 'form_uploads/form_uploads/'
FILE_FORM_UPLOAD_DIR = FILE_FORM_MASTER_DIR+'temporary_files/' ##temporary files from form upload go here
DJANGO_MAILBOX_ATTACHMENT_UPLOAD_TO = 'mailbox_attachments/%Y/%m/%d/' #will be placed under the MEDIA_ROOT folder
print("ROOT_DIR="+str(ROOT_DIR))
print("STATIC_URL="+str(STATIC_URL))
#print("STATICFILES_DIRS="+str(STATICFILES_DIRS))
print("STATIC_ROOT="+str(STATIC_ROOT))
print("MEDIA_ROOT="+str(MEDIA_ROOT))
print("MEDIA_URL="+str(MEDIA_URL))
print("FILE_FORM_MASTER_DIR="+str(FILE_FORM_MASTER_DIR))
print("FILE_FORM_UPLOAD_DIR="+str(FILE_FORM_UPLOAD_DIR))
print("DJANGO_MAILBOX_ATTACHMENT_UPLOAD_TO="+str(DJANGO_MAILBOX_ATTACHMENT_UPLOAD_TO))
