from rest_framework.authentication import TokenAuthentication  

class BearTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'
    