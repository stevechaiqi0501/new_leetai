from django.contrib.messages import constants as messages 
from pathlib import Path
import os

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-b6w4u!g9zzt8jzz)%ybqrsqe*c$d!+dgie*ik#pm!*%gpt&fsp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #アプリ名.apps.pyのLeetai-appを定義しているクラスを指定
    'Leetai_app.apps.LeetaiAppConfig',
    'accounts.apps.AccountsConfig',
    
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'django_bootstrap5',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]

ROOT_URLCONF = 'Leetai_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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
                '%(message)s'
            ])
        }
    }
    }

#静的ファイルの位置を指定
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

# settings.py


MESSAGE_TAGS = {
    messages.ERROR:'alert alert-danger role="alert"',
    messages.WARNING:'alert alert-warning role="alert"',
    messages.SUCCESS:'alert alert-succsee role="alert"',
    messages.INFO:'alert alert-info role="alert"'
}

#ユーザーモデルをこれでデフォから変更できる
AUTH_USER_MODEL = 'accounts.CustomUser'

# django-allauthで利用するdjango.contrib.sitesを使うためにサイト識別IDを設定
SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',  # 一般ユーザー用（メールアドレス認証）
    'django.contrib.auth.backends.ModelBackend',  # 管理サイト用（ユーザー名認証）
)

# メールアドレス認証に変更する設定
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False

# サインアップにメールアドレス確認をはさむよう設定
#メールが送られてきてそのメール上にあるリンクからログインする奴
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True

# ログイン/ログアウト後の遷移先を設定
LOGIN_REDIRECT_URL = 'Leetai:index'
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'

# ログアウトリンクのクリック一発でログアウトする設定
ACCOUNT_LOGOUT_ON_GET = True

# django-allauthが送信するメールの件名に自動付与される接頭辞をブランクにする
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''

# デフォルトのメール送信元を設定
DEFAULT_FROM_EMAIL = os.environ.get('FROM_EMAIL')