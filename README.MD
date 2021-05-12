1) Install virtual environment
2) Install django and optional django-shortcuts
pipenv install django (django-shortcuts)
3) Initialize django project
django-admin startproject backend
4) Create app
django-admin startapp todo

5) Add app in settings

ReactJs integration

6) pipenv install djangorestframework django-cors-headers
7) Add them to installed apps
'corsheaders',
'rest_framework',
8) Add line in settings MIDDLEWARE
'corsheaders.middleware.CorsMiddleware',
9) Add to the bottom of settings document
CORS_ORIGIN_WHITELIST = [
     'http://localhost:3000'
]
10) Create serializer, model, view and update urls

Setting up frontend
11) npx create-react-app frontend
cd frontend
npm start

12)Install bootstrap and reactstrap to provide user interface tools
npm install bootstrap@4.6.0 reactstrap@8.9.0 --legacy-peer-deps

13) Add import 'bootstrap/dist/css/bootstrap.css'; in index.js

14) install npm install axios@0.21.1 to allow making requests to the API endpoints on the backend server

15) Add in package.json line
 "private": true,
  "proxy": "http://localhost:8000",
  "dependencies" 

  without proxy would need to specify full path with proxy can prvide relative paths: axios.get("/api/todos/")