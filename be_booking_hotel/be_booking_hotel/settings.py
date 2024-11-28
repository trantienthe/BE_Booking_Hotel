"""
Django settings for be_booking_hotel project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!ac&aws1x2r0#v5znl-ohq4i!*di@cz4d5qeyd*^)%-ad9&s_#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True


# Application definition

AUTH_USER_MODEL = "e_be_booking_hotel.User"

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'e_be_booking_hotel.apps.EBeBookingHotelConfig',
    'drf_yasg',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    # 'vnpay'
]

JAZZMIN_SETTINGS = {
    'site_title': 'Quản trị website Haven Hotel',  # Tiêu đề của trang quản trị
    'site_header': 'Quản trị website Haven Hotel',  # Tiêu đề trên cùng của trang quản trị
    'site_url': '/',  # URL của trang chủ quản trị
    'welcome_sign': 'Xin chào Admin Haven Hotel',  # Lời chào mừng
    'show_ui_builder': True,  # Hiển thị công cụ xây dựng giao diện
    'changeform_format': 'vertical',  # Định dạng biểu mẫu thay đổi, chọn 'vertical' cho bố cục dọc
    'changeform_add': 'Thêm bản ghi mới',  # Văn bản hiển thị khi thêm bản ghi mới
    'site_brand':'Haven Hotel',
}


# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ),
# }

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'be_booking_hotel.urls'

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
            'builtins': ['templatetags.custom_filters']
        },
    },
]

WSGI_APPLICATION = 'be_booking_hotel.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_booking_hotel',      # Tên cơ sở dữ liệu PostgreSQL
        'USER': 'postgres',       # Tên người dùng PostgreSQL
        'PASSWORD': 'trantienthe',        # Mật khẩu người dùng
        'HOST': 'localhost',                # Địa chỉ máy chủ (thường là 'localhost')
        'PORT': '5432',                     # Cổng kết nối PostgreSQL (mặc định là 5432)
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# xử lý các tệp media (như ảnh)
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# SWAGGER_SETTINGS = {
#     'SECURITY_DEFINITIONS': {
#         'Bearer': {
#             'type': 'apiKey',
#             'name': 'Authorization',
#             'in': 'header',
#             'description': 'JWT authorization uses the Bearer scheme. For example: "Authorization: Bearer {access_token}"'
#         }
#     }
# }

# VNPAY_TMN_CODE = 'WRQMN312'
# VNPAY_HASH_SECRET_KEY = '6OLWVENQ3MNA0X5ONCY6DZXBB733RJQD'
# VNPAY_PAYMENT_URL = 'https://sandbox.vnpayment.vn/merchant_webapi/api/transaction'
# VNPAY_RETURN_URL = 'http://localhost:3000/thanh-to%C3%A1n'

ZALOPAY_CONFIG = {
    "APP_ID": 2553,
    "KEY1": "PcY4iZIKFCIdgZvA6ueMcMHHUbRLYjPL",
    "KEY2": "kLtgPl8HHhfvMuDHPwKfgfsY4Ydm9eIz",
    "CREATE_ENDPOINT": "https://sb-openapi.zalopay.vn/v2/create",
    "STATUS_ENDPOINT": "https://sb-openapi.zalopay.vn/v2/query",
}

