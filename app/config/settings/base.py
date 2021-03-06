import os

from dotenv import load_dotenv

from django_secrets import SECRETS

ALLOWED_HOSTS = []

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.dirname(BASE_DIR)
ENV_PATH = os.path.join(ROOT_DIR, '.env')
LOG_DIR = os.path.join(ROOT_DIR, '.log')
LOG_SIGNAL_DIR = os.path.join(LOG_DIR, 'signal')
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(LOG_SIGNAL_DIR, exist_ok=True)
load_dotenv(ENV_PATH)

# django-aws-secrets-manager
DJANGO_SECRETS_CACHE_PATH = os.path.join(ROOT_DIR, 'secrets.json')
AWS_SECRETS_MANAGER_SECRET_NAME = 'lhy'
AWS_SECRETS_MANAGER_PROFILE = 'lhy-secrets-manager'
AWS_SECRETS_MANAGER_SECRET_SECTION = 'mashup:base'
AWS_SECRETS_MANAGER_REGION_NAME = 'ap-northeast-2'
SECRET_KEY = SECRETS['SECRET_KEY']

# AWS
AWS_S3_ACCESS_KEY_ID = SECRETS['AWS_S3_ACCESS_KEY_ID']
AWS_S3_SECRET_ACCESS_KEY = SECRETS['AWS_S3_SECRET_ACCESS_KEY']
AWS_DEFAULT_ACL = SECRETS['AWS_DEFAULT_ACL']
AWS_BUCKET_ACL = SECRETS['AWS_BUCKET_ACL']
AWS_AUTO_CREATE_BUCKET = SECRETS['AWS_AUTO_CREATE_BUCKET']
AWS_S3_FILE_OVERWRITE = SECRETS['AWS_S3_FILE_OVERWRITE']
AWS_S3_REGION_NAME = 'ap-northeast-2'

# django-dbbackup
DBBACKUP_STORAGE = 'config.storages.DBStorage'
DBBACKUP_STORAGE_OPTIONS = {
    'access_key': SECRETS['AWS_S3_ACCESS_KEY_ID'],
    'secret_key': SECRETS['AWS_S3_SECRET_ACCESS_KEY'],
}

# Email
EMAIL_HOST = SECRETS['EMAIL_HOST']
EMAIL_HOST_USER = SECRETS['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = SECRETS['EMAIL_HOST_PASSWORD']
EMAIL_PORT = SECRETS['EMAIL_PORT']
EMAIL_USE_SSL = SECRETS['EMAIL_USE_SSL']
DEFAULT_FROM_EMAIL = SECRETS['DEFAULT_FROM_EMAIL']

# django-cors-headers
CORS_ORIGIN_WHITELIST = SECRETS['CORS_ORIGIN_WHITELIST']
CORS_ALLOW_CREDENTIALS = True

# Static
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
STATICFILES_DIRS = [STATIC_DIR]

# Auth
LOGIN_URL = 'admin:login'
LOGOUT_REDIRECT_URL = 'index'
AUTH_USER_MODEL = 'members.User'
ADMIN_USERNAME = 'lhy'
ADMIN_PASSWORD = 'pbkdf2_sha256$120000$9SEp9OZWB5Ya$TVY41qkSk2g5WsPuXXYmYtCh1NwFO5ckJFIyMV8Yi4E='
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'members.backends.SettingsBackend',
    'members.backends.PhoneNumberBackend',
    'members.backends.EmailBackend',
    'members.backends.NameBackend',
]

# django-push-notifications
PUSH_NOTIFICATIONS_SETTINGS = {
    'FCM_API_KEY': SECRETS['FCM_API_KEY'],
    'UPDATE_ON_DUPLICATE_REG_ID': True,
}

