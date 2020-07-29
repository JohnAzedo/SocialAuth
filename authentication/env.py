from decouple import config

try:
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('GOOGLE_CLIENT_ID')
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('GOOGLE_CLIENT_SECRET')
except ValueError:
    print('Google OAuth2 no variables')
    
LOGIN_URL = '/login/google-oauth2/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
SOCIAL_AUTH_URL_NAMESPACE = 'authentication'