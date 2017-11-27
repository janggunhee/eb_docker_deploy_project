from .base import *
config_secret = json.loads(open(CONFIG_SECRET_DEV_FILE).read())

# AWS
AWS_ACCESS_KEY_ID = config_secret['aws']['access_key_id']
AWS_SECRET_ACCESS_KEY = config_secret['aws']['secret_access_key']
AWS_STORAGE_BUCKET_NAME = config_secret['aws']['s3_bucket_name']
AWS_S3_SIGNATURE_VERSION = config_secret['aws']['s3_signature_version']
AWS_S3_REGION_NAME = config_secret['aws']['s3_region_name']
AWS_S3_HOST = 's3.ap-northeast-2.amazonaws.com'
S3_USE_SIGV4 = True

# AWS Storage
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

# S3 FileStorage
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'


# Database
DATABASES = config_secret['django']['databases']

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.elasticbeanstalk.com',
    '.janggunhee.com',
]
