# Greeter

A tiny Python web page that says hello. It uses only Python's built-in `http.server`, so there are no dependencies to install.

## Run with Docker

Build the image:

```
docker build -t mahnoorzahra/greeter:1.1 .
```

Run it, then open http://localhost:8080:

```
docker run -d --rm -p 8080:8000 --name greeter mahnoorzahra/greeter:1.1
```

Stop it with `docker stop greeter`.

## Run without the source code

The image is published on Docker Hub, so you can run it without cloning this repo. Versions `1.0` and `1.1` are both available. Pick one with the tag:

```
docker run -d --rm -p 8080:8000 mahnoorzahra/greeter:1.1
```

## Run without Docker

```
python hello.py
```

Then open http://localhost:8000.