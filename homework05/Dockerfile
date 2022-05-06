FROM centos:7.9.2009

RUN yum update -y

RUN yum install -y python3

RUN pip3 install pytest==7.0.0

RUN wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json /data/ML_Data_Sample.json

COPY app.py /code/app.py

RUN chmod +rx .code/app.py

ENV PATH "/code:$PATH"
