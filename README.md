# Create Docker images
```shell
docker build -t fastapi-app .
```

# Run container
```shell
docker run -d -p 8000:8000 fastapi-app
```

# Access the app 
http://localhost:8000

____
# If you want just start app at local laptop, run this command
```shell
uvicorn app.main:app --reload
```

