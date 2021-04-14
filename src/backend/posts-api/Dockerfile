FROM python:alpine
WORKDIR /src
COPY . ./backend/posts-api/
RUN pip install -r ./backend/posts-api/requirements.txt
CMD python backend/posts-api/app.py 