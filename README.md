# P10 - Create a platform for Nutella amateur.

## 1. Introduction.

This program is named "pur beurre". It's a web app that allow user to search for healthier or equaly ealthier food product than the one he or she usually consumes. User can also create n acoount and login in order to save its choice for later consultations.

The programm is built on Django framework. Data used to provide the service are comming from th Open Food Facts API. The programm is hosted by Heroku cloud plateform.

You can check the app on  : https://thpi-purbeurreapp.herokuapp.com

The here below installation steps describes how to make the install on a dev and local environment.

NB: It's a programm written in the context of a Django app eductation module delivered by OpenClassRooms.
 

## 2. Prerequisite.
This program requires the following components:
* Python 3.9.2
* psql (PostgreSQL) 13.2

The others required program will be installed via pip using requirements.txt file (see further).

## 3. Installation.

These instructions are for deployment on a local machine i.e.  for development use.

### 3.1. Download.
Download/clone this repository on your system, at the location that suits you best.
> git clone https://github.com/ThomasPiergiovanni/P8.git

### 3.2. Python 3 install.
Make sure you have Python 3 installed.
> python --version

If not, you can download it and install it from the [python official website](https://www.python.org/). You will find the necessary documentation there.

### 3.3. PostgreSQL 13 install and start.
Make sure you have PostgreSQL 13 installed.
> psql --version

If not, you can download it and install it from the [postgresql official website](https://www.postgresql.org/download/). You will find the necessary documentation there.

### 3.4. Create DB.
Create database.
> createdb -h localhost -p 5432 -U yourusername yourdatabasename

### 3.5. Create & activate a virtual environment (recommended).
In order to avoid system conflicts:

1. Go into your local repository and create a virtual environment using venv package.
> python -m venv env

2. Activate the virtual environment.
> env/scripts/activate

Documentation is also available on the [python official website](https://www.python.org/).

### 3.6. Django and other programms install
Install Django and the others programs on you virtual environment using the requirements.txt file.
>pip install -r requirements.txt

Please refer to [Django documentation](https://docs.djangoproject.com/fr/3.1/) for more information.

### 3.7. Application mandatory settings.
1. Change constants with the appropriate value into **pur_beurre/settings.py** :
* SECRET_KEY = Either add a secret key in your environment variables or directly add a secret key here.
* DATABASE =  Set the appropriate database name, username and password as defined in step 3.4.
* DEBUG = Set *True* in dev env mode.
* ALLOWED_HOSTS = Set *[]* in dev env mode. NB: You need to allow more than only localhost as the selenium, when runnig test generates radom server adresses. 

Example:

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'dbnamethatyouwant',
                'USER': 'yourusername',
                'PASSWORD': 'yourpassowrd',
                'HOST': '',
                'PORT': '5432',
            }
        }
2. Also remove the following statement at the bottom of the file:

Statement to remove:

        django_heroku.settings(locals())

NB: This statement is purely when deploying the app on Heroku server.

### 3.8. Apply DB migrations.
Run migration to setup the DB correctly.
> python manage.py migrate

### 3.9. Import values into DB.
Populate the database with the custom command *reset_db*.
> python manage.py reset_db


### 3.10. Start the program.
To start the program, type the following in your bash.
> python manage.py runserver

The program is now ready to be used on your local environment at the following adress: http://127.0.0.1:8000/.

Please check *5. Users' guide* section bellow to use it.

### 3.11. Test the program.
If you want to perform test after having modified the code, you can run tests.
> python manage.py test

### 3.12. Deactivate the virtual environment.
Once you're done using the program, you should leave the virtual environment. Simply type the following statement in your bash.
> deactivate

### 3.13. Uninstall.
If you want to uninstall the program, simply delete the complete repository form your device.

## 4. Settings.
* Changing settings **must be** done in **pur_beurre/settings.py** file. Make sure to read section *3.7. Application mandatory settings*.
* Changing settings **can be** done in:
 * **pur_beurre/custom_settings/functional_variables.py** file.
 * **pur_beurre/custom_settings/tests_variables.py** file.

### 4.1. *pur_beurre/settings.py.

#### 4.1.1. APP_SECRET_KEY.
DESCRIPTION: Secret key required for Django.  
MANDATORY: Yes.  
DEFAULT SETTINGS: os.environ.get("APP_SECRET_KEY").  
CUSTOM SETTINGS: In a dev environment, you can either  type a secret key here or create environment variable of that name, i.e. APP_SECRET_KEY, with your a secret value(only known to you).

#### 4.1.2. DATABASES.
DESCRIPTION: PostgreSQL database settings.  
MANDATORY: Yes.  
DEFAULT SETTINGS:

        {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'pur_beurre',
                'USER': 'username',
                'PASSWORD': 'userpassword',
                'HOST': '',
                'PORT': '5432',
            }
        }.   
CUSTOM SETTINGS: In a dev environment, you can define DATABASES 'NAME', 'USER' and 'PASSWORD' keys.

### 4.2. *pur_beurre/custom_settings/functional_variables.py

#### 4.2.1. CATEGORIES_ENDPOINT
DESCRIPTION: Open Food Facts (OFF) API categories list endpoint.  
MANDATORY: Yes.  
DEFAULT SETTINGS: "https://fr.openfoodfacts.org/categories.json".
CUSTOM SETTINGS: To use the application with product references from another country than France, use the appropriate ISO-3166-1
Alpha 2 code and replace it in the endpoint (e.g. "https://es.openfoodfacts.org/categories.json" for Spain).  
For more information, please check "https://documenter.getpostman.com/view/8470508/SVtN3Wzy?version=latest#intro". 

#### 4.2.2. SELECTED_CATEGORIES
DESCRIPTION: OFF API products categories type used in the application.  
MANDATORY: Yes.  
DEFAULT SETTINGS: ["en:snacks", "en:desserts", "en:breads",
"en:breakfast-cereals", "en:meals"].  
CUSTOM SETTINGS: Categories can be changed. Value to use can be found in
"https://world.openfoodfacts.org/categories.json" in the
category "tags" "id".   
For more information, please check "https://documenter.getpostman.com/view/8470508/SVtN3Wzy?version=latest#intro".

#### 4.2.3. PRODUCTS_ENDPOINT
DESCRIPTION: OFF API products research functionality endpoint. It returns the product research functionality per country.  
MANDATORY: Yes.  
DEFAULT SETTINGS: "https://fr.openfoodfacts.org/cgi/search.pl".  
CUSTOM SETTINGS: To use the application with product references from another country than France, use the appropriate ISO-3166-1. Alpha 2 code and replace it in the endpoint (e.g. "https://es.openfoodfacts.org/cgi/search.pl"). For more information, please check "https://documenter.getpostman.com/view/8470508/SVtN3Wzy?version=latest#intro".

#### 4.2.4. PRODUCTS_AMOUNT
DESCRIPTION: Amount of product to get from OFF API per product category.  
MANDATORY: Yes.  
DEFAULT SETTINGS: 1000.  
CUSTOM SETTINGS: Can be changed but should not exceed 2000 to avoid upload failure.

## 5. Users' guide.

### 5.1. Program functionalities
The program provides the following functionalities:
1. Create an account.
2. Log in.
3. Search for healthier product than a selected one.
4. Check products nutritional info.
5. For loged in users, save their favorites substitutes products.
6. Logout.

### 5.2. How to.
* Browse to the app url i.e. http://127.0.0.1:8000/ (on the dev environment) and make the research you want. You can create an account and login in order to save your choices for a later sessions.
