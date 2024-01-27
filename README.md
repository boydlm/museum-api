# Install all dependencies and local configuration

## Backend
Install all requirements from the `api/` directory
```
pip install -r requirements.txt
```

Some of the api’s rely on api keys or other secrets. Create the file api/.env with the following contents:
```
HARVARD_API_KEY = <insert api key here>
```

## Frontend
Install all dependencies
```
npm start
```

# Run the application
Start the backend server
```
yarn start-api
```

Start the frontend local server
```
yarn start
```

Go to `localhost:3000/` in your browser

# Running tests

```
pytest test
```