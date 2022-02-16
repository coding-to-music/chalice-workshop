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
