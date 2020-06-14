## Predicting number of people in a place at a current time

## __To run the count model__

1. ```Clone the repository```
2.  install requirements from requirement.txt ```pip install -r requirements.txt ```
3. ```cd ML-model```
4. ```python people_counter.py``` 

> Main requirements are 
> 1. python
> 2. flask
> 3. openCV
> 4. imutils
> 5. dlib
> 6. numpy

The default UID for the test surveillance video is 1, you can change that when replicating for multiple real time camera ids

## __api.py__
It is the api file which runs on localhost server and can serve get request for the current count of people at a particular location by camera unique id (UID)
