### Flask Get URL 

This is a simple API service that returns the content returned by an http request against an endpoint. In other words when you hit the `Flask Get URL` application, it will make an http request to an endpoint, grab its content and present it. By default the endpoint is set to `it20.info` (my blog) but it could be replaced by passing the system variable `URL` (e.g. it could be set to use `www.google.com`, `python.org`, etc). 

#### Use cases

In its simplest form the application can be used to validate basic connectivity (e.g. dns resolution and outbound traffic). In more advanced scenarios this application can be used as a bastion/proxy for http requests. For example, imagine a user may need/want to interact with microservices that are not configured with a public network endpoint. These users could deploy the application in the same network, expose it externally and configure the `URL` variable to interact/query a private microservice (this use case would require more flexibility in the code such as configuring the endpoint at runtime rather than at launch time with a variable and, in addition, it would need to support custom ports and not just defaulting to http/80).   

### How to set up the application

This is a classic Python application. 

It can be launched with: 
```
pip install -r requirements.txt 
python app.py 
```

This application has been tested with `Python3` only. 

### Knwon limitations and to-do 

- provide a way to customize the endpoint at runtime (and not via a system variable at deployment time)
- provide a way to customize the port (and not just assume http/80)
- provide a Dockerfile 

#### Licensing

This application is made available under the [MIT license](./LICENSE). The Python prerequisite required to run this application and their licensing are as follows:
```
Flask - BSD License 
```

