#adding my all dependencies

FROM python:3.9-buster

#ake a workig directory for our app
WORKDIR /app .
#intsall all  required dependencies
COPY reqirements.txt . 
RUN pip install -r requirements.txt
#copy source code
COPY /src .
#run our code
CMD [ "python", "main.py" ]