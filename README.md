# AWS Chalice Workshop, Lambda Functions, ToDo app, DynomoDB, JWT Auth, CI/CD Pipeline

https://chalice-workshop.readthedocs.io/en/latest/index.html

https://github.com/coding-to-music/chalice-workshop

## Outline:

- [Section 0: Introduction to AWS Chalice](https://chalice-workshop.readthedocs.io/en/latest/todo-app/part1/00-intro-chalice.html)
- [Section 1: Create initial Todo application](https://chalice-workshop.readthedocs.io/en/latest/todo-app/part1/01-todo-app-new-project.html)
- [Section 2: Add chalicelib to Todo application](https://chalice-workshop.readthedocs.io/en/latest/todo-app/part1/02-todo-app-chalicelib.html#)
- [Section 3: Add a DynamoDB table for Todo application](https://chalice-workshop.readthedocs.io/en/latest/todo-app/part1/03-todo-app-dynamodb.html)
- [Section 4: Add authorization to Todo application](https://chalice-workshop.readthedocs.io/en/latest/todo-app/part1/04-todo-app-auth.html)

## Prerequisite: Setting up your environment

To start working with AWS Chalice, there are some requirements your development environment must have:

- Python 3.7 or later
- Virtualenv
- AWS credentials
- git
- tree

# Part 0: Introduction to AWS Lambda and Chalice

This section will provide an introduction on how to use AWS Chalice and provide

### Instructions on how to go about building your very first Chalice application

running on AWS Lambda. Steps include:

## Create a virtualenv and install Chalice

To start using Chalice, you will need a new virtualenv with Chalice installed.

### Instructions

Make sure you have Python 3 installed. See the :doc:`env-setup` page for

### Instructions on how to install Python.

1. Create a new virtualenv called `chalice-env` by running the following
   command::

```java
$ python3 -m venv chalice-env
```

2. Activate your newly created virtualenv::

```java
$ source chalice-env/bin/activate
```

If you are using a Windows environment, you will have to run::

```java
> .\chalice-env\Scripts\activate
```

3. Install `chalice` using `pip`::

```java
$ pip install chalice
```

### Verification

1. To check that `chalice` was installed, run::

```java
$ chalice --version
chalice 1.6.0, python 3.7.3, darwin 15.6.0
```

The version of `chalice` must be version `1.6.0` or higher and the version of Python should be 3.7.

## Create a new Chalice application

With `chalice` now installed, it is time to create your first Chalice
application.

### Instructions

1. Run the `chalice new-project` command to create a project called
   `workshop-intro`

```java
$ chalice new-project workshop-intro

```

### Verification

1. A new `workshop-intro` directory should have been created on your behalf.
   Inside of the `workshop-intro` directory, you should have two files: an
   `app.py` file and a `requirements.txt` file::

```java
$ ls workshop-intro
app.py requirements.txt
```

## Hello world Lambda function

Let's create our first Lambda function and deploy it using Chalice.

### Instructions

1. Change directories to your newly created `workshop-intro` directory::

```java
$ cd workshop-intro
```

2. Open the `app.py` file and delete **all** lines of code underneath
   the line: `app = Chalice(app_name='workshop-intro')`. Your `app.py` file
   should only consist of the following lines::

```java
from chalice import Chalice

app = Chalice(app_name='workshop-intro')
```

3. Add a new function `hello_world` decorated by
   [app.lambda_function()](https://chalice.readthedocs.io/en/latest/api.html#Chalice.lambda_function)
   that returns `{"hello": "world"}`. Your `app.py` file should now consist
   of the following lines::

```java
from chalice import Chalice

app = Chalice(app_name='workshop-intro')

@app.lambda_function()
def hello_world(event, context):
    return {'hello': 'world'}
```

4. Run `chalice deploy` to deploy your Chalice application to AWS Lambda::

```java
$ chalice deploy
Creating deployment package.
Creating IAM role: workshop-intro-dev
Creating lambda function: workshop-intro-dev-hello_world
Resources deployed:
  - Lambda ARN: arn:aws:lambda:us-west-2:123456789123:function:workshop-intro-dev-hello_world
```

### Verification

1. Run the `chalice invoke` command to invoke your newly deployed
   `hello_world` Lambda function::

```java
$ chalice invoke -n hello_world
{"hello": "world"}

```

## Lambda function using event parameter

Lambda functions accept two parameters: an `event` and a `context`
parameter. The `event` parameter is used to provide data to the Lambda
function. It is typically a dictionary, but may be a list, string, integer,
float, or `None`. The `context` parameter provides information about the
runtime to the Lambda function. This step will create a Lambda function that
will use data from `event` passed to it to affect its return value.

### Instructions

1. Create an additional Lambda function `hello_name` using the
   `app.lambda_function()` decorator. The function should retrieve the
   value of the `name` key in the `event` parameter and return
   `{'hello': name}`::

```java

@app.lambda_function()
def hello_name(event, context):
    name = event['name']
    return {'hello': name}
```

Your `app.py` file should now consist of the following lines::

```java
from chalice import Chalice

app = Chalice(app_name='workshop-intro')

@app.lambda_function()
def hello_world(event, context):
    return {'hello': 'world'}


@app.lambda_function()
def hello_name(event, context):
    name = event['name']
    return {'hello': name}
```

2. Run `chalice deploy` to deploy your Chalice application with the
   new Lambda function::

```java
$ chalice deploy
Creating deployment package.
Creating IAM role: workshop-intro-dev
Creating lambda function: workshop-intro-dev-hello_world
Resources deployed:
  - Lambda ARN: arn:aws:lambda:us-west-2:123456789123:function:workshop-intro-dev-hello_world
  - Lambda ARN: arn:aws:lambda:us-west-2:123456789123:function:workshop-intro-dev-hello_name
```

### Verification

1. Run `chalice invoke` to invoke the `hello_name` Lambda function with
   `{"name": "Kyle"}` as the event payload::

```java
$ echo '{"name": "Kyle"}' | chalice invoke -n hello_name
{"hello": "Kyle"}
```

2. It is also possible for your Lambda function to encounter runtime errors.
   Passing in an empty event payload when invoking the `hello_name` will
   result in the Lambda Function returning a Traceback::

```java
$ chalice invoke -n hello_name
Traceback (most recent call last):
File "/var/task/chalice/app.py", line 901, in **call**
return self.func(event, context)
File "/var/task/app.py", line 12, in hello_name
name = event['name']
KeyError: 'name'
Error: Unhandled exception in Lambda function, details above.
```

## Delete the Chalice application

Now with an understanding of the basics of AWS Lambda and Chalice, let's
clean up this introduction application by deleting it remotely.

### Instructions

1. Run `chalice delete` to delete the deployed Lambda functions running this
   application::

```java
$ chalice delete
Deleting function: arn:aws:lambda:us-west-2:123456789123:function:workshop-intro-dev-hello_name
Deleting function: arn:aws:lambda:us-west-2:123456789123:function:workshop-intro-dev-hello_world
Deleting IAM role: workshop-intro-dev

```

### Validation

1. Try running `chalice invoke` on the previously deployed Lambda functions::

```java
$ chalice invoke -n hello_world
Could not find invokable resource with name: hello_world
$ chalice invoke -n hello_name
Could not find invokable resource with name: hello_name
```

You should no longer be able to invoke both Lambda functions as they have
been deleted.

# Section 0: Introduction to AWS Chalice

- [Section 0: Introduction to AWS Chalice](https://chalice-workshop.readthedocs.io/en/latest/todo-app/part1/00-intro-chalice.html)

### AWS CLI:

```java
aws --version
```

Output:

```java
aws-cli/2.4.18 Python/3.8.8 Linux/5.4.0-94-generic exe/x86_64.ubuntu.20 prompt/off
```

### aws configure

With the AWS CLI installed, run aws configure to configure your development environment for AWS credentials via its prompts:

```java
$ aws configure
AWS Access Key ID [None]: ****************ABCD
AWS Secret Access Key [None]: ****************abCd
Default region name [None]: us-west-2
Default output format [None]:
```

to check that everything is correctly set up, run the following AWS CLI:

```java
aws ec2 describe-regions
```

Output:

```java
---------------------------------------------------------------------------------
|                                DescribeRegions                                |
+-------------------------------------------------------------------------------+
||                                   Regions                                   ||
|+-----------------------------------+-----------------------+-----------------+|
||             Endpoint              |      OptInStatus      |   RegionName    ||
|+-----------------------------------+-----------------------+-----------------+|
||  ec2.eu-north-1.amazonaws.com     |  opt-in-not-required  |  eu-north-1     ||
||  ec2.ap-south-1.amazonaws.com     |  opt-in-not-required  |  ap-south-1     ||
||  ec2.eu-west-3.amazonaws.com      |  opt-in-not-required  |  eu-west-3      ||
||  ec2.eu-west-2.amazonaws.com      |  opt-in-not-required  |  eu-west-2      ||
||  ec2.eu-west-1.amazonaws.com      |  opt-in-not-required  |  eu-west-1      ||
||  ec2.ap-northeast-3.amazonaws.com |  opt-in-not-required  |  ap-northeast-3 ||
||  ec2.ap-northeast-2.amazonaws.com |  opt-in-not-required  |  ap-northeast-2 ||
||  ec2.ap-northeast-1.amazonaws.com |  opt-in-not-required  |  ap-northeast-1 ||
||  ec2.sa-east-1.amazonaws.com      |  opt-in-not-required  |  sa-east-1      ||
||  ec2.ca-central-1.amazonaws.com   |  opt-in-not-required  |  ca-central-1   ||
||  ec2.ap-southeast-1.amazonaws.com |  opt-in-not-required  |  ap-southeast-1 ||
||  ec2.ap-southeast-2.amazonaws.com |  opt-in-not-required  |  ap-southeast-2 ||
||  ec2.eu-central-1.amazonaws.com   |  opt-in-not-required  |  eu-central-1   ||
||  ec2.us-east-1.amazonaws.com      |  opt-in-not-required  |  us-east-1      ||
||  ec2.us-east-2.amazonaws.com      |  opt-in-not-required  |  us-east-2      ||
||  ec2.us-west-1.amazonaws.com      |  opt-in-not-required  |  us-west-1      ||
||  ec2.us-west-2.amazonaws.com      |  opt-in-not-required  |  us-west-2      ||
|+-----------------------------------+-----------------------+-----------------+|
```

# Part 1: Build a serverless web application with AWS Chalice

The first part of the workshop will introduce AWS Chalice and walk you through
creating a Todo application using AWS Chalice.

# Section 0: Introduction to AWS Chalice

This section will provide an introduction on how to use AWS Chalice and provide
Instructions on how to go about building your very first Chalice application.

## Create a virtualenv and install Chalice

To start using Chalice, you will need a new virtualenv with Chalice installed.

### Instructions

Make sure you have Python 3 installed. See the :doc:`env-setup` page for
Instructions on how to install Python.

1. Create a new virtualenv called `chalice-env` by running the following
   command::

```java
$ python3 -m venv chalice-env
```

2. Activate your newly created virtualenv::

$ source chalice-env/bin/activate

If you are using a Windows environment, you will have to run::

```java
       > .\chalice-env\Scripts\activate
```

3. Install `chalice` using `pip`::

```java
$ pip install chalice
```

### Verification

To check that `chalice` was installed, run::

```java
$  chalice --version
```

This should print out the version of `chalice` that is installed in your
virtualenv.

Also, ensure that Python 3.7 is being used as the Python interpreter for your
virtualenv::

```java
$  python --version
Python 3.7.3
```

## Create a new Chalice application

With `chalice` now installed, it is time to create your first Chalice
application.

### Instructions

1. Run the `chalice new-project` command to create a project called
   `workshop-intro`::

```java
$ chalice new-project workshop-intro
```

### Verification

A new `workshop-intro` directory should have been created on your behalf.
Inside of the `workshop-intro` directory, you should have two files: an
`app.py` file and a `requirements.txt` file::

```java
$ ls workshop-intro
app.py requirements.txt
```

## Deploy the Chalice application

The newly created Chalice application can also be immediately deployed. So
let's deploy it.

### Instructions

1. Change directories to your newly created `workshop-intro` directory::

```java
$ cd workshop-intro
```

2. Run `chalice deploy` to deploy your Chalice application::

```java
$ chalice deploy
    Creating deployment package.
    Creating IAM role: workshop-intro-dev
    Creating lambda function: workshop-intro-dev
    Creating Rest API
    Resources deployed:
      - Lambda ARN: arn:aws:lambda:us-west-2:12345:function:workshop-intro-dev
      - Rest API URL: https://1y2mueb824.execute-api.us-west-2.amazonaws.com/api/
```

### Verification

The `chalice deploy` command should have exited with a return code of `0`::

```java
$ echo $?
0
```

You should also be able to interact with your newly deployed API. To do so,
first install `httpie`::

```java
$ pip install httpie
```

Get the endpoint of your deployed Chalice application with `chalice url`::

```java
$ chalice url
https://1y2mueb824.execute-api.us-west-2.amazonaws.com/api/
```

Now use `httpie` to make an HTTP request to that endpoint::

```java
$ http https://1y2mueb824.execute-api.us-west-2.amazonaws.com/api/
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 18
Content-Type: application/json
Date: Sat, 21 Oct 2017 23:21:41 GMT
Via: 1.1 403d925786ea6bd8903b99a628977c8f.cloudfront.net (CloudFront)
X-Amz-Cf-Id: FlL4RfE3UqiDFocyTlSzCqtvzxWd9pK0M1lCnIsO1KwjhF37XvVTCg==
X-Amzn-Trace-Id: sampled=0;root=1-59ebd683-72e3a6105ff3425da0c7e0ae
X-Cache: Miss from cloudfront
x-amzn-RequestId: 9776fca3-b6b6-11e7-94e4-b130a115985d

    {
        "hello": "world"
    }
```

The HTTP response back should consist of the JSON body: `{"hello": "world"}`

## Add a new route

Now that we have deployed our first Chalice application, let's expand on it
by adding a new `/hello` route.

### Instructions

1. Open the `app.py` file in your favorite editor::

```java
code  app.py
```

2.  Inside of the `app.py` file, add the following function under the
    existing `index()` function::

```java
         @app.route('/hello')
         def hello_workshop():
             return {'hello': 'workshop'}

    Your `app.py` should now consist of the following::

         from chalice import Chalice

         app = Chalice(app_name='workshop-intro')


         @app.route('/')
         def index():
             return {'hello': 'world'}

         @app.route('/hello')
         def hello_workshop():
             return {'hello': 'workshop'}
```

3.  Deploy the updated application using `chalice deploy`::

```java
$ chalice deploy
Creating deployment package.
Updating policy for IAM role: workshop-intro-dev
Updating lambda function: workshop-intro-dev
Updating rest API
Resources deployed: - Lambda ARN: arn:aws:lambda:us-west-2:12345:function:workshop-intro-dev - Rest API URL: https://1y2mueb824.execute-api.us-west-2.amazonaws.com/api/
```

### Validation

Using `httpie`, confirm that the new route was deployed by making an
HTTP request::

```java
$ http https://1y2mueb824.execute-api.us-west-2.amazonaws.com/api/hello
    HTTP/1.1 200 OK
    Connection: keep-alive
    Content-Length: 21
    Content-Type: application/json
    Date: Sat, 21 Oct 2017 23:34:56 GMT
    Via: 1.1 2d8af5cc5befc5d35bb54b4a5b6494c9.cloudfront.net (CloudFront)
    X-Amz-Cf-Id: upMVSIUvjmCRa33IO-4zpYQOU0C94h50F3oJX_iv-vdk-g1IacKq9A==
    X-Amzn-Trace-Id: sampled=0;root=1-59ebd9a0-0a275c8f6794f2e5c59641c7
    X-Cache: Miss from cloudfront
    x-amzn-RequestId: 7233e21a-b6b8-11e7-a3b6-f7221d70ee14

    {
        "hello": "workshop"
    }
```

The HTTP response back should consist of the JSON body:

```java
`{"hello": "workshop"}`
```

## Add a new route with a URI parameter

Next, let's add a new route that accepts a parameter in the URI.

### Instructions

1.  Inside of the `app.py` file, add the following function under the
    existing `hello_workshop()` function::

```java
         @app.route('/hello/{name}')
         def hello_name(name):
             return {'hello': name}
```

    Your `app.py` should now consist of the following::

```java
         from chalice import Chalice

         app = Chalice(app_name='workshop-intro')


         @app.route('/')
         def index():
             return {'hello': 'world'}

         @app.route('/hello')
         def hello_workshop():
             return {'hello': 'workshop'}

         @app.route('/hello/{name}')
         def hello_name(name):
             return {'hello': name}
```

2.  Deploy the updated application using `chalice deploy`::

```java
$ chalice deploy
Creating deployment package.
Updating policy for IAM role: workshop-intro-dev
Updating lambda function: workshop-intro-dev
Updating rest API
Resources deployed: - Lambda ARN: arn:aws:lambda:us-west-2:12345:function:workshop-intro-dev - Rest API URL: https://1y2mueb824.execute-api.us-west-2.amazonaws.com/api/
```

### Verification

Using `httpie`, confirm that the new route was deployed by making an
HTTP request::

```java
$ http https://1y2mueb824.execute-api.us-west-2.amazonaws.com/api/hello/kyle
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 21
Content-Type: application/json
Date: Sat, 21 Oct 2017 23:34:56 GMT
Via: 1.1 2d8af5cc5befc5d35bb54b4a5b6494c9.cloudfront.net (CloudFront)
X-Amz-Cf-Id: upMVSIUvjmCRa33IO-4zpYQOU0C94h50F3oJX_iv-vdk-g1IacKq9A==
X-Amzn-Trace-Id: sampled=0;root=1-59ebd9a0-0a275c8f6794f2e5c59641c7
X-Cache: Miss from cloudfront
x-amzn-RequestId: 7233e21a-b6b8-11e7-a3b6-f7221d70ee14

    {
        "hello": "kyle"
    }
```

The HTTP response back should consist of the JSON body:
`{"hello": "kyle"}`

## Add a new route with a non-GET HTTP method

For our last route, let's add a new route that accepts a different HTTP method
other than `GET`.

### Instructions

1.  Inside of the `app.py` file, add the following function under the
    existing `hello_name()` function::

```java
         @app.route('/hello-post', methods=['POST'])
         def hello_post():
             request_body = app.current_request.json_body
             return {'hello': request_body}
```

    Your `app.py` should now consist of the following::

```java
         from chalice import Chalice

         app = Chalice(app_name='workshop-intro')


         @app.route('/')
         def index():
             return {'hello': 'world'}

         @app.route('/hello')
         def hello_workshop():
             return {'hello': 'workshop'}

         @app.route('/hello/{name}')
         def hello_name(name):
             return {'hello': name}

         @app.route('/hello-post', methods=['POST'])
         def hello_post():
             request_body = app.current_request.json_body
             return {'hello': request_body}
```

2.  Deploy the updated application using `chalice deploy`::

```java
$ chalice deploy
Creating deployment package.
Updating policy for IAM role: workshop-intro-dev
Updating lambda function: workshop-intro-dev
Updating rest API
Resources deployed: - Lambda ARN: arn:aws:lambda:us-west-2:12345:function:workshop-intro-dev - Rest API URL: https://1y2mueb824.execute-api.us-west-2.amazonaws.com/api/
```

### Verification

Using `httpie`, confirm that the new route was deployed by making an
HTTP request::

```java
$ echo '{"request":"body"}' | http POST https://1y2mueb824.execute-api.us-west-2.amazonaws.com/api/hello-post
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 30
Content-Type: application/json
Date: Sat, 21 Oct 2017 23:48:43 GMT
Via: 1.1 805232684895bb3db77c2db44011c8d0.cloudfront.net (CloudFront)
X-Amz-Cf-Id: ah7w7to9Svn_WzGZ1MldMHERCO_sLxMKQi9AcHFLSjLtAdAPhw5z_A==
X-Amzn-Trace-Id: sampled=0;root=1-59ebdcdb-32c834bbd0341b40e3dfd787
X-Cache: Miss from cloudfront
x-amzn-RequestId: 5f0bf184-b6ba-11e7-a22d-9b7d2bcfb95b

    {
        "hello": {
            "request": "body"
        }
    }
```

Notice the HTTP response back should contain the JSON blob that was echoed
into standard input.

## Delete the Chalice application

Now with an understanding of the basics of how to use AWS Chalice, let's
clean up this introduction application by deleting it remotely.

### Instructions

1.  Run `chalice delete` to delete the deployed AWS resources running this
    application::

```java
$ chalice delete
Deleting Rest API: 1y2mueb824
Deleting function: arn:aws:lambda:us-west-2:12345:function:workshop-intro-dev
Deleting IAM role: workshop-intro-dev
```

    If you are prompted on whether to delete a resource when deleting the
    application, go ahead and confirm by entering `y`.

### Verification

To ensure that the API no longer exists remotely, try to make an HTTP request
to the endpoint it was originally deployed to::

```java
$ http https://1y2mueb824.execute-api.us-west-2.amazonaws.com/api/

    http: error: SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert
    handshake failure (_ssl.c:590) while doing GET request to URL:
    https://1y2mueb824.execute-api.us-west-2.amazonaws.com/api/
```

This should result in an SSL error as the remote application no longer exists
and therefore it cannot be connected to it.

# Section 1: Create initial Todo application

For the rest of this workshop, we will be building a serverless Todo
application. The application will allow for creating Todo's, getting Todo's,
updating Todo's, and deleting Todo's. In terms of the REST API, it will
consist of the following:

```java
============= =============== ============
HTTP Method URI Path Description
============= =============== ============
`GET` `/todos/` Gets a list of all Todo's
`POST` `/todos/` Creates a new Todo
`GET` `/todos/{id}` Gets a specific Todo
`DELETE` `/todos/{id}` Deletes a specific Todo
`PUT` `/todos/{id}` Updates the state of a Todo
============= =============== ============
```

Furthermore, a Todo will have the following schema::

```java
{
"description": {"type": "str"},
"uid": {"type: "str"},
"state": {"type: "str", "enum": ["unstarted", "started", "completed"]},
"metadata": {
"type": "object"
},
"username": {"type": "str"}
}
```

This step will focus on how to build a simple in-memory version of the
Todo application. For this section we will be doing the following to create
this version of the application:

## Install Chalice

This step will ensure that `chalice` is installed in your virtualenv.

### Instructions

1. Install `chalice` inside of your virtualenv::

```java
   $ pip install chalice
```

### Verification

To make sure `chalice` was installed correctly, run::

```java
$ chalice --version
```

## Create a new Chalice project

Create the new Chalice project for the Todo application.

### Instructions

1.  Create a new Chalice project called `mytodo` with the `new-project`
    command::

```java
$chalice new-project mytodo
```

### Verification

To ensure that the project was created, list the contents of the newly created
`mytodo` directory::

```java
$ ls mytodo
app.py requirements.txt
```

It should contain an `app.py` file and a `requirements.txt` file.

## Add the starting `app.py`

Copy a boilerplate `app.py` file to begin working on the Todo application

### Instructions

1. If you have not already done so, clone the repository for this workshop::

```java
   $ git clone https://github.com/aws-samples/chalice-workshop.git
```

2. Copy the over the `app.py` file to the `mytodo` Chalice application::

```java
   $ cp ../chalice-workshop/code/todo-app/part1/01-new-project/app.py mytodo/app.py
```

### Verification

To verify that the boilerplate application is working correctly, move into
the `mytodo` application directory and run `chalice local` to spin up
a version of the application running locally::

```java
$ cd mytodo
$ chalice local
Serving on localhost:8000
```

In a separate terminal window now install `httpie`::

```java
$ pip install httpie
```

And make an HTTP request to application running the `localhost`::

```java
$ http localhost:8000/todos
HTTP/1.1 200 OK
Content-Length: 2
Content-Type: application/json
Date: Thu, 19 Oct 2017 23:31:12 GMT
Server: BaseHTTP/0.3 Python/2.7.10

[]
```

This should return an empty list back as there are no Todo's currently in
the application.

## Add a route for creating a Todo

Add a route for creating a Todo.

### Instructions

1. Open the `app.py` in an editor of your choice

2. At the bottom of the `app.py` file add a function called
   `add_new_todo()`

3. Decorate the `add_new_todo()` function with a `route` that only
   accepts `POST` to the URI `/todos`.

4. In the `add_new_todo()` function use the `app.current_request.json_body`
   to add the Todo (which includes its description and metadata) to the
   database.

5. In the `add_new_todo()` function `return` the ID of the Todo that was
   added in the database.

```java
@app.route('/todos', methods=['POST'])
def add_new_todo():
    body = app.current_request.json_body
    return get_app_db().add_item(
        description=body['description'],
        metadata=body.get('metadata'),
    )
```

### Verification

To verify that the new route works, run `chalice local` and in a separate
terminal window run the following using `httpie`::

```java
$ echo '{"description": "My first Todo", "metadata": {}}' | http POST localhost:8000/todos
HTTP/1.1 200 OK
Content-Length: 36
Content-Type: application/json
Date: Thu, 19 Oct 2017 23:44:24 GMT
Server: BaseHTTP/0.3 Python/2.7.10

8cc673f0-7dd3-4e9d-a20b-245fcd34859d
```

This will return the ID of the Todo. For this example, it is `8cc673f0-7dd3-4e9d-a20b-245fcd34859d`.
Now check that it is now listed when you retrieve all Todos::

```java
$ http localhost:8000/todos
HTTP/1.1 200 OK
Content-Length: 142
Content-Type: application/json
Date: Thu, 19 Oct 2017 23:46:53 GMT
Server: BaseHTTP/0.3 Python/2.7.10

    [
        {
            "description": "My first Todo",
            "metadata": {},
            "state": "unstarted",
            "uid": "8cc673f0-7dd3-4e9d-a20b-245fcd34859d",
            "username": "default"
        }
    ]
```

## Add a route for getting a specific Todo

Add a route for getting a specific Todo.

### Instructions

1. In the `app.py`, add a function called `get_todo()` that accepts a
   `uid` as a parameter.

2. Decorate the `get_todo()` function with a `route` that only
   accepts `GET` to the URI `/todos/{uid}`.

3. In the `get_todo()` function `return` the specific Todo item from the
   database using the `uid` function parameter.

@app.route('/todos/{uid}', methods=['GET'])
def get_todo(uid):
return get_app_db().get_item(uid)

### Verification

To verify that the new route works, run `chalice local` and in a separate
terminal window run the following using `httpie`::

```java
$ echo '{"description": "My first Todo", "metadata": {}}' | http POST localhost:8000/todos
HTTP/1.1 200 OK
Content-Length: 36
Content-Type: application/json
Date: Thu, 19 Oct 2017 23:44:24 GMT
Server: BaseHTTP/0.3 Python/2.7.10

8cc673f0-7dd3-4e9d-a20b-245fcd34859d
```

Now use the returned ID `8cc673f0-7dd3-4e9d-a20b-245fcd34859d` to request
the specific Todo::

```java
$ http localhost:8000/todos/8cc673f0-7dd3-4e9d-a20b-245fcd34859d
HTTP/1.1 200 OK
Content-Length: 140
Content-Type: application/json
Date: Thu, 19 Oct 2017 23:52:35 GMT
Server: BaseHTTP/0.3 Python/2.7.10

    {
        "description": "My first Todo",
        "metadata": {},
        "state": "unstarted",
        "uid": "8cc673f0-7dd3-4e9d-a20b-245fcd34859d",
        "username": "default"
    }
```

## Add a route for deleting a specific Todo

Add a route for deleting a specific Todo.

### Instructions

1. In the `app.py`, add a function called `delete_todo()` that accepts a
   `uid` as a parameter.

2. Decorate the `delete_todo()` function with a `route` that only
   accepts `DELETE` to the URI `/todos/{uid}`.

3. In the `delete_todo()` function delete the Todo from the database using
   the `uid` function parameter.

```java
@app.route('/todos/{uid}', methods=['DELETE'])
def delete_todo(uid):
    return get_app_db().delete_item(uid)
```

### Verification

To verify that the new route works, run `chalice local` and in a separate
terminal window run the following using `httpie`::

```java
$ echo '{"description": "My first Todo", "metadata": {}}' | http POST localhost:8000/todos
HTTP/1.1 200 OK
Content-Length: 36
Content-Type: application/json
Date: Thu, 19 Oct 2017 23:44:24 GMT
Server: BaseHTTP/0.3 Python/2.7.10

8cc673f0-7dd3-4e9d-a20b-245fcd34859d
```

Now check that it is now listed when you retrieve all Todos::

```java
$ http localhost:8000/todos
HTTP/1.1 200 OK
Content-Length: 142
Content-Type: application/json
Date: Thu, 19 Oct 2017 23:46:53 GMT
Server: BaseHTTP/0.3 Python/2.7.10

    [
        {
            "description": "My first Todo",
            "metadata": {},
            "state": "unstarted",
            "uid": "8cc673f0-7dd3-4e9d-a20b-245fcd34859d",
            "username": "default"
        }
    ]
```

Now use the returned ID `8cc673f0-7dd3-4e9d-a20b-245fcd34859d` to delete
the specific Todo::

```java
$ http DELETE localhost:8000/todos/8cc673f0-7dd3-4e9d-a20b-245fcd34859d
HTTP/1.1 200 OK
Content-Length: 4
Content-Type: application/json
Date: Thu, 19 Oct 2017 23:57:32 GMT
Server: BaseHTTP/0.3 Python/2.7.10

    null
```

Now if all of the Todo's are listed, it will no longer be present::

```java
$ http localhost:8000/todos
HTTP/1.1 200 OK
Content-Length: 2
Content-Type: application/json
Date: Thu, 19 Oct 2017 23:31:12 GMT
Server: BaseHTTP/0.3 Python/2.7.10

[]
```

## Add a route for updating the state of a specific Todo

Add a route for updating the state of a specific Todo.

### Instructions

1. In the `app.py`, add a function called `update_todo()` that accepts a
   `uid` as a parameter.

2. Decorate the `update_todo()` function with a `route` that only
   accepts `PUT` to the URI `/todos/{uid}`.

3. In the `update_todo()` function use the `app.current_request` to update
   the Todo (which includes its description, metadata, and state) in the
   database for the `uid` provided.

```java
@app.route('/todos/{uid}', methods=['PUT'])
def update_todo(uid):
    body = app.current_request.json_body
    get_app_db().update_item(
        uid,
        description=body.get('description'),
        state=body.get('state'),
        metadata=body.get('metadata'))
```

### Verification

To verify that the new route works, run `chalice local` and in a separate
terminal window run the following using `httpie`::

```java
$ echo '{"description": "My first Todo", "metadata": {}}' | http POST localhost:8000/todos
HTTP/1.1 200 OK
Content-Length: 36
Content-Type: application/json
Date: Thu, 19 Oct 2017 23:44:24 GMT
Server: BaseHTTP/0.3 Python/2.7.10

de9a4981-f7fd-4639-97fb-2af247f20d79
```

Now determine the state of this newly added Todo::

```java
$ http localhost:8000/todos/de9a4981-f7fd-4639-97fb-2af247f20d79
HTTP/1.1 200 OK
Content-Length: 140
Content-Type: application/json
Date: Fri, 20 Oct 2017 00:03:26 GMT
Server: BaseHTTP/0.3 Python/2.7.10

    {
        "description": "My first Todo",
        "metadata": {},
        "state": "unstarted",
        "uid": "de9a4981-f7fd-4639-97fb-2af247f20d79",
        "username": "default"
    }
```

Update the `state` of this Todo to `started`::

```java
$ echo '{"state": "started"}' | http PUT localhost:8000/todos/de9a4981-f7fd-4639-97fb-2af247f20d79
HTTP/1.1 200 OK
Content-Length: 4
Content-Type: application/json
Date: Fri, 20 Oct 2017 00:05:07 GMT
Server: BaseHTTP/0.3 Python/2.7.10

    null
```

Ensure that the Todo has the `started` state when described::

```java
$ http localhost:8000/todos/de9a4981-f7fd-4639-97fb-2af247f20d79
HTTP/1.1 200 OK
Content-Length: 138
Content-Type: application/json
Date: Fri, 20 Oct 2017 00:05:54 GMT
Server: BaseHTTP/0.3 Python/2.7.10

    {
        "description": "My first Todo",
        "metadata": {},
        "state": "started",
        "uid": "de9a4981-f7fd-4639-97fb-2af247f20d79",
        "username": "default"
    }
```

## Final Code

When you are done your final code should look like this:

```java
from uuid import uuid4

from chalice import Chalice


app = Chalice(app_name='mytodo')
app.debug = True
_DB = None
DEFAULT_USERNAME = 'default'


class InMemoryTodoDB(object):
    def __init__(self, state=None):
        if state is None:
            state = {}
        self._state = state

    def list_all_items(self):
        all_items = []
        for username in self._state:
            all_items.extend(self.list_items(username))
        return all_items

    def list_items(self, username=DEFAULT_USERNAME):
        return self._state.get(username, {}).values()

    def add_item(self, description, metadata=None, username=DEFAULT_USERNAME):
        if username not in self._state:
            self._state[username] = {}
        uid = str(uuid4())
        self._state[username][uid] = {
            'uid': uid,
            'description': description,
            'state': 'unstarted',
            'metadata': metadata if metadata is not None else {},
            'username': username
        }
        return uid

    def get_item(self, uid, username=DEFAULT_USERNAME):
        return self._state[username][uid]

    def delete_item(self, uid, username=DEFAULT_USERNAME):
        del self._state[username][uid]

    def update_item(self, uid, description=None, state=None,
                    metadata=None, username=DEFAULT_USERNAME):
        item = self._state[username][uid]
        if description is not None:
            item['description'] = description
        if state is not None:
            item['state'] = state
        if metadata is not None:
            item['metadata'] = metadata


def get_app_db():
    global _DB
    if _DB is None:
        _DB = InMemoryTodoDB()
    return _DB


@app.route('/todos', methods=['GET'])
def get_todos():
    return get_app_db().list_items()


@app.route('/todos', methods=['POST'])
def add_new_todo():
    body = app.current_request.json_body
    return get_app_db().add_item(
        description=body['description'],
        metadata=body.get('metadata'),
    )


@app.route('/todos/{uid}', methods=['GET'])
def get_todo(uid):
    return get_app_db().get_item(uid)


@app.route('/todos/{uid}', methods=['DELETE'])
def delete_todo(uid):
    return get_app_db().delete_item(uid)


@app.route('/todos/{uid}', methods=['PUT'])
def update_todo(uid):
    body = app.current_request.json_body
    get_app_db().update_item(
        uid,
        description=body.get('description'),
        state=body.get('state'),
        metadata=body.get('metadata'))
```

# Section 2: Add `chalicelib` to Todo application

Users will learn about chalicelib in this section by moving the
in-memory db out of `app.py` and into `chalicelib/db.py`

Our `app.py` file is getting a little bit crowded, and as our application
grows it's only going to get worse. To solve this problem we can create a
module called `chalicelib` that Chalice will deploy alongside the `app.py`

## Create `chalicelib` module

Let's start this process by moving our database code out of `app.py` and into
`chalicelib`.

### Instructions

1. Create a new `chalicelib` directory alongside the `app.py` file::

```java
   $ mkdir chalicelib
```

2. Since `chalicelib` is a Python module, it must have an `__init__.py`
   file::

```java
   $ touch chalicelib/**init**.py
```

3. Create a `db.py` file where all database interaction code will live::

```java
   $ touch chalicelib/db.py
```

### Verification

The directory structure of your application should now look like this::

```java
$ tree .
.
├── app.py
├── chalicelib
│   ├── __init__.py
│   └── db.py
└── requirements.txt

1 directory, 4 files
```

## Move database code from `app.py` to the `db.py`

Copy `InMemoryTodoDB` class from `app.py` to `chalicelib/db.py`

### Instructions

1. Cut the class `InMemoryTodoDB` out of `app.py` and paste it into
   `chalicelib/db.py` using your favorite editor

2. Move the following lines from `app.py` to `db.py`::

```java
   from uuid import uuid4

   DEFAULT_USERNAME = 'default'
```

### Verification

Lets try running `chalice local` and check a few routes to see if they still
work::

```java
$ echo '{"description": "My first Todo", "metadata": {}}' | http POST localhost:8000/todos
HTTP/1.1 500 Internal Server Error
Content-Length: 459
Content-Type: text/plain
Date: Fri, 20 Oct 2017 20:58:37 GMT
Server: BaseHTTP/0.3 Python/2.7.13

Traceback (most recent call last):
File "/Users/jcarlyl/.envs/workshop/lib/python2.7/site-packages/chalice/app.py", line 649, in \_get_view_function_response
response = view_function(\*\*function_args)
File "/private/tmp/chalice/add-db/app.py", line 24, in add_new_todo
return get_app_db().add_item(
File "/private/tmp/chalice/add-db/app.py", line 12, in get_app_db
\_DB = InMemoryTodoDB()
NameError: global name 'InMemoryTodoDB' is not defined
```

Since `InMemoryTodoDB` has been moved it now needs to be imported.

## Import `InMemoryTodoDB` from chalicelib

Looks like we forgot to import the `InMemoryTodoDB` from `chalicelib`.
Since `InMemoryTodoDB` is now in a different module, we need to import it.

### Instructions

````

1. At the top of `app.py` add the line::

```java
   from chalicelib.db import InMemoryTodoDB
````

### Verification

````

Let's try that last step one more time::

```java
$ echo '{"description": "My first Todo", "metadata": {}}' | \
 http POST localhost:8000/todos
HTTP/1.1 200 OK
Content-Length: 36
Content-Type: application/json
Date: Fri, 20 Oct 2017 21:18:57 GMT
Server: BaseHTTP/0.3 Python/2.7.13

7fc955af-5a9e-42b5-ad3a-8f5017c91091
````

Now that it appears to work again let's finish verifying all the other routes
still work as expected, starting with checking the state::

```java
$ http localhost:8000/todos/7fc955af-5a9e-42b5-ad3a-8f5017c91091
HTTP/1.1 200 OK
Content-Length: 140
Content-Type: application/json
Date: Fri, 20 Oct 2017 21:21:03 GMT
Server: BaseHTTP/0.3 Python/2.7.13

{
"description": "My first Todo",
"metadata": {},
"state": "unstarted",
"uid": "7fc955af-5a9e-42b5-ad3a-8f5017c91091",
"username": "default"
}
```

Update the `state` of this Todo to `started`::

```java
$ echo '{"state": "started"}' | \
 http PUT localhost:8000/todos/7fc955af-5a9e-42b5-ad3a-8f5017c91091
HTTP/1.1 200 OK
Content-Length: 4
Content-Type: application/json
Date: Fri, 20 Oct 2017 21:21:59 GMT
Server: BaseHTTP/0.3 Python/2.7.13

null
```

Check the `state` again to make sure that it is now `started`::

```java
$ http localhost:8000/todos/7fc955af-5a9e-42b5-ad3a-8f5017c91091
HTTP/1.1 200 OK
Content-Length: 138
Content-Type: application/json
Date: Fri, 20 Oct 2017 21:23:16 GMT
Server: BaseHTTP/0.3 Python/2.7.13

{
"description": "My first Todo",
"metadata": {},
"state": "started",
"uid": "7fc955af-5a9e-42b5-ad3a-8f5017c91091",
"username": "default"
}
```

## Final Code

When you are finished your `app.py` file should look like:

```java
from chalice import Chalice
from chalicelib import db

app = Chalice(app_name='mytodo')
app.debug = True
_DB = None


def get_app_db():
    global _DB
    if _DB is None:
        _DB = db.InMemoryTodoDB()
    return _DB


@app.route('/todos', methods=['GET'])
def get_todos():
    return get_app_db().list_items()


@app.route('/todos', methods=['POST'])
def add_new_todo():
    body = app.current_request.json_body
    return get_app_db().add_item(
        description=body['description'],
        metadata=body.get('metadata'),
    )


@app.route('/todos/{uid}', methods=['GET'])
def get_todo(uid):
    return get_app_db().get_item(uid)


@app.route('/todos/{uid}', methods=['DELETE'])
def delete_todo(uid):
    return get_app_db().delete_item(uid)


@app.route('/todos/{uid}', methods=['PUT'])
def update_todo(uid):
    body = app.current_request.json_body
    get_app_db().update_item(
        uid,
        description=body.get('description'),
        state=body.get('state'),
        metadata=body.get('metadata'))
```

And your `chalicelib/db.py` file should look like:

```python
from uuid import uuid4


DEFAULT_USERNAME = 'default'


class InMemoryTodoDB(object):
    def __init__(self, state=None):
        if state is None:
            state = {}
        self._state = state

    def list_all_items(self):
        all_items = []
        for username in self._state:
            all_items.extend(self.list_items(username))
        return all_items

    def list_items(self, username=DEFAULT_USERNAME):
        return self._state.get(username, {}).values()

    def add_item(self, description, metadata=None, username=DEFAULT_USERNAME):
        if username not in self._state:
            self._state[username] = {}
        uid = str(uuid4())
        self._state[username][uid] = {
            'uid': uid,
            'description': description,
            'state': 'unstarted',
            'metadata': metadata if metadata is not None else {},
            'username': username
        }
        return uid

    def get_item(self, uid, username=DEFAULT_USERNAME):
        return self._state[username][uid]

    def delete_item(self, uid, username=DEFAULT_USERNAME):
        del self._state[username][uid]

    def update_item(self, uid, description=None, state=None,
                    metadata=None, username=DEFAULT_USERNAME):
        item = self._state[username][uid]
        if description is not None:
            item['description'] = description
        if state is not None:
            item['state'] = state
        if metadata is not None:
            item['metadata'] = metadata
```

# Section 3: Add a DynamoDB table for Todo application

In this step, we'll replace the in-memory database with an
Amazon DynamoDB table.

## Initial Setup

The starting code for this step is in the `chalice-workshop/code/todo-app/part1/03-add-dynamodb`
file. If necessary, you can copy over those files as a starting point
for this step::

```java
$ cp ../chalice-workshop/code/todo-app/part1/03-add-dynamodb/app.py app.py
$ cp ../chalice-workshop/code/todo-app/part1/03-add-dynamodb/createtable.py createtable.py
$ cp ../chalice-workshop/code/todo-app/part1/03-add-dynamodb/chalicelib/db.py chalicelib/db.py
$ cp ../chalice-workshop/code/todo-app/part1/03-add-dynamodb/.chalice/policy-dev.json .chalice/policy-dev.json
$ cp ../chalice-workshop/code/todo-app/part1/03-add-dynamodb/.chalice/config.json .chalice/config.json
```

## Create a DynamoDB table

In this section, we're going to create a DynamoDB table and
configure chalice to pass in the table name to our application.

1. First, we'll need to install boto3, the AWS SDK for Python.
   Run this command::

```java
$ pip install boto3
```

2. Add boto3 to our requirements.txt file.
   Chalice uses this file when building the deployment package
   for your app::

```java
$ pip freeze | grep boto3 >> requirements.txt
```

3. Now that boto3 is installed, we can create the DynamoDB table
   Run the `createtable.py` script with the `--table-type app` option.
   This will take a few seconds to run. ::

```java
$ python createtable.py --table-type app
```

5. Verify that this script added the table name to the `.chalice/config.json`
   file. You should see a key named `APP_TABLE_NAME` in this file::

```java
$ cat .chalice/config.json
{
"stages": {
"dev": {
"environment_variables": {
"APP_TABLE_NAME": "todo-app-...."
},
"api_gateway_stage": "api"
}
},
"version": "2.0",
"app_name": "testapp"
}
```

6.  Next, we'll add a test route to double check we've configured
    everything correctly. Open the `app.py` file and these import
    lines to the top of the file::

```java
import os
import boto3
```

7.  Add a new test route:

```java
@app.route('/test-ddb')
def test_ddb():
    resource = boto3.resource('dynamodb')
    table = resource.Table(os.environ['APP_TABLE_NAME'])
    return table.name
```

### Verification

1. Start up the local dev server: `chalice local`
2. Make a request to this test route and verify you get a 200 response::

```java
$ http localhost:8000/test-ddb
HTTP/1.1 200 OK
Content-Length: 45
Content-Type: application/json
Server: BaseHTTP/0.3 Python/2.7.14

todo-app-0b116e7b-f0f8-4548-91d8-95c75898b8b6
```

## Switching the `InMemoryTodoDB` to a `DynamoDBTodo`

Now that we've verified our DynamoDB table is plumbed into our
chalice app correctly, we can update to use a new `DynamoDBTodo`
backend instead of the `InMemoryTodoDB`.

The `chalicelib/db.py` file you copied from
`code/todo-app/part1/03-add-dynamodb/chalicelib/db.py` has a new `DynamoDBTodo`
class. This has the same interface as `InMemoryTodoDB` except that is uses
DynamoDB as the backend. We're going to update our `app.py` to use this new
class.

1.  Remove the `@app.route('/test-ddb')` view function. We
    no longer need it now that we've verified that DynamoDB is correctly
    configured for our app.

2.  Go to the `get_app_db()` function in your `app.py` file. Modify
    this function to use the `DynamoDBTodo` backend:

```java
def get_app_db():
    global _DB
    if _DB is None:
        _DB = db.DynamoDBTodo(
            boto3.resource('dynamodb').Table(
                os.environ['APP_TABLE_NAME'])
        )
    return _DB
```

3.  Go to the top of the `app.py` file. Modify the line `from chalicelib.db import InMemoryTodoDB` to reference `db` instead:

```java
from chalicelib import db
```

### Verification

````

1. Start up the local dev server `chalice local`

2. Create a Todo item::

```java
$ echo '{"description": "My first Todo", "metadata": {}}' | \
 http POST localhost:8000/todos
HTTP/1.1 200 OK
Content-Length: 36
Content-Type: application/json
Date: Thu, 19 Oct 2017 23:44:24 GMT
Server: BaseHTTP/0.3 Python/2.7.10

    de9a4981-f7fd-4639-97fb-2af247f20d79
````

3. Retrieve the Todo item you just created. Keep in mind that your UID will be
   different from what's shown below::

```java
$ http localhost:8000/todos/de9a4981-f7fd-4639-97fb-2af247f20d79
HTTP/1.1 200 OK
Content-Length: 140
Content-Type: application/json
Date: Fri, 20 Oct 2017 00:03:26 GMT
Server: BaseHTTP/0.3 Python/2.7.10

    {
        "description": "My first Todo",
        "metadata": {},
        "state": "unstarted",
        "uid": "de9a4981-f7fd-4639-97fb-2af247f20d79",
        "username": "default"
    }
```

## Deploy your app

1. Now that we've tested locally, we're ready to deploy::

```java
$ chalice deploy
```

### Verification

````

1. First create a Todo item using the API Gateway endpoint::

```java
$ chalice url
https://your-chalice-url/
$ echo '{"description": "My second Todo", "metadata": {}}' | \
http POST https://your-chalice-url/todos
HTTP/1.1 200 OK
Content-Length: 36
Content-Type: application/json

abcdefg-abcdefg
````

2. Verify you can retrieve this item::

```java
$ http https://your-chalice-url/todos/abcdefg-abcdefg
HTTP/1.1 200 OK
Content-Length: 140
Content-Type: application/json

{
"description": "My second Todo",
"metadata": {},
"state": "unstarted",
"uid": "abcdefg-abcdefg",
"username": "default"
}
```

# Section 4: Add authorization to Todo application

If you had noticed from the previous steps, there was a `username` field
for all of the Todos, but the `username` was always set to `default`.
This step will be utilizing the `username` field by exposing the notion
of users and authorization in the Todo application. For this section, we will
be doing the following to add authorization and users to the application:

## Install PyJWT

For authorization, the application is going to be relying on JWT. To depend
on JWT, in the Chalice application `PyJWT` needs to be installed and added
to our `requirements.txt` file.

### Instructions

1. Add `PyJWT` to your `requirements.txt` file::

```java
$ echo PyJWT==1.6.1 >> requirements.txt
```

2. Make sure it is now installed in your virtualenv::

```java
$ pip install -r requirements.txt
```

### Verification

To ensure that it was installed, open the Python REPL and try to import
the `PyJWT` library::

```java
$ python
Python 2.7.10 (default, Mar 10 2016, 09:55:31)
[GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
Type "help", "copyright", "credits" or "license" for more information. >>> import jwt
```

## Copy over auth specific files

In order to add authentication to your Chalice application we have provided a few
files that help with some of the low-level details. We have added an `auth.py` file
to `chalicelib` which abstracts away some of the details of handling JWT tokens. We
have also added a `users.py` script which is a command line utility for creating and
managing a user table.

### Instructions

1. Copy in the `chalice-workshop/code/todo-app/part1/04-add-auth/chalicelib/auth.py`
   file::

```java
$ cp ../chalice-workshop/code/todo-app/part1/04-add-auth/chalicelib/auth.py chalicelib/auth.py
```

2. Copy over the `chalice-workshop/code/todo-app/part1/04-add-auth/users.py` script for
   creating users::

```java
$ cp ../chalice-workshop/code/todo-app/part1/04-add-auth/users.py users.py
```

### Verification

From within the `mytodo` directory of your Todo Chalice application, the
structure should be the following::

```java
$ tree
.
├── app.py
├── chalicelib
│   ├── __init__.py
│   ├── auth.py
│   └── db.py
├── createtable.py
├── requirements.txt
└── users.py
```

## Create a DynamoDB user table

Using the `createtable.py` script, this will create another DynamoDB table
for storing users to use in the Chalice application.

### Instructions

1. Run the `createtable.py` script to create the DynamoDB table::

```java
$ python createtable.py -t users
```

### Verification

````

Check that the return code of the command is `0`::

```java
$ echo $?
0
````

Also `cat` the `.chalice/config.json` to make sure the `USERS_TABLE_NAME`
shows up as an environment variable::

```java
$ cat .chalice/config.json
{
"stages": {
"dev": {
"environment_variables": {
"USERS_TABLE_NAME": "users-app-21658b12-517e-4441-baef-99b8fc2f0b61",
"APP_TABLE_NAME": "todo-app-323ca4c3-54fb-4e49-a584-c52625e5d85d"
},
"autogen_policy": false,
"api_gateway_stage": "api"
}
},
"version": "2.0",
"app_name": "mytodo"
}
```

## Add a user to the user table

Using the `users.py` script, create a new user in your users database to
use with your chalice application.

### Instructions

1. Run the `users.py` script with the `-c` argument to create a user. You
   will be prompted for a username and a password::

```java
$ python users.py -c
Username: user
Password:
```

### Verification

Using the `users.py` script, make sure that the user is listed in your
database::

```java
$ python users.py -l
user
```

Also make sure that the password is correct by testing the username and
password with the `users.py` script::

```java
$ python users.py -t
Username: user
Password:
Password verified.
```

You can also test an incorrect password. You should see this output::

```java
$ python users.py -t
Username: user
Password:
Password ### Verification failed.
```

## Create `get_users_db` function

Now that we have created a DynamoDB user table, we will create a convenience function
for loading it.

### Instructions

1. Add a new variable `_USER_DB` in your `app.py` file with a value of None:

```java
    app = Chalice(app_name='mytodo')
    app.debug = True
    _DB = None
    # This is the new value you're adding.
    _USER_DB = None
```

2. Create a function for fetching our current database table for users. Similar to the
   function that gets the app table. Add this function to your `app.py` file:

```java
def get_users_db():
    global _USER_DB
    if _USER_DB is None:
        _USER_DB = boto3.resource('dynamodb').Table(
            os.environ['USERS_TABLE_NAME'])
    return _USER_DB
```

## Create a login route

We will now create a login route where users can trade their username/password for a
JWT token.

### Instructions

1. Define a new Chalice route `/login` that accepts the POST method and grabs the
   `username` and `password` from the request, and forwards it along to a helper
   function in the `auth` code you copied in earlier which will trade those for a
   JWT token.

```java
@app.route('/login', methods=['POST'])
def login():
    body = app.current_request.json_body
    record = get_users_db().get_item(
        Key={'username': body['username']})['Item']
    jwt_token = auth.get_jwt_token(
        body['username'], body['password'], record)
    return {'token': jwt_token}
```

2. Notice the above code snippit uses the `auth` file that we copied into our
   chalicelib directory at the beginning of this step. Add the following
   import statement to the top of `app.py` so we can use it::

```java
   from chalicelib import auth
```

### Verification

1. Start up a local server using `chalice local`.

2. Using the username and password generated previously, run `chalice local`
   and make an HTTP `POST` request to the `/login` URI::

```java
$ echo '{"username": "user", "password": "password"}' | \
 http POST localhost:8000/login
HTTP/1.1 200 OK
Content-Length: 218
Content-Type: application/json
Date: Fri, 20 Oct 2017 22:48:42 GMT
Server: BaseHTTP/0.3 Python/2.7.10

    {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1MDg1Mzk3MjIsImp0aSI6IjI5ZDJhNmFkLTdlY2YtNDYzZC1iOTY1LTk0M2VhNzU0YWMzYyIsInN1YiI6InVzZXIiLCJuYmYiOjE1MDg1Mzk3MjJ9.95hlpRWARK95aYCh0YE7ls_cvraoenNux8gmIy8vQU8"
    }
```

This should return a JWT to use as an `Authorization` header for that user.

## Create a custom authorizer and attach to a route

To add authorization to our app we will start by defining an authorizer and
attaching it to one of our routes.

### Instructions

1. Create an authorizer function that checks the validity of a JWT token using the
   existing code in the `auth.py` file we copied earlier. If the token is valid
   (didn't throw an error) we will return a policy that allows access to all of our
   routes, and sets the `principal_id` to the username in the JWT token.

2. Once we have defined the authorizer, we will attach it to the `get_todos` route.

```java
@app.authorizer()
def jwt_auth(auth_request):
    token = auth_request.token
    decoded = auth.decode_jwt_token(token)
    return AuthResponse(routes=['*'], principal_id=decoded['sub'])
```

```java
@app.route('/todos', methods=['GET'], authorizer=jwt_auth)
def get_todos():
```

Also make sure to import the `AuthResponse` class at the top of the `app.py` file:

```java
from chalice import AuthResponse
```

### Verification

1. Start the local dev server `chalice local`

2. Try to get the todo, the request should be rejected without authorization::

```java
$ http localhost:8000/todos
HTTP/1.1 401 Unauthorized
Content-Length: 26
Content-Type: application/json
Date: Tue, 24 Oct 2017 02:50:50 GMT
Server: BaseHTTP/0.3 Python/2.7.13
x-amzn-ErrorType: UnauthorizedException
x-amzn-RequestId: 297d1da8-b9a8-4824-a1f3-293607aac715

    {
    "message": "Unauthorized"
    }
```

3. Try the same call again but with your authorization token passed in the
   `Authorization` header::

```java
$ http localhost:8000/todos \
 Authorization:eyJhbGciOi.... really long token here...
Content-Length: 137
Content-Type: application/json
Date: Tue, 24 Oct 2017 02:50:43 GMT
Server: BaseHTTP/0.3 Python/2.7.13

    [
    {
        "description": "My first Todo",
        "metadata": {},
        "state": "unstarted",
        "uid": "f9a992d6-41c0-45a6-84b8-e7239f7d7100",
        "username": "john"
    }
    ]
```

## Attach authorizer to the rest of the routes

Now attach the authorizer to all the other routes except the `login` route.

### Instructions

1. Attach the `jwt_auth` authorizer to the `add_new_todo` route.

2. Attach the `jwt_auth` authorizer to the `get_todo` route.

3. Attach the `jwt_auth` authorizer to the `delete_todo` route.

4. Attach the `jwt_auth` authorizer to the `update_todo` route.

```java
@app.route('/todos', methods=['POST'], authorizer=jwt_auth)
def add_new_todo():
```

```java
@app.route('/todos/{uid}', methods=['GET'], authorizer=jwt_auth)
def get_todo(uid):
```

```java
@app.route('/todos/{uid}', methods=['DELETE'], authorizer=jwt_auth)
def delete_todo(uid):
```

```java
@app.route('/todos/{uid}', methods=['PUT'], authorizer=jwt_auth)
def update_todo(uid):
```

### Verification

1. Start up the local dev server `chalice local`

2. Try each route without an authorization token. You should get a `401`
   Unauthorized response::

```java
$ echo '{"description": "My first Todo", "metadata": {}}' | \
 http POST localhost:8000/todos
HTTP/1.1 401 Unauthorized
Content-Length: 26
Content-Type: application/json
Date: Tue, 24 Oct 2017 03:14:14 GMT
Server: BaseHTTP/0.3 Python/2.7.13
x-amzn-ErrorType: UnauthorizedException
x-amzn-RequestId: 58c2d520-07e6-4535-b034-aaba41bab8ab

    {
    "message": "Unauthorized"
    }

```

```java
$ http GET localhost:8000/todos/fake-id
HTTP/1.1 401 Unauthorized
Content-Length: 26
Content-Type: application/json
Date: Tue, 24 Oct 2017 03:15:10 GMT
Server: BaseHTTP/0.3 Python/2.7.13
x-amzn-ErrorType: UnauthorizedException
x-amzn-RequestId: b2304a70-ff8d-453f-b119-10e75326463a

    {
    "message": "Unauthorized"
    }
```

```java
$ http DELETE localhost:8000/todos/fake-id
HTTP/1.1 401 Unauthorized
Content-Length: 26
Content-Type: application/json
Date: Tue, 24 Oct 2017 03:17:10 GMT
Server: BaseHTTP/0.3 Python/2.7.13
x-amzn-ErrorType: UnauthorizedException
x-amzn-RequestId: 69419241-b244-462b-b108-72091f7d7b5b

    {
    "message": "Unauthorized"
    }

```

```java
$ echo '{"state": "started"}' | http PUT localhost:8000/todos/fake-id
HTTP/1.1 401 Unauthorized
Content-Length: 26
Content-Type: application/json
Date: Tue, 24 Oct 2017 03:18:59 GMT
Server: BaseHTTP/0.3 Python/2.7.13
x-amzn-ErrorType: UnauthorizedException
x-amzn-RequestId: edc77f3d-3d3d-4a29-850a-502f21aeed96

    {
    "message": "Unauthorized"
    }
```

3. Now try to create, get, update, and delete a todo from your application by
   using the `Authorization` header in all your requests::

```java
$ echo '{"description": "My first Todo", "metadata": {}}' | \
 http POST localhost:8000/todos Authorization:eyJhbG... auth token ...
HTTP/1.1 200 OK
Content-Length: 36
Content-Type: application/json
Date: Tue, 24 Oct 2017 03:24:28 GMT
Server: BaseHTTP/0.3 Python/2.7.13

     93dbabdb-3b2f-4029-845b-7754406c494f
```

```java
$ echo '{"state": "started"}' | \
 http PUT localhost:8000/todos/93dbabdb-3b2f-4029-845b-7754406c494f \
 Authorization:eyJhbG... auth token ...
HTTP/1.1 200 OK
Content-Length: 4
Content-Type: application/json
Date: Tue, 24 Oct 2017 03:25:28 GMT
Server: BaseHTTP/0.3 Python/2.7.13

     null
```

```java
$ http localhost:8000/todos/93dbabdb-3b2f-4029-845b-7754406c494f \
 Authorization:eyJhbG... auth token ...
HTTP/1.1 200 OK
Content-Length: 135
Content-Type: application/json
Date: Tue, 24 Oct 2017 03:26:29 GMT
Server: BaseHTTP/0.3 Python/2.7.13

     {
     "description": "My first Todo",
     "metadata": {},
     "state": "started",
     "uid": "93dbabdb-3b2f-4029-845b-7754406c494f",
     "username": "default"
     }
```

```java
$ http DELETE localhost:8000/todos/93dbabdb-3b2f-4029-845b-7754406c494f \
 Authorization:eyJhbG... auth token ...
HTTP/1.1 200 OK
Content-Length: 4
Content-Type: application/json
Date: Tue, 24 Oct 2017 03:27:10 GMT
Server: BaseHTTP/0.3 Python/2.7.13

     null
```

## Use authorizer provided username

Now that we have authorizers hooked up to all our routes we can use that
instead of relying on the default user of `default`.

### Instructions

1. First create a function named `get_authorized_username` that will be used
   to convert the information we have in our `current_request` into a
   username.

```java
def get_authorized_username(current_request):
    return current_request.context['authorizer']['principalId']
```

2. Now we need to update each function that interacts with our database to
   calculate the `username` and pass it to the `xxx_item` method.

```java
@app.route('/todos', methods=['GET'], authorizer=jwt_auth)
def get_todos():
    username = get_authorized_username(app.current_request)
    return get_app_db().list_items(username=username)


@app.route('/todos', methods=['POST'], authorizer=jwt_auth)
def add_new_todo():
    body = app.current_request.json_body
    username = get_authorized_username(app.current_request)
    return get_app_db().add_item(
        username=username,
        description=body['description'],
        metadata=body.get('metadata'),
    )


@app.route('/todos/{uid}', methods=['GET'], authorizer=jwt_auth)
def get_todo(uid):
    username = get_authorized_username(app.current_request)
    return get_app_db().get_item(uid, username=username)


@app.route('/todos/{uid}', methods=['DELETE'], authorizer=jwt_auth)
def delete_todo(uid):
    username = get_authorized_username(app.current_request)
    return get_app_db().delete_item(uid, username=username)


@app.route('/todos/{uid}', methods=['PUT'], authorizer=jwt_auth)
def update_todo(uid):
    body = app.current_request.json_body
    username = get_authorized_username(app.current_request)
    get_app_db().update_item(
        uid,
        description=body.get('description'),
        state=body.get('state'),
        metadata=body.get('metadata'),
        username=username)
```

### Verification

1. Spin up the local Chalice server with `chalice local`.

2. Create a new todo and pass in your auth token::

```java
$ echo '{"description": "a todo", "metadata": {}}' | \
 http POST localhost:8000/todos Authorization:eyJhbG... auth token ...
HTTP/1.1 200 OK
Content-Length: 36
Content-Type: application/json
Date: Tue, 24 Oct 2017 04:16:57 GMT
Server: BaseHTTP/0.3 Python/2.7.13

     71048cc2-8583-41e5-9dfe-b9669d15af7d
```

3. List your todos using the get_todos route::

```java
$ http localhost:8000/todos Authorization:eyJhbG... auth token ...
HTTP/1.1 200 OK
Content-Length: 132
Content-Type: application/json
Date: Tue, 24 Oct 2017 04:21:58 GMT
Server: BaseHTTP/0.3 Python/2.7.13

     [
     {
         "description": "a todo",
         "metadata": {},
         "state": "unstarted",
         "uid": "7212a932-769b-4a19-9531-a950db7006a5",
         "username": "john"
     }
     ]
```

4. Notice that now the username is no longer `default` it should be whatever username
   went with the auth token you supplied.

5. Try making a new user with `python users.py -c` and then get their JWT token
   by calling the login route with their credentials.

6. Call the same route as above as the new user by passing in their JWT token in the
   `Authorization` header. They should get no todos since they have not created any
   yet::

```java
   http localhost:8000/todos 'Authorization:...the other auth token...'
   HTTP/1.1 200 OK
   Content-Length: 2
   Content-Type: application/json
   Date: Tue, 24 Oct 2017 04:25:56 GMT
   Server: BaseHTTP/0.3 Python/2.7.13

   []
```

## Deploying your authorizer code

Now that we have it working locally lets deploy it and verify that it still works.

### Instructions

1. `chalice deploy` your app.

### Verification

1. Try the same two calls above against the real API Gateway endpoint you get from your
   deploy instead of the localhost endpoint. If you lose your endpoint you can run
   `chalice url` which will print out your API Gateway endpoint::

```java
$ http <your endpoint here>/todos \
 Authorization:...auth token that has no todos...
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 2
Content-Type: application/json
Date: Tue, 24 Oct 2017 04:43:20 GMT
Via: 1.1 cff9911a0035fa608bcaa4e9709161b3.cloudfront.net (CloudFront)
X-Amz-Cf-Id: bunfoZShHff_f3AqBPS2d5Ae3ymqgBusANDP9G6NvAZB3gOfr1IsVA==
X-Amzn-Trace-Id: sampled=0;root=1-59f01668-388cc9fa3db607662c2d623c
X-Cache: Miss from cloudfront
x-amzn-RequestId: 06de2818-b93f-11e7-bbb0-b760b41808da

     []
```

```java
$ http <your endpoint here>/todos \
 Authorization:...auth token that has a todo...
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 132
Content-Type: application/json
Date: Tue, 24 Oct 2017 04:43:45 GMT
Via: 1.1 a05e153e17e2a6485edf7bf733e131a4.cloudfront.net (CloudFront)
X-Amz-Cf-Id: wR_7Bp4KglDjF41_9TNxXmc3Oiu2kll5XS1sTCCP_LD1kMC3C-nqOA==
X-Amzn-Trace-Id: sampled=0;root=1-59f01681-bb8ce2d74dc0c6f8fe095f9d
X-Cache: Miss from cloudfront
x-amzn-RequestId: 155f88f7-b93f-11e7-b351-775deacbeb7a

     [
     {
         "description": "a todo",
         "metadata": {},
         "state": "unstarted",
         "uid": "7212a932-769b-4a19-9531-a950db7006a5",
         "username": "john"
     }
     ]
```

## Final Code

When you are finished your `app.py` file should look like:

```java
import os

import boto3
from chalice import Chalice, AuthResponse
from chalicelib import auth, db


app = Chalice(app_name='mytodo')
app.debug = True
_DB = None
_USER_DB = None


@app.route('/login', methods=['POST'])
def login():
    body = app.current_request.json_body
    record = get_users_db().get_item(
        Key={'username': body['username']})['Item']
    jwt_token = auth.get_jwt_token(
        body['username'], body['password'], record)
    return {'token': jwt_token}


@app.authorizer()
def jwt_auth(auth_request):
    token = auth_request.token
    decoded = auth.decode_jwt_token(token)
    return AuthResponse(routes=['*'], principal_id=decoded['sub'])


def get_users_db():
    global _USER_DB
    if _USER_DB is None:
        _USER_DB = boto3.resource('dynamodb').Table(
            os.environ['USERS_TABLE_NAME'])
    return _USER_DB


# Rest API code


def get_app_db():
    global _DB
    if _DB is None:
        _DB = db.DynamoDBTodo(
            boto3.resource('dynamodb').Table(
                os.environ['APP_TABLE_NAME'])
        )
    return _DB


def get_authorized_username(current_request):
    return current_request.context['authorizer']['principalId']


@app.route('/todos', methods=['GET'], authorizer=jwt_auth)
def get_todos():
    username = get_authorized_username(app.current_request)
    return get_app_db().list_items(username=username)


@app.route('/todos', methods=['POST'], authorizer=jwt_auth)
def add_new_todo():
    body = app.current_request.json_body
    username = get_authorized_username(app.current_request)
    return get_app_db().add_item(
        username=username,
        description=body['description'],
        metadata=body.get('metadata'),
    )


@app.route('/todos/{uid}', methods=['GET'], authorizer=jwt_auth)
def get_todo(uid):
    username = get_authorized_username(app.current_request)
    return get_app_db().get_item(uid, username=username)


@app.route('/todos/{uid}', methods=['DELETE'], authorizer=jwt_auth)
def delete_todo(uid):
    username = get_authorized_username(app.current_request)
    return get_app_db().delete_item(uid, username=username)


@app.route('/todos/{uid}', methods=['PUT'], authorizer=jwt_auth)
def update_todo(uid):
    body = app.current_request.json_body
    username = get_authorized_username(app.current_request)
    get_app_db().update_item(
        uid,
        description=body.get('description'),
        state=body.get('state'),
        metadata=body.get('metadata'),
        username=username)
```
