# Greeter

A tiny Python web page that says hello. It uses only Python's built-in `http.server`, so there are no dependencies to install. Open it in a browser and it shows a greeting with my name.

## Run with Docker

Build the image:

```
docker build -t greeter:1.0 .
```

Run it, then open http://localhost:8080:

```
docker run -d --rm -p 8080:8000 --name greeter greeter:1.0
```