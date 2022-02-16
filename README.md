# AWS Chalice Workshop

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
instructions on how to go about building your very first Chalice application
running on AWS Lambda. Steps include:

## Create a virtualenv and install Chalice

To start using Chalice, you will need a new virtualenv with Chalice installed.

### Instructions

Make sure you have Python 3 installed. See the :doc:`env-setup` page for
instructions on how to install Python.

1. Create a new virtualenv called `chalice-env` by running the following
   command::

```
       $ python3 -m venv chalice-env
```

2. Activate your newly created virtualenv::

```
       $ source chalice-env/bin/activate
```

If you are using a Windows environment, you will have to run::

```
       > .\chalice-env\Scripts\activate
```

3. Install `chalice` using `pip`::

```
       $ pip install chalice
```

### Verification

```

1. To check that `chalice` was installed, run::

```

$ chalice --version
chalice 1.6.0, python 3.7.3, darwin 15.6.0

```

   The version of `chalice` must be version `1.6.0` or higher and the
   version of Python should be 3.7.

## Create a new Chalice application

With `chalice` now installed, it is time to create your first Chalice
application.

### Instructions


1. Run the ``chalice new-project`` command to create a project called
   ``workshop-intro``::

```

       $ chalice new-project workshop-intro

```


### Verification
```

1. A new `workshop-intro` directory should have been created on your behalf.
   Inside of the `workshop-intro` directory, you should have two files: an
   `app.py` file and a `requirements.txt` file::

```
   $ ls workshop-intro
   app.py requirements.txt
```

## Hello world Lambda function

Let's create our first Lambda function and deploy it using Chalice.

### Instructions

1. Change directories to your newly created `workshop-intro` directory::

```
    $ cd workshop-intro
```

2. Open the `app.py` file and delete **all** lines of code underneath
   the line: `app = Chalice(app_name='workshop-intro')`. Your `app.py` file
   should only consist of the following lines::

```
    from chalice import Chalice

    app = Chalice(app_name='workshop-intro')
```

3. Add a new function `hello_world` decorated by
   `app.lambda_function() <https://chalice.readthedocs.io/en/latest/api.html#Chalice.lambda_function>`\_\_
   that returns `{"hello": "world"}`. Your `app.py` file should now consist
   of the following lines::

```
    from chalice import Chalice

    app = Chalice(app_name='workshop-intro')

    @app.lambda_function()
    def hello_world(event, context):
        return {'hello': 'world'}
```

4. Run `chalice deploy` to deploy your Chalice application to AWS Lambda::

```
    $ chalice deploy
    Creating deployment package.
    Creating IAM role: workshop-intro-dev
    Creating lambda function: workshop-intro-dev-hello_world
    Resources deployed:
      - Lambda ARN: arn:aws:lambda:us-west-2:123456789123:function:workshop-intro-dev-hello_world
```

### Verification

```

1. Run the `chalice invoke` command to invoke your newly deployed
   `hello_world` Lambda function::

```

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


1. Create an additional Lambda function ``hello_name`` using the
   ``app.lambda_function()`` decorator. The function should retrieve the
   value of the ``name`` key in the ``event`` parameter and return
   ``{'hello': name}``::

```

    @app.lambda_function()
    def hello_name(event, context):
        name = event['name']
        return {'hello': name}

```

   Your ``app.py`` file should now consist of the following lines::

```

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


2. Run ``chalice deploy`` to deploy your Chalice application with the
   new Lambda function::

```

    $ chalice deploy
    Creating deployment package.
    Creating IAM role: workshop-intro-dev
    Creating lambda function: workshop-intro-dev-hello_world
    Resources deployed:
      - Lambda ARN: arn:aws:lambda:us-west-2:123456789123:function:workshop-intro-dev-hello_world
      - Lambda ARN: arn:aws:lambda:us-west-2:123456789123:function:workshop-intro-dev-hello_name

```


### Verification
```

1. Run `chalice invoke` to invoke the `hello_name` Lambda function with
   `{"name": "Kyle"}` as the event payload::

```
   $ echo '{"name": "Kyle"}' | chalice invoke -n hello_name
   {"hello": "Kyle"}
```

2. It is also possible for your Lambda function to encounter runtime errors.
   Passing in an empty event payload when invoking the `hello_name` will
   result in the Lambda Function returning a Traceback::

```
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

```
   $ chalice delete
   Deleting function: arn:aws:lambda:us-west-2:123456789123:function:workshop-intro-dev-hello_name
   Deleting function: arn:aws:lambda:us-west-2:123456789123:function:workshop-intro-dev-hello_world
   Deleting IAM role: workshop-intro-dev
```

### Validation

1. Try running `chalice invoke` on the previously deployed Lambda functions::

```
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
