# Sign in and Register Form

## Introduction

```
A sign in and register form made using React.js as frontend
Express.js as the backend and MongoDb as the database.
```
### Third-Party Libraries Required :

```
For backend:
   "bcrypt": "^5.0.1",
   "cors": "^2.8.5",
   "dotenv": "^10.0.0",
   "express": "^4.17.1",
   "mongoose": "^5.13.2",
   "nodemon": "^2.0.10",
```

```
For Front-End:
  "axios": "^0.21.1",
  "bootstrap": "^5.0.2",
  "react": "^17.0.2",
  "react-dom": "^17.0.2",
  "react-particles-js": "^3.5.3",
  "react-router-dom": "^5.2.0",
  "react-scripts": "4.0.3",
  "web-vitals": "^1.1.2"
```

### How to install the above Library :

- Change to the directory using -
  ```
  cd sign-in-and-register-form
  ```
- For the front-end:-
  ```
  cd client
  npm install
  ```
- For the back-end:-
  ```
  cd api
  npm install
  ```

### How to use it:

- Run this command to start the project.
  ```
  cd api
  npm start
  ```
  ```
  cd client
  npm start
  ```

### How to setup the mongodb:

```
In the config.env file in api
mongodb+srv://yourusername:<password>@cluster0.m9l4p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
use your username and password and database name here you created in MongoDB atlas
```

### Output:

#### Input Image
- First you have to register if you are not already registered:-
 ![image](https://user-images.githubusercontent.com/64858573/125296469-f359e180-e343-11eb-9080-3e976f8540c7.png)
#### Input Image
- Then you have to login using your registered username and password:- \*![image](https://user-images.githubusercontent.com/64858573/125297489-e689bd80-e344-11eb-9e80-c8432888b1ef.png)
#### Output Image
- Then if you want then logout press the logout button:-
 ![image](https://user-images.githubusercontent.com/64858573/125298640-f524a480-e345-11eb-8d6e-e8335df52d09.png)
