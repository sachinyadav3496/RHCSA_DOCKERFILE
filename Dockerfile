FROM    fedora:latest
COPY    app.py  /app/
WORKDIR /app/
EXPOSE 8080:8080
CMD ["python3", "app.py"]