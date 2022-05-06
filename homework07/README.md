# Systems Diagramming

This is a systems diagram I made for turning xml data structures into data structures that are more easily parsed through.


![System Diagram](https://github.com/dilaaaap/coe332sp2022/blob/main/homework07/systemdiagram.png)

## Description

This systems diagram walks you through the steps taken in the midterm to take the raw xml data from the NASA files to change them into dictionary files with formats that are more usable.

The system starts once the user makes a POST request, in this case with the command
```
    curl -X POST localhost:5010/load
```
This POST request then initiates the file to pull the xml files from their respective locations using wget, which are then read into the file.

```
    wget.download("https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesUSA05.xml")
    wget.download("https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_OEM/ISS.OEM_J2K_EPH.xml")
    
    ...
    @app.route('/load.methods = ['POST'])
    ...
        with open(name1,'r') as f:

    ...
        with open(name2,'r') as f:

```

Because the data is in xml format, it is not very easy to iterate through each of the bits of data, so we must change the structure of the data.

The xmltodict library converts the xml file to a dictionary file, although it does not get rid of the doubled keys everywhere.

``` ...
    data1 = xmltodict.parse(f.read())
    ...
    data2 = xmltodict.parse(f.read())
```
To get rid of these, we process the output of xmltodict further, using json.loads and json.dumps. 

```
    json_data1 = json.dumps(data1)
    dict1 = (json.loads(json_data1))
    ...
    json_data2 = json.dumps(data2)
    dict2 = (json.load(json_data2)
```
    
Following this, we are left with a dictionary full of dictionaries. However, we are not yet able to iterate through this properly. To get to the main chunk of data, we have to remove the outer 'layers' of keys surrounding the data that we want. By inspecting the files, you can achieve this by using dict[key1]...[keyn] to chew through however many layers are necessary to remove headers and other unwanted things. To iterate through this dictionary of dictionaries, we will have to give them each a unique identifier, as keys cannot repeat in the same dictionary. The dict(enumerate()) function does exactly this, and assigns each dictionary a number that we can easily reference to see each individual dictionary. 

```
    dict1modify = dict(enumerate(dict1['visible_passes']['visible_pass']))
    ...
    dict2modify = dict(enumerate(dict2['ndm']['oem']['body']['segment']['data']['stateVector']))
```
Now that we have completed this, we have converted the xml files into datasets that are very compatible with the tools we have in Python, allowing us to complete the GET requests.

### Dependencies

* This is based on my midterm python file which is linked here: 
[Midterm app.py](https://github.com/dilaaaap/ISSdataparser/blob/main/app.py)

