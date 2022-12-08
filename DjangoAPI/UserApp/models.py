from django.db import models

###-------------------------------Commands to Create stables in SQLite Database File-------------------------------###
#                                                                                                                   #
# Note: You need to execute this commands with the enviroment active (reference 'Commands.rtf') and CD 'DjangoAPI'  #
#                                                                                                                   #
# -> python3 manage.py makemigrations UserApp                                                                       #
#       This creates an intermediate file in the migrations                                                         #
#       folder which have the details of the changes that will go into the database file                            #
#                                                                                                                   #
# -> python3 manage.py migrate UserApp                                                                              #
#       Commits the changes to the database file#                                                                   #
#------------------------------------------------------------------------------------------------------------------###

###--------------------------------------Note--------------------------------------###
#   Don't forget to update serializers.py and views.py if models are modified       #
###--------------------------------------------------------------------------------###

class User(models.Model):
    UserId = models.AutoField(primary_key=True)         #This is an auto-increment field
    UserFirstName = models.CharField(max_length=100)
    UserLastName = models.CharField(max_length=100)
    DateOfJoining = models.DateField(max_length=100)



