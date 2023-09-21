Welcome to the home base for cookbook content. 

This web app serves the purpose as my personal web domain, and as a anyone's personal virtual book storage.

Here are some concepts that are different than most projects. The flow goes like this. manage.py checks if a local environment 
variable called localenv exists. IF it exists, then use localenv.py INSTEAD of settings.py. Heres an excerpt from manage.py


def main():
    """..................IMPORTANT!!!
    ...............This manage.py file is modified to check if a local environment variable exists. 
    ...............IF localenv has been declared
    ...............USE Foodblog.localenv.py 
    ...............IF NOT localenv
    ...............use Foodblog.settings.py
    
    """
                        # this is where you can change your name of the variable
    env = os.environ.get('localenv')

    if env:

        os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'FoodBlog.{env}')

    else:

        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FoodBlog.settings')


STEP 1. create a local environment variable called localenv with a value of 'localenv'.

How to: 

    a.  In windows (sry mac users) go to your search menu OR press windows_key + S , and search 'edit environment variables'. Click the 'Edit system
environment variables' option, which will open system properties. If NOT in the advanced tab already, open the advanced tab and then click the button
'environment variables' located at the bottom right of the window. 

    b.  This should take you to the environment variables page where you can add, edit, or delete your local variables.  

So now that a local environment variable exists, our app knows that it should use the localenv.py file for settings.

STEP 2. Create a database and wire it into your localenv.py file. The example used in the localenv file is for MySQL.

    ATTENTION!! If you are new to MySQL. Here's the quick low down. 
          a. You want to have MySQL workbench. It's FREE and works very well out of the box. Here is the link. https://dev.mysql.com/downloads/workbench/
          b. Once you've finished downloading you can launch MySQL and create a connection by pressing the circular plus icon, next to a label
          that says, MySQL Connections.
          c. This should open a 'Setup New Connection' menu with the following entries. Connection, Host Name, User Name, Password.
              - Connection is the name of the connection (surprisingly not very important name it what you want)
              - Host Name is the ip address that MySQL is going to host at. You want it to stay 127.0.0.1 since we are working with the local host.
              -The Username and password will be important later. (we need to save them into the environment variables)
          d. Login to your new connection and create a schema. The button is is silo with a plus, located below the Query option within the main dashboard.
              -name your shcema whatever you want, but create the environment variable so OS module can find the correct information for your database.
          e. This should create a connection and launch your database server. Check to make sure everything is good with the server tab located on the dashboard.

STEP 4. Declare the SCHEMA_NAME, DB_USER, and DB_PASSWORD variables in your local environment. That way Django can login to your database.


Heres the code where these steps are relevant. Located in localenv.py

SCHEMA_NAME= os.environ.get('NAME')
DB_USER= os.environ.get('DB_USER')
DB_PASSWORD= os.environ.get('DB_PASSWORD')

localenv.py

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',#<- Defines the Mysql backend in django.
        'NAME': SCHEMA_NAME, #<--------- Name of schema in MySQL 
        'USER': DB_USER,     #<--------- User Name 
        'PASSWORD': DB_PASSWORD,  #<- Password
        'HOST': '127.0.0.1',  #<---------Stays 127.0.0.1 Unless you host your Mysql DB on a server.
        'PORT': '3306', #<----------------Port 3306 is the standard port for mysql
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }      
        
    }  
} 

This should complete the setup of your new local environment. At this point, you should be able to enter the manage.py directory. And
run>>> py manage.py runserver.



Here is the entire programs process in a nutshell:

Py manage.py searches for an environment variable called localenv with a value of localenv. This determines if you are working locally
OR on the server. You want localenv.py to be used for settings. Never touch settings.py unless you want to launch your project on another 
server. localenv.py loads a second set of templates called localtemplates. So you can use localtemplates to test your Django/HTML implementations.
and use localenv.py to choose your desired database. In my case, MySql.

If you have trouble accessing the admin page. be sure to add a / after admin. so the path should be http://127.0.0.1:8000/admin/ 
