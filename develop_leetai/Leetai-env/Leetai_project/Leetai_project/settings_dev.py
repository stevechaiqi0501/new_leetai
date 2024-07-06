from .settings_common import *
from django.contrib.messages import constants as messages 
from pathlib import Path
import os

SECRET_KEY = 'django-insecure-b6w4u!g9zzt8jzz)%ybqrsqe*c$d!+dgie*ik#pm!*%gpt&fsp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

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

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MESSAGE_TAGS = {
    messages.ERROR:'alert alert-danger',
    messages.WARNING:'alert alert-warning',
    messages.SUCCESS:'alert alert-succsee',
    messages.INFO:'alert alert-info'
}