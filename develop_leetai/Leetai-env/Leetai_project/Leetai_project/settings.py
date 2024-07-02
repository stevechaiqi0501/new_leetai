
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-b6w4u!g9zzt8jzz)%ybqrsqe*c$d!+dgie*ik#pm!*%gpt&fsp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #アプリ名.apps.pyのLeetai-appを定義しているクラスを指定
    'Leetai_app.apps.LeetaiAppConfig'
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

ROOT_URLCONF = 'Leetai_project.urls'

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

WSGI_APPLICATION = 'Leetai_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'BaseDB',
        'USER':'steve',
        'PASSWORD':'ppii8877',
        'HOST':'127.0.0.1',
        'PORT':'5432'
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#エラーが発生した時の記録の残し方の変更

LOGGING = {
    'version':1,#1固定
    'disable_existing_loggers':False,#デフォの設定を無効化する
    
    #ログのエントリーポイントがここ
    'loggers':{
        'django':{
            'handlers':['console'],#出力先を決定
            'level':'INFO',#出力にあたってどのレベルまで表示するのか
        },
        
        'Leetai_app':{
            'handlers':['console'],
            'level':'DEBUG',
        }, 
    },
    
    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',#コンソールに出力するためのハンドラ
            'formatter':'dev'#出力形式を決定
        },
    },
    
    'formatters':{
        #DEVがここにあたる、表示のフォーマットをここで決定している
        'dev':{
            'format':'\t'.join([
                '%(asctime)s'
                '[%(levelname)s]'
                '%(pathname)s(Line:%(lineno)d)'
                '%(messasge)s'
            ])
        }
    }
    }

