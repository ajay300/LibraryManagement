
# Library Management 

This is a simple library management system built for Major Project 2021 by AJAY RAJBHAR
## Authors

- [@ajay300](https://github.com/ajay300)


## Functions
### Admin
- Create Admin account and Login.
- Can Add, View, Book
- Can Issue Book (added by Admin) to registered student.
- Can view Issued book with issued date and expiry date.
- Can view Fine (10 rupees for each day after expiry date).
- Can View Students that are registered into system.

### Student
- Create account and Login.
- Can view their issued book only with expiry date and fine(if there any otherwise 0)
---

## Deployment

To deploy this project run

## HOW TO RUN THIS PROJECT
- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
- Open Terminal and Execute Following Commands :
```
python -m pip install -r requirements. txt
```
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```


## CHANGES REQUIRED FOR CONTACT US PAGE
- In settins.py file, You have to give your email and password
```
EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = 'your email password'
EMAIL_RECEIVING_USER = 'youremail@gmail.com'
```

## Drawbacks/LoopHoles
- Anyone can be Admin.

## Feedback
Any suggestion and feedback is welcome. You can message me on facebook
- [Contact on Linkdin](https://www.linkedin.com/in/ajay-rajbhar-7096b2238/)