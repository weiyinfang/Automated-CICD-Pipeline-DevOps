# Stage 1: build the static site with MkDocs
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY mkdocs.yml .
COPY docs/ docs/
RUN mkdocs build --strict -d /build/site

# Stage 2: serve the site with Nginx on port 8080 (the Cloud Run default)
FROM nginx:stable-alpine

COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /build/site /srv/mkdocs/site

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
