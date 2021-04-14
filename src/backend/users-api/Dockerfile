FROM python:alpine
WORKDIR /src
COPY . ./backend/users-api/
RUN pip install -r ./backend/users-api/requirements.txt
CMD python backend/users-api/app.py 