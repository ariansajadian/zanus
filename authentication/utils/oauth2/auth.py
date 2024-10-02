from django.conf import settings
import requests
from exceptions.error.auth.error_exceptions import ValidationError

class GoogleAuthUtils:

    GOOGLE_ID_TOKEN_INFO_URL = 'https://www.googleapis.com/oauth2/v3/tokeninfo'
    GOOGLE_ACCESS_TOKEN_OBTAIN_URL = 'https://oauth2.googleapis.com/token'
    GOOGLE_USER_INFO_URL = 'https://www.googleapis.com/oauth2/v3/userinfo'

    
    def google_get_user_info(self, *, access_token:  str) -> None:
        response = requests.get(
            self.GOOGLE_USER_INFO_URL,
            params={'access_token': access_token}
        )      
        if not response.ok:
            raise ValidationError('Failed to obtain user info from Google.')

        return response.json()