# django-modeladmin-reorder
ADMIN_REORDER = (
    # 공지
    {'app': 'notice', 'label': '공지사항', 'models': (
        'notice.Notice',
        'notice.Attendance',
    )},
    # 사용자
    {'app': 'members', 'label': '사용자', 'models': (
        'members.UserAdminProxy',
        'members.UserPeriodTeam',
        'members.UserPeriodOutcount',
        # {'model': 'members.UserAdminProxy', 'label': '사용자'},
        # {'model': 'members.UserPeriodTeam', 'label': '사용자 활동기수 정보'},
        # {'model': 'members.UserPeriodOutcount', 'label': '세션'},
    )},
    # 기수, 팀
    {'app': 'members', 'label': '기수 & 팀', 'models': (
        'members.Period',
        'members.Team',
    )},
    # 이벤트(LOL)
    # {'app': 'lol', 'label': 'LOL', 'models': (
    #     'lol.Player',
    # )},
    'lol',
    'auth',
    'push_notifications',
)

# DRF
REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    # Permissions
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    # Renderer & Parser
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),
    # Filter backends
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    # Pagination
    'DEFAULT_PAGINATION_CLASS': 'utils.drf.pagination.DefaultPageNumberPagination',

    # Exception
    'EXCEPTION_HANDLER': 'utils.drf.exceptions.rest_exception_handler',

    # Custom
    'JSON_UNDERSCOREIZE': {
        'no_underscore_before_number': True,
    },

}

# drf-yasg
BASIC_DESCRIPTION = '''
base64로 인코딩된 **사용자ID/비밀번호** 쌍을 Header에 전달\n
HTTP Request의 Header `Authorization`에 
`Basic <base64로 인코딩된 "username:password" 문자열>`값을 넣어 전송\n
(개발시 일일이 토큰 발급필요없이 편하게 사용 가능)

```
Authorization: Basic ZGVmYXVsdF9jb21wYW55QGxoeS5rcjpkbGdrc2R1ZA==
```
'''
TOKEN_DESCRIPTION = '''
### [DRF AuthToken](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)
인증정보를 사용해 [AuthToken](#operation/auth_token_create) API에 요청, 결과로 돌아온 **key**를  
HTTP Request의 Header `Authorization`에 `Token <key>`값을 넣어 전송

```
Authorization: Token fs8943eu342cf79d8933jkd
``` 
'''
SWAGGER_SETTINGS = {
    'DEFAULT_AUTO_SCHEMA_CLASS': 'utils.drf.doc.SwaggerAutoSchema',
    'SECURITY_DEFINITIONS': {
        'Basic': {
            'type': 'HTTP Basic Auth (RFC 7617)',
            'description': BASIC_DESCRIPTION,
        },
        'Token': {
            'type': 'DRF AuthToken',
            'description': TOKEN_DESCRIPTION,
        }
    }
}

# django-safedelete
SAFE_DELETE_INTERPRET_UNDELETED_OBJECTS_AS_CREATED = True

# Other modules
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

# Format
DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:M'

# django-phonenumber-field
PHONENUMBER_DEFAULT_REGION = 'KR'
PHONENUMBER_DB_FORMAT = 'NATIONAL'

# Application definition
DJANGO_APPS = [
    'members.apps.MembersConfig',
    'notice.apps.NoticeConfig',
    'study.apps.StudyConfig',
    'events.lol',
    'utils',
]
DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = [
    'admin_reorder',
    'dbbackup',
    'django_extensions',
    'django_filters',
    'phonenumber_field',
    'push_notifications',
    'safedelete',
    'simple_history',
]
DRF_APPS = [
    'drf_yasg',
    'corsheaders',
    'rest_auth',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_api_key',
]
INSTALLED_APPS = DJANGO_APPS + DEFAULT_APPS + THIRD_PARTY_APPS + DRF_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'admin_reorder.middleware.ModelAdminReorder',
    'simple_history.middleware.HistoryRequestMiddleware',
    'members.middleware.RequirePasswordMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(TEMPLATES_DIR, 'jinja2')],
        'APP_DIRS': False,
        'OPTIONS': {
            'environment': 'config.jinja2.environment',
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

# DB
ATOMIC_REQUESTS = True

# Internationalization
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'signal': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_SIGNAL_DIR, 'signal.log'),
            'when': 'midnight',
            'backupCount': '10',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'signal': {
            'handlers': ['signal', 'console'],
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}
