from rest_framework import serializers
from UserApp.models import User

###------------------------------Note------------------------------###
#   Don't forget to update views.py if serializers are modified     #
###----------------------------------------------------------------###


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('UserId',
                  'UserFirstName',
                  'UserLastName',
                  'DateOfJoining')