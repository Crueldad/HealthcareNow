# HealthcareNow

## Application Concept:
Once the Affordable Care Act was signed into law in 2010, having health insurance became mandatory. Deciding on a plan can be laborious especially with for those with low health literacy. The target population for our project are young adults looking to find a health plan that fits their needs.

### Team Members:
1. Ian Crueldad
2. Jacquie Rollins
3. Elmira Akbaripourdibazar
4. Monica Montano
5. Farhad Turabi 

### Stakeholders:
* Campus represenativies
* Students
* Healthcare agencies and hospitals
* Leaders in the healthcare field
* Health insurance providers


#### Requirements:
* User Log In
* Collect User Info
* Make a database
* Provide best healthcare plan


#### User Stories:
1. User should be able to log in
2. User should be able to add information to their profile
3. User should be able to input their healthcare needs and health symptoms 
4. Gather data from users to assess their health needs
5. Based on the information we gather about user’s health need; application will provide a system that determines the best health plans  for users
6. Create a public and private key that would indicate what information belongs to what user without showing an obvious public connection of which public keys belong to which private keys. 


#### Completion Times for User Stories:
1. User should be able to log in: 5 days
2. User should be able to add information to their profile: *5 days*
3. User should be able to select their health symptoms and needs:  *4 days*
4. Gather data from users to assess their health needs:  1 month
5. Based on the information we gather about user’s health need; application will provide a system that determines the best health plans for users:  *1 month*
6. Create a public and private key that would indicate what information belongs to what user without showing an obvious public connection of which public keys belong to which private keys: *3 days*


#### Example of User Stories:

    • I am a F1 visa student. I go to the gym a lot. I have noticed occasionally that I tend to strain some of my muscles after a hard work out.  I am looking for the best insurance plan for me in case I injure myself.* 

    • I am a 25-year-old who is about to be dropped from my parent’s health plan. I engage in multiple risky behaviors in addition to  having multiple mental health problems.  I want to have a health plan that will address my needs for the lowest cost.*

    • I am a 23-year-old student who just found out I am pregnant. I still haven’t decided what I want to do so I’d like to know my    different options regarding abortion, adoption, and maternal child health.*

    • I am uninsured and have been recently diagnosed with cervical cancer. I would like to know what services and treatments are      available to me.

    • Currently, I am a 20-year-old student who is in the middle of joining a sorority. I have decided to live in the house owned by my sorority. I blacked out and slept with a guy and did not realize that protection was not used. After being in pain and noticed a      rash, I consulted Web MD. I have realized there is a high chance that I contracted herpes. I hope there is a plan the offers a reduced cost on generic drugs.*

    • I am a 22-year-old transgender female who was recently diagnosed with HIV. This situation prompted me to stop using crystal meth. I need rehabilitation services and long-term HIV care.  In addition, I was diagnosed with borderline personality disorder, therefore I need dialectical behavioral therapy.*


## Milestone 1:  
- Draft of website  
- Interface and working functional algorithm for collecting user information 
- Create database for log in and register 
- Create chat and help server 


### Allocated Tasks:
* *Jackie:	Develop the App, Databases, Log in*
* *Ian:	    Develop the App, Databases, Log in*
* *Elmira:	User Interface Designer*
* *Monica:	Gather data*
* *Farhad:	Security*


### User Story and Time Estimates: 

#### Iteration 1:
* *Velocity: 0.7*
* *Days of work: 14*
* *Days we finish: 14/0.7=20*
* *Each person work days: 20/5= 4*

##### User should be able to log in 
###### Task 1: 
1. Data model in Django 
2. Create user interface 
3. Commands for inserting new users in database 
4. Hashing username and password 




##### User should be able to add information to their profile 
###### Task 2: 
1. Create user interface
2. Save information to database


#### Iteration 2:
* *Velocity: 0.7*
* *Days of work: 14*
* *Days we finish: 14/0.7=20*
* *Each person work days: 20/5= 4*

##### User should be able to input their healthcare needs and health symptoms: 
###### Task 1: 
1. Create a database with heath categories
2. Input objects on website 


##### Gather data from users to assess their health needs:
###### Task 2: 
1. Set up migration system between user interface and database


## How to run the application
### Environment to run the application
- Python 3.7.8
- Pip 18.1
- Virtual Environment 16.0.0
### Run Application command
1. from application root activate the virtual environment
```ruby
* Mac OS
source ./venv/bin/activate 
* Windows OS
execute/run "activate" file
``` 
2. run Dango server from app folder
```ruby
* use python3 in stead of python if code shows error
cd ./app
python manage.py runserver
```
3. Stop server by Ctrl + C
```ruby
Ctrl + C
```
4. Deactivate the virtualenv when not in use
```ruby
deactivate
```
5. Access application from http://localhost:8000/

6. Sample Application RUN
```ruby
WL-223-234:IST303-Group-Project abinash$
WL-223-234:IST303-Group-Project abinash$ ls
README.md       app             venv
WL-223-234:IST303-Group-Project abinash$ cd app/
WL-223-234:app abinash$ ls
db.sqlite3      manage.py       mysite          news
WL-223-234:app abinash$ source ../venv/bin/activate
(venv) WL-223-234:app abinash$ python3 manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
October 15, 2018 - 23:13:27
Django version 2.1.2, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
### Tests
- Test Settings
1. Test uses following pytest.ini settings
```ruby
[pytest]
DJANGO_SETTINGS_MODULE=mysite.settings_test
addopts = --reuse-db
```
2. DJANGO_SETTINGS_MODULE setting is required for providing django context to test.
```ruby
"--reuse-db" is option provided by pytest-django plugin. It is used so that test enviroment does not delete the test database
```
- Run Tests
1. Run Test from inside "app" folder with command "pytest test" after activating virtual environment. Test are located in app/test folder
```ruby
(venv) WL-198-226:app abinash$ pytest test
================================================ test session starts =================================================
platform darwin -- Python 3.7.0, pytest-3.10.0, py-1.7.0, pluggy-0.7.1
Django settings: mysite.settings_test (from ini file)
rootdir: /Users/abinash/Desktop/CGU/Courses/Software Development/project/IST303-Group-Project/app, inifile: pytest.ini
plugins: django-3.4.3, cov-2.6.0
collected 25 items

test/test_endpoint.py ......x.x.x........                                                                      [ 76%]
test/test_model.py ......                                                                                      [100%]

======================================== 22 passed, 3 xfailed in 2.08 seconds ========================================
(venv) WL-203-33:app abinash$
```









