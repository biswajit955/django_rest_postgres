# MAIN CODE RESIDE INSIDE src

Here i can able to achive these :

## I (DRF-env) this virtual environment. so, use this ( DRF-env\Scripts\activate.bat )

## 1. User Sign Up (http://127.0.0.1:8000/api/profile-singup/)

simlpy just put all the details in email,name,password and your profile gets created you can check by reloading
(http://127.0.0.1:8000/api/profile-singup/)api/password_reset/

## 2. Forgot Password:
    
(http://127.0.0.1:8000/api/password_reset/)


## 3. Uses JWT authentication

Jwt authentication is used , here modheader is used while authorization
For loggin (http://127.0.0.1:8000/api/login/)
put your email and password and you recive the token just pasted that token on modheader request header authorization and
(http://127.0.0.1:8000/api/login/) + user id that is created while making new user you can also check by  (http://127.0.0.1:8000/api/profile/) and simply using the filter
Now you are inside your profile and you can delete your profile if you want

## 4. Must define 3 user levels : 1. Super-admin, 2. Teacher, 3. Student (Use internal Django Groups to achieve the same)

 user levels can be achived by 1// Django admin 2// or 3// by simply using filter in (http://127.0.0.1:8000/api/profile/)


## 5. Teacher must be able to list all the students.

Using Filter

## 6 . Admin must be able to list every user in the database.

By using django admin

## 7. Code should be commented for clarity.

Done

