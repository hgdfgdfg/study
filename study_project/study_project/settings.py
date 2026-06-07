import os
from pathlib import Path

# 1. 基础路径配置
BASE_DIR = Path(__file__).resolve().parent.parent

# 安全密钥（本地开发使用）
SECRET_KEY = 'django-insecure-mock-key-for-study-project-123456'

# 调试模式（开发时保持 True，能看到报错）
DEBUG = True

# 允许访问的主机列表
ALLOWED_HOSTS = ['*']


# 2. 应用注册配置（已为你添加跨域插件和 softstu）
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'corsheaders',  # 【修改 1】跨域配置：注册跨域中间件应用
    'softstu',      # 注册你自己的软件开发应用，使 models.py 生效
]


# 3. 中间件配置（已将跨域中间件放在最顶部）
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 【修改 2】跨域配置：必须放在最顶部！
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'study_project.urls'

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

WSGI_APPLICATION = 'study_project.wsgi.application'


# 4. 数据库配置（软件开发四班专属：SQL Server 免密信任连接 + ODBC 18 证书避坑配置）
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'softstu_db',                   # 你在 SSMS 或命令行中建好的数据库名
        'HOST': 'LAPTOP-D1LAQ43C\\SQLEXPRESS',  # 你的 SQL Server 实例路径（注意双斜杠转义）
        'PORT': '',                             # 默认端口留空
        'OPTIONS': {
            'driver': 'ODBC Driver 18 for SQL Server', 
            # 核心：Trusted_Connection=yes 启用免密登录；TrustServerCertificate=yes 跳过 SSL 证书拦截
            'extra_params': 'Trusted_Connection=yes;TrustServerCertificate=yes;',
        },
    }
}


# 5. 密码验证配置
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


# 6. 语言与时区配置（已改为中文和中国时区）
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True


# 7. 静态文件配置
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 8. 跨域放行权限配置
CORS_ALLOW_ALL_ORIGINS = True  # 【修改 3】跨域配置：允许前端 HTML 页面自由跨域异步请求后端接口