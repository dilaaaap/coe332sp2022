# Networking with Kubernetes -HW6

Building on the Flask and Redis tools from the last homework. We now use deploy our apps using Kubernetes to distribute them over a cluster of computers.

## Description
In this file we use Kubernetes to generate 'pods' using our redis and flask servers. These pods are similar to containers and the yml files allow us to manipulate them to allow them to do various useful things.

In the first part of the homework, we focus on redis. First we modify a yml file to create a PVC or persistent volume claim for our redis server.
```
---
apiVersion: v1
kind: PersistentVolumeClaim
...
  name: dilaaaap-test-redis-pvc
  app: dilaaaap-test-redis
...
 storage: 1Gi
 ```
By doing this we have created a pvc with 1 gigabyte of space for our redis server.

Following this, we make two more yml files for redis; one for deployment and one for service.
```
--
apiVersion: apps/v1
kind: Deployment
...
  labels:
        app: dilaaaap-test-redis
...
- name: dilaaaap-test-data
        persistentVolumeClaim:
          claimName: dilaaaap-test-redis-deployment
```
```
---
apiVersion: v1
kind: Service
metadata:
  name: dilaaap-service
spec:
  type: ClusterIP
  selector:
    app: dilaaaap-test-redis
  ports:
  - name: dilaaaapservicedeployment
    port: 6410
    targetPort: 6410
```
The deployment file generates instances of the redis server while the service file tells them which IP address and port to use.

Similarly, we make files for Flask using yml, this time only with services and deployment
```   
---
apiVersion: v1
kind: Service
metadata:
        username: dilaaaap
        env: test
  name: dilaaaap-flaskflask
spec:
  type: ClusterIP
  selector:
      app: dilaaaap-test-flask
          ports:
          - name:dilaaaap-test-flask
            containerPort: 5010
            port: 5010
            targetPort: 5010
```
```
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: dilaaaapflask
  labels:
        username: dilaaaap
        env: test
    app: dilaaaap-test-flask
spec:
  replicas: 2
  selector:
    matchLabels:
      app: dilaaaap-test-flask
  template:
    metadata:
      labels:
        app: dilaaaap-test-flask
    spec:
      containers:
        - name: dilaaaapflask
          imagePullPolicy: Always
          image: dilaaaap/hello-flask
```
These files function in a similar manner for the Flask files as they did for the redis files.
### Dependencies

* Must be connected to the tacc network to run kubernetes for this assignment.
* Also required are python3,Docker, redis, Flask, and pytest
