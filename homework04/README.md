# Project Title

In this file, we take data from a dataset, Meteorite_Landings.json, and we summarize that data to demonstrate methods of accessing dictionaries and containerization.

## Description
Starting with the original ml_data_analysis.py file, we first modify the main function to instead count the number of landings in each quadrant and then output them using a for loop.

```
    #example with NE
    NE = 0
    ...
    for row in ml_data['meteorite_landings']:
        if check_hemisphere(float(row['reclat']), float(row['reclong'])) == 'Northern & Eastern':
            NE = NE +1 
    ...
    print("There were ", NE, " meteors found in the Northern and Eastern quadrant")
```
After this we add tothe main function to access the json file in a similar manner to obtain the summary data of the types of meteors that were landing.

```
 holder = count_classes(ml_data['meteorite_landings'], 'recclass')
    for key, value in holder.items():
        print("The ", key ,  " class was found ", value, " times.")
```
Following this we containerize the file with Docker, putting all the necessary files to run it into the commands of the Dockerfile.

```

   
FROM centos:7.9.2009

RUN yum update -y

RUN yum install -y python3

RUN pip3 install pytest==7.0.0

COPY ml_data_analysis.py /code/ml_data_analysis.py

RUN chmod +rx /code/ml_data_analysis.py

COPY test_ml.py /code/test_ml.py

ENV PATH "/code:$PATH"
```
This makes a self-contained file that can run and the image of the file is uploaded to dockerhub where it can be shared.
### Dependencies

* My program requires installations of Flask, python3,pytest, and Docker. 

### Installing

* Original, unchanged ml_data_analysis.py file:
[ml_data_analysis.py](https://raw.githubusercontent.com/tacc/coe-332-sp22/main/docs/unit04/scripts/ml_data_analysis.py)
* To pull the docker file, go to:

[Dockerhub Link](https://hub.docker.com/layers/208629873/dilipyy/ml_data_analysis/hw04/images/sha256-45ab5f1d315dcc54c6084be7c0315379dbb944f9328dd360dc5939ceefb81485?context=repo)

* To pull Meteorite_Landings.json, go to:
[Meteorite_Landings.json](https://raw.githubusercontent.com/tacc/coe-332-sp22/main/docs/unit04/scripts/Meteorite_Landings.json)

* For more data to run against ml_data_analysis.py, go to:

[more-meteorites.json](https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json)

### Executing program

* To run this file, after pulling the Docker file from Dockerhub, you can build and run the Docker file with:
```
docker build -t <username>\filename:version

docker run --rm -v $PWD:/data username/ml_data_analysis:1.0 ml_data_analysis.py /data/filename.json
```
in the command line.

You can then test it on the data included in my sample set by simply running it.

```
ml_data_analysis.py Meteorite_Landings.json

```

If you would rather run ml_data_analysis.py against a different dataset, you just need to use wget to pull the file into the docker file and it will run with the file (given that the data structures of the file match with Meteorite_Landings.json)

ex:
```
wget url.com/filename.json
ml_data_analysis.py filename.json
```

