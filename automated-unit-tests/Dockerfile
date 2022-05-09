FROM python:3.7

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY . /usr/src/app/
RUN pip install -r requirements.txt

RUN ls
# Bundle app source
#COPY hello_world.py unit_tests1.py  /usr/src/app/

EXPOSE 5500
ENTRYPOINT ["python"]
CMD ["hello_world.py"]