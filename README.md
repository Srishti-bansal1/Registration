# Introduction <br>
This is a student registration project. In this project I used python language (version 3.9 ) & Django Rest framework (version 4.2.9). This project  used to enrolled the student , read the student information, update the informations and delete the details.  <br>
In this project , I Designed a model and their fields are name , dob , email , state , city , pin.  Migrated the model to create a Table. Connected with MYSQL database. Created APIs for Create, Read, Update and Delete operation. <br>
'register/reg/show' use for read <br> 'register/reg/create' use for create <br> 'register/reg/<id>/modify' use for update <br> 'register/reg/delete_all' use for delete all registration. 
<br>


# SetUp for Linux or MAC <br>
step 1 : open terminal and clone the code by executing *git clone <https://github.com/Srishti-bansal1/Registration.git>*
<br>
step 2 : Install virtual environment  with command : pip install virtualenv
<br>
step 3 : Activate the virtual environment with command : source  REgEnv/bin/activate
<br>
step 4 : Move in projct file with command : cd RegPro
<br>
step 5 : Execute migration command to create table in database using command : python mange.py migrate
<br>
step 6 : Run the server with command : python manage.py runserver 8002
<br>

# API Documentation -<br>
        1. Create :- End point - register/reg/create 

                     request body - {	"name"   : <str> ,
                                        "dob"    : <str>,
                                        "email"  : <str>,
                                        "state"  : <str> ,
                                        "city"   : <str> ,
                                        "pin"    : <int>
                                        }	
                     response body - {	"id "    : <int>,
                                        "name"   : <str> ,
                                        "dob"    : <str>,
                                        "email"  : <str>,
                                        "state"  : <str> ,
                                        "city"   : <str> ,
                                        "pin"    : <int>
                                        }
                                    	

        2. Read :- End point - register/reg/show 
        
                   response body - {	"id "    : <int>,
                                        "name"   : <str> ,
                                        "dob"    : <str>,
                                        "email"  : <str>,
                                        "state"  : <str> ,
                                        "city"   : <str> ,
                                        "pin"    : <int>
                                        }	
                                        

        3. Update :-  End point - register/reg/<id>/modify
        
                      request body - {	"name"   : <str> ,
                                        "dob"    : <str>,
                                        "email"  : <str>,
                                        "state"  : <str> ,
                                        "city"   : <str> ,
                                        "pin"    : <int>
                                        }	
                                    
                      response body - {	"id "    : <int>,
                                        "name"   : <str> ,
                                        "dob"    : <str>,
                                        "email"  : <str>,
                                        "state"  : <str> ,
                                        "city"   : <str> ,
                                        "pin"    : <int>
                                        }	       
                                                     
        
        4. Delete :- End point - register/reg/delete_all
    
                     response body - empty