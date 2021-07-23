'''
# AWS Cloud Development Kit Core Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

This library includes the basic building blocks of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) (AWS CDK). It defines the core classes that are used in the rest of the
AWS Construct Library.

See the [AWS CDK Developer
Guide](https://docs.aws.amazon.com/cdk/latest/guide/home.html) for
information of most of the capabilities of this library. The rest of this
README will only cover topics not already covered in the Developer Guide.

<!--BEGIN CORE DOCUMENTATION-->

## Stacks and Stages

A `Stack` is the smallest physical unit of deployment, and maps directly onto
a CloudFormation Stack. You define a Stack by defining a subclass of `Stack`
-- let's call it `MyStack` -- and instantiating the constructs that make up
your application in `MyStack`'s constructor. You then instantiate this stack
one or more times to define different instances of your application. For example,
you can instantiate it once using few and cheap EC2 instances for testing,
and once again using more and bigger EC2 instances for production.

When your application grows, you may decide that it makes more sense to split it
out across multiple `Stack` classes. This can happen for a number of reasons:

* You could be starting to reach the maximum number of resources allowed in a single
  stack (this is currently 500).
* You could decide you want to separate out stateful resources and stateless resources
  into separate stacks, so that it becomes easy to tear down and recreate the stacks
  that don't have stateful resources.
* There could be a single stack with resources (like a VPC) that are shared
  between multiple instances of other stacks containing your applications.

As soon as your conceptual application starts to encompass multiple stacks,
it is convenient to wrap them in another construct that represents your
logical application. You can then treat that new unit the same way you used
to be able to treat a single stack: by instantiating it multiple times
for different instances of your application.

You can define a custom subclass of `Construct`, holding one or more
`Stack`s, to represent a single logical instance of your application.

As a final note: `Stack`s are not a unit of reuse. They describe physical
deployment layouts, and as such are best left to application builders to
organize their deployments with. If you want to vend a reusable construct,
define it as a subclasses of `Construct`: the consumers of your construct
will decide where to place it in their own stacks.

## Nested Stacks

[Nested stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html) are stacks created as part of other stacks. You create a nested stack within another stack by using the `NestedStack` construct.

As your infrastructure grows, common patterns can emerge in which you declare the same components in multiple templates. You can separate out these common components and create dedicated templates for them. Then use the resource in your template to reference other templates, creating nested stacks.

For example, assume that you have a load balancer configuration that you use for most of your stacks. Instead of copying and pasting the same configurations into your templates, you can create a dedicated template for the load balancer. Then, you just use the resource to reference that template from within other templates.

The following example will define a single top-level stack that contains two nested stacks: each one with a single Amazon S3 bucket:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
class MyNestedStack(cfn.NestedStack):
    def __init__(self, scope, id, *, parameters=None, timeout=None, notifications=None):
        super().__init__(scope, id, parameters=parameters, timeout=timeout, notifications=notifications)

        s3.Bucket(self, "NestedBucket")

class MyParentStack(Stack):
    def __init__(self, scope, id, *, description=None, env=None, stackName=None, tags=None, synthesizer=None, terminationProtection=None, analyticsReporting=None):
        super().__init__(scope, id, description=description, env=env, stackName=stackName, tags=tags, synthesizer=synthesizer, terminationProtection=terminationProtection, analyticsReporting=analyticsReporting)

        MyNestedStack(self, "Nested1")
        MyNestedStack(self, "Nested2")
```

Resources references across nested/parent boundaries (even with multiple levels of nesting) will be wired by the AWS CDK
through CloudFormation parameters and outputs. When a resource from a parent stack is referenced by a nested stack,
a CloudFormation parameter will automatically be added to the nested stack and assigned from the parent; when a resource
from a nested stack is referenced by a parent stack, a CloudFormation output will be automatically be added to the
nested stack and referenced using `Fn::GetAtt "Outputs.Xxx"` from the parent.

Nested stacks also support the use of Docker image and file assets.

## Accessing resources in a different stack

You can access resources in a different stack, as long as they are in the
same account and AWS Region. The following example defines the stack `stack1`,
which defines an Amazon S3 bucket. Then it defines a second stack, `stack2`,
which takes the bucket from stack1 as a constructor property.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
prod = {"account": "123456789012", "region": "us-east-1"}

stack1 = StackThatProvidesABucket(app, "Stack1", env=prod)

# stack2 will take a property { bucket: IBucket }
stack2 = StackThatExpectsABucket(app, "Stack2",
    bucket=stack1.bucket,
    env=prod
)
```

If the AWS CDK determines that the resource is in the same account and
Region, but in a different stack, it automatically synthesizes AWS
CloudFormation
[Exports](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-exports.html)
in the producing stack and an
[Fn::ImportValue](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html)
in the consuming stack to transfer that information from one stack to the
other.

### Removing automatic cross-stack references

The automatic references created by CDK when you use resources across stacks
are convenient, but may block your deployments if you want to remove the
resources that are referenced in this way. You will see an error like:

```text
Export Stack1:ExportsOutputFnGetAtt-****** cannot be deleted as it is in use by Stack1
```

Let's say there is a Bucket in the `stack1`, and the `stack2` references its
`bucket.bucketName`. You now want to remove the bucket and run into the error above.

It's not safe to remove `stack1.bucket` while `stack2` is still using it, so
unblocking yourself from this is a two-step process. This is how it works:

DEPLOYMENT 1: break the relationship

* Make sure `stack2` no longer references `bucket.bucketName` (maybe the consumer
  stack now uses its own bucket, or it writes to an AWS DynamoDB table, or maybe you just
  remove the Lambda Function altogether).
* In the `stack1` class, call `this.exportValue(this.bucket.bucketName)`. This
  will make sure the CloudFormation Export continues to exist while the relationship
  between the two stacks is being broken.
* Deploy (this will effectively only change the `stack2`, but it's safe to deploy both).

DEPLOYMENT 2: remove the resource

* You are now free to remove the `bucket` resource from `stack1`.
* Don't forget to remove the `exportValue()` call as well.
* Deploy again (this time only the `stack1` will be changed -- the bucket will be deleted).

## Durations

To make specifications of time intervals unambiguous, a single class called
`Duration` is used throughout the AWS Construct Library by all constructs
that that take a time interval as a parameter (be it for a timeout, a
rate, or something else).

An instance of Duration is constructed by using one of the static factory
methods on it:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
Duration.seconds(300)# 5 minutes
Duration.minutes(5)# 5 minutes
Duration.hours(1)# 1 hour
Duration.days(7)# 7 days
Duration.parse("PT5M")
```

## Size (Digital Information Quantity)

To make specification of digital storage quantities unambiguous, a class called
`Size` is available.

An instance of `Size` is initialized through one of its static factory methods:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
Size.kibibytes(200)# 200 KiB
Size.mebibytes(5)# 5 MiB
Size.gibibytes(40)# 40 GiB
Size.tebibytes(200)# 200 TiB
Size.pebibytes(3)
```

Instances of `Size` created with one of the units can be converted into others.
By default, conversion to a higher unit will fail if the conversion does not produce
a whole number. This can be overridden by unsetting `integral` property.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
Size.mebibytes(2).to_kibibytes()# yields 2048
Size.kibibytes(2050).to_mebibytes(rounding=SizeRoundingBehavior.FLOOR)
```

## Secrets

To help avoid accidental storage of secrets as plain text, we use the `SecretValue` type to
represent secrets. Any construct that takes a value that should be a secret (such as
a password or an access key) will take a parameter of type `SecretValue`.

The best practice is to store secrets in AWS Secrets Manager and reference them using `SecretValue.secretsManager`:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
secret = SecretValue.secrets_manager("secretId",
    json_field="password", # optional: key of a JSON field to retrieve (defaults to all content),
    version_id="id", # optional: id of the version (default AWSCURRENT)
    version_stage="stage"
)
```

Using AWS Secrets Manager is the recommended way to reference secrets in a CDK app.
`SecretValue` also supports the following secret sources:

* `SecretValue.plainText(secret)`: stores the secret as plain text in your app and the resulting template (not recommended).
* `SecretValue.ssmSecure(param, version)`: refers to a secret stored as a SecureString in the SSM Parameter Store.
* `SecretValue.cfnParameter(param)`: refers to a secret passed through a CloudFormation parameter (must have `NoEcho: true`).
* `SecretValue.cfnDynamicReference(dynref)`: refers to a secret described by a CloudFormation dynamic reference (used by `ssmSecure` and `secretsManager`).

## ARN manipulation

Sometimes you will need to put together or pick apart Amazon Resource Names
(ARNs). The functions `stack.formatArn()` and `stack.parseArn()` exist for
this purpose.

`formatArn()` can be used to build an ARN from components. It will automatically
use the region and account of the stack you're calling it on:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# Builds "arn:<PARTITION>:lambda:<REGION>:<ACCOUNT>:function:MyFunction"
stack.format_arn(
    service="lambda",
    resource="function",
    sep=":",
    resource_name="MyFunction"
)
```

`parseArn()` can be used to get a single component from an ARN. `parseArn()`
will correctly deal with both literal ARNs and deploy-time values (tokens),
but in case of a deploy-time value be aware that the result will be another
deploy-time value which cannot be inspected in the CDK application.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# Extracts the function name out of an AWS Lambda Function ARN
arn_components = stack.parse_arn(arn, ":")
function_name = arn_components.resource_name
```

Note that depending on the service, the resource separator can be either
`:` or `/`, and the resource name can be either the 6th or 7th
component in the ARN. When using these functions, you will need to know
the format of the ARN you are dealing with.

For an exhaustive list of ARN formats used in AWS, see [AWS ARNs and
Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html)
in the AWS General Reference.

## Dependencies

### Construct Dependencies

Sometimes AWS resources depend on other resources, and the creation of one
resource must be completed before the next one can be started.

In general, CloudFormation will correctly infer the dependency relationship
between resources based on the property values that are used. In the cases where
it doesn't, the AWS Construct Library will add the dependency relationship for
you.

If you need to add an ordering dependency that is not automatically inferred,
you do so by adding a dependency relationship using
`constructA.node.addDependency(constructB)`. This will add a dependency
relationship between all resources in the scope of `constructA` and all
resources in the scope of `constructB`.

If you want a single object to represent a set of constructs that are not
necessarily in the same scope, you can use a `ConcreteDependable`. The
following creates a single object that represents a dependency on two
constructs, `constructB` and `constructC`:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# Declare the dependable object
b_and_c = ConcreteDependable()
b_and_c.add(construct_b)
b_and_c.add(construct_c)

# Take the dependency
construct_a.node.add_dependency(b_and_c)
```

### Stack Dependencies

Two different stack instances can have a dependency on one another. This
happens when an resource from one stack is referenced in another stack. In
that case, CDK records the cross-stack referencing of resources,
automatically produces the right CloudFormation primitives, and adds a
dependency between the two stacks. You can also manually add a dependency
between two stacks by using the `stackA.addDependency(stackB)` method.

A stack dependency has the following implications:

* Cyclic dependencies are not allowed, so if `stackA` is using resources from
  `stackB`, the reverse is not possible anymore.
* Stacks with dependencies between them are treated specially by the CDK
  toolkit:

  * If `stackA` depends on `stackB`, running `cdk deploy stackA` will also
    automatically deploy `stackB`.
  * `stackB`'s deployment will be performed *before* `stackA`'s deployment.

## Custom Resources

Custom Resources are CloudFormation resources that are implemented by arbitrary
user code. They can do arbitrary lookups or modifications during a
CloudFormation deployment.

To define a custom resource, use the `CustomResource` construct:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
CustomResource(self, "MyMagicalResource",
    resource_type="Custom::MyCustomResource", # must start with 'Custom::'

    # the resource properties
    properties={
        "Property1": "foo",
        "Property2": "bar"
    },

    # the ARN of the provider (SNS/Lambda) which handles
    # CREATE, UPDATE or DELETE events for this resource type
    # see next section for details
    service_token="ARN"
)
```

### Custom Resource Providers

Custom resources are backed by a **custom resource provider** which can be
implemented in one of the following ways. The following table compares the
various provider types (ordered from low-level to high-level):

| Provider                                                             | Compute Type | Error Handling | Submit to CloudFormation | Max Timeout     | Language | Footprint |
|----------------------------------------------------------------------|:------------:|:--------------:|:------------------------:|:---------------:|:--------:|:---------:|
| [sns.Topic](#amazon-sns-topic)                                       | Self-managed | Manual         | Manual                   | Unlimited       | Any      | Depends   |
| [lambda.Function](#aws-lambda-function)                              | AWS Lambda   | Manual         | Manual                   | 15min           | Any      | Small     |
| [core.CustomResourceProvider](#the-corecustomresourceprovider-class) | Lambda       | Auto           | Auto                     | 15min           | Node.js  | Small     |
| [custom-resources.Provider](#the-custom-resource-provider-framework) | Lambda       | Auto           | Auto                     | Unlimited Async | Any      | Large     |

Legend:

* **Compute type**: which type of compute can is used to execute the handler.
* **Error Handling**: whether errors thrown by handler code are automatically
  trapped and a FAILED response is submitted to CloudFormation. If this is
  "Manual", developers must take care of trapping errors. Otherwise, events
  could cause stacks to hang.
* **Submit to CloudFormation**: whether the framework takes care of submitting
  SUCCESS/FAILED responses to CloudFormation through the event's response URL.
* **Max Timeout**: maximum allows/possible timeout.
* **Language**: which programming languages can be used to implement handlers.
* **Footprint**: how many resources are used by the provider framework itself.

**A NOTE ABOUT SINGLETONS**

When defining resources for a custom resource provider, you will likely want to
define them as a *stack singleton* so that only a single instance of the
provider is created in your stack and which is used by all custom resources of
that type.

Here is a basic pattern for defining stack singletons in the CDK. The following
examples ensures that only a single SNS topic is defined:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
def get_or_create(self, scope):
    stack = Stack.of(scope)
    uniqueid = "GloballyUniqueIdForSingleton"return stack.node.try_find_child(uniqueid) ?? sns.Topic(stack, uniqueid)
```

#### Amazon SNS Topic

Every time a resource event occurs (CREATE/UPDATE/DELETE), an SNS notification
is sent to the SNS topic. Users must process these notifications (e.g. through a
fleet of worker hosts) and submit success/failure responses to the
CloudFormation service.

Set `serviceToken` to `topic.topicArn`  in order to use this provider:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
topic = sns.Topic(self, "MyProvider")

CustomResource(self, "MyResource",
    service_token=topic.topic_arn
)
```

#### AWS Lambda Function

An AWS lambda function is called *directly* by CloudFormation for all resource
events. The handler must take care of explicitly submitting a success/failure
response to the CloudFormation service and handle various error cases.

Set `serviceToken` to `lambda.functionArn` to use this provider:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
fn = lambda_.Function(self, "MyProvider", function_props)

CustomResource(self, "MyResource",
    service_token=fn.function_arn
)
```

#### The `core.CustomResourceProvider` class

The class [`@aws-cdk/core.CustomResourceProvider`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_core.CustomResourceProvider.html) offers a basic low-level
framework designed to implement simple and slim custom resource providers. It
currently only supports Node.js-based user handlers, and it does not have
support for asynchronous waiting (handler cannot exceed the 15min lambda
timeout).

The provider has a built-in singleton method which uses the resource type as a
stack-unique identifier and returns the service token:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
service_token = CustomResourceProvider.get_or_create(self, "Custom::MyCustomResourceType",
    code_directory=f"{__dirname}/my-handler",
    runtime=CustomResourceProviderRuntime.NODEJS_12_X,
    description="Lambda function created by the custom resource provider"
)

CustomResource(self, "MyResource",
    resource_type="Custom::MyCustomResourceType",
    service_token=service_token
)
```

The directory (`my-handler` in the above example) must include an `index.js` file. It cannot import
external dependencies or files outside this directory. It must export an async
function named `handler`. This function accepts the CloudFormation resource
event object and returns an object with the following structure:

```js
exports.handler = async function(event) {
  const id = event.PhysicalResourceId; // only for "Update" and "Delete"
  const props = event.ResourceProperties;
  const oldProps = event.OldResourceProperties; // only for "Update"s

  switch (event.RequestType) {
    case "Create":
      // ...

    case "Update":
      // ...

      // if an error is thrown, a FAILED response will be submitted to CFN
      throw new Error('Failed!');

    case "Delete":
      // ...
  }

  return {
    // (optional) the value resolved from `resource.ref`
    // defaults to "event.PhysicalResourceId" or "event.RequestId"
    PhysicalResourceId: "REF",

    // (optional) calling `resource.getAtt("Att1")` on the custom resource in the CDK app
    // will return the value "BAR".
    Data: {
      Att1: "BAR",
      Att2: "BAZ"
    },

    // (optional) user-visible message
    Reason: "User-visible message",

    // (optional) hides values from the console
    NoEcho: true
  };
}
```

Here is an complete example of a custom resource that summarizes two numbers:

`sum-handler/index.js`:

```js
exports.handler = async (e) => {
  return {
    Data: {
      Result: e.ResourceProperties.lhs + e.ResourceProperties.rhs,
    },
  };
};
```

`sum.ts`:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
from aws_cdk.core import Construct, CustomResource, CustomResourceProvider, CustomResourceProviderRuntime, Token

class Sum(Construct):

    def __init__(self, scope, id, *, lhs, rhs):
        super().__init__(scope, id)

        resource_type = "Custom::Sum"
        service_token = CustomResourceProvider.get_or_create(self, resource_type,
            code_directory=f"{__dirname}/sum-handler",
            runtime=CustomResourceProviderRuntime.NODEJS_12_X
        )

        resource = CustomResource(self, "Resource",
            resource_type=resource_type,
            service_token=service_token,
            properties={
                "lhs": lhs,
                "rhs": rhs
            }
        )

        self.result = Token.as_number(resource.get_att("Result"))
```

Usage will look like this:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
sum = Sum(self, "MySum", lhs=40, rhs=2)
CfnOutput(self, "Result", value=Token.as_string(sum.result))
```

To access the ARN of the provider's AWS Lambda function role, use the `getOrCreateProvider()`
built-in singleton method:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
provider = CustomResourceProvider.get_or_create_provider(self, "Custom::MyCustomResourceType",
    code_directory=f"{__dirname}/my-handler",
    runtime=CustomResourceProviderRuntime.NODEJS_12_X
)

role_arn = provider.role_arn
```

This role ARN can then be used in resource-based IAM policies.

#### The Custom Resource Provider Framework

The [`@aws-cdk/custom-resources`](https://docs.aws.amazon.com/cdk/api/latest/docs/custom-resources-readme.html) module includes an advanced framework for
implementing custom resource providers.

Handlers are implemented as AWS Lambda functions, which means that they can be
implemented in any Lambda-supported runtime. Furthermore, this provider has an
asynchronous mode, which means that users can provide an `isComplete` lambda
function which is called periodically until the operation is complete. This
allows implementing providers that can take up to two hours to stabilize.

Set `serviceToken` to `provider.serviceToken` to use this type of provider:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
provider = customresources.Provider(self, "MyProvider",
    on_event_handler=on_event_handler,
    is_complete_handler=is_complete_handler
)

CustomResource(self, "MyResource",
    service_token=provider.service_token
)
```

See the [documentation](https://docs.aws.amazon.com/cdk/api/latest/docs/custom-resources-readme.html) for more details.

## AWS CloudFormation features

A CDK stack synthesizes to an AWS CloudFormation Template. This section
explains how this module allows users to access low-level CloudFormation
features when needed.

### Stack Outputs

CloudFormation [stack outputs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html) and exports are created using
the `CfnOutput` class:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
CfnOutput(self, "OutputName",
    value=my_bucket.bucket_name,
    description="The name of an S3 bucket", # Optional
    export_name="TheAwesomeBucket"
)
```

### Parameters

CloudFormation templates support the use of [Parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html) to
customize a template. They enable CloudFormation users to input custom values to
a template each time a stack is created or updated. While the CDK design
philosophy favors using build-time parameterization, users may need to use
CloudFormation in a number of cases (for example, when migrating an existing
stack to the AWS CDK).

Template parameters can be added to a stack by using the `CfnParameter` class:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
CfnParameter(self, "MyParameter",
    type="Number",
    default=1337
)
```

The value of parameters can then be obtained using one of the `value` methods.
As parameters are only resolved at deployment time, the values obtained are
placeholder tokens for the real value (`Token.isUnresolved()` would return `true`
for those):

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
param = CfnParameter(self, "ParameterName")

# If the parameter is a String
param.value_as_string

# If the parameter is a Number
param.value_as_number

# If the parameter is a List
param.value_as_list
```

### Pseudo Parameters

CloudFormation supports a number of [pseudo parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.html),
which resolve to useful values at deployment time. CloudFormation pseudo
parameters can be obtained from static members of the `Aws` class.

It is generally recommended to access pseudo parameters from the scope's `stack`
instead, which guarantees the values produced are qualifying the designated
stack, which is essential in cases where resources are shared cross-stack:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# "this" is the current construct
stack = Stack.of(self)

stack.account# Returns the AWS::AccountId for this stack (or the literal value if known)
stack.region# Returns the AWS::Region for this stack (or the literal value if known)
stack.partition
```

### Resource Options

CloudFormation resources can also specify [resource
attributes](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-product-attribute-reference.html). The `CfnResource` class allows
accessing those through the `cfnOptions` property:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
raw_bucket = s3.CfnBucket(self, "Bucket")
# -or-
raw_bucket_alt = my_bucket.node.default_child

# then
raw_bucket.cfn_options.condition = CfnCondition(self, "EnableBucket")
raw_bucket.cfn_options.metadata = {
    "metadata_key": "MetadataValue"
}
```

Resource dependencies (the `DependsOn` attribute) is modified using the
`cfnResource.addDependsOn` method:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
resource_a = CfnResource(self, "ResourceA", resource_props)
resource_b = CfnResource(self, "ResourceB", resource_props)

resource_b.add_depends_on(resource_a)
```

### Intrinsic Functions and Condition Expressions

CloudFormation supports [intrinsic functions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html). These functions
can be accessed from the `Fn` class, which provides type-safe methods for each
intrinsic function as well as condition expressions:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# To use Fn::Base64
Fn.base64("SGVsbG8gQ0RLIQo=")

# To compose condition expressions:
environment_parameter = CfnParameter(self, "Environment")
Fn.condition_and(
    # The "Environment" CloudFormation template parameter evaluates to "Production"
    Fn.condition_equals("Production", environment_parameter),
    # The AWS::Region pseudo-parameter value is NOT equal to "us-east-1"
    Fn.condition_not(Fn.condition_equals("us-east-1", Aws.REGION)))
```

When working with deploy-time values (those for which `Token.isUnresolved`
returns `true`), idiomatic conditionals from the programming language cannot be
used (the value will not be known until deployment time). When conditional logic
needs to be expressed with un-resolved values, it is necessary to use
CloudFormation conditions by means of the `CfnCondition` class:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
environment_parameter = CfnParameter(self, "Environment")
is_prod = CfnCondition(self, "IsProduction",
    expression=Fn.condition_equals("Production", environment_parameter)
)

# Configuration value that is a different string based on IsProduction
stage = Fn.condition_if(is_prod.logical_id, "Beta", "Prod").to_string()

# Make Bucket creation condition to IsProduction by accessing
# and overriding the CloudFormation resource
bucket = s3.Bucket(self, "Bucket")
cfn_bucket = my_bucket.node.default_child
cfn_bucket.cfn_options.condition = is_prod
```

### Mappings

CloudFormation [mappings](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/mappings-section-structure.html) are created and queried using the
`CfnMappings` class:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
region_table = CfnMapping(self, "RegionTable",
    mapping={
        "region_name": {
            "us-east-1": "US East (N. Virginia)",
            "us-east-2": "US East (Ohio)"
        }
    }
)

region_table.find_in_map("regionName", Aws.REGION)
```

This will yield the following template:

```yaml
Mappings:
  RegionTable:
    regionName:
      us-east-1: US East (N. Virginia)
      us-east-2: US East (Ohio)
```

### Dynamic References

CloudFormation supports [dynamically resolving](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html) values
for SSM parameters (including secure strings) and Secrets Manager. Encoding such
references is done using the `CfnDynamicReference` class:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
CfnDynamicReference(CfnDynamicReferenceService.SECRETS_MANAGER, "secret-id:secret-string:json-key:version-stage:version-id")
```

### Template Options & Transform

CloudFormation templates support a number of options, including which Macros or
[Transforms](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-section-structure.html) to use when deploying the stack. Those can be
configured using the `stack.templateOptions` property:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
stack = Stack(app, "StackName")

stack.template_options.description = "This will appear in the AWS console"
stack.template_options.transforms = ["AWS::Serverless-2016-10-31"]
stack.template_options.metadata = {
    "metadata_key": "MetadataValue"
}
```

### Emitting Raw Resources

The `CfnResource` class allows emitting arbitrary entries in the
[Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html) section of the CloudFormation template.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
CfnResource(self, "ResourceId",
    type="AWS::S3::Bucket",
    properties={
        "BucketName": "bucket-name"
    }
)
```

As for any other resource, the logical ID in the CloudFormation template will be
generated by the AWS CDK, but the type and properties will be copied verbatim in
the synthesized template.

### Including raw CloudFormation template fragments

When migrating a CloudFormation stack to the AWS CDK, it can be useful to
include fragments of an existing template verbatim in the synthesized template.
This can be achieved using the `CfnInclude` class.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
CfnInclude(self, "ID",
    template={
        "Resources": {
            "Bucket": {
                "Type": "AWS::S3::Bucket",
                "Properties": {
                    "BucketName": "my-shiny-bucket"
                }
            }
        }
    }
)
```

### Termination Protection

You can prevent a stack from being accidentally deleted by enabling termination
protection on the stack. If a user attempts to delete a stack with termination
protection enabled, the deletion fails and the stack--including its status--remains
unchanged. Enabling or disabling termination protection on a stack sets it for any
nested stacks belonging to that stack as well. You can enable termination protection
on a stack by setting the `terminationProtection` prop to `true`.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
stack = Stack(app, "StackName",
    termination_protection=True
)
```

By default, termination protection is disabled.

### CfnJson

`CfnJson` allows you to postpone the resolution of a JSON blob from
deployment-time. This is useful in cases where the CloudFormation JSON template
cannot express a certain value.

A common example is to use `CfnJson` in order to render a JSON map which needs
to use intrinsic functions in keys. Since JSON map keys must be strings, it is
impossible to use intrinsics in keys and `CfnJson` can help.

The following example defines an IAM role which can only be assumed by
principals that are tagged with a specific tag.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
tag_param = CfnParameter(self, "TagName")

string_equals = CfnJson(self, "ConditionJson",
    value={
        f"aws:PrincipalTag/{tagParam.valueAsString}": True
    }
)

principal = iam.AccountRootPrincipal().with_conditions({
    "StringEquals": string_equals
})

iam.Role(self, "MyRole", assumed_by=principal)
```

**Explanation**: since in this example we pass the tag name through a parameter, it
can only be resolved during deployment. The resolved value can be represented in
the template through a `{ "Ref": "TagName" }`. However, since we want to use
this value inside a [`aws:PrincipalTag/TAG-NAME`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principaltag)
IAM operator, we need it in the *key* of a `StringEquals` condition. JSON keys
*must be* strings, so to circumvent this limitation, we use `CfnJson`
to "delay" the rendition of this template section to deploy-time. This means
that the value of `StringEquals` in the template will be `{ "Fn::GetAtt": [ "ConditionJson", "Value" ] }`, and will only "expand" to the operator we synthesized during deployment.

### Stack Resource Limit

When deploying to AWS CloudFormation, it needs to keep in check the amount of resources being added inside a Stack. Currently it's possible to check the limits in the [AWS CloudFormation quotas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) page.

It's possible to synthesize the project with more Resources than the allowed (or even reduce the number of Resources).

Set the context key `@aws-cdk/core:stackResourceLimit` with the proper value, being 0 for disable the limit of resources.

<!--END CORE DOCUMENTATION-->
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.cloud_assembly_schema
import aws_cdk.cx_api
import constructs


class Annotations(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.Annotations"):
    '''Includes API for attaching annotations such as warning messages to constructs.'''

    @jsii.member(jsii_name="of") # type: ignore[misc]
    @builtins.classmethod
    def of(cls, scope: constructs.IConstruct) -> "Annotations":
        '''Returns the annotations API for a construct scope.

        :param scope: The scope.
        '''
        return typing.cast("Annotations", jsii.sinvoke(cls, "of", [scope]))

    @jsii.member(jsii_name="addDeprecation")
    def add_deprecation(self, api: builtins.str, message: builtins.str) -> None:
        '''Adds a deprecation warning for a specific API.

        Deprecations will be added only once per construct as a warning and will be
        deduplicated based on the ``api``.

        If the environment variable ``CDK_BLOCK_DEPRECATIONS`` is set, this method
        will throw an error instead with the deprecation message.

        :param api: The API being deprecated in the format ``module.Class.property`` (e.g. ``@aws-cdk/core.Construct.node``).
        :param message: The deprecation message to display, with information about alternatives.
        '''
        return typing.cast(None, jsii.invoke(self, "addDeprecation", [api, message]))

    @jsii.member(jsii_name="addError")
    def add_error(self, message: builtins.str) -> None:
        '''Adds an { "error":  } metadata entry to this construct.

        The toolkit will fail synthesis when errors are reported.

        :param message: The error message.
        '''
        return typing.cast(None, jsii.invoke(self, "addError", [message]))

    @jsii.member(jsii_name="addInfo")
    def add_info(self, message: builtins.str) -> None:
        '''Adds an info metadata entry to this construct.

        The CLI will display the info message when apps are synthesized.

        :param message: The info message.
        '''
        return typing.cast(None, jsii.invoke(self, "addInfo", [message]))

    @jsii.member(jsii_name="addWarning")
    def add_warning(self, message: builtins.str) -> None:
        '''Adds a warning metadata entry to this construct.

        The CLI will display the warning when an app is synthesized, or fail if run
        in --strict mode.

        :param message: The warning message.
        '''
        return typing.cast(None, jsii.invoke(self, "addWarning", [message]))


@jsii.data_type(
    jsii_type="@aws-cdk/core.AppProps",
    jsii_struct_bases=[],
    name_mapping={
        "analytics_reporting": "analyticsReporting",
        "auto_synth": "autoSynth",
        "context": "context",
        "outdir": "outdir",
        "runtime_info": "runtimeInfo",
        "stack_traces": "stackTraces",
        "tree_metadata": "treeMetadata",
    },
)
class AppProps:
    def __init__(
        self,
        *,
        analytics_reporting: typing.Optional[builtins.bool] = None,
        auto_synth: typing.Optional[builtins.bool] = None,
        context: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        outdir: typing.Optional[builtins.str] = None,
        runtime_info: typing.Optional[builtins.bool] = None,
        stack_traces: typing.Optional[builtins.bool] = None,
        tree_metadata: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Initialization props for apps.

        :param analytics_reporting: Include runtime versioning information in the Stacks of this app. Default: Value of 'aws:cdk:version-reporting' context key
        :param auto_synth: Automatically call ``synth()`` before the program exits. If you set this, you don't have to call ``synth()`` explicitly. Note that this feature is only available for certain programming languages, and calling ``synth()`` is still recommended. Default: true if running via CDK CLI (``CDK_OUTDIR`` is set), ``false`` otherwise
        :param context: Additional context values for the application. Context set by the CLI or the ``context`` key in ``cdk.json`` has precedence. Context can be read from any construct using ``node.getContext(key)``. Default: - no additional context
        :param outdir: The output directory into which to emit synthesized artifacts. Default: - If this value is *not* set, considers the environment variable ``CDK_OUTDIR``. If ``CDK_OUTDIR`` is not defined, uses a temp directory.
        :param runtime_info: (deprecated) Include runtime versioning information in the Stacks of this app. Default: Value of 'aws:cdk:version-reporting' context key
        :param stack_traces: Include construct creation stack trace in the ``aws:cdk:trace`` metadata key of all constructs. Default: true stack traces are included unless ``aws:cdk:disable-stack-trace`` is set in the context.
        :param tree_metadata: Include construct tree metadata as part of the Cloud Assembly. Default: true
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if analytics_reporting is not None:
            self._values["analytics_reporting"] = analytics_reporting
        if auto_synth is not None:
            self._values["auto_synth"] = auto_synth
        if context is not None:
            self._values["context"] = context
        if outdir is not None:
            self._values["outdir"] = outdir
        if runtime_info is not None:
            self._values["runtime_info"] = runtime_info
        if stack_traces is not None:
            self._values["stack_traces"] = stack_traces
        if tree_metadata is not None:
            self._values["tree_metadata"] = tree_metadata

    @builtins.property
    def analytics_reporting(self) -> typing.Optional[builtins.bool]:
        '''Include runtime versioning information in the Stacks of this app.

        :default: Value of 'aws:cdk:version-reporting' context key
        '''
        result = self._values.get("analytics_reporting")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def auto_synth(self) -> typing.Optional[builtins.bool]:
        '''Automatically call ``synth()`` before the program exits.

        If you set this, you don't have to call ``synth()`` explicitly. Note that
        this feature is only available for certain programming languages, and
        calling ``synth()`` is still recommended.

        :default:

        true if running via CDK CLI (``CDK_OUTDIR`` is set), ``false``
        otherwise
        '''
        result = self._values.get("auto_synth")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def context(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Additional context values for the application.

        Context set by the CLI or the ``context`` key in ``cdk.json`` has precedence.

        Context can be read from any construct using ``node.getContext(key)``.

        :default: - no additional context
        '''
        result = self._values.get("context")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def outdir(self) -> typing.Optional[builtins.str]:
        '''The output directory into which to emit synthesized artifacts.

        :default:

        - If this value is *not* set, considers the environment variable ``CDK_OUTDIR``.
        If ``CDK_OUTDIR`` is not defined, uses a temp directory.
        '''
        result = self._values.get("outdir")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime_info(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Include runtime versioning information in the Stacks of this app.

        :default: Value of 'aws:cdk:version-reporting' context key

        :deprecated: use ``versionReporting`` instead

        :stability: deprecated
        '''
        result = self._values.get("runtime_info")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def stack_traces(self) -> typing.Optional[builtins.bool]:
        '''Include construct creation stack trace in the ``aws:cdk:trace`` metadata key of all constructs.

        :default: true stack traces are included unless ``aws:cdk:disable-stack-trace`` is set in the context.
        '''
        result = self._values.get("stack_traces")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tree_metadata(self) -> typing.Optional[builtins.bool]:
        '''Include construct tree metadata as part of the Cloud Assembly.

        :default: true
        '''
        result = self._values.get("tree_metadata")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Arn(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.Arn"):
    @jsii.member(jsii_name="extractResourceName") # type: ignore[misc]
    @builtins.classmethod
    def extract_resource_name(
        cls,
        arn: builtins.str,
        resource_type: builtins.str,
    ) -> builtins.str:
        '''Extract the full resource name from an ARN.

        Necessary for resource names (paths) that may contain the separator, like
        ``arn:aws:iam::111111111111:role/path/to/role/name``.

        Only works if we statically know the expected ``resourceType`` beforehand, since we're going
        to use that to split the string on ':/' (and take the right-hand side).

        We can't extract the 'resourceType' from the ARN at hand, because CloudFormation Expressions
        only allow literals in the 'separator' argument to ``{ Fn::Split }``, and so it can't be
        ``{ Fn::Select: [5, { Fn::Split: [':', ARN] }}``.

        Only necessary for ARN formats for which the type-name separator is ``/``.

        :param arn: -
        :param resource_type: -
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "extractResourceName", [arn, resource_type]))

    @jsii.member(jsii_name="format") # type: ignore[misc]
    @builtins.classmethod
    def format(cls, components: "ArnComponents", stack: "Stack") -> builtins.str:
        '''Creates an ARN from components.

        If ``partition``, ``region`` or ``account`` are not specified, the stack's
        partition, region and account will be used.

        If any component is the empty string, an empty string will be inserted
        into the generated ARN at the location that component corresponds to.

        The ARN will be formatted as follows:

        arn:{partition}:{service}:{region}:{account}:{resource}{sep}{resource-name}

        The required ARN pieces that are omitted will be taken from the stack that
        the 'scope' is attached to. If all ARN pieces are supplied, the supplied scope
        can be 'undefined'.

        :param components: -
        :param stack: -
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "format", [components, stack]))

    @jsii.member(jsii_name="parse") # type: ignore[misc]
    @builtins.classmethod
    def parse(
        cls,
        arn: builtins.str,
        sep_if_token: typing.Optional[builtins.str] = None,
        has_name: typing.Optional[builtins.bool] = None,
    ) -> "ArnComponents":
        '''(deprecated) Given an ARN, parses it and returns components.

        IF THE ARN IS A CONCRETE STRING...

        ...it will be parsed and validated. The separator (``sep``) will be set to '/'
        if the 6th component includes a '/', in which case, ``resource`` will be set
        to the value before the '/' and ``resourceName`` will be the rest. In case
        there is no '/', ``resource`` will be set to the 6th components and
        ``resourceName`` will be set to the rest of the string.

        IF THE ARN IS A TOKEN...

        ...it cannot be validated, since we don't have the actual value yet at the
        time of this function call. You will have to supply ``sepIfToken`` and
        whether or not ARNs of the expected format usually have resource names
        in order to parse it properly. The resulting ``ArnComponents`` object will
        contain tokens for the subexpressions of the ARN, not string literals.

        If the resource name could possibly contain the separator char, the actual
        resource name cannot be properly parsed. This only occurs if the separator
        char is '/', and happens for example for S3 object ARNs, IAM Role ARNs,
        IAM OIDC Provider ARNs, etc. To properly extract the resource name from a
        Tokenized ARN, you must know the resource type and call
        ``Arn.extractResourceName``.

        :param arn: The ARN to parse.
        :param sep_if_token: The separator used to separate resource from resourceName.
        :param has_name: Whether there is a name component in the ARN at all. For example, SNS Topics ARNs have the 'resource' component contain the topic name, and no 'resourceName' component.

        :return:

        an ArnComponents object which allows access to the various
        components of the ARN.

        :deprecated: use split instead

        :stability: deprecated
        '''
        return typing.cast("ArnComponents", jsii.sinvoke(cls, "parse", [arn, sep_if_token, has_name]))

    @jsii.member(jsii_name="split") # type: ignore[misc]
    @builtins.classmethod
    def split(cls, arn: builtins.str, arn_format: "ArnFormat") -> "ArnComponents":
        '''Splits the provided ARN into its components.

        Works both if 'arn' is a string like 'arn:aws:s3:::bucket',
        and a Token representing a dynamic CloudFormation expression
        (in which case the returned components will also be dynamic CloudFormation expressions,
        encoded as Tokens).

        :param arn: the ARN to split into its components.
        :param arn_format: the expected format of 'arn' - depends on what format the service 'arn' represents uses.
        '''
        return typing.cast("ArnComponents", jsii.sinvoke(cls, "split", [arn, arn_format]))


@jsii.data_type(
    jsii_type="@aws-cdk/core.ArnComponents",
    jsii_struct_bases=[],
    name_mapping={
        "resource": "resource",
        "service": "service",
        "account": "account",
        "arn_format": "arnFormat",
        "partition": "partition",
        "region": "region",
        "resource_name": "resourceName",
        "sep": "sep",
    },
)
class ArnComponents:
    def __init__(
        self,
        *,
        resource: builtins.str,
        service: builtins.str,
        account: typing.Optional[builtins.str] = None,
        arn_format: typing.Optional["ArnFormat"] = None,
        partition: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        resource_name: typing.Optional[builtins.str] = None,
        sep: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param resource: Resource type (e.g. "table", "autoScalingGroup", "certificate"). For some resource types, e.g. S3 buckets, this field defines the bucket name.
        :param service: The service namespace that identifies the AWS product (for example, 's3', 'iam', 'codepipline').
        :param account: The ID of the AWS account that owns the resource, without the hyphens. For example, 123456789012. Note that the ARNs for some resources don't require an account number, so this component might be omitted. Default: The account the stack is deployed to.
        :param arn_format: The specific ARN format to use for this ARN value. Default: - uses value of ``sep`` as the separator for formatting, ``ArnFormat.SLASH_RESOURCE_NAME`` if that property was also not provided
        :param partition: The partition that the resource is in. For standard AWS regions, the partition is aws. If you have resources in other partitions, the partition is aws-partitionname. For example, the partition for resources in the China (Beijing) region is aws-cn. Default: The AWS partition the stack is deployed to.
        :param region: The region the resource resides in. Note that the ARNs for some resources do not require a region, so this component might be omitted. Default: The region the stack is deployed to.
        :param resource_name: Resource name or path within the resource (i.e. S3 bucket object key) or a wildcard such as ``"*"``. This is service-dependent.
        :param sep: (deprecated) Separator between resource type and the resource. Can be either '/', ':' or an empty string. Will only be used if resourceName is defined. Default: '/'
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "resource": resource,
            "service": service,
        }
        if account is not None:
            self._values["account"] = account
        if arn_format is not None:
            self._values["arn_format"] = arn_format
        if partition is not None:
            self._values["partition"] = partition
        if region is not None:
            self._values["region"] = region
        if resource_name is not None:
            self._values["resource_name"] = resource_name
        if sep is not None:
            self._values["sep"] = sep

    @builtins.property
    def resource(self) -> builtins.str:
        '''Resource type (e.g. "table", "autoScalingGroup", "certificate"). For some resource types, e.g. S3 buckets, this field defines the bucket name.'''
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> builtins.str:
        '''The service namespace that identifies the AWS product (for example, 's3', 'iam', 'codepipline').'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''The ID of the AWS account that owns the resource, without the hyphens.

        For example, 123456789012. Note that the ARNs for some resources don't
        require an account number, so this component might be omitted.

        :default: The account the stack is deployed to.
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def arn_format(self) -> typing.Optional["ArnFormat"]:
        '''The specific ARN format to use for this ARN value.

        :default:

        - uses value of ``sep`` as the separator for formatting,
        ``ArnFormat.SLASH_RESOURCE_NAME`` if that property was also not provided
        '''
        result = self._values.get("arn_format")
        return typing.cast(typing.Optional["ArnFormat"], result)

    @builtins.property
    def partition(self) -> typing.Optional[builtins.str]:
        '''The partition that the resource is in.

        For standard AWS regions, the
        partition is aws. If you have resources in other partitions, the
        partition is aws-partitionname. For example, the partition for resources
        in the China (Beijing) region is aws-cn.

        :default: The AWS partition the stack is deployed to.
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region the resource resides in.

        Note that the ARNs for some resources
        do not require a region, so this component might be omitted.

        :default: The region the stack is deployed to.
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_name(self) -> typing.Optional[builtins.str]:
        '''Resource name or path within the resource (i.e. S3 bucket object key) or a wildcard such as ``"*"``. This is service-dependent.'''
        result = self._values.get("resource_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sep(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Separator between resource type and the resource.

        Can be either '/', ':' or an empty string. Will only be used if resourceName is defined.

        :default: '/'

        :deprecated: use arnFormat instead

        :stability: deprecated
        '''
        result = self._values.get("sep")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ArnComponents(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/core.ArnFormat")
class ArnFormat(enum.Enum):
    '''An enum representing the various ARN formats that different services use.'''

    NO_RESOURCE_NAME = "NO_RESOURCE_NAME"
    '''This represents a format where there is no 'resourceName' part.

    This format is used for S3 resources,
    like 'arn:aws:s3:::bucket'.
    Everything after the last colon is considered the 'resource',
    even if it contains slashes,
    like in 'arn:aws:s3:::bucket/object.zip'.
    '''
    COLON_RESOURCE_NAME = "COLON_RESOURCE_NAME"
    '''This represents a format where the 'resource' and 'resourceName' parts are separated with a colon.

    Like in: 'arn:aws:service:region:account:resource:resourceName'.
    Everything after the last colon is considered the 'resourceName',
    even if it contains slashes,
    like in 'arn:aws:apigateway:region:account:resource:/test/mydemoresource/*'.
    '''
    SLASH_RESOURCE_NAME = "SLASH_RESOURCE_NAME"
    '''This represents a format where the 'resource' and 'resourceName' parts are separated with a slash.

    Like in: 'arn:aws:service:region:account:resource/resourceName'.
    Everything after the separating slash is considered the 'resourceName',
    even if it contains colons,
    like in 'arn:aws:cognito-sync:region:account:identitypool/us-east-1:1a1a1a1a-ffff-1111-9999-12345678:bla'.
    '''
    SLASH_RESOURCE_SLASH_RESOURCE_NAME = "SLASH_RESOURCE_SLASH_RESOURCE_NAME"
    '''This represents a format where the 'resource' and 'resourceName' parts are seperated with a slash, but there is also an additional slash after the colon separating 'account' from 'resource'.

    Like in: 'arn:aws:service:region:account:/resource/resourceName'.
    Note that the leading slash is *not* included in the parsed 'resource' part.
    '''


class Aspects(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.Aspects"):
    '''Aspects can be applied to CDK tree scopes and can operate on the tree before synthesis.'''

    @jsii.member(jsii_name="of") # type: ignore[misc]
    @builtins.classmethod
    def of(cls, scope: "IConstruct") -> "Aspects":
        '''Returns the ``Aspects`` object associated with a construct scope.

        :param scope: The scope for which these aspects will apply.
        '''
        return typing.cast("Aspects", jsii.sinvoke(cls, "of", [scope]))

    @jsii.member(jsii_name="add")
    def add(self, aspect: "IAspect") -> None:
        '''Adds an aspect to apply this scope before synthesis.

        :param aspect: The aspect to add.
        '''
        return typing.cast(None, jsii.invoke(self, "add", [aspect]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="aspects")
    def aspects(self) -> typing.List["IAspect"]:
        '''The list of aspects which were directly applied on this scope.'''
        return typing.cast(typing.List["IAspect"], jsii.get(self, "aspects"))


@jsii.enum(jsii_type="@aws-cdk/core.AssetHashType")
class AssetHashType(enum.Enum):
    '''The type of asset hash.

    NOTE: the hash is used in order to identify a specific revision of the asset, and
    used for optimizing and caching deployment activities related to this asset such as
    packaging, uploading to Amazon S3, etc.
    '''

    SOURCE = "SOURCE"
    '''Based on the content of the source path.

    When bundling, use ``SOURCE`` when the content of the bundling output is not
    stable across repeated bundling operations.
    '''
    BUNDLE = "BUNDLE"
    '''(deprecated) Based on the content of the bundled path.

    :deprecated: use ``OUTPUT`` instead

    :stability: deprecated
    '''
    OUTPUT = "OUTPUT"
    '''Based on the content of the bundling output.

    Use ``OUTPUT`` when the source of the asset is a top level folder containing
    code and/or dependencies that are not directly linked to the asset.
    '''
    CUSTOM = "CUSTOM"
    '''Use a custom hash.'''


@jsii.data_type(
    jsii_type="@aws-cdk/core.AssetOptions",
    jsii_struct_bases=[],
    name_mapping={
        "asset_hash": "assetHash",
        "asset_hash_type": "assetHashType",
        "bundling": "bundling",
    },
)
class AssetOptions:
    def __init__(
        self,
        *,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[AssetHashType] = None,
        bundling: typing.Optional["BundlingOptions"] = None,
    ) -> None:
        '''Asset hash options.

        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container or a custom bundling provider. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        '''
        if isinstance(bundling, dict):
            bundling = BundlingOptions(**bundling)
        self._values: typing.Dict[str, typing.Any] = {}
        if asset_hash is not None:
            self._values["asset_hash"] = asset_hash
        if asset_hash_type is not None:
            self._values["asset_hash_type"] = asset_hash_type
        if bundling is not None:
            self._values["bundling"] = bundling

    @builtins.property
    def asset_hash(self) -> typing.Optional[builtins.str]:
        '''Specify a custom hash for this asset.

        If ``assetHashType`` is set it must
        be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will
        be SHA256 hashed and encoded as hex. The resulting hash will be the asset
        hash.

        NOTE: the hash is used in order to identify a specific revision of the asset, and
        used for optimizing and caching deployment activities related to this asset such as
        packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will
        need to make sure it is updated every time the asset changes, or otherwise it is
        possible that some deployments will not be invalidated.

        :default: - based on ``assetHashType``
        '''
        result = self._values.get("asset_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def asset_hash_type(self) -> typing.Optional[AssetHashType]:
        '''Specifies the type of hash to calculate for this asset.

        If ``assetHash`` is configured, this option must be ``undefined`` or
        ``AssetHashType.CUSTOM``.

        :default:

        - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is
        explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        '''
        result = self._values.get("asset_hash_type")
        return typing.cast(typing.Optional[AssetHashType], result)

    @builtins.property
    def bundling(self) -> typing.Optional["BundlingOptions"]:
        '''Bundle the asset by executing a command in a Docker container or a custom bundling provider.

        The asset path will be mounted at ``/asset-input``. The Docker
        container is responsible for putting content at ``/asset-output``.
        The content at ``/asset-output`` will be zipped and used as the
        final asset.

        :default:

        - uploaded as-is to S3 if the asset is a regular file or a .zip file,
        archived into a .zip file and uploaded to S3 otherwise
        '''
        result = self._values.get("bundling")
        return typing.cast(typing.Optional["BundlingOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssetOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Aws(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.Aws"):
    '''Accessor for pseudo parameters.

    Since pseudo parameters need to be anchored to a stack somewhere in the
    construct tree, this class takes an scope parameter; the pseudo parameter
    values can be obtained as properties from an scoped object.
    '''

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="ACCOUNT_ID")
    def ACCOUNT_ID(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "ACCOUNT_ID"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="NO_VALUE")
    def NO_VALUE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "NO_VALUE"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="NOTIFICATION_ARNS")
    def NOTIFICATION_ARNS(cls) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.sget(cls, "NOTIFICATION_ARNS"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="PARTITION")
    def PARTITION(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "PARTITION"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="REGION")
    def REGION(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "REGION"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="STACK_ID")
    def STACK_ID(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "STACK_ID"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="STACK_NAME")
    def STACK_NAME(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "STACK_NAME"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="URL_SUFFIX")
    def URL_SUFFIX(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "URL_SUFFIX"))


@jsii.data_type(
    jsii_type="@aws-cdk/core.BootstraplessSynthesizerProps",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_formation_execution_role_arn": "cloudFormationExecutionRoleArn",
        "deploy_role_arn": "deployRoleArn",
    },
)
class BootstraplessSynthesizerProps:
    def __init__(
        self,
        *,
        cloud_formation_execution_role_arn: typing.Optional[builtins.str] = None,
        deploy_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Construction properties of {@link BootstraplessSynthesizer}.

        :param cloud_formation_execution_role_arn: The CFN execution Role ARN to use. Default: - No CloudFormation role (use CLI credentials)
        :param deploy_role_arn: The deploy Role ARN to use. Default: - No deploy role (use CLI credentials)
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if cloud_formation_execution_role_arn is not None:
            self._values["cloud_formation_execution_role_arn"] = cloud_formation_execution_role_arn
        if deploy_role_arn is not None:
            self._values["deploy_role_arn"] = deploy_role_arn

    @builtins.property
    def cloud_formation_execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The CFN execution Role ARN to use.

        :default: - No CloudFormation role (use CLI credentials)
        '''
        result = self._values.get("cloud_formation_execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deploy_role_arn(self) -> typing.Optional[builtins.str]:
        '''The deploy Role ARN to use.

        :default: - No deploy role (use CLI credentials)
        '''
        result = self._values.get("deploy_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BootstraplessSynthesizerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BundlingDockerImage(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.BundlingDockerImage",
):
    '''(deprecated) A Docker image used for asset bundling.

    :deprecated: use DockerImage

    :stability: deprecated
    '''

    def __init__(
        self,
        image: builtins.str,
        _image_hash: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image: The Docker image.
        :param _image_hash: -

        :stability: deprecated
        '''
        jsii.create(BundlingDockerImage, self, [image, _image_hash])

    @jsii.member(jsii_name="fromAsset") # type: ignore[misc]
    @builtins.classmethod
    def from_asset(
        cls,
        path: builtins.str,
        *,
        build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        file: typing.Optional[builtins.str] = None,
        platform: typing.Optional[builtins.str] = None,
    ) -> "BundlingDockerImage":
        '''(deprecated) Reference an image that's built directly from sources on disk.

        :param path: The path to the directory containing the Docker file.
        :param build_args: Build args. Default: - no build args
        :param file: Name of the Dockerfile, must relative to the docker build path. Default: ``Dockerfile``
        :param platform: Set platform if server is multi-platform capable. *Requires Docker Engine API v1.38+*. Default: - no platform specified

        :deprecated: use DockerImage.fromBuild()

        :stability: deprecated
        '''
        options = DockerBuildOptions(
            build_args=build_args, file=file, platform=platform
        )

        return typing.cast("BundlingDockerImage", jsii.sinvoke(cls, "fromAsset", [path, options]))

    @jsii.member(jsii_name="fromRegistry") # type: ignore[misc]
    @builtins.classmethod
    def from_registry(cls, image: builtins.str) -> "DockerImage":
        '''(deprecated) Reference an image on DockerHub or another online registry.

        :param image: the image name.

        :stability: deprecated
        '''
        return typing.cast("DockerImage", jsii.sinvoke(cls, "fromRegistry", [image]))

    @jsii.member(jsii_name="cp")
    def cp(
        self,
        image_path: builtins.str,
        output_path: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''(deprecated) Copies a file or directory out of the Docker image to the local filesystem.

        If ``outputPath`` is omitted the destination path is a temporary directory.

        :param image_path: the path in the Docker image.
        :param output_path: the destination path for the copy operation.

        :return: the destination path

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "cp", [image_path, output_path]))

    @jsii.member(jsii_name="run")
    def run(
        self,
        *,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        security_opt: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Sequence["DockerVolume"]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(deprecated) Runs a Docker image.

        :param command: The command to run in the container. Default: - run the command defined in the image
        :param entrypoint: The entrypoint to run in the container. Default: - run the entrypoint defined in the image
        :param environment: The environment variables to pass to the container. Default: - no environment variables.
        :param security_opt: `Security configuration <https://docs.docker.com/engine/reference/run/#security-configuration>`_ when running the docker container. Default: - no security options
        :param user: The user to use when running the container. Default: - root or image default
        :param volumes: Docker volumes to mount. Default: - no volumes are mounted
        :param working_directory: Working directory inside the container. Default: - image default

        :stability: deprecated
        '''
        options = DockerRunOptions(
            command=command,
            entrypoint=entrypoint,
            environment=environment,
            security_opt=security_opt,
            user=user,
            volumes=volumes,
            working_directory=working_directory,
        )

        return typing.cast(None, jsii.invoke(self, "run", [options]))

    @jsii.member(jsii_name="toJSON")
    def to_json(self) -> builtins.str:
        '''(deprecated) Provides a stable representation of this image for JSON serialization.

        :return: The overridden image name if set or image hash name in that order

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toJSON", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        '''(deprecated) The Docker image.

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.get(self, "image"))


@jsii.data_type(
    jsii_type="@aws-cdk/core.BundlingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "image": "image",
        "command": "command",
        "entrypoint": "entrypoint",
        "environment": "environment",
        "local": "local",
        "output_type": "outputType",
        "security_opt": "securityOpt",
        "user": "user",
        "volumes": "volumes",
        "working_directory": "workingDirectory",
    },
)
class BundlingOptions:
    def __init__(
        self,
        *,
        image: "DockerImage",
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        local: typing.Optional["ILocalBundling"] = None,
        output_type: typing.Optional["BundlingOutput"] = None,
        security_opt: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Sequence["DockerVolume"]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Bundling options.

        :param image: The Docker image where the command will run.
        :param command: The command to run in the Docker container. Default: - run the command defined in the image
        :param entrypoint: The entrypoint to run in the Docker container. Default: - run the entrypoint defined in the image
        :param environment: The environment variables to pass to the Docker container. Default: - no environment variables.
        :param local: Local bundling provider. The provider implements a method ``tryBundle()`` which should return ``true`` if local bundling was performed. If ``false`` is returned, docker bundling will be done. Default: - bundling will only be performed in a Docker container
        :param output_type: The type of output that this bundling operation is producing. Default: BundlingOutput.AUTO_DISCOVER
        :param security_opt: `Security configuration <https://docs.docker.com/engine/reference/run/#security-configuration>`_ when running the docker container. Default: - no security options
        :param user: The user to use when running the Docker container. user | user:group | uid | uid:gid | user:gid | uid:group Default: - uid:gid of the current user or 1000:1000 on Windows
        :param volumes: Additional Docker volumes to mount. Default: - no additional volumes are mounted
        :param working_directory: Working directory inside the Docker container. Default: /asset-input
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "image": image,
        }
        if command is not None:
            self._values["command"] = command
        if entrypoint is not None:
            self._values["entrypoint"] = entrypoint
        if environment is not None:
            self._values["environment"] = environment
        if local is not None:
            self._values["local"] = local
        if output_type is not None:
            self._values["output_type"] = output_type
        if security_opt is not None:
            self._values["security_opt"] = security_opt
        if user is not None:
            self._values["user"] = user
        if volumes is not None:
            self._values["volumes"] = volumes
        if working_directory is not None:
            self._values["working_directory"] = working_directory

    @builtins.property
    def image(self) -> "DockerImage":
        '''The Docker image where the command will run.'''
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast("DockerImage", result)

    @builtins.property
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The command to run in the Docker container.

        :default: - run the command defined in the image

        :see: https://docs.docker.com/engine/reference/run/

        Example::

            # Example automatically generated. See https://github.com/aws/jsii/issues/826
            ["npm", "install"]
        '''
        result = self._values.get("command")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The entrypoint to run in the Docker container.

        :default: - run the entrypoint defined in the image

        :see: https://docs.docker.com/engine/reference/builder/#entrypoint

        Example::

            # Example automatically generated. See https://github.com/aws/jsii/issues/826
            ["/bin/sh", "-c"]
        '''
        result = self._values.get("entrypoint")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The environment variables to pass to the Docker container.

        :default: - no environment variables.
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def local(self) -> typing.Optional["ILocalBundling"]:
        '''Local bundling provider.

        The provider implements a method ``tryBundle()`` which should return ``true``
        if local bundling was performed. If ``false`` is returned, docker bundling
        will be done.

        :default: - bundling will only be performed in a Docker container
        '''
        result = self._values.get("local")
        return typing.cast(typing.Optional["ILocalBundling"], result)

    @builtins.property
    def output_type(self) -> typing.Optional["BundlingOutput"]:
        '''The type of output that this bundling operation is producing.

        :default: BundlingOutput.AUTO_DISCOVER
        '''
        result = self._values.get("output_type")
        return typing.cast(typing.Optional["BundlingOutput"], result)

    @builtins.property
    def security_opt(self) -> typing.Optional[builtins.str]:
        '''`Security configuration <https://docs.docker.com/engine/reference/run/#security-configuration>`_ when running the docker container.

        :default: - no security options
        '''
        result = self._values.get("security_opt")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''The user to use when running the Docker container.

        user | user:group | uid | uid:gid | user:gid | uid:group

        :default: - uid:gid of the current user or 1000:1000 on Windows

        :see: https://docs.docker.com/engine/reference/run/#user
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List["DockerVolume"]]:
        '''Additional Docker volumes to mount.

        :default: - no additional volumes are mounted
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List["DockerVolume"]], result)

    @builtins.property
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''Working directory inside the Docker container.

        :default: /asset-input
        '''
        result = self._values.get("working_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BundlingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/core.BundlingOutput")
class BundlingOutput(enum.Enum):
    '''The type of output that a bundling operation is producing.'''

    ARCHIVED = "ARCHIVED"
    '''The bundling output directory includes a single .zip or .jar file which will be used as the final bundle. If the output directory does not include exactly a single archive, bundling will fail.'''
    NOT_ARCHIVED = "NOT_ARCHIVED"
    '''The bundling output directory contains one or more files which will be archived and uploaded as a .zip file to S3.'''
    AUTO_DISCOVER = "AUTO_DISCOVER"
    '''If the bundling output directory contains a single archive file (zip or jar) it will be used as the bundle output as-is.

    Otherwise all the files in the bundling output directory will be zipped.
    '''


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnAutoScalingReplacingUpdate",
    jsii_struct_bases=[],
    name_mapping={"will_replace": "willReplace"},
)
class CfnAutoScalingReplacingUpdate:
    def __init__(self, *, will_replace: typing.Optional[builtins.bool] = None) -> None:
        '''Specifies whether an Auto Scaling group and the instances it contains are replaced during an update.

        During replacement,
        AWS CloudFormation retains the old group until it finishes creating the new one. If the update fails, AWS CloudFormation
        can roll back to the old Auto Scaling group and delete the new Auto Scaling group.

        While AWS CloudFormation creates the new group, it doesn't detach or attach any instances. After successfully creating
        the new Auto Scaling group, AWS CloudFormation deletes the old Auto Scaling group during the cleanup process.

        When you set the WillReplace parameter, remember to specify a matching CreationPolicy. If the minimum number of
        instances (specified by the MinSuccessfulInstancesPercent property) don't signal success within the Timeout period
        (specified in the CreationPolicy policy), the replacement update fails and AWS CloudFormation rolls back to the old
        Auto Scaling group.

        :param will_replace: 
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if will_replace is not None:
            self._values["will_replace"] = will_replace

    @builtins.property
    def will_replace(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("will_replace")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAutoScalingReplacingUpdate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnAutoScalingRollingUpdate",
    jsii_struct_bases=[],
    name_mapping={
        "max_batch_size": "maxBatchSize",
        "min_instances_in_service": "minInstancesInService",
        "min_successful_instances_percent": "minSuccessfulInstancesPercent",
        "pause_time": "pauseTime",
        "suspend_processes": "suspendProcesses",
        "wait_on_resource_signals": "waitOnResourceSignals",
    },
)
class CfnAutoScalingRollingUpdate:
    def __init__(
        self,
        *,
        max_batch_size: typing.Optional[jsii.Number] = None,
        min_instances_in_service: typing.Optional[jsii.Number] = None,
        min_successful_instances_percent: typing.Optional[jsii.Number] = None,
        pause_time: typing.Optional[builtins.str] = None,
        suspend_processes: typing.Optional[typing.Sequence[builtins.str]] = None,
        wait_on_resource_signals: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''To specify how AWS CloudFormation handles rolling updates for an Auto Scaling group, use the AutoScalingRollingUpdate policy.

        Rolling updates enable you to specify whether AWS CloudFormation updates instances that are in an Auto Scaling
        group in batches or all at once.

        :param max_batch_size: Specifies the maximum number of instances that AWS CloudFormation updates.
        :param min_instances_in_service: Specifies the minimum number of instances that must be in service within the Auto Scaling group while AWS CloudFormation updates old instances.
        :param min_successful_instances_percent: Specifies the percentage of instances in an Auto Scaling rolling update that must signal success for an update to succeed. You can specify a value from 0 to 100. AWS CloudFormation rounds to the nearest tenth of a percent. For example, if you update five instances with a minimum successful percentage of 50, three instances must signal success. If an instance doesn't send a signal within the time specified in the PauseTime property, AWS CloudFormation assumes that the instance wasn't updated. If you specify this property, you must also enable the WaitOnResourceSignals and PauseTime properties.
        :param pause_time: The amount of time that AWS CloudFormation pauses after making a change to a batch of instances to give those instances time to start software applications. For example, you might need to specify PauseTime when scaling up the number of instances in an Auto Scaling group. If you enable the WaitOnResourceSignals property, PauseTime is the amount of time that AWS CloudFormation should wait for the Auto Scaling group to receive the required number of valid signals from added or replaced instances. If the PauseTime is exceeded before the Auto Scaling group receives the required number of signals, the update fails. For best results, specify a time period that gives your applications sufficient time to get started. If the update needs to be rolled back, a short PauseTime can cause the rollback to fail. Specify PauseTime in the ISO8601 duration format (in the format PT#H#M#S, where each # is the number of hours, minutes, and seconds, respectively). The maximum PauseTime is one hour (PT1H).
        :param suspend_processes: Specifies the Auto Scaling processes to suspend during a stack update. Suspending processes prevents Auto Scaling from interfering with a stack update. For example, you can suspend alarming so that Auto Scaling doesn't execute scaling policies associated with an alarm. For valid values, see the ScalingProcesses.member.N parameter for the SuspendProcesses action in the Auto Scaling API Reference.
        :param wait_on_resource_signals: Specifies whether the Auto Scaling group waits on signals from new instances during an update. Use this property to ensure that instances have completed installing and configuring applications before the Auto Scaling group update proceeds. AWS CloudFormation suspends the update of an Auto Scaling group after new EC2 instances are launched into the group. AWS CloudFormation must receive a signal from each new instance within the specified PauseTime before continuing the update. To signal the Auto Scaling group, use the cfn-signal helper script or SignalResource API. To have instances wait for an Elastic Load Balancing health check before they signal success, add a health-check verification by using the cfn-init helper script. For an example, see the verify_instance_health command in the Auto Scaling rolling updates sample template.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if max_batch_size is not None:
            self._values["max_batch_size"] = max_batch_size
        if min_instances_in_service is not None:
            self._values["min_instances_in_service"] = min_instances_in_service
        if min_successful_instances_percent is not None:
            self._values["min_successful_instances_percent"] = min_successful_instances_percent
        if pause_time is not None:
            self._values["pause_time"] = pause_time
        if suspend_processes is not None:
            self._values["suspend_processes"] = suspend_processes
        if wait_on_resource_signals is not None:
            self._values["wait_on_resource_signals"] = wait_on_resource_signals

    @builtins.property
    def max_batch_size(self) -> typing.Optional[jsii.Number]:
        '''Specifies the maximum number of instances that AWS CloudFormation updates.'''
        result = self._values.get("max_batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_instances_in_service(self) -> typing.Optional[jsii.Number]:
        '''Specifies the minimum number of instances that must be in service within the Auto Scaling group while AWS CloudFormation updates old instances.'''
        result = self._values.get("min_instances_in_service")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_successful_instances_percent(self) -> typing.Optional[jsii.Number]:
        '''Specifies the percentage of instances in an Auto Scaling rolling update that must signal success for an update to succeed.

        You can specify a value from 0 to 100. AWS CloudFormation rounds to the nearest tenth of a percent. For example, if you
        update five instances with a minimum successful percentage of 50, three instances must signal success.

        If an instance doesn't send a signal within the time specified in the PauseTime property, AWS CloudFormation assumes
        that the instance wasn't updated.

        If you specify this property, you must also enable the WaitOnResourceSignals and PauseTime properties.
        '''
        result = self._values.get("min_successful_instances_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pause_time(self) -> typing.Optional[builtins.str]:
        '''The amount of time that AWS CloudFormation pauses after making a change to a batch of instances to give those instances time to start software applications.

        For example, you might need to specify PauseTime when scaling up the number of
        instances in an Auto Scaling group.

        If you enable the WaitOnResourceSignals property, PauseTime is the amount of time that AWS CloudFormation should wait
        for the Auto Scaling group to receive the required number of valid signals from added or replaced instances. If the
        PauseTime is exceeded before the Auto Scaling group receives the required number of signals, the update fails. For best
        results, specify a time period that gives your applications sufficient time to get started. If the update needs to be
        rolled back, a short PauseTime can cause the rollback to fail.

        Specify PauseTime in the ISO8601 duration format (in the format PT#H#M#S, where each # is the number of hours, minutes,
        and seconds, respectively). The maximum PauseTime is one hour (PT1H).
        '''
        result = self._values.get("pause_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def suspend_processes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the Auto Scaling processes to suspend during a stack update.

        Suspending processes prevents Auto Scaling from
        interfering with a stack update. For example, you can suspend alarming so that Auto Scaling doesn't execute scaling
        policies associated with an alarm. For valid values, see the ScalingProcesses.member.N parameter for the SuspendProcesses
        action in the Auto Scaling API Reference.
        '''
        result = self._values.get("suspend_processes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def wait_on_resource_signals(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether the Auto Scaling group waits on signals from new instances during an update.

        Use this property to
        ensure that instances have completed installing and configuring applications before the Auto Scaling group update proceeds.
        AWS CloudFormation suspends the update of an Auto Scaling group after new EC2 instances are launched into the group.
        AWS CloudFormation must receive a signal from each new instance within the specified PauseTime before continuing the update.
        To signal the Auto Scaling group, use the cfn-signal helper script or SignalResource API.

        To have instances wait for an Elastic Load Balancing health check before they signal success, add a health-check
        verification by using the cfn-init helper script. For an example, see the verify_instance_health command in the Auto Scaling
        rolling updates sample template.
        '''
        result = self._values.get("wait_on_resource_signals")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAutoScalingRollingUpdate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnAutoScalingScheduledAction",
    jsii_struct_bases=[],
    name_mapping={
        "ignore_unmodified_group_size_properties": "ignoreUnmodifiedGroupSizeProperties",
    },
)
class CfnAutoScalingScheduledAction:
    def __init__(
        self,
        *,
        ignore_unmodified_group_size_properties: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''With scheduled actions, the group size properties of an Auto Scaling group can change at any time.

        When you update a
        stack with an Auto Scaling group and scheduled action, AWS CloudFormation always sets the group size property values of
        your Auto Scaling group to the values that are defined in the AWS::AutoScaling::AutoScalingGroup resource of your template,
        even if a scheduled action is in effect.

        If you do not want AWS CloudFormation to change any of the group size property values when you have a scheduled action in
        effect, use the AutoScalingScheduledAction update policy to prevent AWS CloudFormation from changing the MinSize, MaxSize,
        or DesiredCapacity properties unless you have modified these values in your template.\\

        :param ignore_unmodified_group_size_properties: 
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if ignore_unmodified_group_size_properties is not None:
            self._values["ignore_unmodified_group_size_properties"] = ignore_unmodified_group_size_properties

    @builtins.property
    def ignore_unmodified_group_size_properties(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("ignore_unmodified_group_size_properties")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAutoScalingScheduledAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/core.CfnCapabilities")
class CfnCapabilities(enum.Enum):
    '''Capabilities that affect whether CloudFormation is allowed to change IAM resources.'''

    NONE = "NONE"
    '''No IAM Capabilities.

    Pass this capability if you wish to block the creation IAM resources.

    :link: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities
    '''
    ANONYMOUS_IAM = "ANONYMOUS_IAM"
    '''Capability to create anonymous IAM resources.

    Pass this capability if you're only creating anonymous resources.

    :link: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities
    '''
    NAMED_IAM = "NAMED_IAM"
    '''Capability to create named IAM resources.

    Pass this capability if you're creating IAM resources that have physical
    names.

    ``CloudFormationCapabilities.NamedIAM`` implies ``CloudFormationCapabilities.IAM``; you don't have to pass both.

    :link: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities
    '''
    AUTO_EXPAND = "AUTO_EXPAND"
    '''Capability to run CloudFormation macros.

    Pass this capability if your template includes macros, for example AWS::Include or AWS::Serverless.

    :link: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStack.html
    '''


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnCodeDeployBlueGreenAdditionalOptions",
    jsii_struct_bases=[],
    name_mapping={"termination_wait_time_in_minutes": "terminationWaitTimeInMinutes"},
)
class CfnCodeDeployBlueGreenAdditionalOptions:
    def __init__(
        self,
        *,
        termination_wait_time_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Additional options for the blue/green deployment.

        The type of the {@link CfnCodeDeployBlueGreenHookProps.additionalOptions} property.

        :param termination_wait_time_in_minutes: Specifies time to wait, in minutes, before terminating the blue resources. Default: - 5 minutes
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if termination_wait_time_in_minutes is not None:
            self._values["termination_wait_time_in_minutes"] = termination_wait_time_in_minutes

    @builtins.property
    def termination_wait_time_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Specifies time to wait, in minutes, before terminating the blue resources.

        :default: - 5 minutes
        '''
        result = self._values.get("termination_wait_time_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCodeDeployBlueGreenAdditionalOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnCodeDeployBlueGreenApplication",
    jsii_struct_bases=[],
    name_mapping={"ecs_attributes": "ecsAttributes", "target": "target"},
)
class CfnCodeDeployBlueGreenApplication:
    def __init__(
        self,
        *,
        ecs_attributes: "CfnCodeDeployBlueGreenEcsAttributes",
        target: "CfnCodeDeployBlueGreenApplicationTarget",
    ) -> None:
        '''The application actually being deployed.

        Type of the {@link CfnCodeDeployBlueGreenHookProps.applications} property.

        :param ecs_attributes: The detailed attributes of the deployed target.
        :param target: The target that is being deployed.
        '''
        if isinstance(ecs_attributes, dict):
            ecs_attributes = CfnCodeDeployBlueGreenEcsAttributes(**ecs_attributes)
        if isinstance(target, dict):
            target = CfnCodeDeployBlueGreenApplicationTarget(**target)
        self._values: typing.Dict[str, typing.Any] = {
            "ecs_attributes": ecs_attributes,
            "target": target,
        }

    @builtins.property
    def ecs_attributes(self) -> "CfnCodeDeployBlueGreenEcsAttributes":
        '''The detailed attributes of the deployed target.'''
        result = self._values.get("ecs_attributes")
        assert result is not None, "Required property 'ecs_attributes' is missing"
        return typing.cast("CfnCodeDeployBlueGreenEcsAttributes", result)

    @builtins.property
    def target(self) -> "CfnCodeDeployBlueGreenApplicationTarget":
        '''The target that is being deployed.'''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast("CfnCodeDeployBlueGreenApplicationTarget", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCodeDeployBlueGreenApplication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnCodeDeployBlueGreenApplicationTarget",
    jsii_struct_bases=[],
    name_mapping={"logical_id": "logicalId", "type": "type"},
)
class CfnCodeDeployBlueGreenApplicationTarget:
    def __init__(self, *, logical_id: builtins.str, type: builtins.str) -> None:
        '''Type of the {@link CfnCodeDeployBlueGreenApplication.target} property.

        :param logical_id: The logical id of the target resource.
        :param type: The resource type of the target being deployed. Right now, the only allowed value is 'AWS::ECS::Service'.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "logical_id": logical_id,
            "type": type,
        }

    @builtins.property
    def logical_id(self) -> builtins.str:
        '''The logical id of the target resource.'''
        result = self._values.get("logical_id")
        assert result is not None, "Required property 'logical_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The resource type of the target being deployed.

        Right now, the only allowed value is 'AWS::ECS::Service'.
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCodeDeployBlueGreenApplicationTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnCodeDeployBlueGreenEcsAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "task_definitions": "taskDefinitions",
        "task_sets": "taskSets",
        "traffic_routing": "trafficRouting",
    },
)
class CfnCodeDeployBlueGreenEcsAttributes:
    def __init__(
        self,
        *,
        task_definitions: typing.Sequence[builtins.str],
        task_sets: typing.Sequence[builtins.str],
        traffic_routing: "CfnTrafficRouting",
    ) -> None:
        '''The attributes of the ECS Service being deployed.

        Type of the {@link CfnCodeDeployBlueGreenApplication.ecsAttributes} property.

        :param task_definitions: The logical IDs of the blue and green, respectively, AWS::ECS::TaskDefinition task definitions.
        :param task_sets: The logical IDs of the blue and green, respectively, AWS::ECS::TaskSet task sets.
        :param traffic_routing: The traffic routing configuration.
        '''
        if isinstance(traffic_routing, dict):
            traffic_routing = CfnTrafficRouting(**traffic_routing)
        self._values: typing.Dict[str, typing.Any] = {
            "task_definitions": task_definitions,
            "task_sets": task_sets,
            "traffic_routing": traffic_routing,
        }

    @builtins.property
    def task_definitions(self) -> typing.List[builtins.str]:
        '''The logical IDs of the blue and green, respectively, AWS::ECS::TaskDefinition task definitions.'''
        result = self._values.get("task_definitions")
        assert result is not None, "Required property 'task_definitions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def task_sets(self) -> typing.List[builtins.str]:
        '''The logical IDs of the blue and green, respectively, AWS::ECS::TaskSet task sets.'''
        result = self._values.get("task_sets")
        assert result is not None, "Required property 'task_sets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def traffic_routing(self) -> "CfnTrafficRouting":
        '''The traffic routing configuration.'''
        result = self._values.get("traffic_routing")
        assert result is not None, "Required property 'traffic_routing' is missing"
        return typing.cast("CfnTrafficRouting", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCodeDeployBlueGreenEcsAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnCodeDeployBlueGreenHookProps",
    jsii_struct_bases=[],
    name_mapping={
        "applications": "applications",
        "service_role": "serviceRole",
        "additional_options": "additionalOptions",
        "lifecycle_event_hooks": "lifecycleEventHooks",
        "traffic_routing_config": "trafficRoutingConfig",
    },
)
class CfnCodeDeployBlueGreenHookProps:
    def __init__(
        self,
        *,
        applications: typing.Sequence[CfnCodeDeployBlueGreenApplication],
        service_role: builtins.str,
        additional_options: typing.Optional[CfnCodeDeployBlueGreenAdditionalOptions] = None,
        lifecycle_event_hooks: typing.Optional["CfnCodeDeployBlueGreenLifecycleEventHooks"] = None,
        traffic_routing_config: typing.Optional["CfnTrafficRoutingConfig"] = None,
    ) -> None:
        '''Construction properties of {@link CfnCodeDeployBlueGreenHook}.

        :param applications: Properties of the Amazon ECS applications being deployed.
        :param service_role: The IAM Role for CloudFormation to use to perform blue-green deployments.
        :param additional_options: Additional options for the blue/green deployment. Default: - no additional options
        :param lifecycle_event_hooks: Use lifecycle event hooks to specify a Lambda function that CodeDeploy can call to validate a deployment. You can use the same function or a different one for deployment lifecycle events. Following completion of the validation tests, the Lambda {@link CfnCodeDeployBlueGreenLifecycleEventHooks.afterAllowTraffic} function calls back CodeDeploy and delivers a result of 'Succeeded' or 'Failed'. Default: - no lifecycle event hooks
        :param traffic_routing_config: Traffic routing configuration settings. Default: - time-based canary traffic shifting, with a 15% step percentage and a five minute bake time
        '''
        if isinstance(additional_options, dict):
            additional_options = CfnCodeDeployBlueGreenAdditionalOptions(**additional_options)
        if isinstance(lifecycle_event_hooks, dict):
            lifecycle_event_hooks = CfnCodeDeployBlueGreenLifecycleEventHooks(**lifecycle_event_hooks)
        if isinstance(traffic_routing_config, dict):
            traffic_routing_config = CfnTrafficRoutingConfig(**traffic_routing_config)
        self._values: typing.Dict[str, typing.Any] = {
            "applications": applications,
            "service_role": service_role,
        }
        if additional_options is not None:
            self._values["additional_options"] = additional_options
        if lifecycle_event_hooks is not None:
            self._values["lifecycle_event_hooks"] = lifecycle_event_hooks
        if traffic_routing_config is not None:
            self._values["traffic_routing_config"] = traffic_routing_config

    @builtins.property
    def applications(self) -> typing.List[CfnCodeDeployBlueGreenApplication]:
        '''Properties of the Amazon ECS applications being deployed.'''
        result = self._values.get("applications")
        assert result is not None, "Required property 'applications' is missing"
        return typing.cast(typing.List[CfnCodeDeployBlueGreenApplication], result)

    @builtins.property
    def service_role(self) -> builtins.str:
        '''The IAM Role for CloudFormation to use to perform blue-green deployments.'''
        result = self._values.get("service_role")
        assert result is not None, "Required property 'service_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_options(
        self,
    ) -> typing.Optional[CfnCodeDeployBlueGreenAdditionalOptions]:
        '''Additional options for the blue/green deployment.

        :default: - no additional options
        '''
        result = self._values.get("additional_options")
        return typing.cast(typing.Optional[CfnCodeDeployBlueGreenAdditionalOptions], result)

    @builtins.property
    def lifecycle_event_hooks(
        self,
    ) -> typing.Optional["CfnCodeDeployBlueGreenLifecycleEventHooks"]:
        '''Use lifecycle event hooks to specify a Lambda function that CodeDeploy can call to validate a deployment.

        You can use the same function or a different one for deployment lifecycle events.
        Following completion of the validation tests,
        the Lambda {@link CfnCodeDeployBlueGreenLifecycleEventHooks.afterAllowTraffic}
        function calls back CodeDeploy and delivers a result of 'Succeeded' or 'Failed'.

        :default: - no lifecycle event hooks
        '''
        result = self._values.get("lifecycle_event_hooks")
        return typing.cast(typing.Optional["CfnCodeDeployBlueGreenLifecycleEventHooks"], result)

    @builtins.property
    def traffic_routing_config(self) -> typing.Optional["CfnTrafficRoutingConfig"]:
        '''Traffic routing configuration settings.

        :default: - time-based canary traffic shifting, with a 15% step percentage and a five minute bake time
        '''
        result = self._values.get("traffic_routing_config")
        return typing.cast(typing.Optional["CfnTrafficRoutingConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCodeDeployBlueGreenHookProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnCodeDeployBlueGreenLifecycleEventHooks",
    jsii_struct_bases=[],
    name_mapping={
        "after_allow_test_traffic": "afterAllowTestTraffic",
        "after_allow_traffic": "afterAllowTraffic",
        "after_install": "afterInstall",
        "before_allow_traffic": "beforeAllowTraffic",
        "before_install": "beforeInstall",
    },
)
class CfnCodeDeployBlueGreenLifecycleEventHooks:
    def __init__(
        self,
        *,
        after_allow_test_traffic: typing.Optional[builtins.str] = None,
        after_allow_traffic: typing.Optional[builtins.str] = None,
        after_install: typing.Optional[builtins.str] = None,
        before_allow_traffic: typing.Optional[builtins.str] = None,
        before_install: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Lifecycle events for blue-green deployments.

        The type of the {@link CfnCodeDeployBlueGreenHookProps.lifecycleEventHooks} property.

        :param after_allow_test_traffic: Function to use to run tasks after the test listener serves traffic to the replacement task set. Default: - none
        :param after_allow_traffic: Function to use to run tasks after the second target group serves traffic to the replacement task set. Default: - none
        :param after_install: Function to use to run tasks after the replacement task set is created and one of the target groups is associated with it. Default: - none
        :param before_allow_traffic: Function to use to run tasks after the second target group is associated with the replacement task set, but before traffic is shifted to the replacement task set. Default: - none
        :param before_install: Function to use to run tasks before the replacement task set is created. Default: - none
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if after_allow_test_traffic is not None:
            self._values["after_allow_test_traffic"] = after_allow_test_traffic
        if after_allow_traffic is not None:
            self._values["after_allow_traffic"] = after_allow_traffic
        if after_install is not None:
            self._values["after_install"] = after_install
        if before_allow_traffic is not None:
            self._values["before_allow_traffic"] = before_allow_traffic
        if before_install is not None:
            self._values["before_install"] = before_install

    @builtins.property
    def after_allow_test_traffic(self) -> typing.Optional[builtins.str]:
        '''Function to use to run tasks after the test listener serves traffic to the replacement task set.

        :default: - none
        '''
        result = self._values.get("after_allow_test_traffic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def after_allow_traffic(self) -> typing.Optional[builtins.str]:
        '''Function to use to run tasks after the second target group serves traffic to the replacement task set.

        :default: - none
        '''
        result = self._values.get("after_allow_traffic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def after_install(self) -> typing.Optional[builtins.str]:
        '''Function to use to run tasks after the replacement task set is created and one of the target groups is associated with it.

        :default: - none
        '''
        result = self._values.get("after_install")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def before_allow_traffic(self) -> typing.Optional[builtins.str]:
        '''Function to use to run tasks after the second target group is associated with the replacement task set, but before traffic is shifted to the replacement task set.

        :default: - none
        '''
        result = self._values.get("before_allow_traffic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def before_install(self) -> typing.Optional[builtins.str]:
        '''Function to use to run tasks before the replacement task set is created.

        :default: - none
        '''
        result = self._values.get("before_install")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCodeDeployBlueGreenLifecycleEventHooks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnCodeDeployLambdaAliasUpdate",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "deployment_group_name": "deploymentGroupName",
        "after_allow_traffic_hook": "afterAllowTrafficHook",
        "before_allow_traffic_hook": "beforeAllowTrafficHook",
    },
)
class CfnCodeDeployLambdaAliasUpdate:
    def __init__(
        self,
        *,
        application_name: builtins.str,
        deployment_group_name: builtins.str,
        after_allow_traffic_hook: typing.Optional[builtins.str] = None,
        before_allow_traffic_hook: typing.Optional[builtins.str] = None,
    ) -> None:
        '''To perform an AWS CodeDeploy deployment when the version changes on an AWS::Lambda::Alias resource, use the CodeDeployLambdaAliasUpdate update policy.

        :param application_name: The name of the AWS CodeDeploy application.
        :param deployment_group_name: The name of the AWS CodeDeploy deployment group. This is where the traffic-shifting policy is set.
        :param after_allow_traffic_hook: The name of the Lambda function to run after traffic routing completes.
        :param before_allow_traffic_hook: The name of the Lambda function to run before traffic routing starts.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_name": application_name,
            "deployment_group_name": deployment_group_name,
        }
        if after_allow_traffic_hook is not None:
            self._values["after_allow_traffic_hook"] = after_allow_traffic_hook
        if before_allow_traffic_hook is not None:
            self._values["before_allow_traffic_hook"] = before_allow_traffic_hook

    @builtins.property
    def application_name(self) -> builtins.str:
        '''The name of the AWS CodeDeploy application.'''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deployment_group_name(self) -> builtins.str:
        '''The name of the AWS CodeDeploy deployment group.

        This is where the traffic-shifting policy is set.
        '''
        result = self._values.get("deployment_group_name")
        assert result is not None, "Required property 'deployment_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def after_allow_traffic_hook(self) -> typing.Optional[builtins.str]:
        '''The name of the Lambda function to run after traffic routing completes.'''
        result = self._values.get("after_allow_traffic_hook")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def before_allow_traffic_hook(self) -> typing.Optional[builtins.str]:
        '''The name of the Lambda function to run before traffic routing starts.'''
        result = self._values.get("before_allow_traffic_hook")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCodeDeployLambdaAliasUpdate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnConditionProps",
    jsii_struct_bases=[],
    name_mapping={"expression": "expression"},
)
class CfnConditionProps:
    def __init__(
        self,
        *,
        expression: typing.Optional["ICfnConditionExpression"] = None,
    ) -> None:
        '''
        :param expression: The expression that the condition will evaluate. Default: - None.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if expression is not None:
            self._values["expression"] = expression

    @builtins.property
    def expression(self) -> typing.Optional["ICfnConditionExpression"]:
        '''The expression that the condition will evaluate.

        :default: - None.
        '''
        result = self._values.get("expression")
        return typing.cast(typing.Optional["ICfnConditionExpression"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConditionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnCreationPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "auto_scaling_creation_policy": "autoScalingCreationPolicy",
        "resource_signal": "resourceSignal",
    },
)
class CfnCreationPolicy:
    def __init__(
        self,
        *,
        auto_scaling_creation_policy: typing.Optional["CfnResourceAutoScalingCreationPolicy"] = None,
        resource_signal: typing.Optional["CfnResourceSignal"] = None,
    ) -> None:
        '''Associate the CreationPolicy attribute with a resource to prevent its status from reaching create complete until AWS CloudFormation receives a specified number of success signals or the timeout period is exceeded.

        To signal a
        resource, you can use the cfn-signal helper script or SignalResource API. AWS CloudFormation publishes valid signals
        to the stack events so that you track the number of signals sent.

        The creation policy is invoked only when AWS CloudFormation creates the associated resource. Currently, the only
        AWS CloudFormation resources that support creation policies are AWS::AutoScaling::AutoScalingGroup, AWS::EC2::Instance,
        and AWS::CloudFormation::WaitCondition.

        Use the CreationPolicy attribute when you want to wait on resource configuration actions before stack creation proceeds.
        For example, if you install and configure software applications on an EC2 instance, you might want those applications to
        be running before proceeding. In such cases, you can add a CreationPolicy attribute to the instance, and then send a success
        signal to the instance after the applications are installed and configured. For a detailed example, see Deploying Applications
        on Amazon EC2 with AWS CloudFormation.

        :param auto_scaling_creation_policy: For an Auto Scaling group replacement update, specifies how many instances must signal success for the update to succeed.
        :param resource_signal: When AWS CloudFormation creates the associated resource, configures the number of required success signals and the length of time that AWS CloudFormation waits for those signals.
        '''
        if isinstance(auto_scaling_creation_policy, dict):
            auto_scaling_creation_policy = CfnResourceAutoScalingCreationPolicy(**auto_scaling_creation_policy)
        if isinstance(resource_signal, dict):
            resource_signal = CfnResourceSignal(**resource_signal)
        self._values: typing.Dict[str, typing.Any] = {}
        if auto_scaling_creation_policy is not None:
            self._values["auto_scaling_creation_policy"] = auto_scaling_creation_policy
        if resource_signal is not None:
            self._values["resource_signal"] = resource_signal

    @builtins.property
    def auto_scaling_creation_policy(
        self,
    ) -> typing.Optional["CfnResourceAutoScalingCreationPolicy"]:
        '''For an Auto Scaling group replacement update, specifies how many instances must signal success for the update to succeed.'''
        result = self._values.get("auto_scaling_creation_policy")
        return typing.cast(typing.Optional["CfnResourceAutoScalingCreationPolicy"], result)

    @builtins.property
    def resource_signal(self) -> typing.Optional["CfnResourceSignal"]:
        '''When AWS CloudFormation creates the associated resource, configures the number of required success signals and the length of time that AWS CloudFormation waits for those signals.'''
        result = self._values.get("resource_signal")
        return typing.cast(typing.Optional["CfnResourceSignal"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCreationPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnCustomResourceProps",
    jsii_struct_bases=[],
    name_mapping={"service_token": "serviceToken"},
)
class CfnCustomResourceProps:
    def __init__(self, *, service_token: builtins.str) -> None:
        '''Properties for defining a ``AWS::CloudFormation::CustomResource``.

        :param service_token: ``AWS::CloudFormation::CustomResource.ServiceToken``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "service_token": service_token,
        }

    @builtins.property
    def service_token(self) -> builtins.str:
        '''``AWS::CloudFormation::CustomResource.ServiceToken``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html#cfn-customresource-servicetoken
        '''
        result = self._values.get("service_token")
        assert result is not None, "Required property 'service_token' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCustomResourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/core.CfnDeletionPolicy")
class CfnDeletionPolicy(enum.Enum):
    '''With the DeletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted.

    You specify a DeletionPolicy attribute for each resource that you want to control. If a resource has no DeletionPolicy
    attribute, AWS CloudFormation deletes the resource by default. Note that this capability also applies to update operations
    that lead to resources being removed.
    '''

    DELETE = "DELETE"
    '''AWS CloudFormation deletes the resource and all its content if applicable during stack deletion.

    You can add this
    deletion policy to any resource type. By default, if you don't specify a DeletionPolicy, AWS CloudFormation deletes
    your resources. However, be aware of the following considerations:
    '''
    RETAIN = "RETAIN"
    '''AWS CloudFormation keeps the resource without deleting the resource or its contents when its stack is deleted.

    You can add this deletion policy to any resource type. Note that when AWS CloudFormation completes the stack deletion,
    the stack will be in Delete_Complete state; however, resources that are retained continue to exist and continue to incur
    applicable charges until you delete those resources.
    '''
    SNAPSHOT = "SNAPSHOT"
    '''For resources that support snapshots (AWS::EC2::Volume, AWS::ElastiCache::CacheCluster, AWS::ElastiCache::ReplicationGroup, AWS::RDS::DBInstance, AWS::RDS::DBCluster, and AWS::Redshift::Cluster), AWS CloudFormation creates a snapshot for the resource before deleting it.

    Note that when AWS CloudFormation completes the stack deletion, the stack will be in the
    Delete_Complete state; however, the snapshots that are created with this policy continue to exist and continue to
    incur applicable charges until you delete those snapshots.
    '''


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnDynamicReferenceProps",
    jsii_struct_bases=[],
    name_mapping={"reference_key": "referenceKey", "service": "service"},
)
class CfnDynamicReferenceProps:
    def __init__(
        self,
        *,
        reference_key: builtins.str,
        service: "CfnDynamicReferenceService",
    ) -> None:
        '''Properties for a Dynamic Reference.

        :param reference_key: The reference key of the dynamic reference.
        :param service: The service to retrieve the dynamic reference from.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "reference_key": reference_key,
            "service": service,
        }

    @builtins.property
    def reference_key(self) -> builtins.str:
        '''The reference key of the dynamic reference.'''
        result = self._values.get("reference_key")
        assert result is not None, "Required property 'reference_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> "CfnDynamicReferenceService":
        '''The service to retrieve the dynamic reference from.'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast("CfnDynamicReferenceService", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDynamicReferenceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/core.CfnDynamicReferenceService")
class CfnDynamicReferenceService(enum.Enum):
    '''The service to retrieve the dynamic reference from.'''

    SSM = "SSM"
    '''Plaintext value stored in AWS Systems Manager Parameter Store.'''
    SSM_SECURE = "SSM_SECURE"
    '''Secure string stored in AWS Systems Manager Parameter Store.'''
    SECRETS_MANAGER = "SECRETS_MANAGER"
    '''Secret stored in AWS Secrets Manager.'''


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnHookProps",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "properties": "properties"},
)
class CfnHookProps:
    def __init__(
        self,
        *,
        type: builtins.str,
        properties: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''Construction properties of {@link CfnHook}.

        :param type: The type of the hook (for example, "AWS::CodeDeploy::BlueGreen").
        :param properties: The properties of the hook. Default: - no properties
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if properties is not None:
            self._values["properties"] = properties

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the hook (for example, "AWS::CodeDeploy::BlueGreen").'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''The properties of the hook.

        :default: - no properties
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHookProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnIncludeProps",
    jsii_struct_bases=[],
    name_mapping={"template": "template"},
)
class CfnIncludeProps:
    def __init__(self, *, template: typing.Mapping[typing.Any, typing.Any]) -> None:
        '''(deprecated) Construction properties for {@link CfnInclude}.

        :param template: (deprecated) The CloudFormation template to include in the stack (as is).

        :deprecated: use the CfnInclude class from the cloudformation-include module instead

        :stability: deprecated
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "template": template,
        }

    @builtins.property
    def template(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''(deprecated) The CloudFormation template to include in the stack (as is).

        :stability: deprecated
        '''
        result = self._values.get("template")
        assert result is not None, "Required property 'template' is missing"
        return typing.cast(typing.Mapping[typing.Any, typing.Any], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIncludeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnJsonProps",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class CfnJsonProps:
    def __init__(self, *, value: typing.Any) -> None:
        '''
        :param value: The value to resolve. Can be any JavaScript object, including tokens and references in keys or values.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(self) -> typing.Any:
        '''The value to resolve.

        Can be any JavaScript object, including tokens and
        references in keys or values.
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnJsonProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnMacroProps",
    jsii_struct_bases=[],
    name_mapping={
        "function_name": "functionName",
        "name": "name",
        "description": "description",
        "log_group_name": "logGroupName",
        "log_role_arn": "logRoleArn",
    },
)
class CfnMacroProps:
    def __init__(
        self,
        *,
        function_name: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::Macro``.

        :param function_name: ``AWS::CloudFormation::Macro.FunctionName``.
        :param name: ``AWS::CloudFormation::Macro.Name``.
        :param description: ``AWS::CloudFormation::Macro.Description``.
        :param log_group_name: ``AWS::CloudFormation::Macro.LogGroupName``.
        :param log_role_arn: ``AWS::CloudFormation::Macro.LogRoleARN``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "function_name": function_name,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if log_group_name is not None:
            self._values["log_group_name"] = log_group_name
        if log_role_arn is not None:
            self._values["log_role_arn"] = log_role_arn

    @builtins.property
    def function_name(self) -> builtins.str:
        '''``AWS::CloudFormation::Macro.FunctionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-functionname
        '''
        result = self._values.get("function_name")
        assert result is not None, "Required property 'function_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::CloudFormation::Macro.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::Macro.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::Macro.LogGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-loggroupname
        '''
        result = self._values.get("log_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::Macro.LogRoleARN``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-logrolearn
        '''
        result = self._values.get("log_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMacroProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnMappingProps",
    jsii_struct_bases=[],
    name_mapping={"mapping": "mapping"},
)
class CfnMappingProps:
    def __init__(
        self,
        *,
        mapping: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param mapping: Mapping of key to a set of corresponding set of named values. The key identifies a map of name-value pairs and must be unique within the mapping. For example, if you want to set values based on a region, you can create a mapping that uses the region name as a key and contains the values you want to specify for each specific region. Default: - No mapping.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if mapping is not None:
            self._values["mapping"] = mapping

    @builtins.property
    def mapping(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]]:
        '''Mapping of key to a set of corresponding set of named values.

        The key identifies a map of name-value pairs and must be unique within the mapping.

        For example, if you want to set values based on a region, you can create a mapping
        that uses the region name as a key and contains the values you want to specify for
        each specific region.

        :default: - No mapping.
        '''
        result = self._values.get("mapping")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMappingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnModuleDefaultVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "module_name": "moduleName",
        "version_id": "versionId",
    },
)
class CfnModuleDefaultVersionProps:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        module_name: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::ModuleDefaultVersion``.

        :param arn: ``AWS::CloudFormation::ModuleDefaultVersion.Arn``.
        :param module_name: ``AWS::CloudFormation::ModuleDefaultVersion.ModuleName``.
        :param version_id: ``AWS::CloudFormation::ModuleDefaultVersion.VersionId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if module_name is not None:
            self._values["module_name"] = module_name
        if version_id is not None:
            self._values["version_id"] = version_id

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ModuleDefaultVersion.Arn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html#cfn-cloudformation-moduledefaultversion-arn
        '''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def module_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ModuleDefaultVersion.ModuleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html#cfn-cloudformation-moduledefaultversion-modulename
        '''
        result = self._values.get("module_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ModuleDefaultVersion.VersionId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html#cfn-cloudformation-moduledefaultversion-versionid
        '''
        result = self._values.get("version_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModuleDefaultVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnModuleVersionProps",
    jsii_struct_bases=[],
    name_mapping={"module_name": "moduleName", "module_package": "modulePackage"},
)
class CfnModuleVersionProps:
    def __init__(
        self,
        *,
        module_name: builtins.str,
        module_package: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::ModuleVersion``.

        :param module_name: ``AWS::CloudFormation::ModuleVersion.ModuleName``.
        :param module_package: ``AWS::CloudFormation::ModuleVersion.ModulePackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "module_name": module_name,
            "module_package": module_package,
        }

    @builtins.property
    def module_name(self) -> builtins.str:
        '''``AWS::CloudFormation::ModuleVersion.ModuleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html#cfn-cloudformation-moduleversion-modulename
        '''
        result = self._values.get("module_name")
        assert result is not None, "Required property 'module_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def module_package(self) -> builtins.str:
        '''``AWS::CloudFormation::ModuleVersion.ModulePackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html#cfn-cloudformation-moduleversion-modulepackage
        '''
        result = self._values.get("module_package")
        assert result is not None, "Required property 'module_package' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModuleVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnOutputProps",
    jsii_struct_bases=[],
    name_mapping={
        "value": "value",
        "condition": "condition",
        "description": "description",
        "export_name": "exportName",
    },
)
class CfnOutputProps:
    def __init__(
        self,
        *,
        value: builtins.str,
        condition: typing.Optional["CfnCondition"] = None,
        description: typing.Optional[builtins.str] = None,
        export_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param value: The value of the property returned by the aws cloudformation describe-stacks command. The value of an output can include literals, parameter references, pseudo-parameters, a mapping value, or intrinsic functions.
        :param condition: A condition to associate with this output value. If the condition evaluates to ``false``, this output value will not be included in the stack. Default: - No condition is associated with the output.
        :param description: A String type that describes the output value. The description can be a maximum of 4 K in length. Default: - No description.
        :param export_name: The name used to export the value of this output across stacks. To import the value from another stack, use ``Fn.importValue(exportName)``. Default: - the output is not exported
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }
        if condition is not None:
            self._values["condition"] = condition
        if description is not None:
            self._values["description"] = description
        if export_name is not None:
            self._values["export_name"] = export_name

    @builtins.property
    def value(self) -> builtins.str:
        '''The value of the property returned by the aws cloudformation describe-stacks command.

        The value of an output can include literals, parameter references, pseudo-parameters,
        a mapping value, or intrinsic functions.
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition(self) -> typing.Optional["CfnCondition"]:
        '''A condition to associate with this output value.

        If the condition evaluates
        to ``false``, this output value will not be included in the stack.

        :default: - No condition is associated with the output.
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional["CfnCondition"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A String type that describes the output value.

        The description can be a maximum of 4 K in length.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def export_name(self) -> typing.Optional[builtins.str]:
        '''The name used to export the value of this output across stacks.

        To import the value from another stack, use ``Fn.importValue(exportName)``.

        :default: - the output is not exported
        '''
        result = self._values.get("export_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOutputProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnParameterProps",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_pattern": "allowedPattern",
        "allowed_values": "allowedValues",
        "constraint_description": "constraintDescription",
        "default": "default",
        "description": "description",
        "max_length": "maxLength",
        "max_value": "maxValue",
        "min_length": "minLength",
        "min_value": "minValue",
        "no_echo": "noEcho",
        "type": "type",
    },
)
class CfnParameterProps:
    def __init__(
        self,
        *,
        allowed_pattern: typing.Optional[builtins.str] = None,
        allowed_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        constraint_description: typing.Optional[builtins.str] = None,
        default: typing.Any = None,
        description: typing.Optional[builtins.str] = None,
        max_length: typing.Optional[jsii.Number] = None,
        max_value: typing.Optional[jsii.Number] = None,
        min_length: typing.Optional[jsii.Number] = None,
        min_value: typing.Optional[jsii.Number] = None,
        no_echo: typing.Optional[builtins.bool] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allowed_pattern: A regular expression that represents the patterns to allow for String types. Default: - No constraints on patterns allowed for parameter.
        :param allowed_values: An array containing the list of values allowed for the parameter. Default: - No constraints on values allowed for parameter.
        :param constraint_description: A string that explains a constraint when the constraint is violated. For example, without a constraint description, a parameter that has an allowed pattern of [A-Za-z0-9]+ displays the following error message when the user specifies an invalid value: Default: - No description with customized error message when user specifies invalid values.
        :param default: A value of the appropriate type for the template to use if no value is specified when a stack is created. If you define constraints for the parameter, you must specify a value that adheres to those constraints. Default: - No default value for parameter.
        :param description: A string of up to 4000 characters that describes the parameter. Default: - No description for the parameter.
        :param max_length: An integer value that determines the largest number of characters you want to allow for String types. Default: - None.
        :param max_value: A numeric value that determines the largest numeric value you want to allow for Number types. Default: - None.
        :param min_length: An integer value that determines the smallest number of characters you want to allow for String types. Default: - None.
        :param min_value: A numeric value that determines the smallest numeric value you want to allow for Number types. Default: - None.
        :param no_echo: Whether to mask the parameter value when anyone makes a call that describes the stack. If you set the value to ``true``, the parameter value is masked with asterisks (``*****``). Default: - Parameter values are not masked.
        :param type: The data type for the parameter (DataType). Default: String
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed_pattern is not None:
            self._values["allowed_pattern"] = allowed_pattern
        if allowed_values is not None:
            self._values["allowed_values"] = allowed_values
        if constraint_description is not None:
            self._values["constraint_description"] = constraint_description
        if default is not None:
            self._values["default"] = default
        if description is not None:
            self._values["description"] = description
        if max_length is not None:
            self._values["max_length"] = max_length
        if max_value is not None:
            self._values["max_value"] = max_value
        if min_length is not None:
            self._values["min_length"] = min_length
        if min_value is not None:
            self._values["min_value"] = min_value
        if no_echo is not None:
            self._values["no_echo"] = no_echo
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def allowed_pattern(self) -> typing.Optional[builtins.str]:
        '''A regular expression that represents the patterns to allow for String types.

        :default: - No constraints on patterns allowed for parameter.
        '''
        result = self._values.get("allowed_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def allowed_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array containing the list of values allowed for the parameter.

        :default: - No constraints on values allowed for parameter.
        '''
        result = self._values.get("allowed_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def constraint_description(self) -> typing.Optional[builtins.str]:
        '''A string that explains a constraint when the constraint is violated.

        For example, without a constraint description, a parameter that has an allowed
        pattern of [A-Za-z0-9]+ displays the following error message when the user specifies
        an invalid value:

        :default: - No description with customized error message when user specifies invalid values.
        '''
        result = self._values.get("constraint_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default(self) -> typing.Any:
        '''A value of the appropriate type for the template to use if no value is specified when a stack is created.

        If you define constraints for the parameter, you must specify
        a value that adheres to those constraints.

        :default: - No default value for parameter.
        '''
        result = self._values.get("default")
        return typing.cast(typing.Any, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A string of up to 4000 characters that describes the parameter.

        :default: - No description for the parameter.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_length(self) -> typing.Optional[jsii.Number]:
        '''An integer value that determines the largest number of characters you want to allow for String types.

        :default: - None.
        '''
        result = self._values.get("max_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_value(self) -> typing.Optional[jsii.Number]:
        '''A numeric value that determines the largest numeric value you want to allow for Number types.

        :default: - None.
        '''
        result = self._values.get("max_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_length(self) -> typing.Optional[jsii.Number]:
        '''An integer value that determines the smallest number of characters you want to allow for String types.

        :default: - None.
        '''
        result = self._values.get("min_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_value(self) -> typing.Optional[jsii.Number]:
        '''A numeric value that determines the smallest numeric value you want to allow for Number types.

        :default: - None.
        '''
        result = self._values.get("min_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def no_echo(self) -> typing.Optional[builtins.bool]:
        '''Whether to mask the parameter value when anyone makes a call that describes the stack.

        If you set the value to ``true``, the parameter value is masked with asterisks (``*****``).

        :default: - Parameter values are not masked.
        '''
        result = self._values.get("no_echo")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The data type for the parameter (DataType).

        :default: String
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnParameterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnPublicTypeVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "arn": "arn",
        "log_delivery_bucket": "logDeliveryBucket",
        "public_version_number": "publicVersionNumber",
        "type": "type",
        "type_name": "typeName",
    },
)
class CfnPublicTypeVersionProps:
    def __init__(
        self,
        *,
        arn: typing.Optional[builtins.str] = None,
        log_delivery_bucket: typing.Optional[builtins.str] = None,
        public_version_number: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::PublicTypeVersion``.

        :param arn: ``AWS::CloudFormation::PublicTypeVersion.Arn``.
        :param log_delivery_bucket: ``AWS::CloudFormation::PublicTypeVersion.LogDeliveryBucket``.
        :param public_version_number: ``AWS::CloudFormation::PublicTypeVersion.PublicVersionNumber``.
        :param type: ``AWS::CloudFormation::PublicTypeVersion.Type``.
        :param type_name: ``AWS::CloudFormation::PublicTypeVersion.TypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if arn is not None:
            self._values["arn"] = arn
        if log_delivery_bucket is not None:
            self._values["log_delivery_bucket"] = log_delivery_bucket
        if public_version_number is not None:
            self._values["public_version_number"] = public_version_number
        if type is not None:
            self._values["type"] = type
        if type_name is not None:
            self._values["type_name"] = type_name

    @builtins.property
    def arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::PublicTypeVersion.Arn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-arn
        '''
        result = self._values.get("arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_delivery_bucket(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::PublicTypeVersion.LogDeliveryBucket``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-logdeliverybucket
        '''
        result = self._values.get("log_delivery_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_version_number(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::PublicTypeVersion.PublicVersionNumber``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-publicversionnumber
        '''
        result = self._values.get("public_version_number")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::PublicTypeVersion.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::PublicTypeVersion.TypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-typename
        '''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPublicTypeVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnPublisherProps",
    jsii_struct_bases=[],
    name_mapping={
        "accept_terms_and_conditions": "acceptTermsAndConditions",
        "connection_arn": "connectionArn",
    },
)
class CfnPublisherProps:
    def __init__(
        self,
        *,
        accept_terms_and_conditions: typing.Union[builtins.bool, "IResolvable"],
        connection_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::Publisher``.

        :param accept_terms_and_conditions: ``AWS::CloudFormation::Publisher.AcceptTermsAndConditions``.
        :param connection_arn: ``AWS::CloudFormation::Publisher.ConnectionArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "accept_terms_and_conditions": accept_terms_and_conditions,
        }
        if connection_arn is not None:
            self._values["connection_arn"] = connection_arn

    @builtins.property
    def accept_terms_and_conditions(self) -> typing.Union[builtins.bool, "IResolvable"]:
        '''``AWS::CloudFormation::Publisher.AcceptTermsAndConditions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html#cfn-cloudformation-publisher-accepttermsandconditions
        '''
        result = self._values.get("accept_terms_and_conditions")
        assert result is not None, "Required property 'accept_terms_and_conditions' is missing"
        return typing.cast(typing.Union[builtins.bool, "IResolvable"], result)

    @builtins.property
    def connection_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::Publisher.ConnectionArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html#cfn-cloudformation-publisher-connectionarn
        '''
        result = self._values.get("connection_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPublisherProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnResourceAutoScalingCreationPolicy",
    jsii_struct_bases=[],
    name_mapping={"min_successful_instances_percent": "minSuccessfulInstancesPercent"},
)
class CfnResourceAutoScalingCreationPolicy:
    def __init__(
        self,
        *,
        min_successful_instances_percent: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''For an Auto Scaling group replacement update, specifies how many instances must signal success for the update to succeed.

        :param min_successful_instances_percent: Specifies the percentage of instances in an Auto Scaling replacement update that must signal success for the update to succeed. You can specify a value from 0 to 100. AWS CloudFormation rounds to the nearest tenth of a percent. For example, if you update five instances with a minimum successful percentage of 50, three instances must signal success. If an instance doesn't send a signal within the time specified by the Timeout property, AWS CloudFormation assumes that the instance wasn't created.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if min_successful_instances_percent is not None:
            self._values["min_successful_instances_percent"] = min_successful_instances_percent

    @builtins.property
    def min_successful_instances_percent(self) -> typing.Optional[jsii.Number]:
        '''Specifies the percentage of instances in an Auto Scaling replacement update that must signal success for the update to succeed.

        You can specify a value from 0 to 100. AWS CloudFormation rounds to the nearest tenth of a percent.
        For example, if you update five instances with a minimum successful percentage of 50, three instances must signal success.
        If an instance doesn't send a signal within the time specified by the Timeout property, AWS CloudFormation assumes that the
        instance wasn't created.
        '''
        result = self._values.get("min_successful_instances_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceAutoScalingCreationPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnResourceDefaultVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "type_name": "typeName",
        "type_version_arn": "typeVersionArn",
        "version_id": "versionId",
    },
)
class CfnResourceDefaultVersionProps:
    def __init__(
        self,
        *,
        type_name: typing.Optional[builtins.str] = None,
        type_version_arn: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::ResourceDefaultVersion``.

        :param type_name: ``AWS::CloudFormation::ResourceDefaultVersion.TypeName``.
        :param type_version_arn: ``AWS::CloudFormation::ResourceDefaultVersion.TypeVersionArn``.
        :param version_id: ``AWS::CloudFormation::ResourceDefaultVersion.VersionId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if type_name is not None:
            self._values["type_name"] = type_name
        if type_version_arn is not None:
            self._values["type_version_arn"] = type_version_arn
        if version_id is not None:
            self._values["version_id"] = version_id

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ResourceDefaultVersion.TypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html#cfn-cloudformation-resourcedefaultversion-typename
        '''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_version_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ResourceDefaultVersion.TypeVersionArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html#cfn-cloudformation-resourcedefaultversion-typeversionarn
        '''
        result = self._values.get("type_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ResourceDefaultVersion.VersionId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html#cfn-cloudformation-resourcedefaultversion-versionid
        '''
        result = self._values.get("version_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceDefaultVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnResourceProps",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "properties": "properties"},
)
class CfnResourceProps:
    def __init__(
        self,
        *,
        type: builtins.str,
        properties: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param type: CloudFormation resource type (e.g. ``AWS::S3::Bucket``).
        :param properties: Resource properties. Default: - No resource properties.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if properties is not None:
            self._values["properties"] = properties

    @builtins.property
    def type(self) -> builtins.str:
        '''CloudFormation resource type (e.g. ``AWS::S3::Bucket``).'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Resource properties.

        :default: - No resource properties.
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnResourceSignal",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "timeout": "timeout"},
)
class CfnResourceSignal:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''When AWS CloudFormation creates the associated resource, configures the number of required success signals and the length of time that AWS CloudFormation waits for those signals.

        :param count: The number of success signals AWS CloudFormation must receive before it sets the resource status as CREATE_COMPLETE. If the resource receives a failure signal or doesn't receive the specified number of signals before the timeout period expires, the resource creation fails and AWS CloudFormation rolls the stack back.
        :param timeout: The length of time that AWS CloudFormation waits for the number of signals that was specified in the Count property. The timeout period starts after AWS CloudFormation starts creating the resource, and the timeout expires no sooner than the time you specify but can occur shortly thereafter. The maximum time that you can specify is 12 hours.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''The number of success signals AWS CloudFormation must receive before it sets the resource status as CREATE_COMPLETE.

        If the resource receives a failure signal or doesn't receive the specified number of signals before the timeout period
        expires, the resource creation fails and AWS CloudFormation rolls the stack back.
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''The length of time that AWS CloudFormation waits for the number of signals that was specified in the Count property.

        The timeout period starts after AWS CloudFormation starts creating the resource, and the timeout expires no sooner
        than the time you specify but can occur shortly thereafter. The maximum time that you can specify is 12 hours.
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceSignal(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnResourceVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "schema_handler_package": "schemaHandlerPackage",
        "type_name": "typeName",
        "execution_role_arn": "executionRoleArn",
        "logging_config": "loggingConfig",
    },
)
class CfnResourceVersionProps:
    def __init__(
        self,
        *,
        schema_handler_package: builtins.str,
        type_name: builtins.str,
        execution_role_arn: typing.Optional[builtins.str] = None,
        logging_config: typing.Optional[typing.Union["IResolvable", "CfnResourceVersion.LoggingConfigProperty"]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::ResourceVersion``.

        :param schema_handler_package: ``AWS::CloudFormation::ResourceVersion.SchemaHandlerPackage``.
        :param type_name: ``AWS::CloudFormation::ResourceVersion.TypeName``.
        :param execution_role_arn: ``AWS::CloudFormation::ResourceVersion.ExecutionRoleArn``.
        :param logging_config: ``AWS::CloudFormation::ResourceVersion.LoggingConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "schema_handler_package": schema_handler_package,
            "type_name": type_name,
        }
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if logging_config is not None:
            self._values["logging_config"] = logging_config

    @builtins.property
    def schema_handler_package(self) -> builtins.str:
        '''``AWS::CloudFormation::ResourceVersion.SchemaHandlerPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-schemahandlerpackage
        '''
        result = self._values.get("schema_handler_package")
        assert result is not None, "Required property 'schema_handler_package' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type_name(self) -> builtins.str:
        '''``AWS::CloudFormation::ResourceVersion.TypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-typename
        '''
        result = self._values.get("type_name")
        assert result is not None, "Required property 'type_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ResourceVersion.ExecutionRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_config(
        self,
    ) -> typing.Optional[typing.Union["IResolvable", "CfnResourceVersion.LoggingConfigProperty"]]:
        '''``AWS::CloudFormation::ResourceVersion.LoggingConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-loggingconfig
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional[typing.Union["IResolvable", "CfnResourceVersion.LoggingConfigProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnRuleAssertion",
    jsii_struct_bases=[],
    name_mapping={"assert_": "assert", "assert_description": "assertDescription"},
)
class CfnRuleAssertion:
    def __init__(
        self,
        *,
        assert_: "ICfnConditionExpression",
        assert_description: builtins.str,
    ) -> None:
        '''A rule assertion.

        :param assert_: The assertion.
        :param assert_description: The assertion description.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "assert_": assert_,
            "assert_description": assert_description,
        }

    @builtins.property
    def assert_(self) -> "ICfnConditionExpression":
        '''The assertion.'''
        result = self._values.get("assert_")
        assert result is not None, "Required property 'assert_' is missing"
        return typing.cast("ICfnConditionExpression", result)

    @builtins.property
    def assert_description(self) -> builtins.str:
        '''The assertion description.'''
        result = self._values.get("assert_description")
        assert result is not None, "Required property 'assert_description' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRuleAssertion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnRuleProps",
    jsii_struct_bases=[],
    name_mapping={"assertions": "assertions", "rule_condition": "ruleCondition"},
)
class CfnRuleProps:
    def __init__(
        self,
        *,
        assertions: typing.Optional[typing.Sequence[CfnRuleAssertion]] = None,
        rule_condition: typing.Optional["ICfnConditionExpression"] = None,
    ) -> None:
        '''A rule can include a RuleCondition property and must include an Assertions property.

        For each rule, you can define only one rule condition; you can define one or more asserts within the Assertions property.
        You define a rule condition and assertions by using rule-specific intrinsic functions.

        You can use the following rule-specific intrinsic functions to define rule conditions and assertions:

        Fn::And
        Fn::Contains
        Fn::EachMemberEquals
        Fn::EachMemberIn
        Fn::Equals
        Fn::If
        Fn::Not
        Fn::Or
        Fn::RefAll
        Fn::ValueOf
        Fn::ValueOfAll

        https://docs.aws.amazon.com/servicecatalog/latest/adminguide/reference-template_constraint_rules.html

        :param assertions: Assertions which define the rule. Default: - No assertions for the rule.
        :param rule_condition: If the rule condition evaluates to false, the rule doesn't take effect. If the function in the rule condition evaluates to true, expressions in each assert are evaluated and applied. Default: - Rule's assertions will always take effect.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if assertions is not None:
            self._values["assertions"] = assertions
        if rule_condition is not None:
            self._values["rule_condition"] = rule_condition

    @builtins.property
    def assertions(self) -> typing.Optional[typing.List[CfnRuleAssertion]]:
        '''Assertions which define the rule.

        :default: - No assertions for the rule.
        '''
        result = self._values.get("assertions")
        return typing.cast(typing.Optional[typing.List[CfnRuleAssertion]], result)

    @builtins.property
    def rule_condition(self) -> typing.Optional["ICfnConditionExpression"]:
        '''If the rule condition evaluates to false, the rule doesn't take effect.

        If the function in the rule condition evaluates to true, expressions in each assert are evaluated and applied.

        :default: - Rule's assertions will always take effect.
        '''
        result = self._values.get("rule_condition")
        return typing.cast(typing.Optional["ICfnConditionExpression"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnStackProps",
    jsii_struct_bases=[],
    name_mapping={
        "template_url": "templateUrl",
        "notification_arns": "notificationArns",
        "parameters": "parameters",
        "tags": "tags",
        "timeout_in_minutes": "timeoutInMinutes",
    },
)
class CfnStackProps:
    def __init__(
        self,
        *,
        template_url: builtins.str,
        notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Optional[typing.Union["IResolvable", typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence["CfnTag"]] = None,
        timeout_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::Stack``.

        :param template_url: ``AWS::CloudFormation::Stack.TemplateURL``.
        :param notification_arns: ``AWS::CloudFormation::Stack.NotificationARNs``.
        :param parameters: ``AWS::CloudFormation::Stack.Parameters``.
        :param tags: ``AWS::CloudFormation::Stack.Tags``.
        :param timeout_in_minutes: ``AWS::CloudFormation::Stack.TimeoutInMinutes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "template_url": template_url,
        }
        if notification_arns is not None:
            self._values["notification_arns"] = notification_arns
        if parameters is not None:
            self._values["parameters"] = parameters
        if tags is not None:
            self._values["tags"] = tags
        if timeout_in_minutes is not None:
            self._values["timeout_in_minutes"] = timeout_in_minutes

    @builtins.property
    def template_url(self) -> builtins.str:
        '''``AWS::CloudFormation::Stack.TemplateURL``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-templateurl
        '''
        result = self._values.get("template_url")
        assert result is not None, "Required property 'template_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notification_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::CloudFormation::Stack.NotificationARNs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-notificationarns
        '''
        result = self._values.get("notification_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union["IResolvable", typing.Mapping[builtins.str, builtins.str]]]:
        '''``AWS::CloudFormation::Stack.Parameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union["IResolvable", typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["CfnTag"]]:
        '''``AWS::CloudFormation::Stack.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["CfnTag"]], result)

    @builtins.property
    def timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''``AWS::CloudFormation::Stack.TimeoutInMinutes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-timeoutinminutes
        '''
        result = self._values.get("timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnStackSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "permission_model": "permissionModel",
        "stack_set_name": "stackSetName",
        "administration_role_arn": "administrationRoleArn",
        "auto_deployment": "autoDeployment",
        "call_as": "callAs",
        "capabilities": "capabilities",
        "description": "description",
        "execution_role_name": "executionRoleName",
        "operation_preferences": "operationPreferences",
        "parameters": "parameters",
        "stack_instances_group": "stackInstancesGroup",
        "tags": "tags",
        "template_body": "templateBody",
        "template_url": "templateUrl",
    },
)
class CfnStackSetProps:
    def __init__(
        self,
        *,
        permission_model: builtins.str,
        stack_set_name: builtins.str,
        administration_role_arn: typing.Optional[builtins.str] = None,
        auto_deployment: typing.Optional[typing.Union["IResolvable", "CfnStackSet.AutoDeploymentProperty"]] = None,
        call_as: typing.Optional[builtins.str] = None,
        capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        execution_role_name: typing.Optional[builtins.str] = None,
        operation_preferences: typing.Optional[typing.Union["IResolvable", "CfnStackSet.OperationPreferencesProperty"]] = None,
        parameters: typing.Optional[typing.Union["IResolvable", typing.Sequence[typing.Union["IResolvable", "CfnStackSet.ParameterProperty"]]]] = None,
        stack_instances_group: typing.Optional[typing.Union["IResolvable", typing.Sequence[typing.Union["IResolvable", "CfnStackSet.StackInstancesProperty"]]]] = None,
        tags: typing.Optional[typing.Sequence["CfnTag"]] = None,
        template_body: typing.Optional[builtins.str] = None,
        template_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::StackSet``.

        :param permission_model: ``AWS::CloudFormation::StackSet.PermissionModel``.
        :param stack_set_name: ``AWS::CloudFormation::StackSet.StackSetName``.
        :param administration_role_arn: ``AWS::CloudFormation::StackSet.AdministrationRoleARN``.
        :param auto_deployment: ``AWS::CloudFormation::StackSet.AutoDeployment``.
        :param call_as: ``AWS::CloudFormation::StackSet.CallAs``.
        :param capabilities: ``AWS::CloudFormation::StackSet.Capabilities``.
        :param description: ``AWS::CloudFormation::StackSet.Description``.
        :param execution_role_name: ``AWS::CloudFormation::StackSet.ExecutionRoleName``.
        :param operation_preferences: ``AWS::CloudFormation::StackSet.OperationPreferences``.
        :param parameters: ``AWS::CloudFormation::StackSet.Parameters``.
        :param stack_instances_group: ``AWS::CloudFormation::StackSet.StackInstancesGroup``.
        :param tags: ``AWS::CloudFormation::StackSet.Tags``.
        :param template_body: ``AWS::CloudFormation::StackSet.TemplateBody``.
        :param template_url: ``AWS::CloudFormation::StackSet.TemplateURL``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "permission_model": permission_model,
            "stack_set_name": stack_set_name,
        }
        if administration_role_arn is not None:
            self._values["administration_role_arn"] = administration_role_arn
        if auto_deployment is not None:
            self._values["auto_deployment"] = auto_deployment
        if call_as is not None:
            self._values["call_as"] = call_as
        if capabilities is not None:
            self._values["capabilities"] = capabilities
        if description is not None:
            self._values["description"] = description
        if execution_role_name is not None:
            self._values["execution_role_name"] = execution_role_name
        if operation_preferences is not None:
            self._values["operation_preferences"] = operation_preferences
        if parameters is not None:
            self._values["parameters"] = parameters
        if stack_instances_group is not None:
            self._values["stack_instances_group"] = stack_instances_group
        if tags is not None:
            self._values["tags"] = tags
        if template_body is not None:
            self._values["template_body"] = template_body
        if template_url is not None:
            self._values["template_url"] = template_url

    @builtins.property
    def permission_model(self) -> builtins.str:
        '''``AWS::CloudFormation::StackSet.PermissionModel``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-permissionmodel
        '''
        result = self._values.get("permission_model")
        assert result is not None, "Required property 'permission_model' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_set_name(self) -> builtins.str:
        '''``AWS::CloudFormation::StackSet.StackSetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-stacksetname
        '''
        result = self._values.get("stack_set_name")
        assert result is not None, "Required property 'stack_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def administration_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.AdministrationRoleARN``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-administrationrolearn
        '''
        result = self._values.get("administration_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_deployment(
        self,
    ) -> typing.Optional[typing.Union["IResolvable", "CfnStackSet.AutoDeploymentProperty"]]:
        '''``AWS::CloudFormation::StackSet.AutoDeployment``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-autodeployment
        '''
        result = self._values.get("auto_deployment")
        return typing.cast(typing.Optional[typing.Union["IResolvable", "CfnStackSet.AutoDeploymentProperty"]], result)

    @builtins.property
    def call_as(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.CallAs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-callas
        '''
        result = self._values.get("call_as")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::CloudFormation::StackSet.Capabilities``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-capabilities
        '''
        result = self._values.get("capabilities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_role_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.ExecutionRoleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-executionrolename
        '''
        result = self._values.get("execution_role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operation_preferences(
        self,
    ) -> typing.Optional[typing.Union["IResolvable", "CfnStackSet.OperationPreferencesProperty"]]:
        '''``AWS::CloudFormation::StackSet.OperationPreferences``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-operationpreferences
        '''
        result = self._values.get("operation_preferences")
        return typing.cast(typing.Optional[typing.Union["IResolvable", "CfnStackSet.OperationPreferencesProperty"]], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union["IResolvable", typing.List[typing.Union["IResolvable", "CfnStackSet.ParameterProperty"]]]]:
        '''``AWS::CloudFormation::StackSet.Parameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union["IResolvable", typing.List[typing.Union["IResolvable", "CfnStackSet.ParameterProperty"]]]], result)

    @builtins.property
    def stack_instances_group(
        self,
    ) -> typing.Optional[typing.Union["IResolvable", typing.List[typing.Union["IResolvable", "CfnStackSet.StackInstancesProperty"]]]]:
        '''``AWS::CloudFormation::StackSet.StackInstancesGroup``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-stackinstancesgroup
        '''
        result = self._values.get("stack_instances_group")
        return typing.cast(typing.Optional[typing.Union["IResolvable", typing.List[typing.Union["IResolvable", "CfnStackSet.StackInstancesProperty"]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["CfnTag"]]:
        '''``AWS::CloudFormation::StackSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["CfnTag"]], result)

    @builtins.property
    def template_body(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.TemplateBody``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-templatebody
        '''
        result = self._values.get("template_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_url(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.TemplateURL``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-templateurl
        '''
        result = self._values.get("template_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStackSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnTag",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class CfnTag:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: 
        :param value: 

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''
        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html#cfn-resource-tags-key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''
        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html#cfn-resource-tags-value
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnTrafficRoute",
    jsii_struct_bases=[],
    name_mapping={"logical_id": "logicalId", "type": "type"},
)
class CfnTrafficRoute:
    def __init__(self, *, logical_id: builtins.str, type: builtins.str) -> None:
        '''A traffic route, representing where the traffic is being directed to.

        :param logical_id: The logical id of the target resource.
        :param type: The resource type of the route. Today, the only allowed value is 'AWS::ElasticLoadBalancingV2::Listener'.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "logical_id": logical_id,
            "type": type,
        }

    @builtins.property
    def logical_id(self) -> builtins.str:
        '''The logical id of the target resource.'''
        result = self._values.get("logical_id")
        assert result is not None, "Required property 'logical_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The resource type of the route.

        Today, the only allowed value is 'AWS::ElasticLoadBalancingV2::Listener'.
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTrafficRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnTrafficRouting",
    jsii_struct_bases=[],
    name_mapping={
        "prod_traffic_route": "prodTrafficRoute",
        "target_groups": "targetGroups",
        "test_traffic_route": "testTrafficRoute",
    },
)
class CfnTrafficRouting:
    def __init__(
        self,
        *,
        prod_traffic_route: CfnTrafficRoute,
        target_groups: typing.Sequence[builtins.str],
        test_traffic_route: CfnTrafficRoute,
    ) -> None:
        '''Type of the {@link CfnCodeDeployBlueGreenEcsAttributes.trafficRouting} property.

        :param prod_traffic_route: The listener to be used by your load balancer to direct traffic to your target groups.
        :param target_groups: The logical IDs of the blue and green, respectively, AWS::ElasticLoadBalancingV2::TargetGroup target groups.
        :param test_traffic_route: The listener to be used by your load balancer to direct traffic to your target groups.
        '''
        if isinstance(prod_traffic_route, dict):
            prod_traffic_route = CfnTrafficRoute(**prod_traffic_route)
        if isinstance(test_traffic_route, dict):
            test_traffic_route = CfnTrafficRoute(**test_traffic_route)
        self._values: typing.Dict[str, typing.Any] = {
            "prod_traffic_route": prod_traffic_route,
            "target_groups": target_groups,
            "test_traffic_route": test_traffic_route,
        }

    @builtins.property
    def prod_traffic_route(self) -> CfnTrafficRoute:
        '''The listener to be used by your load balancer to direct traffic to your target groups.'''
        result = self._values.get("prod_traffic_route")
        assert result is not None, "Required property 'prod_traffic_route' is missing"
        return typing.cast(CfnTrafficRoute, result)

    @builtins.property
    def target_groups(self) -> typing.List[builtins.str]:
        '''The logical IDs of the blue and green, respectively, AWS::ElasticLoadBalancingV2::TargetGroup target groups.'''
        result = self._values.get("target_groups")
        assert result is not None, "Required property 'target_groups' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def test_traffic_route(self) -> CfnTrafficRoute:
        '''The listener to be used by your load balancer to direct traffic to your target groups.'''
        result = self._values.get("test_traffic_route")
        assert result is not None, "Required property 'test_traffic_route' is missing"
        return typing.cast(CfnTrafficRoute, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTrafficRouting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnTrafficRoutingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "time_based_canary": "timeBasedCanary",
        "time_based_linear": "timeBasedLinear",
    },
)
class CfnTrafficRoutingConfig:
    def __init__(
        self,
        *,
        type: "CfnTrafficRoutingType",
        time_based_canary: typing.Optional["CfnTrafficRoutingTimeBasedCanary"] = None,
        time_based_linear: typing.Optional["CfnTrafficRoutingTimeBasedLinear"] = None,
    ) -> None:
        '''Traffic routing configuration settings.

        The type of the {@link CfnCodeDeployBlueGreenHookProps.trafficRoutingConfig} property.

        :param type: The type of traffic shifting used by the blue-green deployment configuration.
        :param time_based_canary: The configuration for traffic routing when {@link type} is {@link CfnTrafficRoutingType.TIME_BASED_CANARY}. Default: - none
        :param time_based_linear: The configuration for traffic routing when {@link type} is {@link CfnTrafficRoutingType.TIME_BASED_LINEAR}. Default: - none
        '''
        if isinstance(time_based_canary, dict):
            time_based_canary = CfnTrafficRoutingTimeBasedCanary(**time_based_canary)
        if isinstance(time_based_linear, dict):
            time_based_linear = CfnTrafficRoutingTimeBasedLinear(**time_based_linear)
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if time_based_canary is not None:
            self._values["time_based_canary"] = time_based_canary
        if time_based_linear is not None:
            self._values["time_based_linear"] = time_based_linear

    @builtins.property
    def type(self) -> "CfnTrafficRoutingType":
        '''The type of traffic shifting used by the blue-green deployment configuration.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("CfnTrafficRoutingType", result)

    @builtins.property
    def time_based_canary(self) -> typing.Optional["CfnTrafficRoutingTimeBasedCanary"]:
        '''The configuration for traffic routing when {@link type} is {@link CfnTrafficRoutingType.TIME_BASED_CANARY}.

        :default: - none
        '''
        result = self._values.get("time_based_canary")
        return typing.cast(typing.Optional["CfnTrafficRoutingTimeBasedCanary"], result)

    @builtins.property
    def time_based_linear(self) -> typing.Optional["CfnTrafficRoutingTimeBasedLinear"]:
        '''The configuration for traffic routing when {@link type} is {@link CfnTrafficRoutingType.TIME_BASED_LINEAR}.

        :default: - none
        '''
        result = self._values.get("time_based_linear")
        return typing.cast(typing.Optional["CfnTrafficRoutingTimeBasedLinear"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTrafficRoutingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnTrafficRoutingTimeBasedCanary",
    jsii_struct_bases=[],
    name_mapping={
        "bake_time_mins": "bakeTimeMins",
        "step_percentage": "stepPercentage",
    },
)
class CfnTrafficRoutingTimeBasedCanary:
    def __init__(
        self,
        *,
        bake_time_mins: typing.Optional[jsii.Number] = None,
        step_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''The traffic routing configuration if {@link CfnTrafficRoutingConfig.type} is {@link CfnTrafficRoutingType.TIME_BASED_CANARY}.

        :param bake_time_mins: The number of minutes between the first and second traffic shifts of a time-based canary deployment. Default: 5
        :param step_percentage: The percentage of traffic to shift in the first increment of a time-based canary deployment. The step percentage must be 14% or greater. Default: 15
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if bake_time_mins is not None:
            self._values["bake_time_mins"] = bake_time_mins
        if step_percentage is not None:
            self._values["step_percentage"] = step_percentage

    @builtins.property
    def bake_time_mins(self) -> typing.Optional[jsii.Number]:
        '''The number of minutes between the first and second traffic shifts of a time-based canary deployment.

        :default: 5
        '''
        result = self._values.get("bake_time_mins")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def step_percentage(self) -> typing.Optional[jsii.Number]:
        '''The percentage of traffic to shift in the first increment of a time-based canary deployment.

        The step percentage must be 14% or greater.

        :default: 15
        '''
        result = self._values.get("step_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTrafficRoutingTimeBasedCanary(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnTrafficRoutingTimeBasedLinear",
    jsii_struct_bases=[],
    name_mapping={
        "bake_time_mins": "bakeTimeMins",
        "step_percentage": "stepPercentage",
    },
)
class CfnTrafficRoutingTimeBasedLinear:
    def __init__(
        self,
        *,
        bake_time_mins: typing.Optional[jsii.Number] = None,
        step_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''The traffic routing configuration if {@link CfnTrafficRoutingConfig.type} is {@link CfnTrafficRoutingType.TIME_BASED_LINEAR}.

        :param bake_time_mins: The number of minutes between the first and second traffic shifts of a time-based linear deployment. Default: 5
        :param step_percentage: The percentage of traffic that is shifted at the start of each increment of a time-based linear deployment. The step percentage must be 14% or greater. Default: 15
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if bake_time_mins is not None:
            self._values["bake_time_mins"] = bake_time_mins
        if step_percentage is not None:
            self._values["step_percentage"] = step_percentage

    @builtins.property
    def bake_time_mins(self) -> typing.Optional[jsii.Number]:
        '''The number of minutes between the first and second traffic shifts of a time-based linear deployment.

        :default: 5
        '''
        result = self._values.get("bake_time_mins")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def step_percentage(self) -> typing.Optional[jsii.Number]:
        '''The percentage of traffic that is shifted at the start of each increment of a time-based linear deployment.

        The step percentage must be 14% or greater.

        :default: 15
        '''
        result = self._values.get("step_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTrafficRoutingTimeBasedLinear(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/core.CfnTrafficRoutingType")
class CfnTrafficRoutingType(enum.Enum):
    '''The possible types of traffic shifting for the blue-green deployment configuration.

    The type of the {@link CfnTrafficRoutingConfig.type} property.
    '''

    ALL_AT_ONCE = "ALL_AT_ONCE"
    '''Switch from blue to green at once.'''
    TIME_BASED_CANARY = "TIME_BASED_CANARY"
    '''Specifies a configuration that shifts traffic from blue to green in two increments.'''
    TIME_BASED_LINEAR = "TIME_BASED_LINEAR"
    '''Specifies a configuration that shifts traffic from blue to green in equal increments, with an equal number of minutes between each increment.'''


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnTypeActivationProps",
    jsii_struct_bases=[],
    name_mapping={
        "auto_update": "autoUpdate",
        "execution_role_arn": "executionRoleArn",
        "logging_config": "loggingConfig",
        "major_version": "majorVersion",
        "public_type_arn": "publicTypeArn",
        "publisher_id": "publisherId",
        "type": "type",
        "type_name": "typeName",
        "type_name_alias": "typeNameAlias",
        "version_bump": "versionBump",
    },
)
class CfnTypeActivationProps:
    def __init__(
        self,
        *,
        auto_update: typing.Optional[typing.Union[builtins.bool, "IResolvable"]] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        logging_config: typing.Optional[typing.Union["IResolvable", "CfnTypeActivation.LoggingConfigProperty"]] = None,
        major_version: typing.Optional[builtins.str] = None,
        public_type_arn: typing.Optional[builtins.str] = None,
        publisher_id: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
        type_name_alias: typing.Optional[builtins.str] = None,
        version_bump: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::TypeActivation``.

        :param auto_update: ``AWS::CloudFormation::TypeActivation.AutoUpdate``.
        :param execution_role_arn: ``AWS::CloudFormation::TypeActivation.ExecutionRoleArn``.
        :param logging_config: ``AWS::CloudFormation::TypeActivation.LoggingConfig``.
        :param major_version: ``AWS::CloudFormation::TypeActivation.MajorVersion``.
        :param public_type_arn: ``AWS::CloudFormation::TypeActivation.PublicTypeArn``.
        :param publisher_id: ``AWS::CloudFormation::TypeActivation.PublisherId``.
        :param type: ``AWS::CloudFormation::TypeActivation.Type``.
        :param type_name: ``AWS::CloudFormation::TypeActivation.TypeName``.
        :param type_name_alias: ``AWS::CloudFormation::TypeActivation.TypeNameAlias``.
        :param version_bump: ``AWS::CloudFormation::TypeActivation.VersionBump``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if auto_update is not None:
            self._values["auto_update"] = auto_update
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if major_version is not None:
            self._values["major_version"] = major_version
        if public_type_arn is not None:
            self._values["public_type_arn"] = public_type_arn
        if publisher_id is not None:
            self._values["publisher_id"] = publisher_id
        if type is not None:
            self._values["type"] = type
        if type_name is not None:
            self._values["type_name"] = type_name
        if type_name_alias is not None:
            self._values["type_name_alias"] = type_name_alias
        if version_bump is not None:
            self._values["version_bump"] = version_bump

    @builtins.property
    def auto_update(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "IResolvable"]]:
        '''``AWS::CloudFormation::TypeActivation.AutoUpdate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-autoupdate
        '''
        result = self._values.get("auto_update")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "IResolvable"]], result)

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.ExecutionRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_config(
        self,
    ) -> typing.Optional[typing.Union["IResolvable", "CfnTypeActivation.LoggingConfigProperty"]]:
        '''``AWS::CloudFormation::TypeActivation.LoggingConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-loggingconfig
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional[typing.Union["IResolvable", "CfnTypeActivation.LoggingConfigProperty"]], result)

    @builtins.property
    def major_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.MajorVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-majorversion
        '''
        result = self._values.get("major_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_type_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.PublicTypeArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-publictypearn
        '''
        result = self._values.get("public_type_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publisher_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.PublisherId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-publisherid
        '''
        result = self._values.get("publisher_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.TypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-typename
        '''
        result = self._values.get("type_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_name_alias(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.TypeNameAlias``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-typenamealias
        '''
        result = self._values.get("type_name_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_bump(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.VersionBump``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-versionbump
        '''
        result = self._values.get("version_bump")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTypeActivationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnUpdatePolicy",
    jsii_struct_bases=[],
    name_mapping={
        "auto_scaling_replacing_update": "autoScalingReplacingUpdate",
        "auto_scaling_rolling_update": "autoScalingRollingUpdate",
        "auto_scaling_scheduled_action": "autoScalingScheduledAction",
        "code_deploy_lambda_alias_update": "codeDeployLambdaAliasUpdate",
        "enable_version_upgrade": "enableVersionUpgrade",
        "use_online_resharding": "useOnlineResharding",
    },
)
class CfnUpdatePolicy:
    def __init__(
        self,
        *,
        auto_scaling_replacing_update: typing.Optional[CfnAutoScalingReplacingUpdate] = None,
        auto_scaling_rolling_update: typing.Optional[CfnAutoScalingRollingUpdate] = None,
        auto_scaling_scheduled_action: typing.Optional[CfnAutoScalingScheduledAction] = None,
        code_deploy_lambda_alias_update: typing.Optional[CfnCodeDeployLambdaAliasUpdate] = None,
        enable_version_upgrade: typing.Optional[builtins.bool] = None,
        use_online_resharding: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Use the UpdatePolicy attribute to specify how AWS CloudFormation handles updates to the AWS::AutoScaling::AutoScalingGroup resource.

        AWS CloudFormation invokes one of three update policies depending on the type of change you make or whether a
        scheduled action is associated with the Auto Scaling group.

        :param auto_scaling_replacing_update: Specifies whether an Auto Scaling group and the instances it contains are replaced during an update. During replacement, AWS CloudFormation retains the old group until it finishes creating the new one. If the update fails, AWS CloudFormation can roll back to the old Auto Scaling group and delete the new Auto Scaling group.
        :param auto_scaling_rolling_update: To specify how AWS CloudFormation handles rolling updates for an Auto Scaling group, use the AutoScalingRollingUpdate policy. Rolling updates enable you to specify whether AWS CloudFormation updates instances that are in an Auto Scaling group in batches or all at once.
        :param auto_scaling_scheduled_action: To specify how AWS CloudFormation handles updates for the MinSize, MaxSize, and DesiredCapacity properties when the AWS::AutoScaling::AutoScalingGroup resource has an associated scheduled action, use the AutoScalingScheduledAction policy.
        :param code_deploy_lambda_alias_update: To perform an AWS CodeDeploy deployment when the version changes on an AWS::Lambda::Alias resource, use the CodeDeployLambdaAliasUpdate update policy.
        :param enable_version_upgrade: To upgrade an Amazon ES domain to a new version of Elasticsearch rather than replacing the entire AWS::Elasticsearch::Domain resource, use the EnableVersionUpgrade update policy.
        :param use_online_resharding: To modify a replication group's shards by adding or removing shards, rather than replacing the entire AWS::ElastiCache::ReplicationGroup resource, use the UseOnlineResharding update policy.
        '''
        if isinstance(auto_scaling_replacing_update, dict):
            auto_scaling_replacing_update = CfnAutoScalingReplacingUpdate(**auto_scaling_replacing_update)
        if isinstance(auto_scaling_rolling_update, dict):
            auto_scaling_rolling_update = CfnAutoScalingRollingUpdate(**auto_scaling_rolling_update)
        if isinstance(auto_scaling_scheduled_action, dict):
            auto_scaling_scheduled_action = CfnAutoScalingScheduledAction(**auto_scaling_scheduled_action)
        if isinstance(code_deploy_lambda_alias_update, dict):
            code_deploy_lambda_alias_update = CfnCodeDeployLambdaAliasUpdate(**code_deploy_lambda_alias_update)
        self._values: typing.Dict[str, typing.Any] = {}
        if auto_scaling_replacing_update is not None:
            self._values["auto_scaling_replacing_update"] = auto_scaling_replacing_update
        if auto_scaling_rolling_update is not None:
            self._values["auto_scaling_rolling_update"] = auto_scaling_rolling_update
        if auto_scaling_scheduled_action is not None:
            self._values["auto_scaling_scheduled_action"] = auto_scaling_scheduled_action
        if code_deploy_lambda_alias_update is not None:
            self._values["code_deploy_lambda_alias_update"] = code_deploy_lambda_alias_update
        if enable_version_upgrade is not None:
            self._values["enable_version_upgrade"] = enable_version_upgrade
        if use_online_resharding is not None:
            self._values["use_online_resharding"] = use_online_resharding

    @builtins.property
    def auto_scaling_replacing_update(
        self,
    ) -> typing.Optional[CfnAutoScalingReplacingUpdate]:
        '''Specifies whether an Auto Scaling group and the instances it contains are replaced during an update.

        During replacement,
        AWS CloudFormation retains the old group until it finishes creating the new one. If the update fails, AWS CloudFormation
        can roll back to the old Auto Scaling group and delete the new Auto Scaling group.
        '''
        result = self._values.get("auto_scaling_replacing_update")
        return typing.cast(typing.Optional[CfnAutoScalingReplacingUpdate], result)

    @builtins.property
    def auto_scaling_rolling_update(
        self,
    ) -> typing.Optional[CfnAutoScalingRollingUpdate]:
        '''To specify how AWS CloudFormation handles rolling updates for an Auto Scaling group, use the AutoScalingRollingUpdate policy.

        Rolling updates enable you to specify whether AWS CloudFormation updates instances that are in an Auto Scaling
        group in batches or all at once.
        '''
        result = self._values.get("auto_scaling_rolling_update")
        return typing.cast(typing.Optional[CfnAutoScalingRollingUpdate], result)

    @builtins.property
    def auto_scaling_scheduled_action(
        self,
    ) -> typing.Optional[CfnAutoScalingScheduledAction]:
        '''To specify how AWS CloudFormation handles updates for the MinSize, MaxSize, and DesiredCapacity properties when the AWS::AutoScaling::AutoScalingGroup resource has an associated scheduled action, use the AutoScalingScheduledAction policy.'''
        result = self._values.get("auto_scaling_scheduled_action")
        return typing.cast(typing.Optional[CfnAutoScalingScheduledAction], result)

    @builtins.property
    def code_deploy_lambda_alias_update(
        self,
    ) -> typing.Optional[CfnCodeDeployLambdaAliasUpdate]:
        '''To perform an AWS CodeDeploy deployment when the version changes on an AWS::Lambda::Alias resource, use the CodeDeployLambdaAliasUpdate update policy.'''
        result = self._values.get("code_deploy_lambda_alias_update")
        return typing.cast(typing.Optional[CfnCodeDeployLambdaAliasUpdate], result)

    @builtins.property
    def enable_version_upgrade(self) -> typing.Optional[builtins.bool]:
        '''To upgrade an Amazon ES domain to a new version of Elasticsearch rather than replacing the entire AWS::Elasticsearch::Domain resource, use the EnableVersionUpgrade update policy.'''
        result = self._values.get("enable_version_upgrade")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def use_online_resharding(self) -> typing.Optional[builtins.bool]:
        '''To modify a replication group's shards by adding or removing shards, rather than replacing the entire AWS::ElastiCache::ReplicationGroup resource, use the UseOnlineResharding update policy.'''
        result = self._values.get("use_online_resharding")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUpdatePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CfnWaitConditionProps",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "handle": "handle", "timeout": "timeout"},
)
class CfnWaitConditionProps:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        handle: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CloudFormation::WaitCondition``.

        :param count: ``AWS::CloudFormation::WaitCondition.Count``.
        :param handle: ``AWS::CloudFormation::WaitCondition.Handle``.
        :param timeout: ``AWS::CloudFormation::WaitCondition.Timeout``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if handle is not None:
            self._values["handle"] = handle
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''``AWS::CloudFormation::WaitCondition.Count``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-count
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def handle(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::WaitCondition.Handle``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-handle
        '''
        result = self._values.get("handle")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::WaitCondition.Timeout``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWaitConditionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConstructNode(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.ConstructNode"):
    '''Represents the construct node in the scope tree.'''

    def __init__(
        self,
        host: "Construct",
        scope: "IConstruct",
        id: builtins.str,
    ) -> None:
        '''
        :param host: -
        :param scope: -
        :param id: -
        '''
        jsii.create(ConstructNode, self, [host, scope, id])

    @jsii.member(jsii_name="prepare") # type: ignore[misc]
    @builtins.classmethod
    def prepare(cls, node: "ConstructNode") -> None:
        '''(deprecated) Invokes "prepare" on all constructs (depth-first, post-order) in the tree under ``node``.

        :param node: The root node.

        :deprecated: Use ``app.synth()`` instead

        :stability: deprecated
        '''
        return typing.cast(None, jsii.sinvoke(cls, "prepare", [node]))

    @jsii.member(jsii_name="synth") # type: ignore[misc]
    @builtins.classmethod
    def synth(
        cls,
        node: "ConstructNode",
        *,
        outdir: typing.Optional[builtins.str] = None,
        skip_validation: typing.Optional[builtins.bool] = None,
        validate_on_synthesis: typing.Optional[builtins.bool] = None,
        runtime_info: typing.Optional[aws_cdk.cx_api.RuntimeInfo] = None,
    ) -> aws_cdk.cx_api.CloudAssembly:
        '''(deprecated) Synthesizes a CloudAssembly from a construct tree.

        :param node: The root of the construct tree.
        :param outdir: (deprecated) The output directory into which to synthesize the cloud assembly. Default: - creates a temporary directory
        :param skip_validation: (deprecated) Whether synthesis should skip the validation phase. Default: false
        :param validate_on_synthesis: (deprecated) Whether the stack should be validated after synthesis to check for error metadata. Default: - false
        :param runtime_info: (deprecated) Include the specified runtime information (module versions) in manifest. Default: - if this option is not specified, runtime info will not be included

        :deprecated: Use ``app.synth()`` or ``stage.synth()`` instead

        :stability: deprecated
        '''
        options = SynthesisOptions(
            outdir=outdir,
            skip_validation=skip_validation,
            validate_on_synthesis=validate_on_synthesis,
            runtime_info=runtime_info,
        )

        return typing.cast(aws_cdk.cx_api.CloudAssembly, jsii.sinvoke(cls, "synth", [node, options]))

    @jsii.member(jsii_name="validate") # type: ignore[misc]
    @builtins.classmethod
    def validate(cls, node: "ConstructNode") -> typing.List["ValidationError"]:
        '''Invokes "validate" on all constructs in the tree (depth-first, pre-order) and returns the list of all errors.

        An empty list indicates that there are no errors.

        :param node: The root node.
        '''
        return typing.cast(typing.List["ValidationError"], jsii.sinvoke(cls, "validate", [node]))

    @jsii.member(jsii_name="addDependency")
    def add_dependency(self, *dependencies: "IDependable") -> None:
        '''Add an ordering dependency on another Construct.

        All constructs in the dependency's scope will be deployed before any
        construct in this construct's scope.

        :param dependencies: -
        '''
        return typing.cast(None, jsii.invoke(self, "addDependency", [*dependencies]))

    @jsii.member(jsii_name="addError")
    def add_error(self, message: builtins.str) -> None:
        '''(deprecated) DEPRECATED: Adds an { "error":  } metadata entry to this construct.

        The toolkit will fail synthesis when errors are reported.

        :param message: The error message.

        :deprecated: use ``Annotations.of(construct).addError()``

        :stability: deprecated
        '''
        return typing.cast(None, jsii.invoke(self, "addError", [message]))

    @jsii.member(jsii_name="addInfo")
    def add_info(self, message: builtins.str) -> None:
        '''(deprecated) DEPRECATED: Adds a { "info":  } metadata entry to this construct.

        The toolkit will display the info message when apps are synthesized.

        :param message: The info message.

        :deprecated: use ``Annotations.of(construct).addInfo()``

        :stability: deprecated
        '''
        return typing.cast(None, jsii.invoke(self, "addInfo", [message]))

    @jsii.member(jsii_name="addMetadata")
    def add_metadata(
        self,
        type: builtins.str,
        data: typing.Any,
        from_function: typing.Any = None,
    ) -> None:
        '''Adds a metadata entry to this construct.

        Entries are arbitrary values and will also include a stack trace to allow tracing back to
        the code location for when the entry was added. It can be used, for example, to include source
        mapping in CloudFormation templates to improve diagnostics.

        :param type: a string denoting the type of metadata.
        :param data: the value of the metadata (can be a Token). If null/undefined, metadata will not be added.
        :param from_function: a function under which to restrict the metadata entry's stack trace (defaults to this.addMetadata).
        '''
        return typing.cast(None, jsii.invoke(self, "addMetadata", [type, data, from_function]))

    @jsii.member(jsii_name="addValidation")
    def add_validation(self, validation: constructs.IValidation) -> None:
        '''Add a validator to this construct Node.

        :param validation: -
        '''
        return typing.cast(None, jsii.invoke(self, "addValidation", [validation]))

    @jsii.member(jsii_name="addWarning")
    def add_warning(self, message: builtins.str) -> None:
        '''(deprecated) DEPRECATED: Adds a { "warning":  } metadata entry to this construct.

        The toolkit will display the warning when an app is synthesized, or fail
        if run in --strict mode.

        :param message: The warning message.

        :deprecated: use ``Annotations.of(construct).addWarning()``

        :stability: deprecated
        '''
        return typing.cast(None, jsii.invoke(self, "addWarning", [message]))

    @jsii.member(jsii_name="applyAspect")
    def apply_aspect(self, aspect: "IAspect") -> None:
        '''(deprecated) DEPRECATED: Applies the aspect to this Constructs node.

        :param aspect: -

        :deprecated:

        This API is going to be removed in the next major version of
        the AWS CDK. Please use ``Aspects.of(scope).add()`` instead.

        :stability: deprecated
        '''
        return typing.cast(None, jsii.invoke(self, "applyAspect", [aspect]))

    @jsii.member(jsii_name="findAll")
    def find_all(
        self,
        order: typing.Optional["ConstructOrder"] = None,
    ) -> typing.List["IConstruct"]:
        '''Return this construct and all of its children in the given order.

        :param order: -
        '''
        return typing.cast(typing.List["IConstruct"], jsii.invoke(self, "findAll", [order]))

    @jsii.member(jsii_name="findChild")
    def find_child(self, id: builtins.str) -> "IConstruct":
        '''Return a direct child by id.

        Throws an error if the child is not found.

        :param id: Identifier of direct child.

        :return: Child with the given id.
        '''
        return typing.cast("IConstruct", jsii.invoke(self, "findChild", [id]))

    @jsii.member(jsii_name="setContext")
    def set_context(self, key: builtins.str, value: typing.Any) -> None:
        '''This can be used to set contextual values.

        Context must be set before any children are added, since children may consult context info during construction.
        If the key already exists, it will be overridden.

        :param key: The context key.
        :param value: The context value.
        '''
        return typing.cast(None, jsii.invoke(self, "setContext", [key, value]))

    @jsii.member(jsii_name="tryFindChild")
    def try_find_child(self, id: builtins.str) -> typing.Optional["IConstruct"]:
        '''Return a direct child by id, or undefined.

        :param id: Identifier of direct child.

        :return: the child if found, or undefined
        '''
        return typing.cast(typing.Optional["IConstruct"], jsii.invoke(self, "tryFindChild", [id]))

    @jsii.member(jsii_name="tryGetContext")
    def try_get_context(self, key: builtins.str) -> typing.Any:
        '''Retrieves a value from tree context.

        Context is usually initialized at the root, but can be overridden at any point in the tree.

        :param key: The context key.

        :return: The context value or ``undefined`` if there is no context value for the key.
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "tryGetContext", [key]))

    @jsii.member(jsii_name="tryRemoveChild")
    def try_remove_child(self, child_name: builtins.str) -> builtins.bool:
        '''Remove the child with the given name, if present.

        :param child_name: -

        :return: Whether a child with the given name was deleted.
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "tryRemoveChild", [child_name]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="PATH_SEP")
    def PATH_SEP(cls) -> builtins.str:
        '''Separator used to delimit construct path components.'''
        return typing.cast(builtins.str, jsii.sget(cls, "PATH_SEP"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="addr")
    def addr(self) -> builtins.str:
        '''Returns an opaque tree-unique address for this construct.

        Addresses are 42 characters hexadecimal strings. They begin with "c8"
        followed by 40 lowercase hexadecimal characters (0-9a-f).

        Addresses are calculated using a SHA-1 of the components of the construct
        path.

        To enable refactorings of construct trees, constructs with the ID ``Default``
        will be excluded from the calculation. In those cases constructs in the
        same tree may have the same addreess.

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            c83a2846e506bcc5f10682b564084bca2d275709ee
        '''
        return typing.cast(builtins.str, jsii.get(self, "addr"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="children")
    def children(self) -> typing.List["IConstruct"]:
        '''All direct children of this construct.'''
        return typing.cast(typing.List["IConstruct"], jsii.get(self, "children"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dependencies")
    def dependencies(self) -> typing.List["Dependency"]:
        '''Return all dependencies registered on this node or any of its children.'''
        return typing.cast(typing.List["Dependency"], jsii.get(self, "dependencies"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''The id of this construct within the current scope.

        This is a a scope-unique id. To obtain an app-unique id for this construct, use ``uniqueId``.
        '''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="locked")
    def locked(self) -> builtins.bool:
        '''Returns true if this construct or the scopes in which it is defined are locked.'''
        return typing.cast(builtins.bool, jsii.get(self, "locked"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.List[aws_cdk.cx_api.MetadataEntry]:
        '''(deprecated) DEPRECATED.

        :deprecated: use ``metadataEntry``

        :stability: deprecated
        '''
        return typing.cast(typing.List[aws_cdk.cx_api.MetadataEntry], jsii.get(self, "metadata"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="metadataEntry")
    def metadata_entry(self) -> typing.List[constructs.MetadataEntry]:
        '''An immutable array of metadata objects associated with this construct.

        This can be used, for example, to implement support for deprecation notices, source mapping, etc.
        '''
        return typing.cast(typing.List[constructs.MetadataEntry], jsii.get(self, "metadataEntry"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        '''The full, absolute path of this construct in the tree.

        Components are separated by '/'.
        '''
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="root")
    def root(self) -> "IConstruct":
        '''
        :return: The root of the construct tree.
        '''
        return typing.cast("IConstruct", jsii.get(self, "root"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scopes")
    def scopes(self) -> typing.List["IConstruct"]:
        '''All parent scopes of this construct.

        :return:

        a list of parent scopes. The last element in the list will always
        be the current construct and the first element will be the root of the
        tree.
        '''
        return typing.cast(typing.List["IConstruct"], jsii.get(self, "scopes"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="uniqueId")
    def unique_id(self) -> builtins.str:
        '''(deprecated) A tree-global unique alphanumeric identifier for this construct.

        Includes
        all components of the tree.

        :deprecated:

        use ``node.addr`` to obtain a consistent 42 character address for
        this node (see https://github.com/aws/constructs/pull/314)

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.get(self, "uniqueId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scope")
    def scope(self) -> typing.Optional["IConstruct"]:
        '''Returns the scope in which this construct is defined.

        The value is ``undefined`` at the root of the construct scope tree.
        '''
        return typing.cast(typing.Optional["IConstruct"], jsii.get(self, "scope"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultChild")
    def default_child(self) -> typing.Optional["IConstruct"]:
        '''Returns the child construct that has the id ``Default`` or ``Resource"``.

        This is usually the construct that provides the bulk of the underlying functionality.
        Useful for modifications of the underlying construct that are not available at the higher levels.
        Override the defaultChild property.

        This should only be used in the cases where the correct
        default child is not named 'Resource' or 'Default' as it
        should be.

        If you set this to undefined, the default behavior of finding
        the child named 'Resource' or 'Default' will be used.

        :return: a construct or undefined if there is no default child

        :throws: if there is more than one child
        '''
        return typing.cast(typing.Optional["IConstruct"], jsii.get(self, "defaultChild"))

    @default_child.setter
    def default_child(self, value: typing.Optional["IConstruct"]) -> None:
        jsii.set(self, "defaultChild", value)


@jsii.enum(jsii_type="@aws-cdk/core.ConstructOrder")
class ConstructOrder(enum.Enum):
    '''In what order to return constructs.'''

    PREORDER = "PREORDER"
    '''Depth-first, pre-order.'''
    POSTORDER = "POSTORDER"
    '''Depth-first, post-order (leaf nodes first).'''


class ContextProvider(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.ContextProvider",
):
    '''Base class for the model side of context providers.

    Instances of this class communicate with context provider plugins in the 'cdk
    toolkit' via context variables (input), outputting specialized queries for
    more context variables (output).

    ContextProvider needs access to a Construct to hook into the context mechanism.
    '''

    @jsii.member(jsii_name="getKey") # type: ignore[misc]
    @builtins.classmethod
    def get_key(
        cls,
        scope: constructs.Construct,
        *,
        provider: builtins.str,
        props: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> "GetContextKeyResult":
        '''
        :param scope: -
        :param provider: The context provider to query.
        :param props: Provider-specific properties.

        :return: the context key or undefined if a key cannot be rendered (due to tokens used in any of the props)
        '''
        options = GetContextKeyOptions(provider=provider, props=props)

        return typing.cast("GetContextKeyResult", jsii.sinvoke(cls, "getKey", [scope, options]))

    @jsii.member(jsii_name="getValue") # type: ignore[misc]
    @builtins.classmethod
    def get_value(
        cls,
        scope: constructs.Construct,
        *,
        dummy_value: typing.Any,
        provider: builtins.str,
        props: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> "GetContextValueResult":
        '''
        :param scope: -
        :param dummy_value: The value to return if the context value was not found and a missing context is reported. This should be a dummy value that should preferably fail during deployment since it represents an invalid state.
        :param provider: The context provider to query.
        :param props: Provider-specific properties.
        '''
        options = GetContextValueOptions(
            dummy_value=dummy_value, provider=provider, props=props
        )

        return typing.cast("GetContextValueResult", jsii.sinvoke(cls, "getValue", [scope, options]))


@jsii.data_type(
    jsii_type="@aws-cdk/core.CopyOptions",
    jsii_struct_bases=[],
    name_mapping={
        "exclude": "exclude",
        "follow": "follow",
        "ignore_mode": "ignoreMode",
    },
)
class CopyOptions:
    def __init__(
        self,
        *,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow: typing.Optional["SymlinkFollowMode"] = None,
        ignore_mode: typing.Optional["IgnoreMode"] = None,
    ) -> None:
        '''Options applied when copying directories.

        :param exclude: Glob patterns to exclude from the copy. Default: - nothing is excluded
        :param follow: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for exclude patterns. Default: IgnoreMode.GLOB
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if exclude is not None:
            self._values["exclude"] = exclude
        if follow is not None:
            self._values["follow"] = follow
        if ignore_mode is not None:
            self._values["ignore_mode"] = ignore_mode

    @builtins.property
    def exclude(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Glob patterns to exclude from the copy.

        :default: - nothing is excluded
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def follow(self) -> typing.Optional["SymlinkFollowMode"]:
        '''A strategy for how to handle symlinks.

        :default: SymlinkFollowMode.NEVER
        '''
        result = self._values.get("follow")
        return typing.cast(typing.Optional["SymlinkFollowMode"], result)

    @builtins.property
    def ignore_mode(self) -> typing.Optional["IgnoreMode"]:
        '''The ignore behavior to use for exclude patterns.

        :default: IgnoreMode.GLOB
        '''
        result = self._values.get("ignore_mode")
        return typing.cast(typing.Optional["IgnoreMode"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CopyOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CustomResourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "service_token": "serviceToken",
        "pascal_case_properties": "pascalCaseProperties",
        "properties": "properties",
        "removal_policy": "removalPolicy",
        "resource_type": "resourceType",
    },
)
class CustomResourceProps:
    def __init__(
        self,
        *,
        service_token: builtins.str,
        pascal_case_properties: typing.Optional[builtins.bool] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        removal_policy: typing.Optional["RemovalPolicy"] = None,
        resource_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties to provide a Lambda-backed custom resource.

        :param service_token: The ARN of the provider which implements this custom resource type. You can implement a provider by listening to raw AWS CloudFormation events and specify the ARN of an SNS topic (``topic.topicArn``) or the ARN of an AWS Lambda function (``lambda.functionArn``) or use the CDK's custom `resource provider framework <https://docs.aws.amazon.com/cdk/api/latest/docs/custom-resources-readme.html>`_ which makes it easier to implement robust providers. Provider framework:: // use the provider framework from aws-cdk/custom-resources: const provider = new customresources.Provider(this, 'ResourceProvider', { onEventHandler, isCompleteHandler, // optional }); new CustomResource(this, 'MyResource', { serviceToken: provider.serviceToken, }); AWS Lambda function:: // invoke an AWS Lambda function when a lifecycle event occurs: new CustomResource(this, 'MyResource', { serviceToken: myFunction.functionArn, }); SNS topic:: // publish lifecycle events to an SNS topic: new CustomResource(this, 'MyResource', { serviceToken: myTopic.topicArn, });
        :param pascal_case_properties: Convert all property keys to pascal case. Default: false
        :param properties: Properties to pass to the Lambda. Default: - No properties.
        :param removal_policy: The policy to apply when this resource is removed from the application. Default: cdk.RemovalPolicy.Destroy
        :param resource_type: For custom resources, you can specify AWS::CloudFormation::CustomResource (the default) as the resource type, or you can specify your own resource type name. For example, you can use "Custom::MyCustomResourceTypeName". Custom resource type names must begin with "Custom::" and can include alphanumeric characters and the following characters: _@-. You can specify a custom resource type name up to a maximum length of 60 characters. You cannot change the type during an update. Using your own resource type names helps you quickly differentiate the types of custom resources in your stack. For example, if you had two custom resources that conduct two different ping tests, you could name their type as Custom::PingTester to make them easily identifiable as ping testers (instead of using AWS::CloudFormation::CustomResource). Default: - AWS::CloudFormation::CustomResource
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "service_token": service_token,
        }
        if pascal_case_properties is not None:
            self._values["pascal_case_properties"] = pascal_case_properties
        if properties is not None:
            self._values["properties"] = properties
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if resource_type is not None:
            self._values["resource_type"] = resource_type

    @builtins.property
    def service_token(self) -> builtins.str:
        '''The ARN of the provider which implements this custom resource type.

        You can implement a provider by listening to raw AWS CloudFormation events
        and specify the ARN of an SNS topic (``topic.topicArn``) or the ARN of an AWS
        Lambda function (``lambda.functionArn``) or use the CDK's custom `resource
        provider framework <https://docs.aws.amazon.com/cdk/api/latest/docs/custom-resources-readme.html>`_ which makes it easier to implement robust providers.

        Provider framework::

           # Example automatically generated. See https://github.com/aws/jsii/issues/826
           # use the provider framework from aws-cdk/custom-resources:
           provider = customresources.Provider(self, "ResourceProvider",
               on_event_handler=on_event_handler,
               is_complete_handler=is_complete_handler
           )

           CustomResource(self, "MyResource",
               service_token=provider.service_token
           )

        AWS Lambda function::

           # Example automatically generated. See https://github.com/aws/jsii/issues/826
           # invoke an AWS Lambda function when a lifecycle event occurs:
           CustomResource(self, "MyResource",
               service_token=my_function.function_arn
           )

        SNS topic::

           # Example automatically generated. See https://github.com/aws/jsii/issues/826
           # publish lifecycle events to an SNS topic:
           CustomResource(self, "MyResource",
               service_token=my_topic.topic_arn
           )
        '''
        result = self._values.get("service_token")
        assert result is not None, "Required property 'service_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pascal_case_properties(self) -> typing.Optional[builtins.bool]:
        '''Convert all property keys to pascal case.

        :default: false
        '''
        result = self._values.get("pascal_case_properties")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Properties to pass to the Lambda.

        :default: - No properties.
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["RemovalPolicy"]:
        '''The policy to apply when this resource is removed from the application.

        :default: cdk.RemovalPolicy.Destroy
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["RemovalPolicy"], result)

    @builtins.property
    def resource_type(self) -> typing.Optional[builtins.str]:
        '''For custom resources, you can specify AWS::CloudFormation::CustomResource (the default) as the resource type, or you can specify your own resource type name.

        For example, you can use "Custom::MyCustomResourceTypeName".

        Custom resource type names must begin with "Custom::" and can include
        alphanumeric characters and the following characters: _@-. You can specify
        a custom resource type name up to a maximum length of 60 characters. You
        cannot change the type during an update.

        Using your own resource type names helps you quickly differentiate the
        types of custom resources in your stack. For example, if you had two custom
        resources that conduct two different ping tests, you could name their type
        as Custom::PingTester to make them easily identifiable as ping testers
        (instead of using AWS::CloudFormation::CustomResource).

        :default: - AWS::CloudFormation::CustomResource

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html#aws-cfn-resource-type-name
        '''
        result = self._values.get("resource_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomResourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.CustomResourceProviderProps",
    jsii_struct_bases=[],
    name_mapping={
        "code_directory": "codeDirectory",
        "runtime": "runtime",
        "description": "description",
        "environment": "environment",
        "memory_size": "memorySize",
        "policy_statements": "policyStatements",
        "timeout": "timeout",
    },
)
class CustomResourceProviderProps:
    def __init__(
        self,
        *,
        code_directory: builtins.str,
        runtime: "CustomResourceProviderRuntime",
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        memory_size: typing.Optional["Size"] = None,
        policy_statements: typing.Optional[typing.Sequence[typing.Any]] = None,
        timeout: typing.Optional["Duration"] = None,
    ) -> None:
        '''Initialization properties for ``CustomResourceProvider``.

        :param code_directory: A local file system directory with the provider's code. The code will be bundled into a zip asset and wired to the provider's AWS Lambda function.
        :param runtime: The AWS Lambda runtime and version to use for the provider.
        :param description: A description of the function. Default: - No description.
        :param environment: Key-value pairs that are passed to Lambda as Environment. Default: - No environment variables.
        :param memory_size: The amount of memory that your function has access to. Increasing the function's memory also increases its CPU allocation. Default: Size.mebibytes(128)
        :param policy_statements: A set of IAM policy statements to include in the inline policy of the provider's lambda function. Default: - no additional inline policy
        :param timeout: AWS Lambda timeout for the provider. Default: Duration.minutes(15)
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "code_directory": code_directory,
            "runtime": runtime,
        }
        if description is not None:
            self._values["description"] = description
        if environment is not None:
            self._values["environment"] = environment
        if memory_size is not None:
            self._values["memory_size"] = memory_size
        if policy_statements is not None:
            self._values["policy_statements"] = policy_statements
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def code_directory(self) -> builtins.str:
        '''A local file system directory with the provider's code.

        The code will be
        bundled into a zip asset and wired to the provider's AWS Lambda function.
        '''
        result = self._values.get("code_directory")
        assert result is not None, "Required property 'code_directory' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def runtime(self) -> "CustomResourceProviderRuntime":
        '''The AWS Lambda runtime and version to use for the provider.'''
        result = self._values.get("runtime")
        assert result is not None, "Required property 'runtime' is missing"
        return typing.cast("CustomResourceProviderRuntime", result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the function.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Key-value pairs that are passed to Lambda as Environment.

        :default: - No environment variables.
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def memory_size(self) -> typing.Optional["Size"]:
        '''The amount of memory that your function has access to.

        Increasing the
        function's memory also increases its CPU allocation.

        :default: Size.mebibytes(128)
        '''
        result = self._values.get("memory_size")
        return typing.cast(typing.Optional["Size"], result)

    @builtins.property
    def policy_statements(self) -> typing.Optional[typing.List[typing.Any]]:
        '''A set of IAM policy statements to include in the inline policy of the provider's lambda function.

        :default: - no additional inline policy

        Example::

            # Example automatically generated. See https://github.com/aws/jsii/issues/826
            [{"Effect": "Allow", "Action": "s3:PutObject*", "Resource": "*"}]
        '''
        result = self._values.get("policy_statements")
        return typing.cast(typing.Optional[typing.List[typing.Any]], result)

    @builtins.property
    def timeout(self) -> typing.Optional["Duration"]:
        '''AWS Lambda timeout for the provider.

        :default: Duration.minutes(15)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["Duration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomResourceProviderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/core.CustomResourceProviderRuntime")
class CustomResourceProviderRuntime(enum.Enum):
    '''The lambda runtime to use for the resource provider.

    This also indicates
    which language is used for the handler.
    '''

    NODEJS_12 = "NODEJS_12"
    '''(deprecated) Node.js 12.x.

    :deprecated: Use {@link NODEJS_12_X}

    :stability: deprecated
    '''
    NODEJS_14_X = "NODEJS_14_X"
    '''Node.js 14.x.'''


@jsii.data_type(
    jsii_type="@aws-cdk/core.DefaultStackSynthesizerProps",
    jsii_struct_bases=[],
    name_mapping={
        "bootstrap_stack_version_ssm_parameter": "bootstrapStackVersionSsmParameter",
        "bucket_prefix": "bucketPrefix",
        "cloud_formation_execution_role": "cloudFormationExecutionRole",
        "deploy_role_arn": "deployRoleArn",
        "file_asset_key_arn_export_name": "fileAssetKeyArnExportName",
        "file_asset_publishing_external_id": "fileAssetPublishingExternalId",
        "file_asset_publishing_role_arn": "fileAssetPublishingRoleArn",
        "file_assets_bucket_name": "fileAssetsBucketName",
        "generate_bootstrap_version_rule": "generateBootstrapVersionRule",
        "image_asset_publishing_external_id": "imageAssetPublishingExternalId",
        "image_asset_publishing_role_arn": "imageAssetPublishingRoleArn",
        "image_assets_repository_name": "imageAssetsRepositoryName",
        "lookup_role_arn": "lookupRoleArn",
        "qualifier": "qualifier",
    },
)
class DefaultStackSynthesizerProps:
    def __init__(
        self,
        *,
        bootstrap_stack_version_ssm_parameter: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        cloud_formation_execution_role: typing.Optional[builtins.str] = None,
        deploy_role_arn: typing.Optional[builtins.str] = None,
        file_asset_key_arn_export_name: typing.Optional[builtins.str] = None,
        file_asset_publishing_external_id: typing.Optional[builtins.str] = None,
        file_asset_publishing_role_arn: typing.Optional[builtins.str] = None,
        file_assets_bucket_name: typing.Optional[builtins.str] = None,
        generate_bootstrap_version_rule: typing.Optional[builtins.bool] = None,
        image_asset_publishing_external_id: typing.Optional[builtins.str] = None,
        image_asset_publishing_role_arn: typing.Optional[builtins.str] = None,
        image_assets_repository_name: typing.Optional[builtins.str] = None,
        lookup_role_arn: typing.Optional[builtins.str] = None,
        qualifier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Configuration properties for DefaultStackSynthesizer.

        :param bootstrap_stack_version_ssm_parameter: Bootstrap stack version SSM parameter. The placeholder ``${Qualifier}`` will be replaced with the value of qualifier. Default: DefaultStackSynthesizer.DEFAULT_BOOTSTRAP_STACK_VERSION_SSM_PARAMETER
        :param bucket_prefix: bucketPrefix to use while storing S3 Assets. Default: - DefaultStackSynthesizer.DEFAULT_FILE_ASSET_PREFIX
        :param cloud_formation_execution_role: The role CloudFormation will assume when deploying the Stack. You must supply this if you have given a non-standard name to the execution role. The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: DefaultStackSynthesizer.DEFAULT_CLOUDFORMATION_ROLE_ARN
        :param deploy_role_arn: The role to assume to initiate a deployment in this environment. You must supply this if you have given a non-standard name to the publishing role. The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: DefaultStackSynthesizer.DEFAULT_DEPLOY_ROLE_ARN
        :param file_asset_key_arn_export_name: (deprecated) Name of the CloudFormation Export with the asset key name. You must supply this if you have given a non-standard name to the KMS key export The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: DefaultStackSynthesizer.DEFAULT_FILE_ASSET_KEY_ARN_EXPORT_NAME
        :param file_asset_publishing_external_id: External ID to use when assuming role for file asset publishing. Default: - No external ID
        :param file_asset_publishing_role_arn: The role to use to publish file assets to the S3 bucket in this environment. You must supply this if you have given a non-standard name to the publishing role. The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: DefaultStackSynthesizer.DEFAULT_FILE_ASSET_PUBLISHING_ROLE_ARN
        :param file_assets_bucket_name: Name of the S3 bucket to hold file assets. You must supply this if you have given a non-standard name to the staging bucket. The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: DefaultStackSynthesizer.DEFAULT_FILE_ASSETS_BUCKET_NAME
        :param generate_bootstrap_version_rule: Whether to add a Rule to the stack template verifying the bootstrap stack version. This generally should be left set to ``true``, unless you explicitly want to be able to deploy to an unbootstrapped environment. Default: true
        :param image_asset_publishing_external_id: External ID to use when assuming role for image asset publishing. Default: - No external ID
        :param image_asset_publishing_role_arn: The role to use to publish image assets to the ECR repository in this environment. You must supply this if you have given a non-standard name to the publishing role. The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: DefaultStackSynthesizer.DEFAULT_IMAGE_ASSET_PUBLISHING_ROLE_ARN
        :param image_assets_repository_name: Name of the ECR repository to hold Docker Image assets. You must supply this if you have given a non-standard name to the ECR repository. The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: DefaultStackSynthesizer.DEFAULT_IMAGE_ASSETS_REPOSITORY_NAME
        :param lookup_role_arn: The role to use to look up values from the target AWS account during synthesis. Default: - None
        :param qualifier: Qualifier to disambiguate multiple environments in the same account. You can use this and leave the other naming properties empty if you have deployed the bootstrap environment with standard names but only differnet qualifiers. Default: - Value of context key '
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if bootstrap_stack_version_ssm_parameter is not None:
            self._values["bootstrap_stack_version_ssm_parameter"] = bootstrap_stack_version_ssm_parameter
        if bucket_prefix is not None:
            self._values["bucket_prefix"] = bucket_prefix
        if cloud_formation_execution_role is not None:
            self._values["cloud_formation_execution_role"] = cloud_formation_execution_role
        if deploy_role_arn is not None:
            self._values["deploy_role_arn"] = deploy_role_arn
        if file_asset_key_arn_export_name is not None:
            self._values["file_asset_key_arn_export_name"] = file_asset_key_arn_export_name
        if file_asset_publishing_external_id is not None:
            self._values["file_asset_publishing_external_id"] = file_asset_publishing_external_id
        if file_asset_publishing_role_arn is not None:
            self._values["file_asset_publishing_role_arn"] = file_asset_publishing_role_arn
        if file_assets_bucket_name is not None:
            self._values["file_assets_bucket_name"] = file_assets_bucket_name
        if generate_bootstrap_version_rule is not None:
            self._values["generate_bootstrap_version_rule"] = generate_bootstrap_version_rule
        if image_asset_publishing_external_id is not None:
            self._values["image_asset_publishing_external_id"] = image_asset_publishing_external_id
        if image_asset_publishing_role_arn is not None:
            self._values["image_asset_publishing_role_arn"] = image_asset_publishing_role_arn
        if image_assets_repository_name is not None:
            self._values["image_assets_repository_name"] = image_assets_repository_name
        if lookup_role_arn is not None:
            self._values["lookup_role_arn"] = lookup_role_arn
        if qualifier is not None:
            self._values["qualifier"] = qualifier

    @builtins.property
    def bootstrap_stack_version_ssm_parameter(self) -> typing.Optional[builtins.str]:
        '''Bootstrap stack version SSM parameter.

        The placeholder ``${Qualifier}`` will be replaced with the value of qualifier.

        :default: DefaultStackSynthesizer.DEFAULT_BOOTSTRAP_STACK_VERSION_SSM_PARAMETER
        '''
        result = self._values.get("bootstrap_stack_version_ssm_parameter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bucket_prefix(self) -> typing.Optional[builtins.str]:
        '''bucketPrefix to use while storing S3 Assets.

        :default: - DefaultStackSynthesizer.DEFAULT_FILE_ASSET_PREFIX
        '''
        result = self._values.get("bucket_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_formation_execution_role(self) -> typing.Optional[builtins.str]:
        '''The role CloudFormation will assume when deploying the Stack.

        You must supply this if you have given a non-standard name to the execution role.

        The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will
        be replaced with the values of qualifier and the stack's account and region,
        respectively.

        :default: DefaultStackSynthesizer.DEFAULT_CLOUDFORMATION_ROLE_ARN
        '''
        result = self._values.get("cloud_formation_execution_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deploy_role_arn(self) -> typing.Optional[builtins.str]:
        '''The role to assume to initiate a deployment in this environment.

        You must supply this if you have given a non-standard name to the publishing role.

        The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will
        be replaced with the values of qualifier and the stack's account and region,
        respectively.

        :default: DefaultStackSynthesizer.DEFAULT_DEPLOY_ROLE_ARN
        '''
        result = self._values.get("deploy_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_asset_key_arn_export_name(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Name of the CloudFormation Export with the asset key name.

        You must supply this if you have given a non-standard name to the KMS key export

        The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will
        be replaced with the values of qualifier and the stack's account and region,
        respectively.

        :default: DefaultStackSynthesizer.DEFAULT_FILE_ASSET_KEY_ARN_EXPORT_NAME

        :deprecated: This property is not used anymore

        :stability: deprecated
        '''
        result = self._values.get("file_asset_key_arn_export_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_asset_publishing_external_id(self) -> typing.Optional[builtins.str]:
        '''External ID to use when assuming role for file asset publishing.

        :default: - No external ID
        '''
        result = self._values.get("file_asset_publishing_external_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_asset_publishing_role_arn(self) -> typing.Optional[builtins.str]:
        '''The role to use to publish file assets to the S3 bucket in this environment.

        You must supply this if you have given a non-standard name to the publishing role.

        The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will
        be replaced with the values of qualifier and the stack's account and region,
        respectively.

        :default: DefaultStackSynthesizer.DEFAULT_FILE_ASSET_PUBLISHING_ROLE_ARN
        '''
        result = self._values.get("file_asset_publishing_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_assets_bucket_name(self) -> typing.Optional[builtins.str]:
        '''Name of the S3 bucket to hold file assets.

        You must supply this if you have given a non-standard name to the staging bucket.

        The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will
        be replaced with the values of qualifier and the stack's account and region,
        respectively.

        :default: DefaultStackSynthesizer.DEFAULT_FILE_ASSETS_BUCKET_NAME
        '''
        result = self._values.get("file_assets_bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def generate_bootstrap_version_rule(self) -> typing.Optional[builtins.bool]:
        '''Whether to add a Rule to the stack template verifying the bootstrap stack version.

        This generally should be left set to ``true``, unless you explicitly
        want to be able to deploy to an unbootstrapped environment.

        :default: true
        '''
        result = self._values.get("generate_bootstrap_version_rule")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def image_asset_publishing_external_id(self) -> typing.Optional[builtins.str]:
        '''External ID to use when assuming role for image asset publishing.

        :default: - No external ID
        '''
        result = self._values.get("image_asset_publishing_external_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_asset_publishing_role_arn(self) -> typing.Optional[builtins.str]:
        '''The role to use to publish image assets to the ECR repository in this environment.

        You must supply this if you have given a non-standard name to the publishing role.

        The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will
        be replaced with the values of qualifier and the stack's account and region,
        respectively.

        :default: DefaultStackSynthesizer.DEFAULT_IMAGE_ASSET_PUBLISHING_ROLE_ARN
        '''
        result = self._values.get("image_asset_publishing_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_assets_repository_name(self) -> typing.Optional[builtins.str]:
        '''Name of the ECR repository to hold Docker Image assets.

        You must supply this if you have given a non-standard name to the ECR repository.

        The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will
        be replaced with the values of qualifier and the stack's account and region,
        respectively.

        :default: DefaultStackSynthesizer.DEFAULT_IMAGE_ASSETS_REPOSITORY_NAME
        '''
        result = self._values.get("image_assets_repository_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lookup_role_arn(self) -> typing.Optional[builtins.str]:
        '''The role to use to look up values from the target AWS account during synthesis.

        :default: - None
        '''
        result = self._values.get("lookup_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def qualifier(self) -> typing.Optional[builtins.str]:
        '''Qualifier to disambiguate multiple environments in the same account.

        You can use this and leave the other naming properties empty if you have deployed
        the bootstrap environment with standard names but only differnet qualifiers.

        :default: - Value of context key '

        :aws-cdk: /core:bootstrapQualifier' if set, otherwise ``DefaultStackSynthesizer.DEFAULT_QUALIFIER``
        '''
        result = self._values.get("qualifier")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DefaultStackSynthesizerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DependableTrait(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/core.DependableTrait",
):
    '''Trait for IDependable.

    Traits are interfaces that are privately implemented by objects. Instead of
    showing up in the public interface of a class, they need to be queried
    explicitly. This is used to implement certain framework features that are
    not intended to be used by Construct consumers, and so should be hidden
    from accidental use.

    Example::

        # Example automatically generated. See https://github.com/aws/jsii/issues/826
        # Usage
        roots = DependableTrait.get(construct).dependency_roots
        
        # Definition
        class TraitImplementation(DependableTrait):
            def __init__(self):
                self.dependency_roots = [construct_a, construct_b, construct_c]
        DependableTrait.implement(construct, TraitImplementation())
    '''

    def __init__(self) -> None:
        jsii.create(DependableTrait, self, [])

    @jsii.member(jsii_name="get") # type: ignore[misc]
    @builtins.classmethod
    def get(cls, instance: "IDependable") -> "DependableTrait":
        '''Return the matching DependableTrait for the given class instance.

        :param instance: -
        '''
        return typing.cast("DependableTrait", jsii.sinvoke(cls, "get", [instance]))

    @jsii.member(jsii_name="implement") # type: ignore[misc]
    @builtins.classmethod
    def implement(cls, instance: "IDependable", trait: "DependableTrait") -> None:
        '''Register ``instance`` to have the given DependableTrait.

        Should be called in the class constructor.

        :param instance: -
        :param trait: -
        '''
        return typing.cast(None, jsii.sinvoke(cls, "implement", [instance, trait]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dependencyRoots")
    @abc.abstractmethod
    def dependency_roots(self) -> typing.List["IConstruct"]:
        '''The set of constructs that form the root of this dependable.

        All resources under all returned constructs are included in the ordering
        dependency.
        '''
        ...


class _DependableTraitProxy(DependableTrait):
    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dependencyRoots")
    def dependency_roots(self) -> typing.List["IConstruct"]:
        '''The set of constructs that form the root of this dependable.

        All resources under all returned constructs are included in the ordering
        dependency.
        '''
        return typing.cast(typing.List["IConstruct"], jsii.get(self, "dependencyRoots"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, DependableTrait).__jsii_proxy_class__ = lambda : _DependableTraitProxy


@jsii.data_type(
    jsii_type="@aws-cdk/core.Dependency",
    jsii_struct_bases=[],
    name_mapping={"source": "source", "target": "target"},
)
class Dependency:
    def __init__(self, *, source: "IConstruct", target: "IConstruct") -> None:
        '''A single dependency.

        :param source: Source the dependency.
        :param target: Target of the dependency.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "source": source,
            "target": target,
        }

    @builtins.property
    def source(self) -> "IConstruct":
        '''Source the dependency.'''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast("IConstruct", result)

    @builtins.property
    def target(self) -> "IConstruct":
        '''Target of the dependency.'''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast("IConstruct", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Dependency(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.DockerBuildOptions",
    jsii_struct_bases=[],
    name_mapping={"build_args": "buildArgs", "file": "file", "platform": "platform"},
)
class DockerBuildOptions:
    def __init__(
        self,
        *,
        build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        file: typing.Optional[builtins.str] = None,
        platform: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Docker build options.

        :param build_args: Build args. Default: - no build args
        :param file: Name of the Dockerfile, must relative to the docker build path. Default: ``Dockerfile``
        :param platform: Set platform if server is multi-platform capable. *Requires Docker Engine API v1.38+*. Default: - no platform specified
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if build_args is not None:
            self._values["build_args"] = build_args
        if file is not None:
            self._values["file"] = file
        if platform is not None:
            self._values["platform"] = platform

    @builtins.property
    def build_args(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Build args.

        :default: - no build args
        '''
        result = self._values.get("build_args")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def file(self) -> typing.Optional[builtins.str]:
        '''Name of the Dockerfile, must relative to the docker build path.

        :default: ``Dockerfile``
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def platform(self) -> typing.Optional[builtins.str]:
        '''Set platform if server is multi-platform capable.

        *Requires Docker Engine API v1.38+*.

        :default: - no platform specified

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            "linux/amd64"
        '''
        result = self._values.get("platform")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerBuildOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DockerImage(
    BundlingDockerImage,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.DockerImage",
):
    '''A Docker image.'''

    def __init__(
        self,
        image: builtins.str,
        _image_hash: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image: The Docker image.
        :param _image_hash: -
        '''
        jsii.create(DockerImage, self, [image, _image_hash])

    @jsii.member(jsii_name="fromBuild") # type: ignore[misc]
    @builtins.classmethod
    def from_build(
        cls,
        path: builtins.str,
        *,
        build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        file: typing.Optional[builtins.str] = None,
        platform: typing.Optional[builtins.str] = None,
    ) -> "DockerImage":
        '''Builds a Docker image.

        :param path: The path to the directory containing the Docker file.
        :param build_args: Build args. Default: - no build args
        :param file: Name of the Dockerfile, must relative to the docker build path. Default: ``Dockerfile``
        :param platform: Set platform if server is multi-platform capable. *Requires Docker Engine API v1.38+*. Default: - no platform specified
        '''
        options = DockerBuildOptions(
            build_args=build_args, file=file, platform=platform
        )

        return typing.cast("DockerImage", jsii.sinvoke(cls, "fromBuild", [path, options]))

    @jsii.member(jsii_name="fromRegistry") # type: ignore[misc]
    @builtins.classmethod
    def from_registry(cls, image: builtins.str) -> "DockerImage":
        '''Reference an image on DockerHub or another online registry.

        :param image: the image name.
        '''
        return typing.cast("DockerImage", jsii.sinvoke(cls, "fromRegistry", [image]))

    @jsii.member(jsii_name="cp")
    def cp(
        self,
        image_path: builtins.str,
        output_path: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''Copies a file or directory out of the Docker image to the local filesystem.

        If ``outputPath`` is omitted the destination path is a temporary directory.

        :param image_path: the path in the Docker image.
        :param output_path: the destination path for the copy operation.

        :return: the destination path
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "cp", [image_path, output_path]))

    @jsii.member(jsii_name="run")
    def run(
        self,
        *,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        security_opt: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Sequence["DockerVolume"]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Runs a Docker image.

        :param command: The command to run in the container. Default: - run the command defined in the image
        :param entrypoint: The entrypoint to run in the container. Default: - run the entrypoint defined in the image
        :param environment: The environment variables to pass to the container. Default: - no environment variables.
        :param security_opt: `Security configuration <https://docs.docker.com/engine/reference/run/#security-configuration>`_ when running the docker container. Default: - no security options
        :param user: The user to use when running the container. Default: - root or image default
        :param volumes: Docker volumes to mount. Default: - no volumes are mounted
        :param working_directory: Working directory inside the container. Default: - image default
        '''
        options = DockerRunOptions(
            command=command,
            entrypoint=entrypoint,
            environment=environment,
            security_opt=security_opt,
            user=user,
            volumes=volumes,
            working_directory=working_directory,
        )

        return typing.cast(None, jsii.invoke(self, "run", [options]))

    @jsii.member(jsii_name="toJSON")
    def to_json(self) -> builtins.str:
        '''Provides a stable representation of this image for JSON serialization.

        :return: The overridden image name if set or image hash name in that order
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toJSON", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        '''The Docker image.'''
        return typing.cast(builtins.str, jsii.get(self, "image"))


@jsii.data_type(
    jsii_type="@aws-cdk/core.DockerImageAssetLocation",
    jsii_struct_bases=[],
    name_mapping={"image_uri": "imageUri", "repository_name": "repositoryName"},
)
class DockerImageAssetLocation:
    def __init__(
        self,
        *,
        image_uri: builtins.str,
        repository_name: builtins.str,
    ) -> None:
        '''The location of the published docker image.

        This is where the image can be
        consumed at runtime.

        :param image_uri: The URI of the image in Amazon ECR.
        :param repository_name: The name of the ECR repository.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "image_uri": image_uri,
            "repository_name": repository_name,
        }

    @builtins.property
    def image_uri(self) -> builtins.str:
        '''The URI of the image in Amazon ECR.'''
        result = self._values.get("image_uri")
        assert result is not None, "Required property 'image_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository_name(self) -> builtins.str:
        '''The name of the ECR repository.'''
        result = self._values.get("repository_name")
        assert result is not None, "Required property 'repository_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerImageAssetLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.DockerImageAssetSource",
    jsii_struct_bases=[],
    name_mapping={
        "source_hash": "sourceHash",
        "directory_name": "directoryName",
        "docker_build_args": "dockerBuildArgs",
        "docker_build_target": "dockerBuildTarget",
        "docker_file": "dockerFile",
        "executable": "executable",
        "repository_name": "repositoryName",
    },
)
class DockerImageAssetSource:
    def __init__(
        self,
        *,
        source_hash: builtins.str,
        directory_name: typing.Optional[builtins.str] = None,
        docker_build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        docker_build_target: typing.Optional[builtins.str] = None,
        docker_file: typing.Optional[builtins.str] = None,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        repository_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source_hash: The hash of the contents of the docker build context. This hash is used throughout the system to identify this image and avoid duplicate work in case the source did not change. NOTE: this means that if you wish to update your docker image, you must make a modification to the source (e.g. add some metadata to your Dockerfile).
        :param directory_name: The directory where the Dockerfile is stored, must be relative to the cloud assembly root. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param docker_build_args: Build args to pass to the ``docker build`` command. Since Docker build arguments are resolved before deployment, keys and values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or ``queue.queueUrl``). Only allowed when ``directoryName`` is specified. Default: - no build args are passed
        :param docker_build_target: Docker target to build to. Only allowed when ``directoryName`` is specified. Default: - no target
        :param docker_file: Path to the Dockerfile (relative to the directory). Only allowed when ``directoryName`` is specified. Default: - no file
        :param executable: An external command that will produce the packaged asset. The command should produce the name of a local Docker image on ``stdout``. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param repository_name: (deprecated) ECR repository name. Specify this property if you need to statically address the image, e.g. from a Kubernetes Pod. Note, this is only the repository name, without the registry and the tag parts. Default: - automatically derived from the asset's ID.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "source_hash": source_hash,
        }
        if directory_name is not None:
            self._values["directory_name"] = directory_name
        if docker_build_args is not None:
            self._values["docker_build_args"] = docker_build_args
        if docker_build_target is not None:
            self._values["docker_build_target"] = docker_build_target
        if docker_file is not None:
            self._values["docker_file"] = docker_file
        if executable is not None:
            self._values["executable"] = executable
        if repository_name is not None:
            self._values["repository_name"] = repository_name

    @builtins.property
    def source_hash(self) -> builtins.str:
        '''The hash of the contents of the docker build context.

        This hash is used
        throughout the system to identify this image and avoid duplicate work
        in case the source did not change.

        NOTE: this means that if you wish to update your docker image, you
        must make a modification to the source (e.g. add some metadata to your Dockerfile).
        '''
        result = self._values.get("source_hash")
        assert result is not None, "Required property 'source_hash' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def directory_name(self) -> typing.Optional[builtins.str]:
        '''The directory where the Dockerfile is stored, must be relative to the cloud assembly root.

        :default: - Exactly one of ``directoryName`` and ``executable`` is required
        '''
        result = self._values.get("directory_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_build_args(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Build args to pass to the ``docker build`` command.

        Since Docker build arguments are resolved before deployment, keys and
        values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or
        ``queue.queueUrl``).

        Only allowed when ``directoryName`` is specified.

        :default: - no build args are passed
        '''
        result = self._values.get("docker_build_args")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def docker_build_target(self) -> typing.Optional[builtins.str]:
        '''Docker target to build to.

        Only allowed when ``directoryName`` is specified.

        :default: - no target
        '''
        result = self._values.get("docker_build_target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_file(self) -> typing.Optional[builtins.str]:
        '''Path to the Dockerfile (relative to the directory).

        Only allowed when ``directoryName`` is specified.

        :default: - no file
        '''
        result = self._values.get("docker_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def executable(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An external command that will produce the packaged asset.

        The command should produce the name of a local Docker image on ``stdout``.

        :default: - Exactly one of ``directoryName`` and ``executable`` is required
        '''
        result = self._values.get("executable")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def repository_name(self) -> typing.Optional[builtins.str]:
        '''(deprecated) ECR repository name.

        Specify this property if you need to statically address the image, e.g.
        from a Kubernetes Pod. Note, this is only the repository name, without the
        registry and the tag parts.

        :default: - automatically derived from the asset's ID.

        :deprecated: repository name should be specified at the environment-level and not at the image level

        :stability: deprecated
        '''
        result = self._values.get("repository_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerImageAssetSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.DockerRunOptions",
    jsii_struct_bases=[],
    name_mapping={
        "command": "command",
        "entrypoint": "entrypoint",
        "environment": "environment",
        "security_opt": "securityOpt",
        "user": "user",
        "volumes": "volumes",
        "working_directory": "workingDirectory",
    },
)
class DockerRunOptions:
    def __init__(
        self,
        *,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        security_opt: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Sequence["DockerVolume"]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Docker run options.

        :param command: The command to run in the container. Default: - run the command defined in the image
        :param entrypoint: The entrypoint to run in the container. Default: - run the entrypoint defined in the image
        :param environment: The environment variables to pass to the container. Default: - no environment variables.
        :param security_opt: `Security configuration <https://docs.docker.com/engine/reference/run/#security-configuration>`_ when running the docker container. Default: - no security options
        :param user: The user to use when running the container. Default: - root or image default
        :param volumes: Docker volumes to mount. Default: - no volumes are mounted
        :param working_directory: Working directory inside the container. Default: - image default
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if command is not None:
            self._values["command"] = command
        if entrypoint is not None:
            self._values["entrypoint"] = entrypoint
        if environment is not None:
            self._values["environment"] = environment
        if security_opt is not None:
            self._values["security_opt"] = security_opt
        if user is not None:
            self._values["user"] = user
        if volumes is not None:
            self._values["volumes"] = volumes
        if working_directory is not None:
            self._values["working_directory"] = working_directory

    @builtins.property
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The command to run in the container.

        :default: - run the command defined in the image
        '''
        result = self._values.get("command")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The entrypoint to run in the container.

        :default: - run the entrypoint defined in the image
        '''
        result = self._values.get("entrypoint")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The environment variables to pass to the container.

        :default: - no environment variables.
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def security_opt(self) -> typing.Optional[builtins.str]:
        '''`Security configuration <https://docs.docker.com/engine/reference/run/#security-configuration>`_ when running the docker container.

        :default: - no security options
        '''
        result = self._values.get("security_opt")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''The user to use when running the container.

        :default: - root or image default
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List["DockerVolume"]]:
        '''Docker volumes to mount.

        :default: - no volumes are mounted
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List["DockerVolume"]], result)

    @builtins.property
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''Working directory inside the container.

        :default: - image default
        '''
        result = self._values.get("working_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerRunOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.DockerVolume",
    jsii_struct_bases=[],
    name_mapping={
        "container_path": "containerPath",
        "host_path": "hostPath",
        "consistency": "consistency",
    },
)
class DockerVolume:
    def __init__(
        self,
        *,
        container_path: builtins.str,
        host_path: builtins.str,
        consistency: typing.Optional["DockerVolumeConsistency"] = None,
    ) -> None:
        '''A Docker volume.

        :param container_path: The path where the file or directory is mounted in the container.
        :param host_path: The path to the file or directory on the host machine.
        :param consistency: Mount consistency. Only applicable for macOS Default: DockerConsistency.DELEGATED
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "container_path": container_path,
            "host_path": host_path,
        }
        if consistency is not None:
            self._values["consistency"] = consistency

    @builtins.property
    def container_path(self) -> builtins.str:
        '''The path where the file or directory is mounted in the container.'''
        result = self._values.get("container_path")
        assert result is not None, "Required property 'container_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host_path(self) -> builtins.str:
        '''The path to the file or directory on the host machine.'''
        result = self._values.get("host_path")
        assert result is not None, "Required property 'host_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def consistency(self) -> typing.Optional["DockerVolumeConsistency"]:
        '''Mount consistency.

        Only applicable for macOS

        :default: DockerConsistency.DELEGATED

        :see: https://docs.docker.com/storage/bind-mounts/#configure-mount-consistency-for-macos
        '''
        result = self._values.get("consistency")
        return typing.cast(typing.Optional["DockerVolumeConsistency"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DockerVolume(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/core.DockerVolumeConsistency")
class DockerVolumeConsistency(enum.Enum):
    '''Supported Docker volume consistency types.

    Only valid on macOS due to the way file storage works on Mac
    '''

    CONSISTENT = "CONSISTENT"
    '''Read/write operations inside the Docker container are applied immediately on the mounted host machine volumes.'''
    DELEGATED = "DELEGATED"
    '''Read/write operations on mounted Docker volumes are first written inside the container and then synchronized to the host machine.'''
    CACHED = "CACHED"
    '''Read/write operations on mounted Docker volumes are first applied on the host machine and then synchronized to the container.'''


class Duration(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.Duration"):
    '''Represents a length of time.

    The amount can be specified either as a literal value (e.g: ``10``) which
    cannot be negative, or as an unresolved number token.

    When the amount is passed as a token, unit conversion is not possible.
    '''

    @jsii.member(jsii_name="days") # type: ignore[misc]
    @builtins.classmethod
    def days(cls, amount: jsii.Number) -> "Duration":
        '''Create a Duration representing an amount of days.

        :param amount: the amount of Days the ``Duration`` will represent.

        :return: a new ``Duration`` representing ``amount`` Days.
        '''
        return typing.cast("Duration", jsii.sinvoke(cls, "days", [amount]))

    @jsii.member(jsii_name="hours") # type: ignore[misc]
    @builtins.classmethod
    def hours(cls, amount: jsii.Number) -> "Duration":
        '''Create a Duration representing an amount of hours.

        :param amount: the amount of Hours the ``Duration`` will represent.

        :return: a new ``Duration`` representing ``amount`` Hours.
        '''
        return typing.cast("Duration", jsii.sinvoke(cls, "hours", [amount]))

    @jsii.member(jsii_name="millis") # type: ignore[misc]
    @builtins.classmethod
    def millis(cls, amount: jsii.Number) -> "Duration":
        '''Create a Duration representing an amount of milliseconds.

        :param amount: the amount of Milliseconds the ``Duration`` will represent.

        :return: a new ``Duration`` representing ``amount`` ms.
        '''
        return typing.cast("Duration", jsii.sinvoke(cls, "millis", [amount]))

    @jsii.member(jsii_name="minutes") # type: ignore[misc]
    @builtins.classmethod
    def minutes(cls, amount: jsii.Number) -> "Duration":
        '''Create a Duration representing an amount of minutes.

        :param amount: the amount of Minutes the ``Duration`` will represent.

        :return: a new ``Duration`` representing ``amount`` Minutes.
        '''
        return typing.cast("Duration", jsii.sinvoke(cls, "minutes", [amount]))

    @jsii.member(jsii_name="parse") # type: ignore[misc]
    @builtins.classmethod
    def parse(cls, duration: builtins.str) -> "Duration":
        '''Parse a period formatted according to the ISO 8601 standard.

        :param duration: an ISO-formtted duration to be parsed.

        :return: the parsed ``Duration``.

        :see: https://www.iso.org/fr/standard/70907.html
        '''
        return typing.cast("Duration", jsii.sinvoke(cls, "parse", [duration]))

    @jsii.member(jsii_name="seconds") # type: ignore[misc]
    @builtins.classmethod
    def seconds(cls, amount: jsii.Number) -> "Duration":
        '''Create a Duration representing an amount of seconds.

        :param amount: the amount of Seconds the ``Duration`` will represent.

        :return: a new ``Duration`` representing ``amount`` Seconds.
        '''
        return typing.cast("Duration", jsii.sinvoke(cls, "seconds", [amount]))

    @jsii.member(jsii_name="formatTokenToNumber")
    def format_token_to_number(self) -> builtins.str:
        '''Returns stringified number of duration.'''
        return typing.cast(builtins.str, jsii.invoke(self, "formatTokenToNumber", []))

    @jsii.member(jsii_name="isUnresolved")
    def is_unresolved(self) -> builtins.bool:
        '''Checks if duration is a token or a resolvable object.'''
        return typing.cast(builtins.bool, jsii.invoke(self, "isUnresolved", []))

    @jsii.member(jsii_name="plus")
    def plus(self, rhs: "Duration") -> "Duration":
        '''Add two Durations together.

        :param rhs: -
        '''
        return typing.cast("Duration", jsii.invoke(self, "plus", [rhs]))

    @jsii.member(jsii_name="toDays")
    def to_days(
        self,
        *,
        integral: typing.Optional[builtins.bool] = None,
    ) -> jsii.Number:
        '''Return the total number of days in this Duration.

        :param integral: If ``true``, conversions into a larger time unit (e.g. ``Seconds`` to ``Minutes``) will fail if the result is not an integer. Default: true

        :return: the value of this ``Duration`` expressed in Days.
        '''
        opts = TimeConversionOptions(integral=integral)

        return typing.cast(jsii.Number, jsii.invoke(self, "toDays", [opts]))

    @jsii.member(jsii_name="toHours")
    def to_hours(
        self,
        *,
        integral: typing.Optional[builtins.bool] = None,
    ) -> jsii.Number:
        '''Return the total number of hours in this Duration.

        :param integral: If ``true``, conversions into a larger time unit (e.g. ``Seconds`` to ``Minutes``) will fail if the result is not an integer. Default: true

        :return: the value of this ``Duration`` expressed in Hours.
        '''
        opts = TimeConversionOptions(integral=integral)

        return typing.cast(jsii.Number, jsii.invoke(self, "toHours", [opts]))

    @jsii.member(jsii_name="toHumanString")
    def to_human_string(self) -> builtins.str:
        '''Turn this duration into a human-readable string.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toHumanString", []))

    @jsii.member(jsii_name="toIsoString")
    def to_iso_string(self) -> builtins.str:
        '''Return an ISO 8601 representation of this period.

        :return: a string starting with 'P' describing the period

        :see: https://www.iso.org/fr/standard/70907.html
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toIsoString", []))

    @jsii.member(jsii_name="toMilliseconds")
    def to_milliseconds(
        self,
        *,
        integral: typing.Optional[builtins.bool] = None,
    ) -> jsii.Number:
        '''Return the total number of milliseconds in this Duration.

        :param integral: If ``true``, conversions into a larger time unit (e.g. ``Seconds`` to ``Minutes``) will fail if the result is not an integer. Default: true

        :return: the value of this ``Duration`` expressed in Milliseconds.
        '''
        opts = TimeConversionOptions(integral=integral)

        return typing.cast(jsii.Number, jsii.invoke(self, "toMilliseconds", [opts]))

    @jsii.member(jsii_name="toMinutes")
    def to_minutes(
        self,
        *,
        integral: typing.Optional[builtins.bool] = None,
    ) -> jsii.Number:
        '''Return the total number of minutes in this Duration.

        :param integral: If ``true``, conversions into a larger time unit (e.g. ``Seconds`` to ``Minutes``) will fail if the result is not an integer. Default: true

        :return: the value of this ``Duration`` expressed in Minutes.
        '''
        opts = TimeConversionOptions(integral=integral)

        return typing.cast(jsii.Number, jsii.invoke(self, "toMinutes", [opts]))

    @jsii.member(jsii_name="toSeconds")
    def to_seconds(
        self,
        *,
        integral: typing.Optional[builtins.bool] = None,
    ) -> jsii.Number:
        '''Return the total number of seconds in this Duration.

        :param integral: If ``true``, conversions into a larger time unit (e.g. ``Seconds`` to ``Minutes``) will fail if the result is not an integer. Default: true

        :return: the value of this ``Duration`` expressed in Seconds.
        '''
        opts = TimeConversionOptions(integral=integral)

        return typing.cast(jsii.Number, jsii.invoke(self, "toSeconds", [opts]))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of this ``Duration`` that is also a Token that cannot be successfully resolved.

        This
        protects users against inadvertently stringifying a ``Duration`` object, when they should have called one of the
        ``to*`` methods instead.
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @jsii.member(jsii_name="unitLabel")
    def unit_label(self) -> builtins.str:
        '''Returns unit of the duration.'''
        return typing.cast(builtins.str, jsii.invoke(self, "unitLabel", []))


@jsii.data_type(
    jsii_type="@aws-cdk/core.EncodingOptions",
    jsii_struct_bases=[],
    name_mapping={"display_hint": "displayHint"},
)
class EncodingOptions:
    def __init__(self, *, display_hint: typing.Optional[builtins.str] = None) -> None:
        '''Properties to string encodings.

        :param display_hint: A hint for the Token's purpose when stringifying it.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if display_hint is not None:
            self._values["display_hint"] = display_hint

    @builtins.property
    def display_hint(self) -> typing.Optional[builtins.str]:
        '''A hint for the Token's purpose when stringifying it.'''
        result = self._values.get("display_hint")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EncodingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.Environment",
    jsii_struct_bases=[],
    name_mapping={"account": "account", "region": "region"},
)
class Environment:
    def __init__(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The deployment environment for a stack.

        :param account: The AWS account ID for this environment. This can be either a concrete value such as ``585191031104`` or ``Aws.accountId`` which indicates that account ID will only be determined during deployment (it will resolve to the CloudFormation intrinsic ``{"Ref":"AWS::AccountId"}``). Note that certain features, such as cross-stack references and environmental context providers require concerete region information and will cause this stack to emit synthesis errors. Default: Aws.accountId which means that the stack will be account-agnostic.
        :param region: The AWS region for this environment. This can be either a concrete value such as ``eu-west-2`` or ``Aws.region`` which indicates that account ID will only be determined during deployment (it will resolve to the CloudFormation intrinsic ``{"Ref":"AWS::Region"}``). Note that certain features, such as cross-stack references and environmental context providers require concerete region information and will cause this stack to emit synthesis errors. Default: Aws.region which means that the stack will be region-agnostic.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if account is not None:
            self._values["account"] = account
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID for this environment.

        This can be either a concrete value such as ``585191031104`` or ``Aws.accountId`` which
        indicates that account ID will only be determined during deployment (it
        will resolve to the CloudFormation intrinsic ``{"Ref":"AWS::AccountId"}``).
        Note that certain features, such as cross-stack references and
        environmental context providers require concerete region information and
        will cause this stack to emit synthesis errors.

        :default: Aws.accountId which means that the stack will be account-agnostic.
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The AWS region for this environment.

        This can be either a concrete value such as ``eu-west-2`` or ``Aws.region``
        which indicates that account ID will only be determined during deployment
        (it will resolve to the CloudFormation intrinsic ``{"Ref":"AWS::Region"}``).
        Note that certain features, such as cross-stack references and
        environmental context providers require concerete region information and
        will cause this stack to emit synthesis errors.

        :default: Aws.region which means that the stack will be region-agnostic.
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Environment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Expiration(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.Expiration"):
    '''Represents a date of expiration.

    The amount can be specified either as a Date object, timestamp, Duration or string.
    '''

    @jsii.member(jsii_name="after") # type: ignore[misc]
    @builtins.classmethod
    def after(cls, t: Duration) -> "Expiration":
        '''Expire once the specified duration has passed since deployment time.

        :param t: the duration to wait before expiring.
        '''
        return typing.cast("Expiration", jsii.sinvoke(cls, "after", [t]))

    @jsii.member(jsii_name="atDate") # type: ignore[misc]
    @builtins.classmethod
    def at_date(cls, d: datetime.datetime) -> "Expiration":
        '''Expire at the specified date.

        :param d: date to expire at.
        '''
        return typing.cast("Expiration", jsii.sinvoke(cls, "atDate", [d]))

    @jsii.member(jsii_name="atTimestamp") # type: ignore[misc]
    @builtins.classmethod
    def at_timestamp(cls, t: jsii.Number) -> "Expiration":
        '''Expire at the specified timestamp.

        :param t: timestamp in unix milliseconds.
        '''
        return typing.cast("Expiration", jsii.sinvoke(cls, "atTimestamp", [t]))

    @jsii.member(jsii_name="fromString") # type: ignore[misc]
    @builtins.classmethod
    def from_string(cls, s: builtins.str) -> "Expiration":
        '''Expire at specified date, represented as a string.

        :param s: the string that represents date to expire at.
        '''
        return typing.cast("Expiration", jsii.sinvoke(cls, "fromString", [s]))

    @jsii.member(jsii_name="isAfter")
    def is_after(self, t: Duration) -> builtins.bool:
        '''Check if Exipiration expires after input.

        :param t: the duration to check against.
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "isAfter", [t]))

    @jsii.member(jsii_name="isBefore")
    def is_before(self, t: Duration) -> builtins.bool:
        '''Check if Exipiration expires before input.

        :param t: the duration to check against.
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "isBefore", [t]))

    @jsii.member(jsii_name="toEpoch")
    def to_epoch(self) -> jsii.Number:
        '''Exipration Value in a formatted Unix Epoch Time in seconds.'''
        return typing.cast(jsii.Number, jsii.invoke(self, "toEpoch", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="date")
    def date(self) -> datetime.datetime:
        '''Expiration value as a Date object.'''
        return typing.cast(datetime.datetime, jsii.get(self, "date"))


@jsii.data_type(
    jsii_type="@aws-cdk/core.ExportValueOptions",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class ExportValueOptions:
    def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
        '''Options for the ``stack.exportValue()`` method.

        :param name: The name of the export to create. Default: - A name is automatically chosen
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the export to create.

        :default: - A name is automatically chosen
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExportValueOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FeatureFlags(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.FeatureFlags"):
    '''Features that are implemented behind a flag in order to preserve backwards compatibility for existing apps.

    The list of flags are available in the
    ``@aws-cdk/cx-api`` module.

    The state of the flag for this application is stored as a CDK context variable.
    '''

    @jsii.member(jsii_name="of") # type: ignore[misc]
    @builtins.classmethod
    def of(cls, scope: "Construct") -> "FeatureFlags":
        '''Inspect feature flags on the construct node's context.

        :param scope: -
        '''
        return typing.cast("FeatureFlags", jsii.sinvoke(cls, "of", [scope]))

    @jsii.member(jsii_name="isEnabled")
    def is_enabled(self, feature_flag: builtins.str) -> typing.Optional[builtins.bool]:
        '''Check whether a feature flag is enabled.

        If configured, the flag is present in
        the construct node context. Falls back to the defaults defined in the ``cx-api``
        module.

        :param feature_flag: -
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.invoke(self, "isEnabled", [feature_flag]))


@jsii.data_type(
    jsii_type="@aws-cdk/core.FileAssetLocation",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "http_url": "httpUrl",
        "object_key": "objectKey",
        "s3_object_url": "s3ObjectUrl",
        "kms_key_arn": "kmsKeyArn",
        "s3_url": "s3Url",
    },
)
class FileAssetLocation:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        http_url: builtins.str,
        object_key: builtins.str,
        s3_object_url: builtins.str,
        kms_key_arn: typing.Optional[builtins.str] = None,
        s3_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''The location of the published file asset.

        This is where the asset
        can be consumed at runtime.

        :param bucket_name: The name of the Amazon S3 bucket.
        :param http_url: The HTTP URL of this asset on Amazon S3.
        :param object_key: The Amazon S3 object key.
        :param s3_object_url: The S3 URL of this asset on Amazon S3.
        :param kms_key_arn: (deprecated) The ARN of the KMS key used to encrypt the file asset bucket, if any. If so, the consuming role should be given "kms:Decrypt" permissions in its identity policy. It's the responsibility of they key's creator to make sure that all consumers that the key's key policy is configured such that the key can be used by all consumers that need it. The default bootstrap stack provisioned by the CDK CLI ensures this, and can be used as an example for how to configure the key properly. Default: - Asset bucket is not encrypted
        :param s3_url: (deprecated) The HTTP URL of this asset on Amazon S3. Default: - value specified in ``httpUrl`` is used.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
            "http_url": http_url,
            "object_key": object_key,
            "s3_object_url": s3_object_url,
        }
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if s3_url is not None:
            self._values["s3_url"] = s3_url

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''The name of the Amazon S3 bucket.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def http_url(self) -> builtins.str:
        '''The HTTP URL of this asset on Amazon S3.

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            https:
        '''
        result = self._values.get("http_url")
        assert result is not None, "Required property 'http_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object_key(self) -> builtins.str:
        '''The Amazon S3 object key.'''
        result = self._values.get("object_key")
        assert result is not None, "Required property 'object_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_object_url(self) -> builtins.str:
        '''The S3 URL of this asset on Amazon S3.

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            s3:
        '''
        result = self._values.get("s3_object_url")
        assert result is not None, "Required property 's3_object_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The ARN of the KMS key used to encrypt the file asset bucket, if any.

        If so, the consuming role should be given "kms:Decrypt" permissions in its
        identity policy.

        It's the responsibility of they key's creator to make sure that all
        consumers that the key's key policy is configured such that the key can be used
        by all consumers that need it.

        The default bootstrap stack provisioned by the CDK CLI ensures this, and
        can be used as an example for how to configure the key properly.

        :default: - Asset bucket is not encrypted

        :deprecated:

        Since bootstrap bucket v4, the key policy properly allows use of the
        key via the bucket and no additional parameters have to be granted anymore.

        :stability: deprecated
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_url(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The HTTP URL of this asset on Amazon S3.

        :default: - value specified in ``httpUrl`` is used.

        :deprecated: use ``httpUrl``

        :stability: deprecated
        '''
        result = self._values.get("s3_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileAssetLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/core.FileAssetPackaging")
class FileAssetPackaging(enum.Enum):
    '''Packaging modes for file assets.'''

    ZIP_DIRECTORY = "ZIP_DIRECTORY"
    '''The asset source path points to a directory, which should be archived using zip and and then uploaded to Amazon S3.'''
    FILE = "FILE"
    '''The asset source path points to a single file, which should be uploaded to Amazon S3.'''


@jsii.data_type(
    jsii_type="@aws-cdk/core.FileAssetSource",
    jsii_struct_bases=[],
    name_mapping={
        "source_hash": "sourceHash",
        "executable": "executable",
        "file_name": "fileName",
        "packaging": "packaging",
    },
)
class FileAssetSource:
    def __init__(
        self,
        *,
        source_hash: builtins.str,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_name: typing.Optional[builtins.str] = None,
        packaging: typing.Optional[FileAssetPackaging] = None,
    ) -> None:
        '''Represents the source for a file asset.

        :param source_hash: A hash on the content source. This hash is used to uniquely identify this asset throughout the system. If this value doesn't change, the asset will not be rebuilt or republished.
        :param executable: An external command that will produce the packaged asset. The command should produce the location of a ZIP file on ``stdout``. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param file_name: The path, relative to the root of the cloud assembly, in which this asset source resides. This can be a path to a file or a directory, depending on the packaging type. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param packaging: Which type of packaging to perform. Default: - Required if ``fileName`` is specified.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "source_hash": source_hash,
        }
        if executable is not None:
            self._values["executable"] = executable
        if file_name is not None:
            self._values["file_name"] = file_name
        if packaging is not None:
            self._values["packaging"] = packaging

    @builtins.property
    def source_hash(self) -> builtins.str:
        '''A hash on the content source.

        This hash is used to uniquely identify this
        asset throughout the system. If this value doesn't change, the asset will
        not be rebuilt or republished.
        '''
        result = self._values.get("source_hash")
        assert result is not None, "Required property 'source_hash' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def executable(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An external command that will produce the packaged asset.

        The command should produce the location of a ZIP file on ``stdout``.

        :default: - Exactly one of ``directory`` and ``executable`` is required
        '''
        result = self._values.get("executable")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def file_name(self) -> typing.Optional[builtins.str]:
        '''The path, relative to the root of the cloud assembly, in which this asset source resides.

        This can be a path to a file or a directory, depending on the
        packaging type.

        :default: - Exactly one of ``directory`` and ``executable`` is required
        '''
        result = self._values.get("file_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def packaging(self) -> typing.Optional[FileAssetPackaging]:
        '''Which type of packaging to perform.

        :default: - Required if ``fileName`` is specified.
        '''
        result = self._values.get("packaging")
        return typing.cast(typing.Optional[FileAssetPackaging], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileAssetSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.FileCopyOptions",
    jsii_struct_bases=[],
    name_mapping={
        "exclude": "exclude",
        "follow_symlinks": "followSymlinks",
        "ignore_mode": "ignoreMode",
    },
)
class FileCopyOptions:
    def __init__(
        self,
        *,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional["SymlinkFollowMode"] = None,
        ignore_mode: typing.Optional["IgnoreMode"] = None,
    ) -> None:
        '''Options applied when copying directories into the staging location.

        :param exclude: Glob patterns to exclude from the copy. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for exclude patterns. Default: IgnoreMode.GLOB
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if exclude is not None:
            self._values["exclude"] = exclude
        if follow_symlinks is not None:
            self._values["follow_symlinks"] = follow_symlinks
        if ignore_mode is not None:
            self._values["ignore_mode"] = ignore_mode

    @builtins.property
    def exclude(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Glob patterns to exclude from the copy.

        :default: - nothing is excluded
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def follow_symlinks(self) -> typing.Optional["SymlinkFollowMode"]:
        '''A strategy for how to handle symlinks.

        :default: SymlinkFollowMode.NEVER
        '''
        result = self._values.get("follow_symlinks")
        return typing.cast(typing.Optional["SymlinkFollowMode"], result)

    @builtins.property
    def ignore_mode(self) -> typing.Optional["IgnoreMode"]:
        '''The ignore behavior to use for exclude patterns.

        :default: IgnoreMode.GLOB
        '''
        result = self._values.get("ignore_mode")
        return typing.cast(typing.Optional["IgnoreMode"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileCopyOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.FileFingerprintOptions",
    jsii_struct_bases=[FileCopyOptions],
    name_mapping={
        "exclude": "exclude",
        "follow_symlinks": "followSymlinks",
        "ignore_mode": "ignoreMode",
        "extra_hash": "extraHash",
    },
)
class FileFingerprintOptions(FileCopyOptions):
    def __init__(
        self,
        *,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional["SymlinkFollowMode"] = None,
        ignore_mode: typing.Optional["IgnoreMode"] = None,
        extra_hash: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options related to calculating source hash.

        :param exclude: Glob patterns to exclude from the copy. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for exclude patterns. Default: IgnoreMode.GLOB
        :param extra_hash: Extra information to encode into the fingerprint (e.g. build instructions and other inputs). Default: - hash is only based on source content
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if exclude is not None:
            self._values["exclude"] = exclude
        if follow_symlinks is not None:
            self._values["follow_symlinks"] = follow_symlinks
        if ignore_mode is not None:
            self._values["ignore_mode"] = ignore_mode
        if extra_hash is not None:
            self._values["extra_hash"] = extra_hash

    @builtins.property
    def exclude(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Glob patterns to exclude from the copy.

        :default: - nothing is excluded
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def follow_symlinks(self) -> typing.Optional["SymlinkFollowMode"]:
        '''A strategy for how to handle symlinks.

        :default: SymlinkFollowMode.NEVER
        '''
        result = self._values.get("follow_symlinks")
        return typing.cast(typing.Optional["SymlinkFollowMode"], result)

    @builtins.property
    def ignore_mode(self) -> typing.Optional["IgnoreMode"]:
        '''The ignore behavior to use for exclude patterns.

        :default: IgnoreMode.GLOB
        '''
        result = self._values.get("ignore_mode")
        return typing.cast(typing.Optional["IgnoreMode"], result)

    @builtins.property
    def extra_hash(self) -> typing.Optional[builtins.str]:
        '''Extra information to encode into the fingerprint (e.g. build instructions and other inputs).

        :default: - hash is only based on source content
        '''
        result = self._values.get("extra_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileFingerprintOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FileSystem(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.FileSystem"):
    '''File system utilities.'''

    def __init__(self) -> None:
        jsii.create(FileSystem, self, [])

    @jsii.member(jsii_name="copyDirectory") # type: ignore[misc]
    @builtins.classmethod
    def copy_directory(
        cls,
        src_dir: builtins.str,
        dest_dir: builtins.str,
        options: typing.Optional[CopyOptions] = None,
        root_dir: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Copies an entire directory structure.

        :param src_dir: Source directory.
        :param dest_dir: Destination directory.
        :param options: options.
        :param root_dir: Root directory to calculate exclusions from.
        '''
        return typing.cast(None, jsii.sinvoke(cls, "copyDirectory", [src_dir, dest_dir, options, root_dir]))

    @jsii.member(jsii_name="fingerprint") # type: ignore[misc]
    @builtins.classmethod
    def fingerprint(
        cls,
        file_or_directory: builtins.str,
        *,
        extra_hash: typing.Optional[builtins.str] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow: typing.Optional["SymlinkFollowMode"] = None,
        ignore_mode: typing.Optional["IgnoreMode"] = None,
    ) -> builtins.str:
        '''Produces fingerprint based on the contents of a single file or an entire directory tree.

        The fingerprint will also include:

        1. An extra string if defined in ``options.extra``.
        2. The set of exclude patterns, if defined in ``options.exclude``
        3. The symlink follow mode value.

        :param file_or_directory: The directory or file to fingerprint.
        :param extra_hash: Extra information to encode into the fingerprint (e.g. build instructions and other inputs). Default: - hash is only based on source content
        :param exclude: Glob patterns to exclude from the copy. Default: - nothing is excluded
        :param follow: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for exclude patterns. Default: IgnoreMode.GLOB
        '''
        options = FingerprintOptions(
            extra_hash=extra_hash,
            exclude=exclude,
            follow=follow,
            ignore_mode=ignore_mode,
        )

        return typing.cast(builtins.str, jsii.sinvoke(cls, "fingerprint", [file_or_directory, options]))

    @jsii.member(jsii_name="isEmpty") # type: ignore[misc]
    @builtins.classmethod
    def is_empty(cls, dir: builtins.str) -> builtins.bool:
        '''Checks whether a directory is empty.

        :param dir: The directory to check.
        '''
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isEmpty", [dir]))

    @jsii.member(jsii_name="mkdtemp") # type: ignore[misc]
    @builtins.classmethod
    def mkdtemp(cls, prefix: builtins.str) -> builtins.str:
        '''Creates a unique temporary directory in the **system temp directory**.

        :param prefix: A prefix for the directory name. Six random characters will be generated and appended behind this prefix.
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "mkdtemp", [prefix]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="tmpdir")
    def tmpdir(cls) -> builtins.str:
        '''The real path of the system temp directory.'''
        return typing.cast(builtins.str, jsii.sget(cls, "tmpdir"))


@jsii.data_type(
    jsii_type="@aws-cdk/core.FingerprintOptions",
    jsii_struct_bases=[CopyOptions],
    name_mapping={
        "exclude": "exclude",
        "follow": "follow",
        "ignore_mode": "ignoreMode",
        "extra_hash": "extraHash",
    },
)
class FingerprintOptions(CopyOptions):
    def __init__(
        self,
        *,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow: typing.Optional["SymlinkFollowMode"] = None,
        ignore_mode: typing.Optional["IgnoreMode"] = None,
        extra_hash: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options related to calculating source hash.

        :param exclude: Glob patterns to exclude from the copy. Default: - nothing is excluded
        :param follow: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for exclude patterns. Default: IgnoreMode.GLOB
        :param extra_hash: Extra information to encode into the fingerprint (e.g. build instructions and other inputs). Default: - hash is only based on source content
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if exclude is not None:
            self._values["exclude"] = exclude
        if follow is not None:
            self._values["follow"] = follow
        if ignore_mode is not None:
            self._values["ignore_mode"] = ignore_mode
        if extra_hash is not None:
            self._values["extra_hash"] = extra_hash

    @builtins.property
    def exclude(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Glob patterns to exclude from the copy.

        :default: - nothing is excluded
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def follow(self) -> typing.Optional["SymlinkFollowMode"]:
        '''A strategy for how to handle symlinks.

        :default: SymlinkFollowMode.NEVER
        '''
        result = self._values.get("follow")
        return typing.cast(typing.Optional["SymlinkFollowMode"], result)

    @builtins.property
    def ignore_mode(self) -> typing.Optional["IgnoreMode"]:
        '''The ignore behavior to use for exclude patterns.

        :default: IgnoreMode.GLOB
        '''
        result = self._values.get("ignore_mode")
        return typing.cast(typing.Optional["IgnoreMode"], result)

    @builtins.property
    def extra_hash(self) -> typing.Optional[builtins.str]:
        '''Extra information to encode into the fingerprint (e.g. build instructions and other inputs).

        :default: - hash is only based on source content
        '''
        result = self._values.get("extra_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FingerprintOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Fn(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.Fn"):
    '''CloudFormation intrinsic functions.

    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html
    '''

    @jsii.member(jsii_name="base64") # type: ignore[misc]
    @builtins.classmethod
    def base64(cls, data: builtins.str) -> builtins.str:
        '''The intrinsic function ``Fn::Base64`` returns the Base64 representation of the input string.

        This function is typically used to pass encoded data to
        Amazon EC2 instances by way of the UserData property.

        :param data: The string value you want to convert to Base64.

        :return: a token represented as a string
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "base64", [data]))

    @jsii.member(jsii_name="cidr") # type: ignore[misc]
    @builtins.classmethod
    def cidr(
        cls,
        ip_block: builtins.str,
        count: jsii.Number,
        size_mask: typing.Optional[builtins.str] = None,
    ) -> typing.List[builtins.str]:
        '''The intrinsic function ``Fn::Cidr`` returns the specified Cidr address block.

        :param ip_block: The user-specified default Cidr address block.
        :param count: The number of subnets' Cidr block wanted. Count can be 1 to 256.
        :param size_mask: The digit covered in the subnet.

        :return: a token represented as a string
        '''
        return typing.cast(typing.List[builtins.str], jsii.sinvoke(cls, "cidr", [ip_block, count, size_mask]))

    @jsii.member(jsii_name="conditionAnd") # type: ignore[misc]
    @builtins.classmethod
    def condition_and(
        cls,
        *conditions: "ICfnConditionExpression",
    ) -> "ICfnConditionExpression":
        '''Returns true if all the specified conditions evaluate to true, or returns false if any one of the conditions evaluates to false.

        ``Fn::And`` acts as
        an AND operator. The minimum number of conditions that you can include is
        1.

        :param conditions: conditions to AND.

        :return: an FnCondition token
        '''
        return typing.cast("ICfnConditionExpression", jsii.sinvoke(cls, "conditionAnd", [*conditions]))

    @jsii.member(jsii_name="conditionContains") # type: ignore[misc]
    @builtins.classmethod
    def condition_contains(
        cls,
        list_of_strings: typing.Sequence[builtins.str],
        value: builtins.str,
    ) -> "ICfnConditionExpression":
        '''Returns true if a specified string matches at least one value in a list of strings.

        :param list_of_strings: A list of strings, such as "A", "B", "C".
        :param value: A string, such as "A", that you want to compare against a list of strings.

        :return: an FnCondition token
        '''
        return typing.cast("ICfnConditionExpression", jsii.sinvoke(cls, "conditionContains", [list_of_strings, value]))

    @jsii.member(jsii_name="conditionEachMemberEquals") # type: ignore[misc]
    @builtins.classmethod
    def condition_each_member_equals(
        cls,
        list_of_strings: typing.Sequence[builtins.str],
        value: builtins.str,
    ) -> "ICfnConditionExpression":
        '''Returns true if a specified string matches all values in a list.

        :param list_of_strings: A list of strings, such as "A", "B", "C".
        :param value: A string, such as "A", that you want to compare against a list of strings.

        :return: an FnCondition token
        '''
        return typing.cast("ICfnConditionExpression", jsii.sinvoke(cls, "conditionEachMemberEquals", [list_of_strings, value]))

    @jsii.member(jsii_name="conditionEachMemberIn") # type: ignore[misc]
    @builtins.classmethod
    def condition_each_member_in(
        cls,
        strings_to_check: typing.Sequence[builtins.str],
        strings_to_match: typing.Sequence[builtins.str],
    ) -> "ICfnConditionExpression":
        '''Returns true if each member in a list of strings matches at least one value in a second list of strings.

        :param strings_to_check: A list of strings, such as "A", "B", "C". AWS CloudFormation checks whether each member in the strings_to_check parameter is in the strings_to_match parameter.
        :param strings_to_match: A list of strings, such as "A", "B", "C". Each member in the strings_to_match parameter is compared against the members of the strings_to_check parameter.

        :return: an FnCondition token
        '''
        return typing.cast("ICfnConditionExpression", jsii.sinvoke(cls, "conditionEachMemberIn", [strings_to_check, strings_to_match]))

    @jsii.member(jsii_name="conditionEquals") # type: ignore[misc]
    @builtins.classmethod
    def condition_equals(
        cls,
        lhs: typing.Any,
        rhs: typing.Any,
    ) -> "ICfnConditionExpression":
        '''Compares if two values are equal.

        Returns true if the two values are equal
        or false if they aren't.

        :param lhs: A value of any type that you want to compare.
        :param rhs: A value of any type that you want to compare.

        :return: an FnCondition token
        '''
        return typing.cast("ICfnConditionExpression", jsii.sinvoke(cls, "conditionEquals", [lhs, rhs]))

    @jsii.member(jsii_name="conditionIf") # type: ignore[misc]
    @builtins.classmethod
    def condition_if(
        cls,
        condition_id: builtins.str,
        value_if_true: typing.Any,
        value_if_false: typing.Any,
    ) -> "ICfnConditionExpression":
        '''Returns one value if the specified condition evaluates to true and another value if the specified condition evaluates to false.

        Currently, AWS
        CloudFormation supports the ``Fn::If`` intrinsic function in the metadata
        attribute, update policy attribute, and property values in the Resources
        section and Outputs sections of a template. You can use the AWS::NoValue
        pseudo parameter as a return value to remove the corresponding property.

        :param condition_id: A reference to a condition in the Conditions section. Use the condition's name to reference it.
        :param value_if_true: A value to be returned if the specified condition evaluates to true.
        :param value_if_false: A value to be returned if the specified condition evaluates to false.

        :return: an FnCondition token
        '''
        return typing.cast("ICfnConditionExpression", jsii.sinvoke(cls, "conditionIf", [condition_id, value_if_true, value_if_false]))

    @jsii.member(jsii_name="conditionNot") # type: ignore[misc]
    @builtins.classmethod
    def condition_not(
        cls,
        condition: "ICfnConditionExpression",
    ) -> "ICfnConditionExpression":
        '''Returns true for a condition that evaluates to false or returns false for a condition that evaluates to true.

        ``Fn::Not`` acts as a NOT operator.

        :param condition: A condition such as ``Fn::Equals`` that evaluates to true or false.

        :return: an FnCondition token
        '''
        return typing.cast("ICfnConditionExpression", jsii.sinvoke(cls, "conditionNot", [condition]))

    @jsii.member(jsii_name="conditionOr") # type: ignore[misc]
    @builtins.classmethod
    def condition_or(
        cls,
        *conditions: "ICfnConditionExpression",
    ) -> "ICfnConditionExpression":
        '''Returns true if any one of the specified conditions evaluate to true, or returns false if all of the conditions evaluates to false.

        ``Fn::Or`` acts
        as an OR operator. The minimum number of conditions that you can include is
        1.

        :param conditions: conditions that evaluates to true or false.

        :return: an FnCondition token
        '''
        return typing.cast("ICfnConditionExpression", jsii.sinvoke(cls, "conditionOr", [*conditions]))

    @jsii.member(jsii_name="findInMap") # type: ignore[misc]
    @builtins.classmethod
    def find_in_map(
        cls,
        map_name: builtins.str,
        top_level_key: builtins.str,
        second_level_key: builtins.str,
    ) -> builtins.str:
        '''The intrinsic function ``Fn::FindInMap`` returns the value corresponding to keys in a two-level map that is declared in the Mappings section.

        :param map_name: -
        :param top_level_key: -
        :param second_level_key: -

        :return: a token represented as a string
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "findInMap", [map_name, top_level_key, second_level_key]))

    @jsii.member(jsii_name="getAtt") # type: ignore[misc]
    @builtins.classmethod
    def get_att(
        cls,
        logical_name_of_resource: builtins.str,
        attribute_name: builtins.str,
    ) -> "IResolvable":
        '''The ``Fn::GetAtt`` intrinsic function returns the value of an attribute from a resource in the template.

        :param logical_name_of_resource: The logical name (also called logical ID) of the resource that contains the attribute that you want.
        :param attribute_name: The name of the resource-specific attribute whose value you want. See the resource's reference page for details about the attributes available for that resource type.

        :return: an IResolvable object
        '''
        return typing.cast("IResolvable", jsii.sinvoke(cls, "getAtt", [logical_name_of_resource, attribute_name]))

    @jsii.member(jsii_name="getAzs") # type: ignore[misc]
    @builtins.classmethod
    def get_azs(
        cls,
        region: typing.Optional[builtins.str] = None,
    ) -> typing.List[builtins.str]:
        '''The intrinsic function ``Fn::GetAZs`` returns an array that lists Availability Zones for a specified region.

        Because customers have access to
        different Availability Zones, the intrinsic function ``Fn::GetAZs`` enables
        template authors to write templates that adapt to the calling user's
        access. That way you don't have to hard-code a full list of Availability
        Zones for a specified region.

        :param region: The name of the region for which you want to get the Availability Zones. You can use the AWS::Region pseudo parameter to specify the region in which the stack is created. Specifying an empty string is equivalent to specifying AWS::Region.

        :return: a token represented as a string array
        '''
        return typing.cast(typing.List[builtins.str], jsii.sinvoke(cls, "getAzs", [region]))

    @jsii.member(jsii_name="importListValue") # type: ignore[misc]
    @builtins.classmethod
    def import_list_value(
        cls,
        shared_value_to_import: builtins.str,
        assumed_length: jsii.Number,
        delimiter: typing.Optional[builtins.str] = None,
    ) -> typing.List[builtins.str]:
        '''Like ``Fn.importValue``, but import a list with a known length.

        If you explicitly want a list with an unknown length, call ``Fn.split(',', Fn.importValue(exportName))``. See the documentation of ``Fn.split`` to read
        more about the limitations of using lists of unknown length.

        ``Fn.importListValue(exportName, assumedLength)`` is the same as
        ``Fn.split(',', Fn.importValue(exportName), assumedLength)``,
        but easier to read and impossible to forget to pass ``assumedLength``.

        :param shared_value_to_import: -
        :param assumed_length: -
        :param delimiter: -
        '''
        return typing.cast(typing.List[builtins.str], jsii.sinvoke(cls, "importListValue", [shared_value_to_import, assumed_length, delimiter]))

    @jsii.member(jsii_name="importValue") # type: ignore[misc]
    @builtins.classmethod
    def import_value(cls, shared_value_to_import: builtins.str) -> builtins.str:
        '''The intrinsic function ``Fn::ImportValue`` returns the value of an output exported by another stack.

        You typically use this function to create
        cross-stack references. In the following example template snippets, Stack A
        exports VPC security group values and Stack B imports them.

        :param shared_value_to_import: The stack output value that you want to import.

        :return: a token represented as a string
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "importValue", [shared_value_to_import]))

    @jsii.member(jsii_name="join") # type: ignore[misc]
    @builtins.classmethod
    def join(
        cls,
        delimiter: builtins.str,
        list_of_values: typing.Sequence[builtins.str],
    ) -> builtins.str:
        '''The intrinsic function ``Fn::Join`` appends a set of values into a single value, separated by the specified delimiter.

        If a delimiter is the empty
        string, the set of values are concatenated with no delimiter.

        :param delimiter: The value you want to occur between fragments. The delimiter will occur between fragments only. It will not terminate the final value.
        :param list_of_values: The list of values you want combined.

        :return: a token represented as a string
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "join", [delimiter, list_of_values]))

    @jsii.member(jsii_name="parseDomainName") # type: ignore[misc]
    @builtins.classmethod
    def parse_domain_name(cls, url: builtins.str) -> builtins.str:
        '''Given an url, parse the domain name.

        :param url: the url to parse.
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "parseDomainName", [url]))

    @jsii.member(jsii_name="ref") # type: ignore[misc]
    @builtins.classmethod
    def ref(cls, logical_name: builtins.str) -> builtins.str:
        '''The ``Ref`` intrinsic function returns the value of the specified parameter or resource.

        Note that it doesn't validate the logicalName, it mainly serves paremeter/resource reference defined in a ``CfnInclude`` template.

        :param logical_name: The logical name of a parameter/resource for which you want to retrieve its value.
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "ref", [logical_name]))

    @jsii.member(jsii_name="refAll") # type: ignore[misc]
    @builtins.classmethod
    def ref_all(cls, parameter_type: builtins.str) -> typing.List[builtins.str]:
        '''Returns all values for a specified parameter type.

        :param parameter_type: An AWS-specific parameter type, such as AWS::EC2::SecurityGroup::Id or AWS::EC2::VPC::Id. For more information, see Parameters in the AWS CloudFormation User Guide.

        :return: a token represented as a string array
        '''
        return typing.cast(typing.List[builtins.str], jsii.sinvoke(cls, "refAll", [parameter_type]))

    @jsii.member(jsii_name="select") # type: ignore[misc]
    @builtins.classmethod
    def select(
        cls,
        index: jsii.Number,
        array: typing.Sequence[builtins.str],
    ) -> builtins.str:
        '''The intrinsic function ``Fn::Select`` returns a single object from a list of objects by index.

        :param index: The index of the object to retrieve. This must be a value from zero to N-1, where N represents the number of elements in the array.
        :param array: The list of objects to select from. This list must not be null, nor can it have null entries.

        :return: a token represented as a string
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "select", [index, array]))

    @jsii.member(jsii_name="split") # type: ignore[misc]
    @builtins.classmethod
    def split(
        cls,
        delimiter: builtins.str,
        source: builtins.str,
        assumed_length: typing.Optional[jsii.Number] = None,
    ) -> typing.List[builtins.str]:
        '''Split a string token into a token list of string values.

        Specify the location of splits with a delimiter such as ',' (a comma).
        Renders to the ``Fn::Split`` intrinsic function.


        Lists with unknown lengths (default)

        Since this function is used to work with deploy-time values, if ``assumedLength``
        is not given the CDK cannot know the length of the resulting list at synthesis time.
        This brings the following restrictions:

        - You must use ``Fn.select(i, list)`` to pick elements out of the list (you must not use
          ``list[i]``).
        - You cannot add elements to the list, remove elements from the list,
          combine two such lists together, or take a slice of the list.
        - You cannot pass the list to constructs that do any of the above.

        The only valid operation with such a tokenized list is to pass it unmodified to a
        CloudFormation Resource construct.


        Lists with assumed lengths

        Pass ``assumedLength`` if you know the length of the list that will be
        produced by splitting. The actual list length at deploy time may be
        *longer* than the number you pass, but not *shorter*.

        The returned list will look like::

           [Fn.select(0, split), Fn.select(1, split), Fn.select(2, split), ...]

        The restrictions from the section "Lists with unknown lengths" will now be lifted,
        at the expense of having to know and fix the length of the list.

        :param delimiter: A string value that determines where the source string is divided.
        :param source: The string value that you want to split.
        :param assumed_length: The length of the list that will be produced by splitting.

        :return: a token represented as a string array
        '''
        return typing.cast(typing.List[builtins.str], jsii.sinvoke(cls, "split", [delimiter, source, assumed_length]))

    @jsii.member(jsii_name="sub") # type: ignore[misc]
    @builtins.classmethod
    def sub(
        cls,
        body: builtins.str,
        variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> builtins.str:
        '''The intrinsic function ``Fn::Sub`` substitutes variables in an input string with values that you specify.

        In your templates, you can use this function
        to construct commands or outputs that include values that aren't available
        until you create or update a stack.

        :param body: A string with variables that AWS CloudFormation substitutes with their associated values at runtime. Write variables as ${MyVarName}. Variables can be template parameter names, resource logical IDs, resource attributes, or a variable in a key-value map. If you specify only template parameter names, resource logical IDs, and resource attributes, don't specify a key-value map.
        :param variables: The name of a variable that you included in the String parameter. The value that AWS CloudFormation substitutes for the associated variable name at runtime.

        :return: a token represented as a string
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "sub", [body, variables]))

    @jsii.member(jsii_name="transform") # type: ignore[misc]
    @builtins.classmethod
    def transform(
        cls,
        macro_name: builtins.str,
        parameters: typing.Mapping[builtins.str, typing.Any],
    ) -> "IResolvable":
        '''Creates a token representing the ``Fn::Transform`` expression.

        :param macro_name: The name of the macro to perform the processing.
        :param parameters: The parameters to be passed to the macro.

        :return: a token representing the transform expression

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-transform.html
        '''
        return typing.cast("IResolvable", jsii.sinvoke(cls, "transform", [macro_name, parameters]))

    @jsii.member(jsii_name="valueOf") # type: ignore[misc]
    @builtins.classmethod
    def value_of(
        cls,
        parameter_or_logical_id: builtins.str,
        attribute: builtins.str,
    ) -> builtins.str:
        '''Returns an attribute value or list of values for a specific parameter and attribute.

        :param parameter_or_logical_id: The name of a parameter for which you want to retrieve attribute values. The parameter must be declared in the Parameters section of the template.
        :param attribute: The name of an attribute from which you want to retrieve a value.

        :return: a token represented as a string
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "valueOf", [parameter_or_logical_id, attribute]))

    @jsii.member(jsii_name="valueOfAll") # type: ignore[misc]
    @builtins.classmethod
    def value_of_all(
        cls,
        parameter_type: builtins.str,
        attribute: builtins.str,
    ) -> typing.List[builtins.str]:
        '''Returns a list of all attribute values for a given parameter type and attribute.

        :param parameter_type: An AWS-specific parameter type, such as AWS::EC2::SecurityGroup::Id or AWS::EC2::VPC::Id. For more information, see Parameters in the AWS CloudFormation User Guide.
        :param attribute: The name of an attribute from which you want to retrieve a value. For more information about attributes, see Supported Attributes.

        :return: a token represented as a string array
        '''
        return typing.cast(typing.List[builtins.str], jsii.sinvoke(cls, "valueOfAll", [parameter_type, attribute]))


@jsii.data_type(
    jsii_type="@aws-cdk/core.GetContextKeyOptions",
    jsii_struct_bases=[],
    name_mapping={"provider": "provider", "props": "props"},
)
class GetContextKeyOptions:
    def __init__(
        self,
        *,
        provider: builtins.str,
        props: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''
        :param provider: The context provider to query.
        :param props: Provider-specific properties.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "provider": provider,
        }
        if props is not None:
            self._values["props"] = props

    @builtins.property
    def provider(self) -> builtins.str:
        '''The context provider to query.'''
        result = self._values.get("provider")
        assert result is not None, "Required property 'provider' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def props(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Provider-specific properties.'''
        result = self._values.get("props")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GetContextKeyOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.GetContextKeyResult",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "props": "props"},
)
class GetContextKeyResult:
    def __init__(
        self,
        *,
        key: builtins.str,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> None:
        '''
        :param key: 
        :param props: 
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "props": props,
        }

    @builtins.property
    def key(self) -> builtins.str:
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def props(self) -> typing.Mapping[builtins.str, typing.Any]:
        result = self._values.get("props")
        assert result is not None, "Required property 'props' is missing"
        return typing.cast(typing.Mapping[builtins.str, typing.Any], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GetContextKeyResult(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.GetContextValueOptions",
    jsii_struct_bases=[GetContextKeyOptions],
    name_mapping={
        "provider": "provider",
        "props": "props",
        "dummy_value": "dummyValue",
    },
)
class GetContextValueOptions(GetContextKeyOptions):
    def __init__(
        self,
        *,
        provider: builtins.str,
        props: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dummy_value: typing.Any,
    ) -> None:
        '''
        :param provider: The context provider to query.
        :param props: Provider-specific properties.
        :param dummy_value: The value to return if the context value was not found and a missing context is reported. This should be a dummy value that should preferably fail during deployment since it represents an invalid state.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "provider": provider,
            "dummy_value": dummy_value,
        }
        if props is not None:
            self._values["props"] = props

    @builtins.property
    def provider(self) -> builtins.str:
        '''The context provider to query.'''
        result = self._values.get("provider")
        assert result is not None, "Required property 'provider' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def props(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Provider-specific properties.'''
        result = self._values.get("props")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def dummy_value(self) -> typing.Any:
        '''The value to return if the context value was not found and a missing context is reported.

        This should be a dummy value that should preferably
        fail during deployment since it represents an invalid state.
        '''
        result = self._values.get("dummy_value")
        assert result is not None, "Required property 'dummy_value' is missing"
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GetContextValueOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.GetContextValueResult",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class GetContextValueResult:
    def __init__(self, *, value: typing.Any = None) -> None:
        '''
        :param value: 
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def value(self) -> typing.Any:
        result = self._values.get("value")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GetContextValueResult(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@aws-cdk/core.IAnyProducer")
class IAnyProducer(typing_extensions.Protocol):
    '''Interface for lazy untyped value producers.'''

    @jsii.member(jsii_name="produce")
    def produce(self, context: "IResolveContext") -> typing.Any:
        '''Produce the value.

        :param context: -
        '''
        ...


class _IAnyProducerProxy:
    '''Interface for lazy untyped value producers.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.IAnyProducer"

    @jsii.member(jsii_name="produce")
    def produce(self, context: "IResolveContext") -> typing.Any:
        '''Produce the value.

        :param context: -
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "produce", [context]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAnyProducer).__jsii_proxy_class__ = lambda : _IAnyProducerProxy


@jsii.interface(jsii_type="@aws-cdk/core.IAspect")
class IAspect(typing_extensions.Protocol):
    '''Represents an Aspect.'''

    @jsii.member(jsii_name="visit")
    def visit(self, node: "IConstruct") -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        ...


class _IAspectProxy:
    '''Represents an Aspect.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.IAspect"

    @jsii.member(jsii_name="visit")
    def visit(self, node: "IConstruct") -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        return typing.cast(None, jsii.invoke(self, "visit", [node]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAspect).__jsii_proxy_class__ = lambda : _IAspectProxy


@jsii.interface(jsii_type="@aws-cdk/core.IAsset")
class IAsset(typing_extensions.Protocol):
    '''Common interface for all assets.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assetHash")
    def asset_hash(self) -> builtins.str:
        '''A hash of this asset, which is available at construction time.

        As this is a plain string, it
        can be used in construct IDs in order to enforce creation of a new resource when the content
        hash has changed.
        '''
        ...


class _IAssetProxy:
    '''Common interface for all assets.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.IAsset"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assetHash")
    def asset_hash(self) -> builtins.str:
        '''A hash of this asset, which is available at construction time.

        As this is a plain string, it
        can be used in construct IDs in order to enforce creation of a new resource when the content
        hash has changed.
        '''
        return typing.cast(builtins.str, jsii.get(self, "assetHash"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAsset).__jsii_proxy_class__ = lambda : _IAssetProxy


@jsii.interface(jsii_type="@aws-cdk/core.ICfnResourceOptions")
class ICfnResourceOptions(typing_extensions.Protocol):
    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="condition")
    def condition(self) -> typing.Optional["CfnCondition"]:
        '''A condition to associate with this resource.

        This means that only if the condition evaluates to 'true' when the stack
        is deployed, the resource will be included. This is provided to allow CDK projects to produce legacy templates, but noramlly
        there is no need to use it in CDK projects.
        '''
        ...

    @condition.setter
    def condition(self, value: typing.Optional["CfnCondition"]) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="creationPolicy")
    def creation_policy(self) -> typing.Optional[CfnCreationPolicy]:
        '''Associate the CreationPolicy attribute with a resource to prevent its status from reaching create complete until AWS CloudFormation receives a specified number of success signals or the timeout period is exceeded.

        To signal a
        resource, you can use the cfn-signal helper script or SignalResource API. AWS CloudFormation publishes valid signals
        to the stack events so that you track the number of signals sent.
        '''
        ...

    @creation_policy.setter
    def creation_policy(self, value: typing.Optional[CfnCreationPolicy]) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deletionPolicy")
    def deletion_policy(self) -> typing.Optional[CfnDeletionPolicy]:
        '''With the DeletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted.

        You specify a DeletionPolicy attribute for each resource that you want to control. If a resource has no DeletionPolicy
        attribute, AWS CloudFormation deletes the resource by default. Note that this capability also applies to update operations
        that lead to resources being removed.
        '''
        ...

    @deletion_policy.setter
    def deletion_policy(self, value: typing.Optional[CfnDeletionPolicy]) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of this resource.

        Used for informational purposes only, is not processed in any way
        (and stays with the CloudFormation template, is not passed to the underlying resource,
        even if it does have a 'description' property).
        '''
        ...

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Metadata associated with the CloudFormation resource.

        This is not the same as the construct metadata which can be added
        using construct.addMetadata(), but would not appear in the CloudFormation template automatically.
        '''
        ...

    @metadata.setter
    def metadata(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Any]],
    ) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="updatePolicy")
    def update_policy(self) -> typing.Optional[CfnUpdatePolicy]:
        '''Use the UpdatePolicy attribute to specify how AWS CloudFormation handles updates to the AWS::AutoScaling::AutoScalingGroup resource.

        AWS CloudFormation invokes one of three update policies depending on the type of change you make or whether a
        scheduled action is associated with the Auto Scaling group.
        '''
        ...

    @update_policy.setter
    def update_policy(self, value: typing.Optional[CfnUpdatePolicy]) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="updateReplacePolicy")
    def update_replace_policy(self) -> typing.Optional[CfnDeletionPolicy]:
        '''Use the UpdateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.'''
        ...

    @update_replace_policy.setter
    def update_replace_policy(self, value: typing.Optional[CfnDeletionPolicy]) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="version")
    def version(self) -> typing.Optional[builtins.str]:
        '''The version of this resource.

        Used only for custom CloudFormation resources.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html
        '''
        ...

    @version.setter
    def version(self, value: typing.Optional[builtins.str]) -> None:
        ...


class _ICfnResourceOptionsProxy:
    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.ICfnResourceOptions"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="condition")
    def condition(self) -> typing.Optional["CfnCondition"]:
        '''A condition to associate with this resource.

        This means that only if the condition evaluates to 'true' when the stack
        is deployed, the resource will be included. This is provided to allow CDK projects to produce legacy templates, but noramlly
        there is no need to use it in CDK projects.
        '''
        return typing.cast(typing.Optional["CfnCondition"], jsii.get(self, "condition"))

    @condition.setter
    def condition(self, value: typing.Optional["CfnCondition"]) -> None:
        jsii.set(self, "condition", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="creationPolicy")
    def creation_policy(self) -> typing.Optional[CfnCreationPolicy]:
        '''Associate the CreationPolicy attribute with a resource to prevent its status from reaching create complete until AWS CloudFormation receives a specified number of success signals or the timeout period is exceeded.

        To signal a
        resource, you can use the cfn-signal helper script or SignalResource API. AWS CloudFormation publishes valid signals
        to the stack events so that you track the number of signals sent.
        '''
        return typing.cast(typing.Optional[CfnCreationPolicy], jsii.get(self, "creationPolicy"))

    @creation_policy.setter
    def creation_policy(self, value: typing.Optional[CfnCreationPolicy]) -> None:
        jsii.set(self, "creationPolicy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deletionPolicy")
    def deletion_policy(self) -> typing.Optional[CfnDeletionPolicy]:
        '''With the DeletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted.

        You specify a DeletionPolicy attribute for each resource that you want to control. If a resource has no DeletionPolicy
        attribute, AWS CloudFormation deletes the resource by default. Note that this capability also applies to update operations
        that lead to resources being removed.
        '''
        return typing.cast(typing.Optional[CfnDeletionPolicy], jsii.get(self, "deletionPolicy"))

    @deletion_policy.setter
    def deletion_policy(self, value: typing.Optional[CfnDeletionPolicy]) -> None:
        jsii.set(self, "deletionPolicy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of this resource.

        Used for informational purposes only, is not processed in any way
        (and stays with the CloudFormation template, is not passed to the underlying resource,
        even if it does have a 'description' property).
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Metadata associated with the CloudFormation resource.

        This is not the same as the construct metadata which can be added
        using construct.addMetadata(), but would not appear in the CloudFormation template automatically.
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Any]],
    ) -> None:
        jsii.set(self, "metadata", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="updatePolicy")
    def update_policy(self) -> typing.Optional[CfnUpdatePolicy]:
        '''Use the UpdatePolicy attribute to specify how AWS CloudFormation handles updates to the AWS::AutoScaling::AutoScalingGroup resource.

        AWS CloudFormation invokes one of three update policies depending on the type of change you make or whether a
        scheduled action is associated with the Auto Scaling group.
        '''
        return typing.cast(typing.Optional[CfnUpdatePolicy], jsii.get(self, "updatePolicy"))

    @update_policy.setter
    def update_policy(self, value: typing.Optional[CfnUpdatePolicy]) -> None:
        jsii.set(self, "updatePolicy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="updateReplacePolicy")
    def update_replace_policy(self) -> typing.Optional[CfnDeletionPolicy]:
        '''Use the UpdateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.'''
        return typing.cast(typing.Optional[CfnDeletionPolicy], jsii.get(self, "updateReplacePolicy"))

    @update_replace_policy.setter
    def update_replace_policy(self, value: typing.Optional[CfnDeletionPolicy]) -> None:
        jsii.set(self, "updateReplacePolicy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="version")
    def version(self) -> typing.Optional[builtins.str]:
        '''The version of this resource.

        Used only for custom CloudFormation resources.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "version"))

    @version.setter
    def version(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "version", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICfnResourceOptions).__jsii_proxy_class__ = lambda : _ICfnResourceOptionsProxy


@jsii.interface(jsii_type="@aws-cdk/core.IDependable")
class IDependable(typing_extensions.Protocol):
    '''Trait marker for classes that can be depended upon.

    The presence of this interface indicates that an object has
    an ``IDependableTrait`` implementation.

    This interface can be used to take an (ordering) dependency on a set of
    constructs. An ordering dependency implies that the resources represented by
    those constructs are deployed before the resources depending ON them are
    deployed.
    '''

    pass


class _IDependableProxy:
    '''Trait marker for classes that can be depended upon.

    The presence of this interface indicates that an object has
    an ``IDependableTrait`` implementation.

    This interface can be used to take an (ordering) dependency on a set of
    constructs. An ordering dependency implies that the resources represented by
    those constructs are deployed before the resources depending ON them are
    deployed.
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.IDependable"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDependable).__jsii_proxy_class__ = lambda : _IDependableProxy


@jsii.interface(jsii_type="@aws-cdk/core.IFragmentConcatenator")
class IFragmentConcatenator(typing_extensions.Protocol):
    '''Function used to concatenate symbols in the target document language.

    Interface so it could potentially be exposed over jsii.
    '''

    @jsii.member(jsii_name="join")
    def join(self, left: typing.Any, right: typing.Any) -> typing.Any:
        '''Join the fragment on the left and on the right.

        :param left: -
        :param right: -
        '''
        ...


class _IFragmentConcatenatorProxy:
    '''Function used to concatenate symbols in the target document language.

    Interface so it could potentially be exposed over jsii.
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.IFragmentConcatenator"

    @jsii.member(jsii_name="join")
    def join(self, left: typing.Any, right: typing.Any) -> typing.Any:
        '''Join the fragment on the left and on the right.

        :param left: -
        :param right: -
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "join", [left, right]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFragmentConcatenator).__jsii_proxy_class__ = lambda : _IFragmentConcatenatorProxy


@jsii.interface(jsii_type="@aws-cdk/core.IInspectable")
class IInspectable(typing_extensions.Protocol):
    '''Interface for examining a construct and exposing metadata.'''

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "TreeInspector") -> None:
        '''Examines construct.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        ...


class _IInspectableProxy:
    '''Interface for examining a construct and exposing metadata.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.IInspectable"

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "TreeInspector") -> None:
        '''Examines construct.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInspectable).__jsii_proxy_class__ = lambda : _IInspectableProxy


@jsii.interface(jsii_type="@aws-cdk/core.IListProducer")
class IListProducer(typing_extensions.Protocol):
    '''Interface for lazy list producers.'''

    @jsii.member(jsii_name="produce")
    def produce(
        self,
        context: "IResolveContext",
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Produce the list value.

        :param context: -
        '''
        ...


class _IListProducerProxy:
    '''Interface for lazy list producers.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.IListProducer"

    @jsii.member(jsii_name="produce")
    def produce(
        self,
        context: "IResolveContext",
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Produce the list value.

        :param context: -
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.invoke(self, "produce", [context]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IListProducer).__jsii_proxy_class__ = lambda : _IListProducerProxy


@jsii.interface(jsii_type="@aws-cdk/core.ILocalBundling")
class ILocalBundling(typing_extensions.Protocol):
    '''Local bundling.'''

    @jsii.member(jsii_name="tryBundle")
    def try_bundle(
        self,
        output_dir: builtins.str,
        *,
        image: DockerImage,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        local: typing.Optional["ILocalBundling"] = None,
        output_type: typing.Optional[BundlingOutput] = None,
        security_opt: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Sequence[DockerVolume]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> builtins.bool:
        '''This method is called before attempting docker bundling to allow the bundler to be executed locally.

        If the local bundler exists, and bundling
        was performed locally, return ``true``. Otherwise, return ``false``.

        :param output_dir: the directory where the bundled asset should be output.
        :param image: The Docker image where the command will run.
        :param command: The command to run in the Docker container. Default: - run the command defined in the image
        :param entrypoint: The entrypoint to run in the Docker container. Default: - run the entrypoint defined in the image
        :param environment: The environment variables to pass to the Docker container. Default: - no environment variables.
        :param local: Local bundling provider. The provider implements a method ``tryBundle()`` which should return ``true`` if local bundling was performed. If ``false`` is returned, docker bundling will be done. Default: - bundling will only be performed in a Docker container
        :param output_type: The type of output that this bundling operation is producing. Default: BundlingOutput.AUTO_DISCOVER
        :param security_opt: `Security configuration <https://docs.docker.com/engine/reference/run/#security-configuration>`_ when running the docker container. Default: - no security options
        :param user: The user to use when running the Docker container. user | user:group | uid | uid:gid | user:gid | uid:group Default: - uid:gid of the current user or 1000:1000 on Windows
        :param volumes: Additional Docker volumes to mount. Default: - no additional volumes are mounted
        :param working_directory: Working directory inside the Docker container. Default: /asset-input
        '''
        ...


class _ILocalBundlingProxy:
    '''Local bundling.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.ILocalBundling"

    @jsii.member(jsii_name="tryBundle")
    def try_bundle(
        self,
        output_dir: builtins.str,
        *,
        image: DockerImage,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        local: typing.Optional[ILocalBundling] = None,
        output_type: typing.Optional[BundlingOutput] = None,
        security_opt: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Sequence[DockerVolume]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> builtins.bool:
        '''This method is called before attempting docker bundling to allow the bundler to be executed locally.

        If the local bundler exists, and bundling
        was performed locally, return ``true``. Otherwise, return ``false``.

        :param output_dir: the directory where the bundled asset should be output.
        :param image: The Docker image where the command will run.
        :param command: The command to run in the Docker container. Default: - run the command defined in the image
        :param entrypoint: The entrypoint to run in the Docker container. Default: - run the entrypoint defined in the image
        :param environment: The environment variables to pass to the Docker container. Default: - no environment variables.
        :param local: Local bundling provider. The provider implements a method ``tryBundle()`` which should return ``true`` if local bundling was performed. If ``false`` is returned, docker bundling will be done. Default: - bundling will only be performed in a Docker container
        :param output_type: The type of output that this bundling operation is producing. Default: BundlingOutput.AUTO_DISCOVER
        :param security_opt: `Security configuration <https://docs.docker.com/engine/reference/run/#security-configuration>`_ when running the docker container. Default: - no security options
        :param user: The user to use when running the Docker container. user | user:group | uid | uid:gid | user:gid | uid:group Default: - uid:gid of the current user or 1000:1000 on Windows
        :param volumes: Additional Docker volumes to mount. Default: - no additional volumes are mounted
        :param working_directory: Working directory inside the Docker container. Default: /asset-input
        '''
        options = BundlingOptions(
            image=image,
            command=command,
            entrypoint=entrypoint,
            environment=environment,
            local=local,
            output_type=output_type,
            security_opt=security_opt,
            user=user,
            volumes=volumes,
            working_directory=working_directory,
        )

        return typing.cast(builtins.bool, jsii.invoke(self, "tryBundle", [output_dir, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocalBundling).__jsii_proxy_class__ = lambda : _ILocalBundlingProxy


@jsii.interface(jsii_type="@aws-cdk/core.INumberProducer")
class INumberProducer(typing_extensions.Protocol):
    '''Interface for lazy number producers.'''

    @jsii.member(jsii_name="produce")
    def produce(self, context: "IResolveContext") -> typing.Optional[jsii.Number]:
        '''Produce the number value.

        :param context: -
        '''
        ...


class _INumberProducerProxy:
    '''Interface for lazy number producers.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.INumberProducer"

    @jsii.member(jsii_name="produce")
    def produce(self, context: "IResolveContext") -> typing.Optional[jsii.Number]:
        '''Produce the number value.

        :param context: -
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.invoke(self, "produce", [context]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INumberProducer).__jsii_proxy_class__ = lambda : _INumberProducerProxy


@jsii.interface(jsii_type="@aws-cdk/core.IPostProcessor")
class IPostProcessor(typing_extensions.Protocol):
    '''A Token that can post-process the complete resolved value, after resolve() has recursed over it.'''

    @jsii.member(jsii_name="postProcess")
    def post_process(self, input: typing.Any, context: "IResolveContext") -> typing.Any:
        '''Process the completely resolved value, after full recursion/resolution has happened.

        :param input: -
        :param context: -
        '''
        ...


class _IPostProcessorProxy:
    '''A Token that can post-process the complete resolved value, after resolve() has recursed over it.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.IPostProcessor"

    @jsii.member(jsii_name="postProcess")
    def post_process(self, input: typing.Any, context: "IResolveContext") -> typing.Any:
        '''Process the completely resolved value, after full recursion/resolution has happened.

        :param input: -
        :param context: -
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "postProcess", [input, context]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPostProcessor).__jsii_proxy_class__ = lambda : _IPostProcessorProxy


@jsii.interface(jsii_type="@aws-cdk/core.IResolvable")
class IResolvable(typing_extensions.Protocol):
    '''Interface for values that can be resolvable later.

    Tokens are special objects that participate in synthesis.
    '''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="creationStack")
    def creation_stack(self) -> typing.List[builtins.str]:
        '''The creation stack of this resolvable which will be appended to errors thrown during resolution.

        This may return an array with a single informational element indicating how
        to get this property populated, if it was skipped for performance reasons.
        '''
        ...

    @jsii.member(jsii_name="resolve")
    def resolve(self, context: "IResolveContext") -> typing.Any:
        '''Produce the Token's value at resolution time.

        :param context: -
        '''
        ...

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Return a string representation of this resolvable object.

        Returns a reversible string representation.
        '''
        ...


class _IResolvableProxy:
    '''Interface for values that can be resolvable later.

    Tokens are special objects that participate in synthesis.
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.IResolvable"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="creationStack")
    def creation_stack(self) -> typing.List[builtins.str]:
        '''The creation stack of this resolvable which will be appended to errors thrown during resolution.

        This may return an array with a single informational element indicating how
        to get this property populated, if it was skipped for performance reasons.
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "creationStack"))

    @jsii.member(jsii_name="resolve")
    def resolve(self, context: "IResolveContext") -> typing.Any:
        '''Produce the Token's value at resolution time.

        :param context: -
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "resolve", [context]))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Return a string representation of this resolvable object.

        Returns a reversible string representation.
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResolvable).__jsii_proxy_class__ = lambda : _IResolvableProxy


@jsii.interface(jsii_type="@aws-cdk/core.IResolveContext")
class IResolveContext(typing_extensions.Protocol):
    '''Current resolution context for tokens.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="preparing")
    def preparing(self) -> builtins.bool:
        '''True when we are still preparing, false if we're rendering the final output.'''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scope")
    def scope(self) -> "IConstruct":
        '''The scope from which resolution has been initiated.'''
        ...

    @jsii.member(jsii_name="registerPostProcessor")
    def register_post_processor(self, post_processor: IPostProcessor) -> None:
        '''Use this postprocessor after the entire token structure has been resolved.

        :param post_processor: -
        '''
        ...

    @jsii.member(jsii_name="resolve")
    def resolve(
        self,
        x: typing.Any,
        *,
        allow_intrinsic_keys: typing.Optional[builtins.bool] = None,
    ) -> typing.Any:
        '''Resolve an inner object.

        :param x: -
        :param allow_intrinsic_keys: Change the 'allowIntrinsicKeys' option. Default: - Unchanged
        '''
        ...


class _IResolveContextProxy:
    '''Current resolution context for tokens.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.IResolveContext"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="preparing")
    def preparing(self) -> builtins.bool:
        '''True when we are still preparing, false if we're rendering the final output.'''
        return typing.cast(builtins.bool, jsii.get(self, "preparing"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scope")
    def scope(self) -> "IConstruct":
        '''The scope from which resolution has been initiated.'''
        return typing.cast("IConstruct", jsii.get(self, "scope"))

    @jsii.member(jsii_name="registerPostProcessor")
    def register_post_processor(self, post_processor: IPostProcessor) -> None:
        '''Use this postprocessor after the entire token structure has been resolved.

        :param post_processor: -
        '''
        return typing.cast(None, jsii.invoke(self, "registerPostProcessor", [post_processor]))

    @jsii.member(jsii_name="resolve")
    def resolve(
        self,
        x: typing.Any,
        *,
        allow_intrinsic_keys: typing.Optional[builtins.bool] = None,
    ) -> typing.Any:
        '''Resolve an inner object.

        :param x: -
        :param allow_intrinsic_keys: Change the 'allowIntrinsicKeys' option. Default: - Unchanged
        '''
        options = ResolveChangeContextOptions(
            allow_intrinsic_keys=allow_intrinsic_keys
        )

        return typing.cast(typing.Any, jsii.invoke(self, "resolve", [x, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResolveContext).__jsii_proxy_class__ = lambda : _IResolveContextProxy


@jsii.interface(jsii_type="@aws-cdk/core.IStableAnyProducer")
class IStableAnyProducer(typing_extensions.Protocol):
    '''Interface for (stable) lazy untyped value producers.'''

    @jsii.member(jsii_name="produce")
    def produce(self) -> typing.Any:
        '''Produce the value.'''
        ...


class _IStableAnyProducerProxy:
    '''Interface for (stable) lazy untyped value producers.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.IStableAnyProducer"

    @jsii.member(jsii_name="produce")
    def produce(self) -> typing.Any:
        '''Produce the value.'''
        return typing.cast(typing.Any, jsii.invoke(self, "produce", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStableAnyProducer).__jsii_proxy_class__ = lambda : _IStableAnyProducerProxy


@jsii.interface(jsii_type="@aws-cdk/core.IStableListProducer")
class IStableListProducer(typing_extensions.Protocol):
    '''Interface for (stable) lazy list producers.'''

    @jsii.member(jsii_name="produce")
    def produce(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Produce the list value.'''
        ...


class _IStableListProducerProxy:
    '''Interface for (stable) lazy list producers.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.IStableListProducer"

    @jsii.member(jsii_name="produce")
    def produce(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Produce the list value.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.invoke(self, "produce", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStableListProducer).__jsii_proxy_class__ = lambda : _IStableListProducerProxy


@jsii.interface(jsii_type="@aws-cdk/core.IStableNumberProducer")
class IStableNumberProducer(typing_extensions.Protocol):
    '''Interface for (stable) lazy number producers.'''

    @jsii.member(jsii_name="produce")
    def produce(self) -> typing.Optional[jsii.Number]:
        '''Produce the number value.'''
        ...


class _IStableNumberProducerProxy:
    '''Interface for (stable) lazy number producers.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.IStableNumberProducer"

    @jsii.member(jsii_name="produce")
    def produce(self) -> typing.Optional[jsii.Number]:
        '''Produce the number value.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.invoke(self, "produce", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStableNumberProducer).__jsii_proxy_class__ = lambda : _IStableNumberProducerProxy


@jsii.interface(jsii_type="@aws-cdk/core.IStableStringProducer")
class IStableStringProducer(typing_extensions.Protocol):
    '''Interface for (stable) lazy string producers.'''

    @jsii.member(jsii_name="produce")
    def produce(self) -> typing.Optional[builtins.str]:
        '''Produce the string value.'''
        ...


class _IStableStringProducerProxy:
    '''Interface for (stable) lazy string producers.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.IStableStringProducer"

    @jsii.member(jsii_name="produce")
    def produce(self) -> typing.Optional[builtins.str]:
        '''Produce the string value.'''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "produce", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStableStringProducer).__jsii_proxy_class__ = lambda : _IStableStringProducerProxy


@jsii.interface(jsii_type="@aws-cdk/core.IStackSynthesizer")
class IStackSynthesizer(typing_extensions.Protocol):
    '''Encodes information how a certain Stack should be deployed.'''

    @jsii.member(jsii_name="addDockerImageAsset")
    def add_docker_image_asset(
        self,
        *,
        source_hash: builtins.str,
        directory_name: typing.Optional[builtins.str] = None,
        docker_build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        docker_build_target: typing.Optional[builtins.str] = None,
        docker_file: typing.Optional[builtins.str] = None,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        repository_name: typing.Optional[builtins.str] = None,
    ) -> DockerImageAssetLocation:
        '''Register a Docker Image Asset.

        Returns the parameters that can be used to refer to the asset inside the template.

        :param source_hash: The hash of the contents of the docker build context. This hash is used throughout the system to identify this image and avoid duplicate work in case the source did not change. NOTE: this means that if you wish to update your docker image, you must make a modification to the source (e.g. add some metadata to your Dockerfile).
        :param directory_name: The directory where the Dockerfile is stored, must be relative to the cloud assembly root. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param docker_build_args: Build args to pass to the ``docker build`` command. Since Docker build arguments are resolved before deployment, keys and values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or ``queue.queueUrl``). Only allowed when ``directoryName`` is specified. Default: - no build args are passed
        :param docker_build_target: Docker target to build to. Only allowed when ``directoryName`` is specified. Default: - no target
        :param docker_file: Path to the Dockerfile (relative to the directory). Only allowed when ``directoryName`` is specified. Default: - no file
        :param executable: An external command that will produce the packaged asset. The command should produce the name of a local Docker image on ``stdout``. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param repository_name: (deprecated) ECR repository name. Specify this property if you need to statically address the image, e.g. from a Kubernetes Pod. Note, this is only the repository name, without the registry and the tag parts. Default: - automatically derived from the asset's ID.
        '''
        ...

    @jsii.member(jsii_name="addFileAsset")
    def add_file_asset(
        self,
        *,
        source_hash: builtins.str,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_name: typing.Optional[builtins.str] = None,
        packaging: typing.Optional[FileAssetPackaging] = None,
    ) -> FileAssetLocation:
        '''Register a File Asset.

        Returns the parameters that can be used to refer to the asset inside the template.

        :param source_hash: A hash on the content source. This hash is used to uniquely identify this asset throughout the system. If this value doesn't change, the asset will not be rebuilt or republished.
        :param executable: An external command that will produce the packaged asset. The command should produce the location of a ZIP file on ``stdout``. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param file_name: The path, relative to the root of the cloud assembly, in which this asset source resides. This can be a path to a file or a directory, depending on the packaging type. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param packaging: Which type of packaging to perform. Default: - Required if ``fileName`` is specified.
        '''
        ...

    @jsii.member(jsii_name="bind")
    def bind(self, stack: "Stack") -> None:
        '''Bind to the stack this environment is going to be used on.

        Must be called before any of the other methods are called.

        :param stack: -
        '''
        ...

    @jsii.member(jsii_name="synthesize")
    def synthesize(self, session: "ISynthesisSession") -> None:
        '''Synthesize the associated stack to the session.

        :param session: -
        '''
        ...


class _IStackSynthesizerProxy:
    '''Encodes information how a certain Stack should be deployed.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.IStackSynthesizer"

    @jsii.member(jsii_name="addDockerImageAsset")
    def add_docker_image_asset(
        self,
        *,
        source_hash: builtins.str,
        directory_name: typing.Optional[builtins.str] = None,
        docker_build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        docker_build_target: typing.Optional[builtins.str] = None,
        docker_file: typing.Optional[builtins.str] = None,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        repository_name: typing.Optional[builtins.str] = None,
    ) -> DockerImageAssetLocation:
        '''Register a Docker Image Asset.

        Returns the parameters that can be used to refer to the asset inside the template.

        :param source_hash: The hash of the contents of the docker build context. This hash is used throughout the system to identify this image and avoid duplicate work in case the source did not change. NOTE: this means that if you wish to update your docker image, you must make a modification to the source (e.g. add some metadata to your Dockerfile).
        :param directory_name: The directory where the Dockerfile is stored, must be relative to the cloud assembly root. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param docker_build_args: Build args to pass to the ``docker build`` command. Since Docker build arguments are resolved before deployment, keys and values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or ``queue.queueUrl``). Only allowed when ``directoryName`` is specified. Default: - no build args are passed
        :param docker_build_target: Docker target to build to. Only allowed when ``directoryName`` is specified. Default: - no target
        :param docker_file: Path to the Dockerfile (relative to the directory). Only allowed when ``directoryName`` is specified. Default: - no file
        :param executable: An external command that will produce the packaged asset. The command should produce the name of a local Docker image on ``stdout``. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param repository_name: (deprecated) ECR repository name. Specify this property if you need to statically address the image, e.g. from a Kubernetes Pod. Note, this is only the repository name, without the registry and the tag parts. Default: - automatically derived from the asset's ID.
        '''
        asset = DockerImageAssetSource(
            source_hash=source_hash,
            directory_name=directory_name,
            docker_build_args=docker_build_args,
            docker_build_target=docker_build_target,
            docker_file=docker_file,
            executable=executable,
            repository_name=repository_name,
        )

        return typing.cast(DockerImageAssetLocation, jsii.invoke(self, "addDockerImageAsset", [asset]))

    @jsii.member(jsii_name="addFileAsset")
    def add_file_asset(
        self,
        *,
        source_hash: builtins.str,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_name: typing.Optional[builtins.str] = None,
        packaging: typing.Optional[FileAssetPackaging] = None,
    ) -> FileAssetLocation:
        '''Register a File Asset.

        Returns the parameters that can be used to refer to the asset inside the template.

        :param source_hash: A hash on the content source. This hash is used to uniquely identify this asset throughout the system. If this value doesn't change, the asset will not be rebuilt or republished.
        :param executable: An external command that will produce the packaged asset. The command should produce the location of a ZIP file on ``stdout``. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param file_name: The path, relative to the root of the cloud assembly, in which this asset source resides. This can be a path to a file or a directory, depending on the packaging type. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param packaging: Which type of packaging to perform. Default: - Required if ``fileName`` is specified.
        '''
        asset = FileAssetSource(
            source_hash=source_hash,
            executable=executable,
            file_name=file_name,
            packaging=packaging,
        )

        return typing.cast(FileAssetLocation, jsii.invoke(self, "addFileAsset", [asset]))

    @jsii.member(jsii_name="bind")
    def bind(self, stack: "Stack") -> None:
        '''Bind to the stack this environment is going to be used on.

        Must be called before any of the other methods are called.

        :param stack: -
        '''
        return typing.cast(None, jsii.invoke(self, "bind", [stack]))

    @jsii.member(jsii_name="synthesize")
    def synthesize(self, session: "ISynthesisSession") -> None:
        '''Synthesize the associated stack to the session.

        :param session: -
        '''
        return typing.cast(None, jsii.invoke(self, "synthesize", [session]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStackSynthesizer).__jsii_proxy_class__ = lambda : _IStackSynthesizerProxy


@jsii.interface(jsii_type="@aws-cdk/core.IStringProducer")
class IStringProducer(typing_extensions.Protocol):
    '''Interface for lazy string producers.'''

    @jsii.member(jsii_name="produce")
    def produce(self, context: IResolveContext) -> typing.Optional[builtins.str]:
        '''Produce the string value.

        :param context: -
        '''
        ...


class _IStringProducerProxy:
    '''Interface for lazy string producers.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.IStringProducer"

    @jsii.member(jsii_name="produce")
    def produce(self, context: IResolveContext) -> typing.Optional[builtins.str]:
        '''Produce the string value.

        :param context: -
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.invoke(self, "produce", [context]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStringProducer).__jsii_proxy_class__ = lambda : _IStringProducerProxy


@jsii.interface(jsii_type="@aws-cdk/core.ISynthesisSession")
class ISynthesisSession(typing_extensions.Protocol):
    '''Represents a single session of synthesis.

    Passed into ``Construct.synthesize()`` methods.
    '''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assembly")
    def assembly(self) -> aws_cdk.cx_api.CloudAssemblyBuilder:
        '''Cloud assembly builder.'''
        ...

    @assembly.setter
    def assembly(self, value: aws_cdk.cx_api.CloudAssemblyBuilder) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outdir")
    def outdir(self) -> builtins.str:
        '''The output directory for this synthesis session.'''
        ...

    @outdir.setter
    def outdir(self, value: builtins.str) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="validateOnSynth")
    def validate_on_synth(self) -> typing.Optional[builtins.bool]:
        '''Whether the stack should be validated after synthesis to check for error metadata.

        :default: - false
        '''
        ...

    @validate_on_synth.setter
    def validate_on_synth(self, value: typing.Optional[builtins.bool]) -> None:
        ...


class _ISynthesisSessionProxy:
    '''Represents a single session of synthesis.

    Passed into ``Construct.synthesize()`` methods.
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.ISynthesisSession"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assembly")
    def assembly(self) -> aws_cdk.cx_api.CloudAssemblyBuilder:
        '''Cloud assembly builder.'''
        return typing.cast(aws_cdk.cx_api.CloudAssemblyBuilder, jsii.get(self, "assembly"))

    @assembly.setter
    def assembly(self, value: aws_cdk.cx_api.CloudAssemblyBuilder) -> None:
        jsii.set(self, "assembly", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outdir")
    def outdir(self) -> builtins.str:
        '''The output directory for this synthesis session.'''
        return typing.cast(builtins.str, jsii.get(self, "outdir"))

    @outdir.setter
    def outdir(self, value: builtins.str) -> None:
        jsii.set(self, "outdir", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="validateOnSynth")
    def validate_on_synth(self) -> typing.Optional[builtins.bool]:
        '''Whether the stack should be validated after synthesis to check for error metadata.

        :default: - false
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "validateOnSynth"))

    @validate_on_synth.setter
    def validate_on_synth(self, value: typing.Optional[builtins.bool]) -> None:
        jsii.set(self, "validateOnSynth", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISynthesisSession).__jsii_proxy_class__ = lambda : _ISynthesisSessionProxy


@jsii.interface(jsii_type="@aws-cdk/core.ITaggable")
class ITaggable(typing_extensions.Protocol):
    '''Interface to implement tags.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> "TagManager":
        '''TagManager to set, remove and format tags.'''
        ...


class _ITaggableProxy:
    '''Interface to implement tags.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.ITaggable"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> "TagManager":
        '''TagManager to set, remove and format tags.'''
        return typing.cast("TagManager", jsii.get(self, "tags"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITaggable).__jsii_proxy_class__ = lambda : _ITaggableProxy


@jsii.interface(jsii_type="@aws-cdk/core.ITemplateOptions")
class ITemplateOptions(typing_extensions.Protocol):
    '''CloudFormation template options for a stack.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Gets or sets the description of this stack.

        If provided, it will be included in the CloudFormation template's "Description" attribute.
        '''
        ...

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Metadata associated with the CloudFormation template.'''
        ...

    @metadata.setter
    def metadata(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Any]],
    ) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateFormatVersion")
    def template_format_version(self) -> typing.Optional[builtins.str]:
        '''Gets or sets the AWSTemplateFormatVersion field of the CloudFormation template.'''
        ...

    @template_format_version.setter
    def template_format_version(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="transform")
    def transform(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Gets or sets the top-level template transform for this stack (e.g. "AWS::Serverless-2016-10-31").

        :deprecated: use ``transforms`` instead.

        :stability: deprecated
        '''
        ...

    @transform.setter
    def transform(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Gets or sets the top-level template transform(s) for this stack (e.g. ``["AWS::Serverless-2016-10-31"]``).'''
        ...

    @transforms.setter
    def transforms(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        ...


class _ITemplateOptionsProxy:
    '''CloudFormation template options for a stack.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.ITemplateOptions"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Gets or sets the description of this stack.

        If provided, it will be included in the CloudFormation template's "Description" attribute.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Metadata associated with the CloudFormation template.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, typing.Any]],
    ) -> None:
        jsii.set(self, "metadata", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateFormatVersion")
    def template_format_version(self) -> typing.Optional[builtins.str]:
        '''Gets or sets the AWSTemplateFormatVersion field of the CloudFormation template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateFormatVersion"))

    @template_format_version.setter
    def template_format_version(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "templateFormatVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="transform")
    def transform(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Gets or sets the top-level template transform for this stack (e.g. "AWS::Serverless-2016-10-31").

        :deprecated: use ``transforms`` instead.

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transform"))

    @transform.setter
    def transform(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "transform", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Gets or sets the top-level template transform(s) for this stack (e.g. ``["AWS::Serverless-2016-10-31"]``).'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "transforms", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITemplateOptions).__jsii_proxy_class__ = lambda : _ITemplateOptionsProxy


@jsii.interface(jsii_type="@aws-cdk/core.ITokenMapper")
class ITokenMapper(typing_extensions.Protocol):
    '''Interface to apply operation to tokens in a string.

    Interface so it can be exported via jsii.
    '''

    @jsii.member(jsii_name="mapToken")
    def map_token(self, t: IResolvable) -> typing.Any:
        '''Replace a single token.

        :param t: -
        '''
        ...


class _ITokenMapperProxy:
    '''Interface to apply operation to tokens in a string.

    Interface so it can be exported via jsii.
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.ITokenMapper"

    @jsii.member(jsii_name="mapToken")
    def map_token(self, t: IResolvable) -> typing.Any:
        '''Replace a single token.

        :param t: -
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "mapToken", [t]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITokenMapper).__jsii_proxy_class__ = lambda : _ITokenMapperProxy


@jsii.interface(jsii_type="@aws-cdk/core.ITokenResolver")
class ITokenResolver(typing_extensions.Protocol):
    '''How to resolve tokens.'''

    @jsii.member(jsii_name="resolveList")
    def resolve_list(
        self,
        l: typing.Sequence[builtins.str],
        context: IResolveContext,
    ) -> typing.Any:
        '''Resolve a tokenized list.

        :param l: -
        :param context: -
        '''
        ...

    @jsii.member(jsii_name="resolveString")
    def resolve_string(
        self,
        s: "TokenizedStringFragments",
        context: IResolveContext,
    ) -> typing.Any:
        '''Resolve a string with at least one stringified token in it.

        (May use concatenation)

        :param s: -
        :param context: -
        '''
        ...

    @jsii.member(jsii_name="resolveToken")
    def resolve_token(
        self,
        t: IResolvable,
        context: IResolveContext,
        post_processor: IPostProcessor,
    ) -> typing.Any:
        '''Resolve a single token.

        :param t: -
        :param context: -
        :param post_processor: -
        '''
        ...


class _ITokenResolverProxy:
    '''How to resolve tokens.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.ITokenResolver"

    @jsii.member(jsii_name="resolveList")
    def resolve_list(
        self,
        l: typing.Sequence[builtins.str],
        context: IResolveContext,
    ) -> typing.Any:
        '''Resolve a tokenized list.

        :param l: -
        :param context: -
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "resolveList", [l, context]))

    @jsii.member(jsii_name="resolveString")
    def resolve_string(
        self,
        s: "TokenizedStringFragments",
        context: IResolveContext,
    ) -> typing.Any:
        '''Resolve a string with at least one stringified token in it.

        (May use concatenation)

        :param s: -
        :param context: -
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "resolveString", [s, context]))

    @jsii.member(jsii_name="resolveToken")
    def resolve_token(
        self,
        t: IResolvable,
        context: IResolveContext,
        post_processor: IPostProcessor,
    ) -> typing.Any:
        '''Resolve a single token.

        :param t: -
        :param context: -
        :param post_processor: -
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "resolveToken", [t, context, post_processor]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITokenResolver).__jsii_proxy_class__ = lambda : _ITokenResolverProxy


@jsii.enum(jsii_type="@aws-cdk/core.IgnoreMode")
class IgnoreMode(enum.Enum):
    '''Determines the ignore behavior to use.'''

    GLOB = "GLOB"
    '''Ignores file paths based on simple glob patterns.

    This is the default for file assets.

    It is also the default for Docker image assets, unless the '@aws-cdk/aws-ecr-assets:dockerIgnoreSupport'
    context flag is set.
    '''
    GIT = "GIT"
    '''Ignores file paths based on the ```.gitignore specification`` <https://git-scm.com/docs/gitignore>`_.'''
    DOCKER = "DOCKER"
    '''Ignores file paths based on the ```.dockerignore specification`` <https://docs.docker.com/engine/reference/builder/#dockerignore-file>`_.

    This is the default for Docker image assets if the '@aws-cdk/aws-ecr-assets:dockerIgnoreSupport'
    context flag is set.
    '''


class IgnoreStrategy(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/core.IgnoreStrategy",
):
    '''Represents file path ignoring behavior.'''

    def __init__(self) -> None:
        jsii.create(IgnoreStrategy, self, [])

    @jsii.member(jsii_name="docker") # type: ignore[misc]
    @builtins.classmethod
    def docker(
        cls,
        absolute_root_path: builtins.str,
        patterns: typing.Sequence[builtins.str],
    ) -> "DockerIgnoreStrategy":
        '''Ignores file paths based on the ```.dockerignore specification`` <https://docs.docker.com/engine/reference/builder/#dockerignore-file>`_.

        :param absolute_root_path: the absolute path to the root directory of the paths to be considered.
        :param patterns: -

        :return: ``DockerIgnorePattern`` associated with the given patterns.
        '''
        return typing.cast("DockerIgnoreStrategy", jsii.sinvoke(cls, "docker", [absolute_root_path, patterns]))

    @jsii.member(jsii_name="fromCopyOptions") # type: ignore[misc]
    @builtins.classmethod
    def from_copy_options(
        cls,
        options: CopyOptions,
        absolute_root_path: builtins.str,
    ) -> "IgnoreStrategy":
        '''Creates an IgnoreStrategy based on the ``ignoreMode`` and ``exclude`` in a ``CopyOptions``.

        :param options: the ``CopyOptions`` to create the ``IgnoreStrategy`` from.
        :param absolute_root_path: the absolute path to the root directory of the paths to be considered.

        :return: ``IgnoreStrategy`` based on the ``CopyOptions``
        '''
        return typing.cast("IgnoreStrategy", jsii.sinvoke(cls, "fromCopyOptions", [options, absolute_root_path]))

    @jsii.member(jsii_name="git") # type: ignore[misc]
    @builtins.classmethod
    def git(
        cls,
        absolute_root_path: builtins.str,
        patterns: typing.Sequence[builtins.str],
    ) -> "GitIgnoreStrategy":
        '''Ignores file paths based on the ```.gitignore specification`` <https://git-scm.com/docs/gitignore>`_.

        :param absolute_root_path: the absolute path to the root directory of the paths to be considered.
        :param patterns: -

        :return: ``GitIgnorePattern`` associated with the given patterns.
        '''
        return typing.cast("GitIgnoreStrategy", jsii.sinvoke(cls, "git", [absolute_root_path, patterns]))

    @jsii.member(jsii_name="glob") # type: ignore[misc]
    @builtins.classmethod
    def glob(
        cls,
        absolute_root_path: builtins.str,
        patterns: typing.Sequence[builtins.str],
    ) -> "GlobIgnoreStrategy":
        '''Ignores file paths based on simple glob patterns.

        :param absolute_root_path: the absolute path to the root directory of the paths to be considered.
        :param patterns: -

        :return: ``GlobIgnorePattern`` associated with the given patterns.
        '''
        return typing.cast("GlobIgnoreStrategy", jsii.sinvoke(cls, "glob", [absolute_root_path, patterns]))

    @jsii.member(jsii_name="add") # type: ignore[misc]
    @abc.abstractmethod
    def add(self, pattern: builtins.str) -> None:
        '''Adds another pattern.

        :param pattern: -

        :params: pattern the pattern to add
        '''
        ...

    @jsii.member(jsii_name="ignores") # type: ignore[misc]
    @abc.abstractmethod
    def ignores(self, absolute_file_path: builtins.str) -> builtins.bool:
        '''Determines whether a given file path should be ignored or not.

        :param absolute_file_path: absolute file path to be assessed against the pattern.

        :return: ``true`` if the file should be ignored
        '''
        ...


class _IgnoreStrategyProxy(IgnoreStrategy):
    @jsii.member(jsii_name="add")
    def add(self, pattern: builtins.str) -> None:
        '''Adds another pattern.

        :param pattern: -

        :params: pattern the pattern to add
        '''
        return typing.cast(None, jsii.invoke(self, "add", [pattern]))

    @jsii.member(jsii_name="ignores")
    def ignores(self, absolute_file_path: builtins.str) -> builtins.bool:
        '''Determines whether a given file path should be ignored or not.

        :param absolute_file_path: absolute file path to be assessed against the pattern.

        :return: ``true`` if the file should be ignored
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "ignores", [absolute_file_path]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, IgnoreStrategy).__jsii_proxy_class__ = lambda : _IgnoreStrategyProxy


@jsii.implements(IResolvable)
class Intrinsic(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.Intrinsic"):
    '''Token subclass that represents values intrinsic to the target document language.

    WARNING: this class should not be externally exposed, but is currently visible
    because of a limitation of jsii (https://github.com/aws/jsii/issues/524).

    This class will disappear in a future release and should not be used.
    '''

    def __init__(
        self,
        value: typing.Any,
        *,
        stack_trace: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param value: -
        :param stack_trace: Capture the stack trace of where this token is created. Default: true
        '''
        options = IntrinsicProps(stack_trace=stack_trace)

        jsii.create(Intrinsic, self, [value, options])

    @jsii.member(jsii_name="newError")
    def _new_error(self, message: builtins.str) -> typing.Any:
        '''Creates a throwable Error object that contains the token creation stack trace.

        :param message: Error message.
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "newError", [message]))

    @jsii.member(jsii_name="resolve")
    def resolve(self, _context: IResolveContext) -> typing.Any:
        '''Produce the Token's value at resolution time.

        :param _context: -
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "resolve", [_context]))

    @jsii.member(jsii_name="toJSON")
    def to_json(self) -> typing.Any:
        '''Turn this Token into JSON.

        Called automatically when JSON.stringify() is called on a Token.
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "toJSON", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Convert an instance of this Token to a string.

        This method will be called implicitly by language runtimes if the object
        is embedded into a string. We treat it the same as an explicit
        stringification.
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="creationStack")
    def creation_stack(self) -> typing.List[builtins.str]:
        '''The captured stack trace which represents the location in which this token was created.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "creationStack"))


@jsii.data_type(
    jsii_type="@aws-cdk/core.IntrinsicProps",
    jsii_struct_bases=[],
    name_mapping={"stack_trace": "stackTrace"},
)
class IntrinsicProps:
    def __init__(self, *, stack_trace: typing.Optional[builtins.bool] = None) -> None:
        '''Customization properties for an Intrinsic token.

        :param stack_trace: Capture the stack trace of where this token is created. Default: true
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if stack_trace is not None:
            self._values["stack_trace"] = stack_trace

    @builtins.property
    def stack_trace(self) -> typing.Optional[builtins.bool]:
        '''Capture the stack trace of where this token is created.

        :default: true
        '''
        result = self._values.get("stack_trace")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IntrinsicProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Lazy(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.Lazy"):
    '''Lazily produce a value.

    Can be used to return a string, list or numeric value whose actual value
    will only be calculated later, during synthesis.
    '''

    @jsii.member(jsii_name="any") # type: ignore[misc]
    @builtins.classmethod
    def any(
        cls,
        producer: IStableAnyProducer,
        *,
        display_hint: typing.Optional[builtins.str] = None,
        omit_empty_array: typing.Optional[builtins.bool] = None,
    ) -> IResolvable:
        '''Defer the one-time calculation of an arbitrarily typed value to synthesis time.

        Use this if you want to render an object to a template whose actual value depends on
        some state mutation that may happen after the construct has been created.

        The inner function will only be invoked one time and cannot depend on
        resolution context.

        :param producer: -
        :param display_hint: Use the given name as a display hint. Default: - No hint
        :param omit_empty_array: If the produced value is an array and it is empty, return 'undefined' instead. Default: false
        '''
        options = LazyAnyValueOptions(
            display_hint=display_hint, omit_empty_array=omit_empty_array
        )

        return typing.cast(IResolvable, jsii.sinvoke(cls, "any", [producer, options]))

    @jsii.member(jsii_name="anyValue") # type: ignore[misc]
    @builtins.classmethod
    def any_value(
        cls,
        producer: IAnyProducer,
        *,
        display_hint: typing.Optional[builtins.str] = None,
        omit_empty_array: typing.Optional[builtins.bool] = None,
    ) -> IResolvable:
        '''(deprecated) Defer the one-time calculation of an arbitrarily typed value to synthesis time.

        Use this if you want to render an object to a template whose actual value depends on
        some state mutation that may happen after the construct has been created.

        :param producer: -
        :param display_hint: Use the given name as a display hint. Default: - No hint
        :param omit_empty_array: If the produced value is an array and it is empty, return 'undefined' instead. Default: false

        :deprecated: Use ``Lazy.any()`` or ``Lazy.uncachedAny()`` instead.

        :stability: deprecated
        '''
        options = LazyAnyValueOptions(
            display_hint=display_hint, omit_empty_array=omit_empty_array
        )

        return typing.cast(IResolvable, jsii.sinvoke(cls, "anyValue", [producer, options]))

    @jsii.member(jsii_name="list") # type: ignore[misc]
    @builtins.classmethod
    def list(
        cls,
        producer: IStableListProducer,
        *,
        display_hint: typing.Optional[builtins.str] = None,
        omit_empty: typing.Optional[builtins.bool] = None,
    ) -> typing.List[builtins.str]:
        '''Defer the one-time calculation of a list value to synthesis time.

        Use this if you want to render a list to a template whose actual value depends on
        some state mutation that may happen after the construct has been created.

        If you are simply looking to force a value to a ``string[]`` type and don't need
        the calculation to be deferred, use ``Token.asList()`` instead.

        The inner function will only be invoked once, and the resolved value
        cannot depend on the Stack the Token is used in.

        :param producer: -
        :param display_hint: Use the given name as a display hint. Default: - No hint
        :param omit_empty: If the produced list is empty, return 'undefined' instead. Default: false
        '''
        options = LazyListValueOptions(
            display_hint=display_hint, omit_empty=omit_empty
        )

        return typing.cast(typing.List[builtins.str], jsii.sinvoke(cls, "list", [producer, options]))

    @jsii.member(jsii_name="listValue") # type: ignore[misc]
    @builtins.classmethod
    def list_value(
        cls,
        producer: IListProducer,
        *,
        display_hint: typing.Optional[builtins.str] = None,
        omit_empty: typing.Optional[builtins.bool] = None,
    ) -> typing.List[builtins.str]:
        '''(deprecated) Defer the one-time calculation of a list value to synthesis time.

        Use this if you want to render a list to a template whose actual value depends on
        some state mutation that may happen after the construct has been created.

        If you are simply looking to force a value to a ``string[]`` type and don't need
        the calculation to be deferred, use ``Token.asList()`` instead.

        :param producer: -
        :param display_hint: Use the given name as a display hint. Default: - No hint
        :param omit_empty: If the produced list is empty, return 'undefined' instead. Default: false

        :deprecated: Use ``Lazy.list()`` or ``Lazy.uncachedList()`` instead.

        :stability: deprecated
        '''
        options = LazyListValueOptions(
            display_hint=display_hint, omit_empty=omit_empty
        )

        return typing.cast(typing.List[builtins.str], jsii.sinvoke(cls, "listValue", [producer, options]))

    @jsii.member(jsii_name="number") # type: ignore[misc]
    @builtins.classmethod
    def number(cls, producer: IStableNumberProducer) -> jsii.Number:
        '''Defer the one-time calculation of a number value to synthesis time.

        Use this if you want to render a number to a template whose actual value depends on
        some state mutation that may happen after the construct has been created.

        If you are simply looking to force a value to a ``number`` type and don't need
        the calculation to be deferred, use ``Token.asNumber()`` instead.

        The inner function will only be invoked once, and the resolved value
        cannot depend on the Stack the Token is used in.

        :param producer: -
        '''
        return typing.cast(jsii.Number, jsii.sinvoke(cls, "number", [producer]))

    @jsii.member(jsii_name="numberValue") # type: ignore[misc]
    @builtins.classmethod
    def number_value(cls, producer: INumberProducer) -> jsii.Number:
        '''(deprecated) Defer the one-time calculation of a number value to synthesis time.

        Use this if you want to render a number to a template whose actual value depends on
        some state mutation that may happen after the construct has been created.

        If you are simply looking to force a value to a ``number`` type and don't need
        the calculation to be deferred, use ``Token.asNumber()`` instead.

        :param producer: -

        :deprecated: Use ``Lazy.number()`` or ``Lazy.uncachedNumber()`` instead.

        :stability: deprecated
        '''
        return typing.cast(jsii.Number, jsii.sinvoke(cls, "numberValue", [producer]))

    @jsii.member(jsii_name="string") # type: ignore[misc]
    @builtins.classmethod
    def string(
        cls,
        producer: IStableStringProducer,
        *,
        display_hint: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''Defer the one-time calculation of a string value to synthesis time.

        Use this if you want to render a string to a template whose actual value depends on
        some state mutation that may happen after the construct has been created.

        If you are simply looking to force a value to a ``string`` type and don't need
        the calculation to be deferred, use ``Token.asString()`` instead.

        The inner function will only be invoked once, and the resolved value
        cannot depend on the Stack the Token is used in.

        :param producer: -
        :param display_hint: Use the given name as a display hint. Default: - No hint
        '''
        options = LazyStringValueOptions(display_hint=display_hint)

        return typing.cast(builtins.str, jsii.sinvoke(cls, "string", [producer, options]))

    @jsii.member(jsii_name="stringValue") # type: ignore[misc]
    @builtins.classmethod
    def string_value(
        cls,
        producer: IStringProducer,
        *,
        display_hint: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''(deprecated) Defer the calculation of a string value to synthesis time.

        Use this if you want to render a string to a template whose actual value depends on
        some state mutation that may happen after the construct has been created.

        If you are simply looking to force a value to a ``string`` type and don't need
        the calculation to be deferred, use ``Token.asString()`` instead.

        :param producer: -
        :param display_hint: Use the given name as a display hint. Default: - No hint

        :deprecated: Use ``Lazy.string()`` or ``Lazy.uncachedString()`` instead.

        :stability: deprecated
        '''
        options = LazyStringValueOptions(display_hint=display_hint)

        return typing.cast(builtins.str, jsii.sinvoke(cls, "stringValue", [producer, options]))

    @jsii.member(jsii_name="uncachedAny") # type: ignore[misc]
    @builtins.classmethod
    def uncached_any(
        cls,
        producer: IAnyProducer,
        *,
        display_hint: typing.Optional[builtins.str] = None,
        omit_empty_array: typing.Optional[builtins.bool] = None,
    ) -> IResolvable:
        '''Defer the calculation of an untyped value to synthesis time.

        Use of this function is not recommended; unless you know you need it for sure, you
        probably don't. Use ``Lazy.any()`` instead.

        The inner function may be invoked multiple times during synthesis. You
        should only use this method if the returned value depends on variables
        that may change during the Aspect application phase of synthesis, or if
        the value depends on the Stack the value is being used in. Both of these
        cases are rare, and only ever occur for AWS Construct Library authors.

        :param producer: -
        :param display_hint: Use the given name as a display hint. Default: - No hint
        :param omit_empty_array: If the produced value is an array and it is empty, return 'undefined' instead. Default: false
        '''
        options = LazyAnyValueOptions(
            display_hint=display_hint, omit_empty_array=omit_empty_array
        )

        return typing.cast(IResolvable, jsii.sinvoke(cls, "uncachedAny", [producer, options]))

    @jsii.member(jsii_name="uncachedList") # type: ignore[misc]
    @builtins.classmethod
    def uncached_list(
        cls,
        producer: IListProducer,
        *,
        display_hint: typing.Optional[builtins.str] = None,
        omit_empty: typing.Optional[builtins.bool] = None,
    ) -> typing.List[builtins.str]:
        '''Defer the calculation of a list value to synthesis time.

        Use of this function is not recommended; unless you know you need it for sure, you
        probably don't. Use ``Lazy.list()`` instead.

        The inner function may be invoked multiple times during synthesis. You
        should only use this method if the returned value depends on variables
        that may change during the Aspect application phase of synthesis, or if
        the value depends on the Stack the value is being used in. Both of these
        cases are rare, and only ever occur for AWS Construct Library authors.

        :param producer: -
        :param display_hint: Use the given name as a display hint. Default: - No hint
        :param omit_empty: If the produced list is empty, return 'undefined' instead. Default: false
        '''
        options = LazyListValueOptions(
            display_hint=display_hint, omit_empty=omit_empty
        )

        return typing.cast(typing.List[builtins.str], jsii.sinvoke(cls, "uncachedList", [producer, options]))

    @jsii.member(jsii_name="uncachedNumber") # type: ignore[misc]
    @builtins.classmethod
    def uncached_number(cls, producer: INumberProducer) -> jsii.Number:
        '''Defer the calculation of a number value to synthesis time.

        Use of this function is not recommended; unless you know you need it for sure, you
        probably don't. Use ``Lazy.number()`` instead.

        The inner function may be invoked multiple times during synthesis. You
        should only use this method if the returned value depends on variables
        that may change during the Aspect application phase of synthesis, or if
        the value depends on the Stack the value is being used in. Both of these
        cases are rare, and only ever occur for AWS Construct Library authors.

        :param producer: -
        '''
        return typing.cast(jsii.Number, jsii.sinvoke(cls, "uncachedNumber", [producer]))

    @jsii.member(jsii_name="uncachedString") # type: ignore[misc]
    @builtins.classmethod
    def uncached_string(
        cls,
        producer: IStringProducer,
        *,
        display_hint: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''Defer the calculation of a string value to synthesis time.

        Use of this function is not recommended; unless you know you need it for sure, you
        probably don't. Use ``Lazy.string()`` instead.

        The inner function may be invoked multiple times during synthesis. You
        should only use this method if the returned value depends on variables
        that may change during the Aspect application phase of synthesis, or if
        the value depends on the Stack the value is being used in. Both of these
        cases are rare, and only ever occur for AWS Construct Library authors.

        :param producer: -
        :param display_hint: Use the given name as a display hint. Default: - No hint
        '''
        options = LazyStringValueOptions(display_hint=display_hint)

        return typing.cast(builtins.str, jsii.sinvoke(cls, "uncachedString", [producer, options]))


@jsii.data_type(
    jsii_type="@aws-cdk/core.LazyAnyValueOptions",
    jsii_struct_bases=[],
    name_mapping={"display_hint": "displayHint", "omit_empty_array": "omitEmptyArray"},
)
class LazyAnyValueOptions:
    def __init__(
        self,
        *,
        display_hint: typing.Optional[builtins.str] = None,
        omit_empty_array: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options for creating lazy untyped tokens.

        :param display_hint: Use the given name as a display hint. Default: - No hint
        :param omit_empty_array: If the produced value is an array and it is empty, return 'undefined' instead. Default: false
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if display_hint is not None:
            self._values["display_hint"] = display_hint
        if omit_empty_array is not None:
            self._values["omit_empty_array"] = omit_empty_array

    @builtins.property
    def display_hint(self) -> typing.Optional[builtins.str]:
        '''Use the given name as a display hint.

        :default: - No hint
        '''
        result = self._values.get("display_hint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def omit_empty_array(self) -> typing.Optional[builtins.bool]:
        '''If the produced value is an array and it is empty, return 'undefined' instead.

        :default: false
        '''
        result = self._values.get("omit_empty_array")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LazyAnyValueOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.LazyListValueOptions",
    jsii_struct_bases=[],
    name_mapping={"display_hint": "displayHint", "omit_empty": "omitEmpty"},
)
class LazyListValueOptions:
    def __init__(
        self,
        *,
        display_hint: typing.Optional[builtins.str] = None,
        omit_empty: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options for creating a lazy list token.

        :param display_hint: Use the given name as a display hint. Default: - No hint
        :param omit_empty: If the produced list is empty, return 'undefined' instead. Default: false
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if display_hint is not None:
            self._values["display_hint"] = display_hint
        if omit_empty is not None:
            self._values["omit_empty"] = omit_empty

    @builtins.property
    def display_hint(self) -> typing.Optional[builtins.str]:
        '''Use the given name as a display hint.

        :default: - No hint
        '''
        result = self._values.get("display_hint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def omit_empty(self) -> typing.Optional[builtins.bool]:
        '''If the produced list is empty, return 'undefined' instead.

        :default: false
        '''
        result = self._values.get("omit_empty")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LazyListValueOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.LazyStringValueOptions",
    jsii_struct_bases=[],
    name_mapping={"display_hint": "displayHint"},
)
class LazyStringValueOptions:
    def __init__(self, *, display_hint: typing.Optional[builtins.str] = None) -> None:
        '''Options for creating a lazy string token.

        :param display_hint: Use the given name as a display hint. Default: - No hint
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if display_hint is not None:
            self._values["display_hint"] = display_hint

    @builtins.property
    def display_hint(self) -> typing.Optional[builtins.str]:
        '''Use the given name as a display hint.

        :default: - No hint
        '''
        result = self._values.get("display_hint")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LazyStringValueOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Names(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.Names"):
    '''Functions for devising unique names for constructs.

    For example, those can be
    used to allocate unique physical names for resources.
    '''

    @jsii.member(jsii_name="nodeUniqueId") # type: ignore[misc]
    @builtins.classmethod
    def node_unique_id(cls, node: ConstructNode) -> builtins.str:
        '''Returns a CloudFormation-compatible unique identifier for a construct based on its path.

        The identifier includes a human readable portion rendered
        from the path components and a hash suffix.

        TODO (v2): replace with API to use ``constructs.Node``.

        :param node: The construct node.

        :return: a unique id based on the construct path
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "nodeUniqueId", [node]))

    @jsii.member(jsii_name="uniqueId") # type: ignore[misc]
    @builtins.classmethod
    def unique_id(cls, construct: constructs.Construct) -> builtins.str:
        '''Returns a CloudFormation-compatible unique identifier for a construct based on its path.

        The identifier includes a human readable portion rendered
        from the path components and a hash suffix.

        :param construct: The construct.

        :return: a unique id based on the construct path
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "uniqueId", [construct]))


@jsii.data_type(
    jsii_type="@aws-cdk/core.NestedStackProps",
    jsii_struct_bases=[],
    name_mapping={
        "notification_arns": "notificationArns",
        "parameters": "parameters",
        "removal_policy": "removalPolicy",
        "timeout": "timeout",
    },
)
class NestedStackProps:
    def __init__(
        self,
        *,
        notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        removal_policy: typing.Optional["RemovalPolicy"] = None,
        timeout: typing.Optional[Duration] = None,
    ) -> None:
        '''Initialization props for the ``NestedStack`` construct.

        :param notification_arns: The Simple Notification Service (SNS) topics to publish stack related events. Default: - notifications are not sent for this stack.
        :param parameters: The set value pairs that represent the parameters passed to CloudFormation when this nested stack is created. Each parameter has a name corresponding to a parameter defined in the embedded template and a value representing the value that you want to set for the parameter. The nested stack construct will automatically synthesize parameters in order to bind references from the parent stack(s) into the nested stack. Default: - no user-defined parameters are passed to the nested stack
        :param removal_policy: Policy to apply when the nested stack is removed. The default is ``Destroy``, because all Removal Policies of resources inside the Nested Stack should already have been set correctly. You normally should not need to set this value. Default: RemovalPolicy.DESTROY
        :param timeout: The length of time that CloudFormation waits for the nested stack to reach the CREATE_COMPLETE state. When CloudFormation detects that the nested stack has reached the CREATE_COMPLETE state, it marks the nested stack resource as CREATE_COMPLETE in the parent stack and resumes creating the parent stack. If the timeout period expires before the nested stack reaches CREATE_COMPLETE, CloudFormation marks the nested stack as failed and rolls back both the nested stack and parent stack. Default: - no timeout
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if notification_arns is not None:
            self._values["notification_arns"] = notification_arns
        if parameters is not None:
            self._values["parameters"] = parameters
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def notification_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Simple Notification Service (SNS) topics to publish stack related events.

        :default: - notifications are not sent for this stack.
        '''
        result = self._values.get("notification_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The set value pairs that represent the parameters passed to CloudFormation when this nested stack is created.

        Each parameter has a name corresponding
        to a parameter defined in the embedded template and a value representing
        the value that you want to set for the parameter.

        The nested stack construct will automatically synthesize parameters in order
        to bind references from the parent stack(s) into the nested stack.

        :default: - no user-defined parameters are passed to the nested stack
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional["RemovalPolicy"]:
        '''Policy to apply when the nested stack is removed.

        The default is ``Destroy``, because all Removal Policies of resources inside the
        Nested Stack should already have been set correctly. You normally should
        not need to set this value.

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional["RemovalPolicy"], result)

    @builtins.property
    def timeout(self) -> typing.Optional[Duration]:
        '''The length of time that CloudFormation waits for the nested stack to reach the CREATE_COMPLETE state.

        When CloudFormation detects that the nested stack has reached the
        CREATE_COMPLETE state, it marks the nested stack resource as
        CREATE_COMPLETE in the parent stack and resumes creating the parent stack.
        If the timeout period expires before the nested stack reaches
        CREATE_COMPLETE, CloudFormation marks the nested stack as failed and rolls
        back both the nested stack and parent stack.

        :default: - no timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NestedStackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PhysicalName(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.PhysicalName"):
    '''Includes special markers for automatic generation of physical names.'''

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="GENERATE_IF_NEEDED")
    def GENERATE_IF_NEEDED(cls) -> builtins.str:
        '''Use this to automatically generate a physical name for an AWS resource only if the resource is referenced across environments (account/region).

        Otherwise, the name will be allocated during deployment by CloudFormation.

        If you are certain that a resource will be referenced across environments,
        you may also specify an explicit physical name for it. This option is
        mostly designed for reusable constructs which may or may not be referenced
        acrossed environments.
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "GENERATE_IF_NEEDED"))


class Reference(
    Intrinsic,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/core.Reference",
):
    '''An intrinsic Token that represents a reference to a construct.

    References are recorded.
    '''

    def __init__(
        self,
        value: typing.Any,
        target: "IConstruct",
        display_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param value: -
        :param target: -
        :param display_name: -
        '''
        jsii.create(Reference, self, [value, target, display_name])

    @jsii.member(jsii_name="isReference") # type: ignore[misc]
    @builtins.classmethod
    def is_reference(cls, x: typing.Any) -> builtins.bool:
        '''Check whether this is actually a Reference.

        :param x: -
        '''
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isReference", [x]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="target")
    def target(self) -> "IConstruct":
        return typing.cast("IConstruct", jsii.get(self, "target"))


class _ReferenceProxy(Reference):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Reference).__jsii_proxy_class__ = lambda : _ReferenceProxy


@jsii.enum(jsii_type="@aws-cdk/core.RemovalPolicy")
class RemovalPolicy(enum.Enum):
    '''Possible values for a resource's Removal Policy.

    The removal policy controls what happens to the resource if it stops being
    managed by CloudFormation. This can happen in one of three situations:

    - The resource is removed from the template, so CloudFormation stops managing it;
    - A change to the resource is made that requires it to be replaced, so CloudFormation stops
      managing it;
    - The stack is deleted, so CloudFormation stops managing all resources in it.

    The Removal Policy applies to all above cases.

    Many stateful resources in the AWS Construct Library will accept a
    ``removalPolicy`` as a property, typically defaulting it to ``RETAIN``.

    If the AWS Construct Library resource does not accept a ``removalPolicy``
    argument, you can always configure it by using the escape hatch mechanism,
    as shown in the following example::

       # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
       cfn_bucket = bucket.node.find_child("Resource")
       cfn_bucket.apply_removal_policy(cdk.RemovalPolicy.DESTROY)
    '''

    DESTROY = "DESTROY"
    '''This is the default removal policy.

    It means that when the resource is
    removed from the app, it will be physically destroyed.
    '''
    RETAIN = "RETAIN"
    '''This uses the 'Retain' DeletionPolicy, which will cause the resource to be retained in the account, but orphaned from the stack.'''
    SNAPSHOT = "SNAPSHOT"
    '''This retention policy deletes the resource, but saves a snapshot of its data before deleting, so that it can be re-created later.

    Only available for some stateful resources,
    like databases, EFS volumes, etc.

    :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html#aws-attribute-deletionpolicy-options
    '''


@jsii.data_type(
    jsii_type="@aws-cdk/core.RemovalPolicyOptions",
    jsii_struct_bases=[],
    name_mapping={
        "apply_to_update_replace_policy": "applyToUpdateReplacePolicy",
        "default": "default",
    },
)
class RemovalPolicyOptions:
    def __init__(
        self,
        *,
        apply_to_update_replace_policy: typing.Optional[builtins.bool] = None,
        default: typing.Optional[RemovalPolicy] = None,
    ) -> None:
        '''
        :param apply_to_update_replace_policy: Apply the same deletion policy to the resource's "UpdateReplacePolicy". Default: true
        :param default: The default policy to apply in case the removal policy is not defined. Default: - Default value is resource specific. To determine the default value for a resoure, please consult that specific resource's documentation.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if apply_to_update_replace_policy is not None:
            self._values["apply_to_update_replace_policy"] = apply_to_update_replace_policy
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def apply_to_update_replace_policy(self) -> typing.Optional[builtins.bool]:
        '''Apply the same deletion policy to the resource's "UpdateReplacePolicy".

        :default: true
        '''
        result = self._values.get("apply_to_update_replace_policy")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def default(self) -> typing.Optional[RemovalPolicy]:
        '''The default policy to apply in case the removal policy is not defined.

        :default:

        - Default value is resource specific. To determine the default value for a resoure,
        please consult that specific resource's documentation.
        '''
        result = self._values.get("default")
        return typing.cast(typing.Optional[RemovalPolicy], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RemovalPolicyOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IAspect)
class RemoveTag(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.RemoveTag"):
    '''The RemoveTag Aspect will handle removing tags from this node and children.'''

    def __init__(
        self,
        key: builtins.str,
        *,
        apply_to_launched_instances: typing.Optional[builtins.bool] = None,
        exclude_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        include_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        priority: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param key: -
        :param apply_to_launched_instances: Whether the tag should be applied to instances in an AutoScalingGroup. Default: true
        :param exclude_resource_types: An array of Resource Types that will not receive this tag. An empty array will allow this tag to be applied to all resources. A non-empty array will apply this tag only if the Resource type is not in this array. Default: []
        :param include_resource_types: An array of Resource Types that will receive this tag. An empty array will match any Resource. A non-empty array will apply this tag only to Resource types that are included in this array. Default: []
        :param priority: Priority of the tag operation. Higher or equal priority tags will take precedence. Setting priority will enable the user to control tags when they need to not follow the default precedence pattern of last applied and closest to the construct in the tree. Default: Default priorities: - 100 for {@link SetTag} - 200 for {@link RemoveTag} - 50 for tags added directly to CloudFormation resources
        '''
        props = TagProps(
            apply_to_launched_instances=apply_to_launched_instances,
            exclude_resource_types=exclude_resource_types,
            include_resource_types=include_resource_types,
            priority=priority,
        )

        jsii.create(RemoveTag, self, [key, props])

    @jsii.member(jsii_name="applyTag")
    def _apply_tag(self, resource: ITaggable) -> None:
        '''
        :param resource: -
        '''
        return typing.cast(None, jsii.invoke(self, "applyTag", [resource]))

    @jsii.member(jsii_name="visit")
    def visit(self, construct: "IConstruct") -> None:
        '''All aspects can visit an IConstruct.

        :param construct: -
        '''
        return typing.cast(None, jsii.invoke(self, "visit", [construct]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        '''The string key for the tag.'''
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def _props(self) -> "TagProps":
        return typing.cast("TagProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@aws-cdk/core.ResolveChangeContextOptions",
    jsii_struct_bases=[],
    name_mapping={"allow_intrinsic_keys": "allowIntrinsicKeys"},
)
class ResolveChangeContextOptions:
    def __init__(
        self,
        *,
        allow_intrinsic_keys: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options that can be changed while doing a recursive resolve.

        :param allow_intrinsic_keys: Change the 'allowIntrinsicKeys' option. Default: - Unchanged
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_intrinsic_keys is not None:
            self._values["allow_intrinsic_keys"] = allow_intrinsic_keys

    @builtins.property
    def allow_intrinsic_keys(self) -> typing.Optional[builtins.bool]:
        '''Change the 'allowIntrinsicKeys' option.

        :default: - Unchanged
        '''
        result = self._values.get("allow_intrinsic_keys")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResolveChangeContextOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.ResolveOptions",
    jsii_struct_bases=[],
    name_mapping={
        "resolver": "resolver",
        "scope": "scope",
        "preparing": "preparing",
        "remove_empty": "removeEmpty",
    },
)
class ResolveOptions:
    def __init__(
        self,
        *,
        resolver: ITokenResolver,
        scope: constructs.IConstruct,
        preparing: typing.Optional[builtins.bool] = None,
        remove_empty: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options to the resolve() operation.

        NOT the same as the ResolveContext; ResolveContext is exposed to Token
        implementors and resolution hooks, whereas this struct is just to bundle
        a number of things that would otherwise be arguments to resolve() in a
        readable way.

        :param resolver: The resolver to apply to any resolvable tokens found.
        :param scope: The scope from which resolution is performed.
        :param preparing: Whether the resolution is being executed during the prepare phase or not. Default: false
        :param remove_empty: Whether to remove undefined elements from arrays and objects when resolving. Default: true
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "resolver": resolver,
            "scope": scope,
        }
        if preparing is not None:
            self._values["preparing"] = preparing
        if remove_empty is not None:
            self._values["remove_empty"] = remove_empty

    @builtins.property
    def resolver(self) -> ITokenResolver:
        '''The resolver to apply to any resolvable tokens found.'''
        result = self._values.get("resolver")
        assert result is not None, "Required property 'resolver' is missing"
        return typing.cast(ITokenResolver, result)

    @builtins.property
    def scope(self) -> constructs.IConstruct:
        '''The scope from which resolution is performed.'''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(constructs.IConstruct, result)

    @builtins.property
    def preparing(self) -> typing.Optional[builtins.bool]:
        '''Whether the resolution is being executed during the prepare phase or not.

        :default: false
        '''
        result = self._values.get("preparing")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def remove_empty(self) -> typing.Optional[builtins.bool]:
        '''Whether to remove undefined elements from arrays and objects when resolving.

        :default: true
        '''
        result = self._values.get("remove_empty")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResolveOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.ResourceEnvironment",
    jsii_struct_bases=[],
    name_mapping={"account": "account", "region": "region"},
)
class ResourceEnvironment:
    def __init__(self, *, account: builtins.str, region: builtins.str) -> None:
        '''Represents the environment a given resource lives in.

        Used as the return value for the {@link IResource.env} property.

        :param account: The AWS account ID that this resource belongs to. Since this can be a Token (for example, when the account is CloudFormation's AWS::AccountId intrinsic), make sure to use Token.compareStrings() instead of just comparing the values for equality.
        :param region: The AWS region that this resource belongs to. Since this can be a Token (for example, when the region is CloudFormation's AWS::Region intrinsic), make sure to use Token.compareStrings() instead of just comparing the values for equality.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "account": account,
            "region": region,
        }

    @builtins.property
    def account(self) -> builtins.str:
        '''The AWS account ID that this resource belongs to.

        Since this can be a Token
        (for example, when the account is CloudFormation's AWS::AccountId intrinsic),
        make sure to use Token.compareStrings()
        instead of just comparing the values for equality.
        '''
        result = self._values.get("account")
        assert result is not None, "Required property 'account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''The AWS region that this resource belongs to.

        Since this can be a Token
        (for example, when the region is CloudFormation's AWS::Region intrinsic),
        make sure to use Token.compareStrings()
        instead of just comparing the values for equality.
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceEnvironment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.ResourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "account": "account",
        "environment_from_arn": "environmentFromArn",
        "physical_name": "physicalName",
        "region": "region",
    },
)
class ResourceProps:
    def __init__(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Construction properties for {@link Resource}.

        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if account is not None:
            self._values["account"] = account
        if environment_from_arn is not None:
            self._values["environment_from_arn"] = environment_from_arn
        if physical_name is not None:
            self._values["physical_name"] = physical_name
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def account(self) -> typing.Optional[builtins.str]:
        '''The AWS account ID this resource belongs to.

        :default: - the resource is in the same account as the stack it belongs to
        '''
        result = self._values.get("account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_from_arn(self) -> typing.Optional[builtins.str]:
        '''ARN to deduce region and account from.

        The ARN is parsed and the account and region are taken from the ARN.
        This should be used for imported resources.

        Cannot be supplied together with either ``account`` or ``region``.

        :default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        '''
        result = self._values.get("environment_from_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def physical_name(self) -> typing.Optional[builtins.str]:
        '''The value passed in by users to the physical name prop of the resource.

        - ``undefined`` implies that a physical name will be allocated by
          CloudFormation during deployment.
        - a concrete value implies a specific physical name
        - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated
          by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation.

        :default: - The physical name will be allocated by CloudFormation at deployment time
        '''
        result = self._values.get("physical_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The AWS region this resource belongs to.

        :default: - the resource is in the same region as the stack it belongs to
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.ReverseOptions",
    jsii_struct_bases=[],
    name_mapping={"fail_concat": "failConcat"},
)
class ReverseOptions:
    def __init__(self, *, fail_concat: typing.Optional[builtins.bool] = None) -> None:
        '''Options for the 'reverse()' operation.

        :param fail_concat: Fail if the given string is a concatenation. If ``false``, just return ``undefined``. Default: true
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if fail_concat is not None:
            self._values["fail_concat"] = fail_concat

    @builtins.property
    def fail_concat(self) -> typing.Optional[builtins.bool]:
        '''Fail if the given string is a concatenation.

        If ``false``, just return ``undefined``.

        :default: true
        '''
        result = self._values.get("fail_concat")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReverseOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ScopedAws(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.ScopedAws"):
    '''Accessor for scoped pseudo parameters.

    These pseudo parameters are anchored to a stack somewhere in the construct
    tree, and their values will be exported automatically.
    '''

    def __init__(self, scope: "Construct") -> None:
        '''
        :param scope: -
        '''
        jsii.create(ScopedAws, self, [scope])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="notificationArns")
    def notification_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notificationArns"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="partition")
    def partition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "partition"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stackId")
    def stack_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stackId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stackName")
    def stack_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stackName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="urlSuffix")
    def url_suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "urlSuffix"))


class SecretValue(
    Intrinsic,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.SecretValue",
):
    '''Work with secret values in the CDK.

    Secret values in the CDK (such as those retrieved from SecretsManager) are
    represented as regular strings, just like other values that are only
    available at deployment time.

    To help you avoid accidental mistakes which would lead to you putting your
    secret values directly into a CloudFormation template, constructs that take
    secret values will not allow you to pass in a literal secret value. They do
    so by calling ``Secret.assertSafeSecret()``.

    You can escape the check by calling ``Secret.plainText()``, but doing
    so is highly discouraged.
    '''

    def __init__(
        self,
        value: typing.Any,
        *,
        stack_trace: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param value: -
        :param stack_trace: Capture the stack trace of where this token is created. Default: true
        '''
        options = IntrinsicProps(stack_trace=stack_trace)

        jsii.create(SecretValue, self, [value, options])

    @jsii.member(jsii_name="cfnDynamicReference") # type: ignore[misc]
    @builtins.classmethod
    def cfn_dynamic_reference(cls, ref: "CfnDynamicReference") -> "SecretValue":
        '''Obtain the secret value through a CloudFormation dynamic reference.

        If possible, use ``SecretValue.ssmSecure`` or ``SecretValue.secretsManager`` directly.

        :param ref: The dynamic reference to use.
        '''
        return typing.cast("SecretValue", jsii.sinvoke(cls, "cfnDynamicReference", [ref]))

    @jsii.member(jsii_name="cfnParameter") # type: ignore[misc]
    @builtins.classmethod
    def cfn_parameter(cls, param: "CfnParameter") -> "SecretValue":
        '''Obtain the secret value through a CloudFormation parameter.

        Generally, this is not a recommended approach. AWS Secrets Manager is the
        recommended way to reference secrets.

        :param param: The CloudFormation parameter to use.
        '''
        return typing.cast("SecretValue", jsii.sinvoke(cls, "cfnParameter", [param]))

    @jsii.member(jsii_name="plainText") # type: ignore[misc]
    @builtins.classmethod
    def plain_text(cls, secret: builtins.str) -> "SecretValue":
        '''Construct a literal secret value for use with secret-aware constructs.

        *Do not use this method for any secrets that you care about.*

        The only reasonable use case for using this method is when you are testing.

        :param secret: -
        '''
        return typing.cast("SecretValue", jsii.sinvoke(cls, "plainText", [secret]))

    @jsii.member(jsii_name="secretsManager") # type: ignore[misc]
    @builtins.classmethod
    def secrets_manager(
        cls,
        secret_id: builtins.str,
        *,
        json_field: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
        version_stage: typing.Optional[builtins.str] = None,
    ) -> "SecretValue":
        '''Creates a ``SecretValue`` with a value which is dynamically loaded from AWS Secrets Manager.

        :param secret_id: The ID or ARN of the secret.
        :param json_field: The key of a JSON field to retrieve. This can only be used if the secret stores a JSON object. Default: - returns all the content stored in the Secrets Manager secret.
        :param version_id: Specifies the unique identifier of the version of the secret you want to use. Can specify at most one of ``versionId`` and ``versionStage``. Default: AWSCURRENT
        :param version_stage: Specifies the secret version that you want to retrieve by the staging label attached to the version. Can specify at most one of ``versionId`` and ``versionStage``. Default: AWSCURRENT
        '''
        options = SecretsManagerSecretOptions(
            json_field=json_field, version_id=version_id, version_stage=version_stage
        )

        return typing.cast("SecretValue", jsii.sinvoke(cls, "secretsManager", [secret_id, options]))

    @jsii.member(jsii_name="ssmSecure") # type: ignore[misc]
    @builtins.classmethod
    def ssm_secure(
        cls,
        parameter_name: builtins.str,
        version: builtins.str,
    ) -> "SecretValue":
        '''Use a secret value stored from a Systems Manager (SSM) parameter.

        :param parameter_name: The name of the parameter in the Systems Manager Parameter Store. The parameter name is case-sensitive.
        :param version: An integer that specifies the version of the parameter to use. You must specify the exact version. You cannot currently specify that AWS CloudFormation use the latest version of a parameter.
        '''
        return typing.cast("SecretValue", jsii.sinvoke(cls, "ssmSecure", [parameter_name, version]))


@jsii.data_type(
    jsii_type="@aws-cdk/core.SecretsManagerSecretOptions",
    jsii_struct_bases=[],
    name_mapping={
        "json_field": "jsonField",
        "version_id": "versionId",
        "version_stage": "versionStage",
    },
)
class SecretsManagerSecretOptions:
    def __init__(
        self,
        *,
        json_field: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
        version_stage: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for referencing a secret value from Secrets Manager.

        :param json_field: The key of a JSON field to retrieve. This can only be used if the secret stores a JSON object. Default: - returns all the content stored in the Secrets Manager secret.
        :param version_id: Specifies the unique identifier of the version of the secret you want to use. Can specify at most one of ``versionId`` and ``versionStage``. Default: AWSCURRENT
        :param version_stage: Specifies the secret version that you want to retrieve by the staging label attached to the version. Can specify at most one of ``versionId`` and ``versionStage``. Default: AWSCURRENT
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if json_field is not None:
            self._values["json_field"] = json_field
        if version_id is not None:
            self._values["version_id"] = version_id
        if version_stage is not None:
            self._values["version_stage"] = version_stage

    @builtins.property
    def json_field(self) -> typing.Optional[builtins.str]:
        '''The key of a JSON field to retrieve.

        This can only be used if the secret
        stores a JSON object.

        :default: - returns all the content stored in the Secrets Manager secret.
        '''
        result = self._values.get("json_field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_id(self) -> typing.Optional[builtins.str]:
        '''Specifies the unique identifier of the version of the secret you want to use.

        Can specify at most one of ``versionId`` and ``versionStage``.

        :default: AWSCURRENT
        '''
        result = self._values.get("version_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_stage(self) -> typing.Optional[builtins.str]:
        '''Specifies the secret version that you want to retrieve by the staging label attached to the version.

        Can specify at most one of ``versionId`` and ``versionStage``.

        :default: AWSCURRENT
        '''
        result = self._values.get("version_stage")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecretsManagerSecretOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Size(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.Size"):
    '''Represents the amount of digital storage.

    The amount can be specified either as a literal value (e.g: ``10``) which
    cannot be negative, or as an unresolved number token.

    When the amount is passed as a token, unit conversion is not possible.
    '''

    @jsii.member(jsii_name="gibibytes") # type: ignore[misc]
    @builtins.classmethod
    def gibibytes(cls, amount: jsii.Number) -> "Size":
        '''Create a Storage representing an amount gibibytes.

        1 GiB = 1024 MiB

        :param amount: the amount of gibibytes to be represented.

        :return: a new ``Size`` instance
        '''
        return typing.cast("Size", jsii.sinvoke(cls, "gibibytes", [amount]))

    @jsii.member(jsii_name="kibibytes") # type: ignore[misc]
    @builtins.classmethod
    def kibibytes(cls, amount: jsii.Number) -> "Size":
        '''Create a Storage representing an amount kibibytes.

        1 KiB = 1024 bytes

        :param amount: the amount of kibibytes to be represented.

        :return: a new ``Size`` instance
        '''
        return typing.cast("Size", jsii.sinvoke(cls, "kibibytes", [amount]))

    @jsii.member(jsii_name="mebibytes") # type: ignore[misc]
    @builtins.classmethod
    def mebibytes(cls, amount: jsii.Number) -> "Size":
        '''Create a Storage representing an amount mebibytes.

        1 MiB = 1024 KiB

        :param amount: the amount of mebibytes to be represented.

        :return: a new ``Size`` instance
        '''
        return typing.cast("Size", jsii.sinvoke(cls, "mebibytes", [amount]))

    @jsii.member(jsii_name="pebibyte") # type: ignore[misc]
    @builtins.classmethod
    def pebibyte(cls, amount: jsii.Number) -> "Size":
        '''(deprecated) Create a Storage representing an amount pebibytes.

        1 PiB = 1024 TiB

        :param amount: -

        :deprecated: use ``pebibytes`` instead

        :stability: deprecated
        '''
        return typing.cast("Size", jsii.sinvoke(cls, "pebibyte", [amount]))

    @jsii.member(jsii_name="pebibytes") # type: ignore[misc]
    @builtins.classmethod
    def pebibytes(cls, amount: jsii.Number) -> "Size":
        '''Create a Storage representing an amount pebibytes.

        1 PiB = 1024 TiB

        :param amount: the amount of pebibytes to be represented.

        :return: a new ``Size`` instance
        '''
        return typing.cast("Size", jsii.sinvoke(cls, "pebibytes", [amount]))

    @jsii.member(jsii_name="tebibytes") # type: ignore[misc]
    @builtins.classmethod
    def tebibytes(cls, amount: jsii.Number) -> "Size":
        '''Create a Storage representing an amount tebibytes.

        1 TiB = 1024 GiB

        :param amount: the amount of tebibytes to be represented.

        :return: a new ``Size`` instance
        '''
        return typing.cast("Size", jsii.sinvoke(cls, "tebibytes", [amount]))

    @jsii.member(jsii_name="toGibibytes")
    def to_gibibytes(
        self,
        *,
        rounding: typing.Optional["SizeRoundingBehavior"] = None,
    ) -> jsii.Number:
        '''Return this storage as a total number of gibibytes.

        :param rounding: How conversions should behave when it encounters a non-integer result. Default: SizeRoundingBehavior.FAIL

        :return: the quantity of bytes expressed in gibibytes
        '''
        opts = SizeConversionOptions(rounding=rounding)

        return typing.cast(jsii.Number, jsii.invoke(self, "toGibibytes", [opts]))

    @jsii.member(jsii_name="toKibibytes")
    def to_kibibytes(
        self,
        *,
        rounding: typing.Optional["SizeRoundingBehavior"] = None,
    ) -> jsii.Number:
        '''Return this storage as a total number of kibibytes.

        :param rounding: How conversions should behave when it encounters a non-integer result. Default: SizeRoundingBehavior.FAIL

        :return: the quantity of bytes expressed in kibibytes
        '''
        opts = SizeConversionOptions(rounding=rounding)

        return typing.cast(jsii.Number, jsii.invoke(self, "toKibibytes", [opts]))

    @jsii.member(jsii_name="toMebibytes")
    def to_mebibytes(
        self,
        *,
        rounding: typing.Optional["SizeRoundingBehavior"] = None,
    ) -> jsii.Number:
        '''Return this storage as a total number of mebibytes.

        :param rounding: How conversions should behave when it encounters a non-integer result. Default: SizeRoundingBehavior.FAIL

        :return: the quantity of bytes expressed in mebibytes
        '''
        opts = SizeConversionOptions(rounding=rounding)

        return typing.cast(jsii.Number, jsii.invoke(self, "toMebibytes", [opts]))

    @jsii.member(jsii_name="toPebibytes")
    def to_pebibytes(
        self,
        *,
        rounding: typing.Optional["SizeRoundingBehavior"] = None,
    ) -> jsii.Number:
        '''Return this storage as a total number of pebibytes.

        :param rounding: How conversions should behave when it encounters a non-integer result. Default: SizeRoundingBehavior.FAIL

        :return: the quantity of bytes expressed in pebibytes
        '''
        opts = SizeConversionOptions(rounding=rounding)

        return typing.cast(jsii.Number, jsii.invoke(self, "toPebibytes", [opts]))

    @jsii.member(jsii_name="toTebibytes")
    def to_tebibytes(
        self,
        *,
        rounding: typing.Optional["SizeRoundingBehavior"] = None,
    ) -> jsii.Number:
        '''Return this storage as a total number of tebibytes.

        :param rounding: How conversions should behave when it encounters a non-integer result. Default: SizeRoundingBehavior.FAIL

        :return: the quantity of bytes expressed in tebibytes
        '''
        opts = SizeConversionOptions(rounding=rounding)

        return typing.cast(jsii.Number, jsii.invoke(self, "toTebibytes", [opts]))


@jsii.data_type(
    jsii_type="@aws-cdk/core.SizeConversionOptions",
    jsii_struct_bases=[],
    name_mapping={"rounding": "rounding"},
)
class SizeConversionOptions:
    def __init__(
        self,
        *,
        rounding: typing.Optional["SizeRoundingBehavior"] = None,
    ) -> None:
        '''Options for how to convert time to a different unit.

        :param rounding: How conversions should behave when it encounters a non-integer result. Default: SizeRoundingBehavior.FAIL
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if rounding is not None:
            self._values["rounding"] = rounding

    @builtins.property
    def rounding(self) -> typing.Optional["SizeRoundingBehavior"]:
        '''How conversions should behave when it encounters a non-integer result.

        :default: SizeRoundingBehavior.FAIL
        '''
        result = self._values.get("rounding")
        return typing.cast(typing.Optional["SizeRoundingBehavior"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SizeConversionOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/core.SizeRoundingBehavior")
class SizeRoundingBehavior(enum.Enum):
    '''Rounding behaviour when converting between units of ``Size``.'''

    FAIL = "FAIL"
    '''Fail the conversion if the result is not an integer.'''
    FLOOR = "FLOOR"
    '''If the result is not an integer, round it to the closest integer less than the result.'''
    NONE = "NONE"
    '''Don't round.

    Return even if the result is a fraction.
    '''


@jsii.data_type(
    jsii_type="@aws-cdk/core.StackProps",
    jsii_struct_bases=[],
    name_mapping={
        "analytics_reporting": "analyticsReporting",
        "description": "description",
        "env": "env",
        "stack_name": "stackName",
        "synthesizer": "synthesizer",
        "tags": "tags",
        "termination_protection": "terminationProtection",
    },
)
class StackProps:
    def __init__(
        self,
        *,
        analytics_reporting: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        env: typing.Optional[Environment] = None,
        stack_name: typing.Optional[builtins.str] = None,
        synthesizer: typing.Optional[IStackSynthesizer] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_protection: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param analytics_reporting: Include runtime versioning information in this Stack. Default: ``analyticsReporting`` setting of containing ``App``, or value of 'aws:cdk:version-reporting' context key
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Set the ``region``/``account`` fields of ``env`` to either a concrete value to select the indicated environment (recommended for production stacks), or to the values of environment variables ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment depend on the AWS credentials/configuration that the CDK CLI is executed under (recommended for development stacks). If the ``Stack`` is instantiated inside a ``Stage``, any undefined ``region``/``account`` fields from ``env`` will default to the same field on the encompassing ``Stage``, if configured there. If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the Stack will be considered "*environment-agnostic*"". Environment-agnostic stacks can be deployed to any environment but may not be able to take advantage of all features of the CDK. For example, they will not be able to use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not automatically translate Service Principals to the right format based on the environment's AWS partition, and other such enhancements. Default: - The environment of the containing ``Stage`` if available, otherwise create the stack will be environment-agnostic.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param synthesizer: Synthesis method to use while deploying this stack. Default: - ``DefaultStackSynthesizer`` if the ``@aws-cdk/core:newStyleStackSynthesis`` feature flag is set, ``LegacyStackSynthesizer`` otherwise.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param termination_protection: Whether to enable termination protection for this stack. Default: false
        '''
        if isinstance(env, dict):
            env = Environment(**env)
        self._values: typing.Dict[str, typing.Any] = {}
        if analytics_reporting is not None:
            self._values["analytics_reporting"] = analytics_reporting
        if description is not None:
            self._values["description"] = description
        if env is not None:
            self._values["env"] = env
        if stack_name is not None:
            self._values["stack_name"] = stack_name
        if synthesizer is not None:
            self._values["synthesizer"] = synthesizer
        if tags is not None:
            self._values["tags"] = tags
        if termination_protection is not None:
            self._values["termination_protection"] = termination_protection

    @builtins.property
    def analytics_reporting(self) -> typing.Optional[builtins.bool]:
        '''Include runtime versioning information in this Stack.

        :default:

        ``analyticsReporting`` setting of containing ``App``, or value of
        'aws:cdk:version-reporting' context key
        '''
        result = self._values.get("analytics_reporting")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the stack.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def env(self) -> typing.Optional[Environment]:
        '''The AWS environment (account/region) where this stack will be deployed.

        Set the ``region``/``account`` fields of ``env`` to either a concrete value to
        select the indicated environment (recommended for production stacks), or to
        the values of environment variables
        ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment
        depend on the AWS credentials/configuration that the CDK CLI is executed
        under (recommended for development stacks).

        If the ``Stack`` is instantiated inside a ``Stage``, any undefined
        ``region``/``account`` fields from ``env`` will default to the same field on the
        encompassing ``Stage``, if configured there.

        If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the
        Stack will be considered "*environment-agnostic*"". Environment-agnostic
        stacks can be deployed to any environment but may not be able to take
        advantage of all features of the CDK. For example, they will not be able to
        use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not
        automatically translate Service Principals to the right format based on the
        environment's AWS partition, and other such enhancements.

        :default:

        - The environment of the containing ``Stage`` if available,
        otherwise create the stack will be environment-agnostic.

        Example::

            # Example automatically generated. See https://github.com/aws/jsii/issues/826
            # Use a concrete account and region to deploy this stack to:
            # `.account` and `.region` will simply return these values.
            Stack(app, "Stack1",
                env=Environment(
                    account="123456789012",
                    region="us-east-1"
                )
            )
            
            # Use the CLI's current credentials to determine the target environment:
            # `.account` and `.region` will reflect the account+region the CLI
            # is configured to use (based on the user CLI credentials)
            Stack(app, "Stack2",
                env=Environment(
                    account=process.env.CDK_DEFAULT_ACCOUNT,
                    region=process.env.CDK_DEFAULT_REGION
                )
            )
            
            # Define multiple stacks stage associated with an environment
            my_stage = Stage(app, "MyStage",
                env=Environment(
                    account="123456789012",
                    region="us-east-1"
                )
            )
            
            # both of these stacks will use the stage's account/region:
            # `.account` and `.region` will resolve to the concrete values as above
            MyStack(my_stage, "Stack1")
            YourStack(my_stage, "Stack2")
            
            # Define an environment-agnostic stack:
            # `.account` and `.region` will resolve to `{ "Ref": "AWS::AccountId" }` and `{ "Ref": "AWS::Region" }` respectively.
            # which will only resolve to actual values by CloudFormation during deployment.
            MyStack(app, "Stack1")
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[Environment], result)

    @builtins.property
    def stack_name(self) -> typing.Optional[builtins.str]:
        '''Name to deploy the stack with.

        :default: - Derived from construct path.
        '''
        result = self._values.get("stack_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def synthesizer(self) -> typing.Optional[IStackSynthesizer]:
        '''Synthesis method to use while deploying this stack.

        :default:

        - ``DefaultStackSynthesizer`` if the ``@aws-cdk/core:newStyleStackSynthesis`` feature flag
        is set, ``LegacyStackSynthesizer`` otherwise.
        '''
        result = self._values.get("synthesizer")
        return typing.cast(typing.Optional[IStackSynthesizer], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Stack tags that will be applied to all the taggable resources and the stack itself.

        :default: {}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def termination_protection(self) -> typing.Optional[builtins.bool]:
        '''Whether to enable termination protection for this stack.

        :default: false
        '''
        result = self._values.get("termination_protection")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IStackSynthesizer)
class StackSynthesizer(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/core.StackSynthesizer",
):
    '''Base class for implementing an IStackSynthesizer.

    This class needs to exist to provide public surface area for external
    implementations of stack synthesizers. The protected methods give
    access to functions that are otherwise @_internal to the framework
    and could not be accessed by external implementors.
    '''

    def __init__(self) -> None:
        jsii.create(StackSynthesizer, self, [])

    @jsii.member(jsii_name="addDockerImageAsset") # type: ignore[misc]
    @abc.abstractmethod
    def add_docker_image_asset(
        self,
        *,
        source_hash: builtins.str,
        directory_name: typing.Optional[builtins.str] = None,
        docker_build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        docker_build_target: typing.Optional[builtins.str] = None,
        docker_file: typing.Optional[builtins.str] = None,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        repository_name: typing.Optional[builtins.str] = None,
    ) -> DockerImageAssetLocation:
        '''Register a Docker Image Asset.

        Returns the parameters that can be used to refer to the asset inside the template.

        :param source_hash: The hash of the contents of the docker build context. This hash is used throughout the system to identify this image and avoid duplicate work in case the source did not change. NOTE: this means that if you wish to update your docker image, you must make a modification to the source (e.g. add some metadata to your Dockerfile).
        :param directory_name: The directory where the Dockerfile is stored, must be relative to the cloud assembly root. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param docker_build_args: Build args to pass to the ``docker build`` command. Since Docker build arguments are resolved before deployment, keys and values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or ``queue.queueUrl``). Only allowed when ``directoryName`` is specified. Default: - no build args are passed
        :param docker_build_target: Docker target to build to. Only allowed when ``directoryName`` is specified. Default: - no target
        :param docker_file: Path to the Dockerfile (relative to the directory). Only allowed when ``directoryName`` is specified. Default: - no file
        :param executable: An external command that will produce the packaged asset. The command should produce the name of a local Docker image on ``stdout``. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param repository_name: (deprecated) ECR repository name. Specify this property if you need to statically address the image, e.g. from a Kubernetes Pod. Note, this is only the repository name, without the registry and the tag parts. Default: - automatically derived from the asset's ID.
        '''
        ...

    @jsii.member(jsii_name="addFileAsset") # type: ignore[misc]
    @abc.abstractmethod
    def add_file_asset(
        self,
        *,
        source_hash: builtins.str,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_name: typing.Optional[builtins.str] = None,
        packaging: typing.Optional[FileAssetPackaging] = None,
    ) -> FileAssetLocation:
        '''Register a File Asset.

        Returns the parameters that can be used to refer to the asset inside the template.

        :param source_hash: A hash on the content source. This hash is used to uniquely identify this asset throughout the system. If this value doesn't change, the asset will not be rebuilt or republished.
        :param executable: An external command that will produce the packaged asset. The command should produce the location of a ZIP file on ``stdout``. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param file_name: The path, relative to the root of the cloud assembly, in which this asset source resides. This can be a path to a file or a directory, depending on the packaging type. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param packaging: Which type of packaging to perform. Default: - Required if ``fileName`` is specified.
        '''
        ...

    @jsii.member(jsii_name="bind") # type: ignore[misc]
    @abc.abstractmethod
    def bind(self, stack: "Stack") -> None:
        '''Bind to the stack this environment is going to be used on.

        Must be called before any of the other methods are called.

        :param stack: -
        '''
        ...

    @jsii.member(jsii_name="emitStackArtifact")
    def _emit_stack_artifact(
        self,
        stack: "Stack",
        session: ISynthesisSession,
        *,
        additional_dependencies: typing.Optional[typing.Sequence[builtins.str]] = None,
        assume_role_arn: typing.Optional[builtins.str] = None,
        bootstrap_stack_version_ssm_parameter: typing.Optional[builtins.str] = None,
        cloud_formation_execution_role_arn: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        requires_bootstrap_stack_version: typing.Optional[jsii.Number] = None,
        stack_template_asset_object_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Write the stack artifact to the session.

        Use default settings to add a CloudFormationStackArtifact artifact to
        the given synthesis session.

        :param stack: -
        :param session: -
        :param additional_dependencies: Identifiers of additional dependencies. Default: - No additional dependencies
        :param assume_role_arn: The role that needs to be assumed to deploy the stack. Default: - No role is assumed (current credentials are used)
        :param bootstrap_stack_version_ssm_parameter: SSM parameter where the bootstrap stack version number can be found. Only used if ``requiresBootstrapStackVersion`` is set. - If this value is not set, the bootstrap stack name must be known at deployment time so the stack version can be looked up from the stack outputs. - If this value is set, the bootstrap stack can have any name because we won't need to look it up. Default: - Bootstrap stack version number looked up
        :param cloud_formation_execution_role_arn: The role that is passed to CloudFormation to execute the change set. Default: - No role is passed (currently assumed role/credentials are used)
        :param parameters: Values for CloudFormation stack parameters that should be passed when the stack is deployed. Default: - No parameters
        :param requires_bootstrap_stack_version: Version of bootstrap stack required to deploy this stack. Default: - No bootstrap stack required
        :param stack_template_asset_object_url: If the stack template has already been included in the asset manifest, its asset URL. Default: - Not uploaded yet, upload just before deploying
        '''
        options = SynthesizeStackArtifactOptions(
            additional_dependencies=additional_dependencies,
            assume_role_arn=assume_role_arn,
            bootstrap_stack_version_ssm_parameter=bootstrap_stack_version_ssm_parameter,
            cloud_formation_execution_role_arn=cloud_formation_execution_role_arn,
            parameters=parameters,
            requires_bootstrap_stack_version=requires_bootstrap_stack_version,
            stack_template_asset_object_url=stack_template_asset_object_url,
        )

        return typing.cast(None, jsii.invoke(self, "emitStackArtifact", [stack, session, options]))

    @jsii.member(jsii_name="synthesize") # type: ignore[misc]
    @abc.abstractmethod
    def synthesize(self, session: ISynthesisSession) -> None:
        '''Synthesize the associated stack to the session.

        :param session: -
        '''
        ...

    @jsii.member(jsii_name="synthesizeStackTemplate")
    def _synthesize_stack_template(
        self,
        stack: "Stack",
        session: ISynthesisSession,
    ) -> None:
        '''Have the stack write out its template.

        :param stack: -
        :param session: -
        '''
        return typing.cast(None, jsii.invoke(self, "synthesizeStackTemplate", [stack, session]))


class _StackSynthesizerProxy(StackSynthesizer):
    @jsii.member(jsii_name="addDockerImageAsset")
    def add_docker_image_asset(
        self,
        *,
        source_hash: builtins.str,
        directory_name: typing.Optional[builtins.str] = None,
        docker_build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        docker_build_target: typing.Optional[builtins.str] = None,
        docker_file: typing.Optional[builtins.str] = None,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        repository_name: typing.Optional[builtins.str] = None,
    ) -> DockerImageAssetLocation:
        '''Register a Docker Image Asset.

        Returns the parameters that can be used to refer to the asset inside the template.

        :param source_hash: The hash of the contents of the docker build context. This hash is used throughout the system to identify this image and avoid duplicate work in case the source did not change. NOTE: this means that if you wish to update your docker image, you must make a modification to the source (e.g. add some metadata to your Dockerfile).
        :param directory_name: The directory where the Dockerfile is stored, must be relative to the cloud assembly root. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param docker_build_args: Build args to pass to the ``docker build`` command. Since Docker build arguments are resolved before deployment, keys and values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or ``queue.queueUrl``). Only allowed when ``directoryName`` is specified. Default: - no build args are passed
        :param docker_build_target: Docker target to build to. Only allowed when ``directoryName`` is specified. Default: - no target
        :param docker_file: Path to the Dockerfile (relative to the directory). Only allowed when ``directoryName`` is specified. Default: - no file
        :param executable: An external command that will produce the packaged asset. The command should produce the name of a local Docker image on ``stdout``. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param repository_name: (deprecated) ECR repository name. Specify this property if you need to statically address the image, e.g. from a Kubernetes Pod. Note, this is only the repository name, without the registry and the tag parts. Default: - automatically derived from the asset's ID.
        '''
        asset = DockerImageAssetSource(
            source_hash=source_hash,
            directory_name=directory_name,
            docker_build_args=docker_build_args,
            docker_build_target=docker_build_target,
            docker_file=docker_file,
            executable=executable,
            repository_name=repository_name,
        )

        return typing.cast(DockerImageAssetLocation, jsii.invoke(self, "addDockerImageAsset", [asset]))

    @jsii.member(jsii_name="addFileAsset")
    def add_file_asset(
        self,
        *,
        source_hash: builtins.str,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_name: typing.Optional[builtins.str] = None,
        packaging: typing.Optional[FileAssetPackaging] = None,
    ) -> FileAssetLocation:
        '''Register a File Asset.

        Returns the parameters that can be used to refer to the asset inside the template.

        :param source_hash: A hash on the content source. This hash is used to uniquely identify this asset throughout the system. If this value doesn't change, the asset will not be rebuilt or republished.
        :param executable: An external command that will produce the packaged asset. The command should produce the location of a ZIP file on ``stdout``. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param file_name: The path, relative to the root of the cloud assembly, in which this asset source resides. This can be a path to a file or a directory, depending on the packaging type. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param packaging: Which type of packaging to perform. Default: - Required if ``fileName`` is specified.
        '''
        asset = FileAssetSource(
            source_hash=source_hash,
            executable=executable,
            file_name=file_name,
            packaging=packaging,
        )

        return typing.cast(FileAssetLocation, jsii.invoke(self, "addFileAsset", [asset]))

    @jsii.member(jsii_name="bind")
    def bind(self, stack: "Stack") -> None:
        '''Bind to the stack this environment is going to be used on.

        Must be called before any of the other methods are called.

        :param stack: -
        '''
        return typing.cast(None, jsii.invoke(self, "bind", [stack]))

    @jsii.member(jsii_name="synthesize")
    def synthesize(self, session: ISynthesisSession) -> None:
        '''Synthesize the associated stack to the session.

        :param session: -
        '''
        return typing.cast(None, jsii.invoke(self, "synthesize", [session]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, StackSynthesizer).__jsii_proxy_class__ = lambda : _StackSynthesizerProxy


@jsii.data_type(
    jsii_type="@aws-cdk/core.StageProps",
    jsii_struct_bases=[],
    name_mapping={"env": "env", "outdir": "outdir"},
)
class StageProps:
    def __init__(
        self,
        *,
        env: typing.Optional[Environment] = None,
        outdir: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Initialization props for a stage.

        :param env: Default AWS environment (account/region) for ``Stack``s in this ``Stage``. Stacks defined inside this ``Stage`` with either ``region`` or ``account`` missing from its env will use the corresponding field given here. If either ``region`` or ``account``is is not configured for ``Stack`` (either on the ``Stack`` itself or on the containing ``Stage``), the Stack will be *environment-agnostic*. Environment-agnostic stacks can be deployed to any environment, may not be able to take advantage of all features of the CDK. For example, they will not be able to use environmental context lookups, will not automatically translate Service Principals to the right format based on the environment's AWS partition, and other such enhancements. Default: - The environments should be configured on the ``Stack``s.
        :param outdir: The output directory into which to emit synthesized artifacts. Can only be specified if this stage is the root stage (the app). If this is specified and this stage is nested within another stage, an error will be thrown. Default: - for nested stages, outdir will be determined as a relative directory to the outdir of the app. For apps, if outdir is not specified, a temporary directory will be created.
        '''
        if isinstance(env, dict):
            env = Environment(**env)
        self._values: typing.Dict[str, typing.Any] = {}
        if env is not None:
            self._values["env"] = env
        if outdir is not None:
            self._values["outdir"] = outdir

    @builtins.property
    def env(self) -> typing.Optional[Environment]:
        '''Default AWS environment (account/region) for ``Stack``s in this ``Stage``.

        Stacks defined inside this ``Stage`` with either ``region`` or ``account`` missing
        from its env will use the corresponding field given here.

        If either ``region`` or ``account``is is not configured for ``Stack`` (either on
        the ``Stack`` itself or on the containing ``Stage``), the Stack will be
        *environment-agnostic*.

        Environment-agnostic stacks can be deployed to any environment, may not be
        able to take advantage of all features of the CDK. For example, they will
        not be able to use environmental context lookups, will not automatically
        translate Service Principals to the right format based on the environment's
        AWS partition, and other such enhancements.

        :default: - The environments should be configured on the ``Stack``s.

        Example::

            # Example automatically generated. See https://github.com/aws/jsii/issues/826
            # Use a concrete account and region to deploy this Stage to
            Stage(app, "Stage1",
                env=Environment(account="123456789012", region="us-east-1")
            )
            
            # Use the CLI's current credentials to determine the target environment
            Stage(app, "Stage2",
                env=Environment(account=process.env.CDK_DEFAULT_ACCOUNT, region=process.env.CDK_DEFAULT_REGION)
            )
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[Environment], result)

    @builtins.property
    def outdir(self) -> typing.Optional[builtins.str]:
        '''The output directory into which to emit synthesized artifacts.

        Can only be specified if this stage is the root stage (the app). If this is
        specified and this stage is nested within another stage, an error will be
        thrown.

        :default:

        - for nested stages, outdir will be determined as a relative
        directory to the outdir of the app. For apps, if outdir is not specified, a
        temporary directory will be created.
        '''
        result = self._values.get("outdir")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StageProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.StageSynthesisOptions",
    jsii_struct_bases=[],
    name_mapping={
        "force": "force",
        "skip_validation": "skipValidation",
        "validate_on_synthesis": "validateOnSynthesis",
    },
)
class StageSynthesisOptions:
    def __init__(
        self,
        *,
        force: typing.Optional[builtins.bool] = None,
        skip_validation: typing.Optional[builtins.bool] = None,
        validate_on_synthesis: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options for assembly synthesis.

        :param force: Force a re-synth, even if the stage has already been synthesized. This is used by tests to allow for incremental verification of the output. Do not use in production. Default: false
        :param skip_validation: Should we skip construct validation. Default: - false
        :param validate_on_synthesis: Whether the stack should be validated after synthesis to check for error metadata. Default: - false
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if force is not None:
            self._values["force"] = force
        if skip_validation is not None:
            self._values["skip_validation"] = skip_validation
        if validate_on_synthesis is not None:
            self._values["validate_on_synthesis"] = validate_on_synthesis

    @builtins.property
    def force(self) -> typing.Optional[builtins.bool]:
        '''Force a re-synth, even if the stage has already been synthesized.

        This is used by tests to allow for incremental verification of the output.
        Do not use in production.

        :default: false
        '''
        result = self._values.get("force")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def skip_validation(self) -> typing.Optional[builtins.bool]:
        '''Should we skip construct validation.

        :default: - false
        '''
        result = self._values.get("skip_validation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def validate_on_synthesis(self) -> typing.Optional[builtins.bool]:
        '''Whether the stack should be validated after synthesis to check for error metadata.

        :default: - false
        '''
        result = self._values.get("validate_on_synthesis")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StageSynthesisOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IFragmentConcatenator)
class StringConcat(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.StringConcat"):
    '''Converts all fragments to strings and concats those.

    Drops 'undefined's.
    '''

    def __init__(self) -> None:
        jsii.create(StringConcat, self, [])

    @jsii.member(jsii_name="join")
    def join(self, left: typing.Any, right: typing.Any) -> typing.Any:
        '''Join the fragment on the left and on the right.

        :param left: -
        :param right: -
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "join", [left, right]))


@jsii.enum(jsii_type="@aws-cdk/core.SymlinkFollowMode")
class SymlinkFollowMode(enum.Enum):
    '''Determines how symlinks are followed.'''

    NEVER = "NEVER"
    '''Never follow symlinks.'''
    ALWAYS = "ALWAYS"
    '''Materialize all symlinks, whether they are internal or external to the source directory.'''
    EXTERNAL = "EXTERNAL"
    '''Only follows symlinks that are external to the source directory.'''
    BLOCK_EXTERNAL = "BLOCK_EXTERNAL"
    '''Forbids source from having any symlinks pointing outside of the source tree.

    This is the safest mode of operation as it ensures that copy operations
    won't materialize files from the user's file system. Internal symlinks are
    not followed.

    If the copy operation runs into an external symlink, it will fail.
    '''


@jsii.data_type(
    jsii_type="@aws-cdk/core.SynthesisOptions",
    jsii_struct_bases=[aws_cdk.cx_api.AssemblyBuildOptions],
    name_mapping={
        "runtime_info": "runtimeInfo",
        "outdir": "outdir",
        "skip_validation": "skipValidation",
        "validate_on_synthesis": "validateOnSynthesis",
    },
)
class SynthesisOptions(aws_cdk.cx_api.AssemblyBuildOptions):
    def __init__(
        self,
        *,
        runtime_info: typing.Optional[aws_cdk.cx_api.RuntimeInfo] = None,
        outdir: typing.Optional[builtins.str] = None,
        skip_validation: typing.Optional[builtins.bool] = None,
        validate_on_synthesis: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(deprecated) Options for synthesis.

        :param runtime_info: (deprecated) Include the specified runtime information (module versions) in manifest. Default: - if this option is not specified, runtime info will not be included
        :param outdir: (deprecated) The output directory into which to synthesize the cloud assembly. Default: - creates a temporary directory
        :param skip_validation: (deprecated) Whether synthesis should skip the validation phase. Default: false
        :param validate_on_synthesis: (deprecated) Whether the stack should be validated after synthesis to check for error metadata. Default: - false

        :deprecated: use ``app.synth()`` or ``stage.synth()`` instead

        :stability: deprecated
        '''
        if isinstance(runtime_info, dict):
            runtime_info = aws_cdk.cx_api.RuntimeInfo(**runtime_info)
        self._values: typing.Dict[str, typing.Any] = {}
        if runtime_info is not None:
            self._values["runtime_info"] = runtime_info
        if outdir is not None:
            self._values["outdir"] = outdir
        if skip_validation is not None:
            self._values["skip_validation"] = skip_validation
        if validate_on_synthesis is not None:
            self._values["validate_on_synthesis"] = validate_on_synthesis

    @builtins.property
    def runtime_info(self) -> typing.Optional[aws_cdk.cx_api.RuntimeInfo]:
        '''(deprecated) Include the specified runtime information (module versions) in manifest.

        :default: - if this option is not specified, runtime info will not be included

        :deprecated:

        All template modifications that should result from this should
        have already been inserted into the template.

        :stability: deprecated
        '''
        result = self._values.get("runtime_info")
        return typing.cast(typing.Optional[aws_cdk.cx_api.RuntimeInfo], result)

    @builtins.property
    def outdir(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The output directory into which to synthesize the cloud assembly.

        :default: - creates a temporary directory

        :stability: deprecated
        '''
        result = self._values.get("outdir")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_validation(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Whether synthesis should skip the validation phase.

        :default: false

        :stability: deprecated
        '''
        result = self._values.get("skip_validation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def validate_on_synthesis(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Whether the stack should be validated after synthesis to check for error metadata.

        :default: - false

        :stability: deprecated
        '''
        result = self._values.get("validate_on_synthesis")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SynthesisOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.SynthesizeStackArtifactOptions",
    jsii_struct_bases=[],
    name_mapping={
        "additional_dependencies": "additionalDependencies",
        "assume_role_arn": "assumeRoleArn",
        "bootstrap_stack_version_ssm_parameter": "bootstrapStackVersionSsmParameter",
        "cloud_formation_execution_role_arn": "cloudFormationExecutionRoleArn",
        "parameters": "parameters",
        "requires_bootstrap_stack_version": "requiresBootstrapStackVersion",
        "stack_template_asset_object_url": "stackTemplateAssetObjectUrl",
    },
)
class SynthesizeStackArtifactOptions:
    def __init__(
        self,
        *,
        additional_dependencies: typing.Optional[typing.Sequence[builtins.str]] = None,
        assume_role_arn: typing.Optional[builtins.str] = None,
        bootstrap_stack_version_ssm_parameter: typing.Optional[builtins.str] = None,
        cloud_formation_execution_role_arn: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        requires_bootstrap_stack_version: typing.Optional[jsii.Number] = None,
        stack_template_asset_object_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Stack artifact options.

        A subset of ``cxschema.AwsCloudFormationStackProperties`` of optional settings that need to be
        configurable by synthesizers, plus ``additionalDependencies``.

        :param additional_dependencies: Identifiers of additional dependencies. Default: - No additional dependencies
        :param assume_role_arn: The role that needs to be assumed to deploy the stack. Default: - No role is assumed (current credentials are used)
        :param bootstrap_stack_version_ssm_parameter: SSM parameter where the bootstrap stack version number can be found. Only used if ``requiresBootstrapStackVersion`` is set. - If this value is not set, the bootstrap stack name must be known at deployment time so the stack version can be looked up from the stack outputs. - If this value is set, the bootstrap stack can have any name because we won't need to look it up. Default: - Bootstrap stack version number looked up
        :param cloud_formation_execution_role_arn: The role that is passed to CloudFormation to execute the change set. Default: - No role is passed (currently assumed role/credentials are used)
        :param parameters: Values for CloudFormation stack parameters that should be passed when the stack is deployed. Default: - No parameters
        :param requires_bootstrap_stack_version: Version of bootstrap stack required to deploy this stack. Default: - No bootstrap stack required
        :param stack_template_asset_object_url: If the stack template has already been included in the asset manifest, its asset URL. Default: - Not uploaded yet, upload just before deploying
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if additional_dependencies is not None:
            self._values["additional_dependencies"] = additional_dependencies
        if assume_role_arn is not None:
            self._values["assume_role_arn"] = assume_role_arn
        if bootstrap_stack_version_ssm_parameter is not None:
            self._values["bootstrap_stack_version_ssm_parameter"] = bootstrap_stack_version_ssm_parameter
        if cloud_formation_execution_role_arn is not None:
            self._values["cloud_formation_execution_role_arn"] = cloud_formation_execution_role_arn
        if parameters is not None:
            self._values["parameters"] = parameters
        if requires_bootstrap_stack_version is not None:
            self._values["requires_bootstrap_stack_version"] = requires_bootstrap_stack_version
        if stack_template_asset_object_url is not None:
            self._values["stack_template_asset_object_url"] = stack_template_asset_object_url

    @builtins.property
    def additional_dependencies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Identifiers of additional dependencies.

        :default: - No additional dependencies
        '''
        result = self._values.get("additional_dependencies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def assume_role_arn(self) -> typing.Optional[builtins.str]:
        '''The role that needs to be assumed to deploy the stack.

        :default: - No role is assumed (current credentials are used)
        '''
        result = self._values.get("assume_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bootstrap_stack_version_ssm_parameter(self) -> typing.Optional[builtins.str]:
        '''SSM parameter where the bootstrap stack version number can be found.

        Only used if ``requiresBootstrapStackVersion`` is set.

        - If this value is not set, the bootstrap stack name must be known at
          deployment time so the stack version can be looked up from the stack
          outputs.
        - If this value is set, the bootstrap stack can have any name because
          we won't need to look it up.

        :default: - Bootstrap stack version number looked up
        '''
        result = self._values.get("bootstrap_stack_version_ssm_parameter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_formation_execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The role that is passed to CloudFormation to execute the change set.

        :default: - No role is passed (currently assumed role/credentials are used)
        '''
        result = self._values.get("cloud_formation_execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Values for CloudFormation stack parameters that should be passed when the stack is deployed.

        :default: - No parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def requires_bootstrap_stack_version(self) -> typing.Optional[jsii.Number]:
        '''Version of bootstrap stack required to deploy this stack.

        :default: - No bootstrap stack required
        '''
        result = self._values.get("requires_bootstrap_stack_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def stack_template_asset_object_url(self) -> typing.Optional[builtins.str]:
        '''If the stack template has already been included in the asset manifest, its asset URL.

        :default: - Not uploaded yet, upload just before deploying
        '''
        result = self._values.get("stack_template_asset_object_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SynthesizeStackArtifactOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IAspect)
class Tag(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.Tag"):
    '''The Tag Aspect will handle adding a tag to this node and cascading tags to children.'''

    def __init__(
        self,
        key: builtins.str,
        value: builtins.str,
        *,
        apply_to_launched_instances: typing.Optional[builtins.bool] = None,
        exclude_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        include_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        priority: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param key: -
        :param value: -
        :param apply_to_launched_instances: Whether the tag should be applied to instances in an AutoScalingGroup. Default: true
        :param exclude_resource_types: An array of Resource Types that will not receive this tag. An empty array will allow this tag to be applied to all resources. A non-empty array will apply this tag only if the Resource type is not in this array. Default: []
        :param include_resource_types: An array of Resource Types that will receive this tag. An empty array will match any Resource. A non-empty array will apply this tag only to Resource types that are included in this array. Default: []
        :param priority: Priority of the tag operation. Higher or equal priority tags will take precedence. Setting priority will enable the user to control tags when they need to not follow the default precedence pattern of last applied and closest to the construct in the tree. Default: Default priorities: - 100 for {@link SetTag} - 200 for {@link RemoveTag} - 50 for tags added directly to CloudFormation resources
        '''
        props = TagProps(
            apply_to_launched_instances=apply_to_launched_instances,
            exclude_resource_types=exclude_resource_types,
            include_resource_types=include_resource_types,
            priority=priority,
        )

        jsii.create(Tag, self, [key, value, props])

    @jsii.member(jsii_name="add") # type: ignore[misc]
    @builtins.classmethod
    def add(
        cls,
        scope: "Construct",
        key: builtins.str,
        value: builtins.str,
        *,
        apply_to_launched_instances: typing.Optional[builtins.bool] = None,
        exclude_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        include_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        priority: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(deprecated) DEPRECATED: add tags to the node of a construct and all its the taggable children.

        :param scope: -
        :param key: -
        :param value: -
        :param apply_to_launched_instances: Whether the tag should be applied to instances in an AutoScalingGroup. Default: true
        :param exclude_resource_types: An array of Resource Types that will not receive this tag. An empty array will allow this tag to be applied to all resources. A non-empty array will apply this tag only if the Resource type is not in this array. Default: []
        :param include_resource_types: An array of Resource Types that will receive this tag. An empty array will match any Resource. A non-empty array will apply this tag only to Resource types that are included in this array. Default: []
        :param priority: Priority of the tag operation. Higher or equal priority tags will take precedence. Setting priority will enable the user to control tags when they need to not follow the default precedence pattern of last applied and closest to the construct in the tree. Default: Default priorities: - 100 for {@link SetTag} - 200 for {@link RemoveTag} - 50 for tags added directly to CloudFormation resources

        :deprecated: use ``Tags.of(scope).add()``

        :stability: deprecated
        '''
        props = TagProps(
            apply_to_launched_instances=apply_to_launched_instances,
            exclude_resource_types=exclude_resource_types,
            include_resource_types=include_resource_types,
            priority=priority,
        )

        return typing.cast(None, jsii.sinvoke(cls, "add", [scope, key, value, props]))

    @jsii.member(jsii_name="remove") # type: ignore[misc]
    @builtins.classmethod
    def remove(
        cls,
        scope: "Construct",
        key: builtins.str,
        *,
        apply_to_launched_instances: typing.Optional[builtins.bool] = None,
        exclude_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        include_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        priority: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(deprecated) DEPRECATED: remove tags to the node of a construct and all its the taggable children.

        :param scope: -
        :param key: -
        :param apply_to_launched_instances: Whether the tag should be applied to instances in an AutoScalingGroup. Default: true
        :param exclude_resource_types: An array of Resource Types that will not receive this tag. An empty array will allow this tag to be applied to all resources. A non-empty array will apply this tag only if the Resource type is not in this array. Default: []
        :param include_resource_types: An array of Resource Types that will receive this tag. An empty array will match any Resource. A non-empty array will apply this tag only to Resource types that are included in this array. Default: []
        :param priority: Priority of the tag operation. Higher or equal priority tags will take precedence. Setting priority will enable the user to control tags when they need to not follow the default precedence pattern of last applied and closest to the construct in the tree. Default: Default priorities: - 100 for {@link SetTag} - 200 for {@link RemoveTag} - 50 for tags added directly to CloudFormation resources

        :deprecated: use ``Tags.of(scope).remove()``

        :stability: deprecated
        '''
        props = TagProps(
            apply_to_launched_instances=apply_to_launched_instances,
            exclude_resource_types=exclude_resource_types,
            include_resource_types=include_resource_types,
            priority=priority,
        )

        return typing.cast(None, jsii.sinvoke(cls, "remove", [scope, key, props]))

    @jsii.member(jsii_name="applyTag")
    def _apply_tag(self, resource: ITaggable) -> None:
        '''
        :param resource: -
        '''
        return typing.cast(None, jsii.invoke(self, "applyTag", [resource]))

    @jsii.member(jsii_name="visit")
    def visit(self, construct: "IConstruct") -> None:
        '''All aspects can visit an IConstruct.

        :param construct: -
        '''
        return typing.cast(None, jsii.invoke(self, "visit", [construct]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        '''The string key for the tag.'''
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def _props(self) -> "TagProps":
        return typing.cast("TagProps", jsii.get(self, "props"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        '''The string value of the tag.'''
        return typing.cast(builtins.str, jsii.get(self, "value"))


class TagManager(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.TagManager"):
    '''TagManager facilitates a common implementation of tagging for Constructs.'''

    def __init__(
        self,
        tag_type: "TagType",
        resource_type_name: builtins.str,
        tag_structure: typing.Any = None,
        *,
        tag_property_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param tag_type: -
        :param resource_type_name: -
        :param tag_structure: -
        :param tag_property_name: The name of the property in CloudFormation for these tags. Normally this is ``tags``, but Cognito UserPool uses UserPoolTags Default: "tags"
        '''
        options = TagManagerOptions(tag_property_name=tag_property_name)

        jsii.create(TagManager, self, [tag_type, resource_type_name, tag_structure, options])

    @jsii.member(jsii_name="isTaggable") # type: ignore[misc]
    @builtins.classmethod
    def is_taggable(cls, construct: typing.Any) -> builtins.bool:
        '''Check whether the given construct is Taggable.

        :param construct: -
        '''
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isTaggable", [construct]))

    @jsii.member(jsii_name="applyTagAspectHere")
    def apply_tag_aspect_here(
        self,
        include: typing.Optional[typing.Sequence[builtins.str]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> builtins.bool:
        '''Determine if the aspect applies here.

        Looks at the include and exclude resourceTypeName arrays to determine if
        the aspect applies here

        :param include: -
        :param exclude: -
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "applyTagAspectHere", [include, exclude]))

    @jsii.member(jsii_name="hasTags")
    def has_tags(self) -> builtins.bool:
        '''Returns true if there are any tags defined.'''
        return typing.cast(builtins.bool, jsii.invoke(self, "hasTags", []))

    @jsii.member(jsii_name="removeTag")
    def remove_tag(self, key: builtins.str, priority: jsii.Number) -> None:
        '''Removes the specified tag from the array if it exists.

        :param key: The tag to remove.
        :param priority: The priority of the remove operation.
        '''
        return typing.cast(None, jsii.invoke(self, "removeTag", [key, priority]))

    @jsii.member(jsii_name="renderTags")
    def render_tags(self) -> typing.Any:
        '''Renders tags into the proper format based on TagType.'''
        return typing.cast(typing.Any, jsii.invoke(self, "renderTags", []))

    @jsii.member(jsii_name="setTag")
    def set_tag(
        self,
        key: builtins.str,
        value: builtins.str,
        priority: typing.Optional[jsii.Number] = None,
        apply_to_launched_instances: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Adds the specified tag to the array of tags.

        :param key: -
        :param value: -
        :param priority: -
        :param apply_to_launched_instances: -
        '''
        return typing.cast(None, jsii.invoke(self, "setTag", [key, value, priority, apply_to_launched_instances]))

    @jsii.member(jsii_name="tagValues")
    def tag_values(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Render the tags in a readable format.'''
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.invoke(self, "tagValues", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tagPropertyName")
    def tag_property_name(self) -> builtins.str:
        '''The property name for tag values.

        Normally this is ``tags`` but some resources choose a different name. Cognito
        UserPool uses UserPoolTags
        '''
        return typing.cast(builtins.str, jsii.get(self, "tagPropertyName"))


@jsii.data_type(
    jsii_type="@aws-cdk/core.TagManagerOptions",
    jsii_struct_bases=[],
    name_mapping={"tag_property_name": "tagPropertyName"},
)
class TagManagerOptions:
    def __init__(
        self,
        *,
        tag_property_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options to configure TagManager behavior.

        :param tag_property_name: The name of the property in CloudFormation for these tags. Normally this is ``tags``, but Cognito UserPool uses UserPoolTags Default: "tags"
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if tag_property_name is not None:
            self._values["tag_property_name"] = tag_property_name

    @builtins.property
    def tag_property_name(self) -> typing.Optional[builtins.str]:
        '''The name of the property in CloudFormation for these tags.

        Normally this is ``tags``, but Cognito UserPool uses UserPoolTags

        :default: "tags"
        '''
        result = self._values.get("tag_property_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagManagerOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/core.TagProps",
    jsii_struct_bases=[],
    name_mapping={
        "apply_to_launched_instances": "applyToLaunchedInstances",
        "exclude_resource_types": "excludeResourceTypes",
        "include_resource_types": "includeResourceTypes",
        "priority": "priority",
    },
)
class TagProps:
    def __init__(
        self,
        *,
        apply_to_launched_instances: typing.Optional[builtins.bool] = None,
        exclude_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        include_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        priority: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for a tag.

        :param apply_to_launched_instances: Whether the tag should be applied to instances in an AutoScalingGroup. Default: true
        :param exclude_resource_types: An array of Resource Types that will not receive this tag. An empty array will allow this tag to be applied to all resources. A non-empty array will apply this tag only if the Resource type is not in this array. Default: []
        :param include_resource_types: An array of Resource Types that will receive this tag. An empty array will match any Resource. A non-empty array will apply this tag only to Resource types that are included in this array. Default: []
        :param priority: Priority of the tag operation. Higher or equal priority tags will take precedence. Setting priority will enable the user to control tags when they need to not follow the default precedence pattern of last applied and closest to the construct in the tree. Default: Default priorities: - 100 for {@link SetTag} - 200 for {@link RemoveTag} - 50 for tags added directly to CloudFormation resources
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if apply_to_launched_instances is not None:
            self._values["apply_to_launched_instances"] = apply_to_launched_instances
        if exclude_resource_types is not None:
            self._values["exclude_resource_types"] = exclude_resource_types
        if include_resource_types is not None:
            self._values["include_resource_types"] = include_resource_types
        if priority is not None:
            self._values["priority"] = priority

    @builtins.property
    def apply_to_launched_instances(self) -> typing.Optional[builtins.bool]:
        '''Whether the tag should be applied to instances in an AutoScalingGroup.

        :default: true
        '''
        result = self._values.get("apply_to_launched_instances")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def exclude_resource_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of Resource Types that will not receive this tag.

        An empty array will allow this tag to be applied to all resources. A
        non-empty array will apply this tag only if the Resource type is not in
        this array.

        :default: []
        '''
        result = self._values.get("exclude_resource_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def include_resource_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of Resource Types that will receive this tag.

        An empty array will match any Resource. A non-empty array will apply this
        tag only to Resource types that are included in this array.

        :default: []
        '''
        result = self._values.get("include_resource_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Priority of the tag operation.

        Higher or equal priority tags will take precedence.

        Setting priority will enable the user to control tags when they need to not
        follow the default precedence pattern of last applied and closest to the
        construct in the tree.

        :default:

        Default priorities:

        - 100 for {@link SetTag}
        - 200 for {@link RemoveTag}
        - 50 for tags added directly to CloudFormation resources
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/core.TagType")
class TagType(enum.Enum):
    STANDARD = "STANDARD"
    AUTOSCALING_GROUP = "AUTOSCALING_GROUP"
    MAP = "MAP"
    KEY_VALUE = "KEY_VALUE"
    NOT_TAGGABLE = "NOT_TAGGABLE"


class Tags(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.Tags"):
    '''Manages AWS tags for all resources within a construct scope.'''

    @jsii.member(jsii_name="of") # type: ignore[misc]
    @builtins.classmethod
    def of(cls, scope: "IConstruct") -> "Tags":
        '''Returns the tags API for this scope.

        :param scope: The scope.
        '''
        return typing.cast("Tags", jsii.sinvoke(cls, "of", [scope]))

    @jsii.member(jsii_name="add")
    def add(
        self,
        key: builtins.str,
        value: builtins.str,
        *,
        apply_to_launched_instances: typing.Optional[builtins.bool] = None,
        exclude_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        include_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        priority: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''add tags to the node of a construct and all its the taggable children.

        :param key: -
        :param value: -
        :param apply_to_launched_instances: Whether the tag should be applied to instances in an AutoScalingGroup. Default: true
        :param exclude_resource_types: An array of Resource Types that will not receive this tag. An empty array will allow this tag to be applied to all resources. A non-empty array will apply this tag only if the Resource type is not in this array. Default: []
        :param include_resource_types: An array of Resource Types that will receive this tag. An empty array will match any Resource. A non-empty array will apply this tag only to Resource types that are included in this array. Default: []
        :param priority: Priority of the tag operation. Higher or equal priority tags will take precedence. Setting priority will enable the user to control tags when they need to not follow the default precedence pattern of last applied and closest to the construct in the tree. Default: Default priorities: - 100 for {@link SetTag} - 200 for {@link RemoveTag} - 50 for tags added directly to CloudFormation resources
        '''
        props = TagProps(
            apply_to_launched_instances=apply_to_launched_instances,
            exclude_resource_types=exclude_resource_types,
            include_resource_types=include_resource_types,
            priority=priority,
        )

        return typing.cast(None, jsii.invoke(self, "add", [key, value, props]))

    @jsii.member(jsii_name="remove")
    def remove(
        self,
        key: builtins.str,
        *,
        apply_to_launched_instances: typing.Optional[builtins.bool] = None,
        exclude_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        include_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        priority: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''remove tags to the node of a construct and all its the taggable children.

        :param key: -
        :param apply_to_launched_instances: Whether the tag should be applied to instances in an AutoScalingGroup. Default: true
        :param exclude_resource_types: An array of Resource Types that will not receive this tag. An empty array will allow this tag to be applied to all resources. A non-empty array will apply this tag only if the Resource type is not in this array. Default: []
        :param include_resource_types: An array of Resource Types that will receive this tag. An empty array will match any Resource. A non-empty array will apply this tag only to Resource types that are included in this array. Default: []
        :param priority: Priority of the tag operation. Higher or equal priority tags will take precedence. Setting priority will enable the user to control tags when they need to not follow the default precedence pattern of last applied and closest to the construct in the tree. Default: Default priorities: - 100 for {@link SetTag} - 200 for {@link RemoveTag} - 50 for tags added directly to CloudFormation resources
        '''
        props = TagProps(
            apply_to_launched_instances=apply_to_launched_instances,
            exclude_resource_types=exclude_resource_types,
            include_resource_types=include_resource_types,
            priority=priority,
        )

        return typing.cast(None, jsii.invoke(self, "remove", [key, props]))


@jsii.data_type(
    jsii_type="@aws-cdk/core.TimeConversionOptions",
    jsii_struct_bases=[],
    name_mapping={"integral": "integral"},
)
class TimeConversionOptions:
    def __init__(self, *, integral: typing.Optional[builtins.bool] = None) -> None:
        '''Options for how to convert time to a different unit.

        :param integral: If ``true``, conversions into a larger time unit (e.g. ``Seconds`` to ``Minutes``) will fail if the result is not an integer. Default: true
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if integral is not None:
            self._values["integral"] = integral

    @builtins.property
    def integral(self) -> typing.Optional[builtins.bool]:
        '''If ``true``, conversions into a larger time unit (e.g. ``Seconds`` to ``Minutes``) will fail if the result is not an integer.

        :default: true
        '''
        result = self._values.get("integral")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TimeConversionOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Token(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.Token"):
    '''Represents a special or lazily-evaluated value.

    Can be used to delay evaluation of a certain value in case, for example,
    that it requires some context or late-bound data. Can also be used to
    mark values that need special processing at document rendering time.

    Tokens can be embedded into strings while retaining their original
    semantics.
    '''

    @jsii.member(jsii_name="asAny") # type: ignore[misc]
    @builtins.classmethod
    def as_any(cls, value: typing.Any) -> IResolvable:
        '''Return a resolvable representation of the given value.

        :param value: -
        '''
        return typing.cast(IResolvable, jsii.sinvoke(cls, "asAny", [value]))

    @jsii.member(jsii_name="asList") # type: ignore[misc]
    @builtins.classmethod
    def as_list(
        cls,
        value: typing.Any,
        *,
        display_hint: typing.Optional[builtins.str] = None,
    ) -> typing.List[builtins.str]:
        '''Return a reversible list representation of this token.

        :param value: -
        :param display_hint: A hint for the Token's purpose when stringifying it.
        '''
        options = EncodingOptions(display_hint=display_hint)

        return typing.cast(typing.List[builtins.str], jsii.sinvoke(cls, "asList", [value, options]))

    @jsii.member(jsii_name="asNumber") # type: ignore[misc]
    @builtins.classmethod
    def as_number(cls, value: typing.Any) -> jsii.Number:
        '''Return a reversible number representation of this token.

        :param value: -
        '''
        return typing.cast(jsii.Number, jsii.sinvoke(cls, "asNumber", [value]))

    @jsii.member(jsii_name="asString") # type: ignore[misc]
    @builtins.classmethod
    def as_string(
        cls,
        value: typing.Any,
        *,
        display_hint: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''Return a reversible string representation of this token.

        If the Token is initialized with a literal, the stringified value of the
        literal is returned. Otherwise, a special quoted string representation
        of the Token is returned that can be embedded into other strings.

        Strings with quoted Tokens in them can be restored back into
        complex values with the Tokens restored by calling ``resolve()``
        on the string.

        :param value: -
        :param display_hint: A hint for the Token's purpose when stringifying it.
        '''
        options = EncodingOptions(display_hint=display_hint)

        return typing.cast(builtins.str, jsii.sinvoke(cls, "asString", [value, options]))

    @jsii.member(jsii_name="compareStrings") # type: ignore[misc]
    @builtins.classmethod
    def compare_strings(
        cls,
        possible_token1: builtins.str,
        possible_token2: builtins.str,
    ) -> "TokenComparison":
        '''Compare two strings that might contain Tokens with each other.

        :param possible_token1: -
        :param possible_token2: -
        '''
        return typing.cast("TokenComparison", jsii.sinvoke(cls, "compareStrings", [possible_token1, possible_token2]))

    @jsii.member(jsii_name="isUnresolved") # type: ignore[misc]
    @builtins.classmethod
    def is_unresolved(cls, obj: typing.Any) -> builtins.bool:
        '''Returns true if obj represents an unresolved value.

        One of these must be true:

        - ``obj`` is an IResolvable
        - ``obj`` is a string containing at least one encoded ``IResolvable``
        - ``obj`` is either an encoded number or list

        This does NOT recurse into lists or objects to see if they
        containing resolvables.

        :param obj: The object to test.
        '''
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isUnresolved", [obj]))


class TokenComparison(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.TokenComparison",
):
    '''An enum-like class that represents the result of comparing two Tokens.

    The return type of {@link Token.compareStrings}.
    '''

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="BOTH_UNRESOLVED")
    def BOTH_UNRESOLVED(cls) -> "TokenComparison":
        '''This means both components are Tokens.'''
        return typing.cast("TokenComparison", jsii.sget(cls, "BOTH_UNRESOLVED"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="DIFFERENT")
    def DIFFERENT(cls) -> "TokenComparison":
        '''This means we're certain the two components are NOT Tokens, and different.'''
        return typing.cast("TokenComparison", jsii.sget(cls, "DIFFERENT"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="ONE_UNRESOLVED")
    def ONE_UNRESOLVED(cls) -> "TokenComparison":
        '''This means exactly one of the components is a Token.'''
        return typing.cast("TokenComparison", jsii.sget(cls, "ONE_UNRESOLVED"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="SAME")
    def SAME(cls) -> "TokenComparison":
        '''This means we're certain the two components are NOT Tokens, and identical.'''
        return typing.cast("TokenComparison", jsii.sget(cls, "SAME"))


class Tokenization(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.Tokenization"):
    '''Less oft-needed functions to manipulate Tokens.'''

    @jsii.member(jsii_name="isResolvable") # type: ignore[misc]
    @builtins.classmethod
    def is_resolvable(cls, obj: typing.Any) -> builtins.bool:
        '''Return whether the given object is an IResolvable object.

        This is different from Token.isUnresolved() which will also check for
        encoded Tokens, whereas this method will only do a type check on the given
        object.

        :param obj: -
        '''
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isResolvable", [obj]))

    @jsii.member(jsii_name="resolve") # type: ignore[misc]
    @builtins.classmethod
    def resolve(
        cls,
        obj: typing.Any,
        *,
        resolver: ITokenResolver,
        scope: constructs.IConstruct,
        preparing: typing.Optional[builtins.bool] = None,
        remove_empty: typing.Optional[builtins.bool] = None,
    ) -> typing.Any:
        '''Resolves an object by evaluating all tokens and removing any undefined or empty objects or arrays.

        Values can only be primitives, arrays or tokens. Other objects (i.e. with methods) will be rejected.

        :param obj: The object to resolve.
        :param resolver: The resolver to apply to any resolvable tokens found.
        :param scope: The scope from which resolution is performed.
        :param preparing: Whether the resolution is being executed during the prepare phase or not. Default: false
        :param remove_empty: Whether to remove undefined elements from arrays and objects when resolving. Default: true
        '''
        options = ResolveOptions(
            resolver=resolver,
            scope=scope,
            preparing=preparing,
            remove_empty=remove_empty,
        )

        return typing.cast(typing.Any, jsii.sinvoke(cls, "resolve", [obj, options]))

    @jsii.member(jsii_name="reverse") # type: ignore[misc]
    @builtins.classmethod
    def reverse(
        cls,
        x: typing.Any,
        *,
        fail_concat: typing.Optional[builtins.bool] = None,
    ) -> typing.Optional[IResolvable]:
        '''Reverse any value into a Resolvable, if possible.

        In case of a string, the string must not be a concatenation.

        :param x: -
        :param fail_concat: Fail if the given string is a concatenation. If ``false``, just return ``undefined``. Default: true
        '''
        options = ReverseOptions(fail_concat=fail_concat)

        return typing.cast(typing.Optional[IResolvable], jsii.sinvoke(cls, "reverse", [x, options]))

    @jsii.member(jsii_name="reverseCompleteString") # type: ignore[misc]
    @builtins.classmethod
    def reverse_complete_string(cls, s: builtins.str) -> typing.Optional[IResolvable]:
        '''Un-encode a string which is either a complete encoded token, or doesn't contain tokens at all.

        It's illegal for the string to be a concatenation of an encoded token and something else.

        :param s: -
        '''
        return typing.cast(typing.Optional[IResolvable], jsii.sinvoke(cls, "reverseCompleteString", [s]))

    @jsii.member(jsii_name="reverseList") # type: ignore[misc]
    @builtins.classmethod
    def reverse_list(
        cls,
        l: typing.Sequence[builtins.str],
    ) -> typing.Optional[IResolvable]:
        '''Un-encode a Tokenized value from a list.

        :param l: -
        '''
        return typing.cast(typing.Optional[IResolvable], jsii.sinvoke(cls, "reverseList", [l]))

    @jsii.member(jsii_name="reverseNumber") # type: ignore[misc]
    @builtins.classmethod
    def reverse_number(cls, n: jsii.Number) -> typing.Optional[IResolvable]:
        '''Un-encode a Tokenized value from a number.

        :param n: -
        '''
        return typing.cast(typing.Optional[IResolvable], jsii.sinvoke(cls, "reverseNumber", [n]))

    @jsii.member(jsii_name="reverseString") # type: ignore[misc]
    @builtins.classmethod
    def reverse_string(cls, s: builtins.str) -> "TokenizedStringFragments":
        '''Un-encode a string potentially containing encoded tokens.

        :param s: -
        '''
        return typing.cast("TokenizedStringFragments", jsii.sinvoke(cls, "reverseString", [s]))

    @jsii.member(jsii_name="stringifyNumber") # type: ignore[misc]
    @builtins.classmethod
    def stringify_number(cls, x: jsii.Number) -> builtins.str:
        '''Stringify a number directly or lazily if it's a Token.

        If it is an object (i.e., { Ref: 'SomeLogicalId' }), return it as-is.

        :param x: -
        '''
        return typing.cast(builtins.str, jsii.sinvoke(cls, "stringifyNumber", [x]))


class TokenizedStringFragments(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.TokenizedStringFragments",
):
    '''Fragments of a concatenated string containing stringified Tokens.'''

    def __init__(self) -> None:
        jsii.create(TokenizedStringFragments, self, [])

    @jsii.member(jsii_name="addIntrinsic")
    def add_intrinsic(self, value: typing.Any) -> None:
        '''
        :param value: -
        '''
        return typing.cast(None, jsii.invoke(self, "addIntrinsic", [value]))

    @jsii.member(jsii_name="addLiteral")
    def add_literal(self, lit: typing.Any) -> None:
        '''
        :param lit: -
        '''
        return typing.cast(None, jsii.invoke(self, "addLiteral", [lit]))

    @jsii.member(jsii_name="addToken")
    def add_token(self, token: IResolvable) -> None:
        '''
        :param token: -
        '''
        return typing.cast(None, jsii.invoke(self, "addToken", [token]))

    @jsii.member(jsii_name="join")
    def join(self, concat: IFragmentConcatenator) -> typing.Any:
        '''Combine the string fragments using the given joiner.

        If there are any

        :param concat: -
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "join", [concat]))

    @jsii.member(jsii_name="mapTokens")
    def map_tokens(self, mapper: ITokenMapper) -> "TokenizedStringFragments":
        '''Apply a transformation function to all tokens in the string.

        :param mapper: -
        '''
        return typing.cast("TokenizedStringFragments", jsii.invoke(self, "mapTokens", [mapper]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firstValue")
    def first_value(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "firstValue"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="length")
    def length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "length"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tokens")
    def tokens(self) -> typing.List[IResolvable]:
        '''Return all Tokens from this string.'''
        return typing.cast(typing.List[IResolvable], jsii.get(self, "tokens"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="firstToken")
    def first_token(self) -> typing.Optional[IResolvable]:
        return typing.cast(typing.Optional[IResolvable], jsii.get(self, "firstToken"))


class TreeInspector(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.TreeInspector"):
    '''Inspector that maintains an attribute bag.'''

    def __init__(self) -> None:
        jsii.create(TreeInspector, self, [])

    @jsii.member(jsii_name="addAttribute")
    def add_attribute(self, key: builtins.str, value: typing.Any) -> None:
        '''Adds attribute to bag.

        Keys should be added by convention to prevent conflicts
        i.e. L1 constructs will contain attributes with keys prefixed with aws:cdk:cloudformation

        :param key: - key for metadata.
        :param value: - value of metadata.
        '''
        return typing.cast(None, jsii.invoke(self, "addAttribute", [key, value]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''Represents the bag of attributes as key-value pairs.'''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "attributes"))


@jsii.data_type(
    jsii_type="@aws-cdk/core.ValidationError",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "source": "source"},
)
class ValidationError:
    def __init__(self, *, message: builtins.str, source: "Construct") -> None:
        '''An error returned during the validation phase.

        :param message: The error message.
        :param source: The construct which emitted the error.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "message": message,
            "source": source,
        }

    @builtins.property
    def message(self) -> builtins.str:
        '''The error message.'''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> "Construct":
        '''The construct which emitted the error.'''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast("Construct", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ValidationError(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ValidationResult(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.ValidationResult",
):
    '''Representation of validation results.

    Models a tree of validation errors so that we have as much information as possible
    about the failure that occurred.
    '''

    def __init__(
        self,
        error_message: typing.Optional[builtins.str] = None,
        results: typing.Optional["ValidationResults"] = None,
    ) -> None:
        '''
        :param error_message: -
        :param results: -
        '''
        jsii.create(ValidationResult, self, [error_message, results])

    @jsii.member(jsii_name="assertSuccess")
    def assert_success(self) -> None:
        '''Turn a failed validation into an exception.'''
        return typing.cast(None, jsii.invoke(self, "assertSuccess", []))

    @jsii.member(jsii_name="errorTree")
    def error_tree(self) -> builtins.str:
        '''Return a string rendering of the tree of validation failures.'''
        return typing.cast(builtins.str, jsii.invoke(self, "errorTree", []))

    @jsii.member(jsii_name="prefix")
    def prefix(self, message: builtins.str) -> "ValidationResult":
        '''Wrap this result with an error message, if it concerns an error.

        :param message: -
        '''
        return typing.cast("ValidationResult", jsii.invoke(self, "prefix", [message]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="errorMessage")
    def error_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorMessage"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="isSuccess")
    def is_success(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "isSuccess"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="results")
    def results(self) -> "ValidationResults":
        return typing.cast("ValidationResults", jsii.get(self, "results"))


class ValidationResults(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.ValidationResults",
):
    '''A collection of validation results.'''

    def __init__(
        self,
        results: typing.Optional[typing.Sequence[ValidationResult]] = None,
    ) -> None:
        '''
        :param results: -
        '''
        jsii.create(ValidationResults, self, [results])

    @jsii.member(jsii_name="collect")
    def collect(self, result: ValidationResult) -> None:
        '''
        :param result: -
        '''
        return typing.cast(None, jsii.invoke(self, "collect", [result]))

    @jsii.member(jsii_name="errorTreeList")
    def error_tree_list(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "errorTreeList", []))

    @jsii.member(jsii_name="wrap")
    def wrap(self, message: builtins.str) -> ValidationResult:
        '''Wrap up all validation results into a single tree node.

        If there are failures in the collection, add a message, otherwise
        return a success.

        :param message: -
        '''
        return typing.cast(ValidationResult, jsii.invoke(self, "wrap", [message]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="isSuccess")
    def is_success(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "isSuccess"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="results")
    def results(self) -> typing.List[ValidationResult]:
        return typing.cast(typing.List[ValidationResult], jsii.get(self, "results"))

    @results.setter
    def results(self, value: typing.List[ValidationResult]) -> None:
        jsii.set(self, "results", value)


@jsii.data_type(
    jsii_type="@aws-cdk/core.AssetStagingProps",
    jsii_struct_bases=[FingerprintOptions, AssetOptions],
    name_mapping={
        "exclude": "exclude",
        "follow": "follow",
        "ignore_mode": "ignoreMode",
        "extra_hash": "extraHash",
        "asset_hash": "assetHash",
        "asset_hash_type": "assetHashType",
        "bundling": "bundling",
        "source_path": "sourcePath",
    },
)
class AssetStagingProps(FingerprintOptions, AssetOptions):
    def __init__(
        self,
        *,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow: typing.Optional[SymlinkFollowMode] = None,
        ignore_mode: typing.Optional[IgnoreMode] = None,
        extra_hash: typing.Optional[builtins.str] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[AssetHashType] = None,
        bundling: typing.Optional[BundlingOptions] = None,
        source_path: builtins.str,
    ) -> None:
        '''Initialization properties for ``AssetStaging``.

        :param exclude: Glob patterns to exclude from the copy. Default: - nothing is excluded
        :param follow: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for exclude patterns. Default: IgnoreMode.GLOB
        :param extra_hash: Extra information to encode into the fingerprint (e.g. build instructions and other inputs). Default: - hash is only based on source content
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container or a custom bundling provider. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        :param source_path: The source file or directory to copy from.
        '''
        if isinstance(bundling, dict):
            bundling = BundlingOptions(**bundling)
        self._values: typing.Dict[str, typing.Any] = {
            "source_path": source_path,
        }
        if exclude is not None:
            self._values["exclude"] = exclude
        if follow is not None:
            self._values["follow"] = follow
        if ignore_mode is not None:
            self._values["ignore_mode"] = ignore_mode
        if extra_hash is not None:
            self._values["extra_hash"] = extra_hash
        if asset_hash is not None:
            self._values["asset_hash"] = asset_hash
        if asset_hash_type is not None:
            self._values["asset_hash_type"] = asset_hash_type
        if bundling is not None:
            self._values["bundling"] = bundling

    @builtins.property
    def exclude(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Glob patterns to exclude from the copy.

        :default: - nothing is excluded
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def follow(self) -> typing.Optional[SymlinkFollowMode]:
        '''A strategy for how to handle symlinks.

        :default: SymlinkFollowMode.NEVER
        '''
        result = self._values.get("follow")
        return typing.cast(typing.Optional[SymlinkFollowMode], result)

    @builtins.property
    def ignore_mode(self) -> typing.Optional[IgnoreMode]:
        '''The ignore behavior to use for exclude patterns.

        :default: IgnoreMode.GLOB
        '''
        result = self._values.get("ignore_mode")
        return typing.cast(typing.Optional[IgnoreMode], result)

    @builtins.property
    def extra_hash(self) -> typing.Optional[builtins.str]:
        '''Extra information to encode into the fingerprint (e.g. build instructions and other inputs).

        :default: - hash is only based on source content
        '''
        result = self._values.get("extra_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def asset_hash(self) -> typing.Optional[builtins.str]:
        '''Specify a custom hash for this asset.

        If ``assetHashType`` is set it must
        be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will
        be SHA256 hashed and encoded as hex. The resulting hash will be the asset
        hash.

        NOTE: the hash is used in order to identify a specific revision of the asset, and
        used for optimizing and caching deployment activities related to this asset such as
        packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will
        need to make sure it is updated every time the asset changes, or otherwise it is
        possible that some deployments will not be invalidated.

        :default: - based on ``assetHashType``
        '''
        result = self._values.get("asset_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def asset_hash_type(self) -> typing.Optional[AssetHashType]:
        '''Specifies the type of hash to calculate for this asset.

        If ``assetHash`` is configured, this option must be ``undefined`` or
        ``AssetHashType.CUSTOM``.

        :default:

        - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is
        explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        '''
        result = self._values.get("asset_hash_type")
        return typing.cast(typing.Optional[AssetHashType], result)

    @builtins.property
    def bundling(self) -> typing.Optional[BundlingOptions]:
        '''Bundle the asset by executing a command in a Docker container or a custom bundling provider.

        The asset path will be mounted at ``/asset-input``. The Docker
        container is responsible for putting content at ``/asset-output``.
        The content at ``/asset-output`` will be zipped and used as the
        final asset.

        :default:

        - uploaded as-is to S3 if the asset is a regular file or a .zip file,
        archived into a .zip file and uploaded to S3 otherwise
        '''
        result = self._values.get("bundling")
        return typing.cast(typing.Optional[BundlingOptions], result)

    @builtins.property
    def source_path(self) -> builtins.str:
        '''The source file or directory to copy from.'''
        result = self._values.get("source_path")
        assert result is not None, "Required property 'source_path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssetStagingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CfnDynamicReference(
    Intrinsic,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnDynamicReference",
):
    '''References a dynamically retrieved value.

    This is a Construct so that subclasses will (eventually) be able to attach
    metadata to themselves without having to change call signatures.

    :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html
    '''

    def __init__(self, service: CfnDynamicReferenceService, key: builtins.str) -> None:
        '''
        :param service: -
        :param key: -
        '''
        jsii.create(CfnDynamicReference, self, [service, key])


@jsii.implements(IDependable)
class ConcreteDependable(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.ConcreteDependable",
):
    '''A set of constructs to be used as a dependable.

    This class can be used when a set of constructs which are disjoint in the
    construct tree needs to be combined to be used as a single dependable.
    '''

    def __init__(self) -> None:
        jsii.create(ConcreteDependable, self, [])

    @jsii.member(jsii_name="add")
    def add(self, construct: "IConstruct") -> None:
        '''Add a construct to the dependency roots.

        :param construct: -
        '''
        return typing.cast(None, jsii.invoke(self, "add", [construct]))


class DefaultStackSynthesizer(
    StackSynthesizer,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.DefaultStackSynthesizer",
):
    '''Uses conventionally named roles and reify asset storage locations.

    This synthesizer is the only StackSynthesizer that generates
    an asset manifest, and is required to deploy CDK applications using the
    ``@aws-cdk/app-delivery`` CI/CD library.

    Requires the environment to have been bootstrapped with Bootstrap Stack V2.
    '''

    def __init__(
        self,
        *,
        bootstrap_stack_version_ssm_parameter: typing.Optional[builtins.str] = None,
        bucket_prefix: typing.Optional[builtins.str] = None,
        cloud_formation_execution_role: typing.Optional[builtins.str] = None,
        deploy_role_arn: typing.Optional[builtins.str] = None,
        file_asset_key_arn_export_name: typing.Optional[builtins.str] = None,
        file_asset_publishing_external_id: typing.Optional[builtins.str] = None,
        file_asset_publishing_role_arn: typing.Optional[builtins.str] = None,
        file_assets_bucket_name: typing.Optional[builtins.str] = None,
        generate_bootstrap_version_rule: typing.Optional[builtins.bool] = None,
        image_asset_publishing_external_id: typing.Optional[builtins.str] = None,
        image_asset_publishing_role_arn: typing.Optional[builtins.str] = None,
        image_assets_repository_name: typing.Optional[builtins.str] = None,
        lookup_role_arn: typing.Optional[builtins.str] = None,
        qualifier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bootstrap_stack_version_ssm_parameter: Bootstrap stack version SSM parameter. The placeholder ``${Qualifier}`` will be replaced with the value of qualifier. Default: DefaultStackSynthesizer.DEFAULT_BOOTSTRAP_STACK_VERSION_SSM_PARAMETER
        :param bucket_prefix: bucketPrefix to use while storing S3 Assets. Default: - DefaultStackSynthesizer.DEFAULT_FILE_ASSET_PREFIX
        :param cloud_formation_execution_role: The role CloudFormation will assume when deploying the Stack. You must supply this if you have given a non-standard name to the execution role. The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: DefaultStackSynthesizer.DEFAULT_CLOUDFORMATION_ROLE_ARN
        :param deploy_role_arn: The role to assume to initiate a deployment in this environment. You must supply this if you have given a non-standard name to the publishing role. The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: DefaultStackSynthesizer.DEFAULT_DEPLOY_ROLE_ARN
        :param file_asset_key_arn_export_name: (deprecated) Name of the CloudFormation Export with the asset key name. You must supply this if you have given a non-standard name to the KMS key export The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: DefaultStackSynthesizer.DEFAULT_FILE_ASSET_KEY_ARN_EXPORT_NAME
        :param file_asset_publishing_external_id: External ID to use when assuming role for file asset publishing. Default: - No external ID
        :param file_asset_publishing_role_arn: The role to use to publish file assets to the S3 bucket in this environment. You must supply this if you have given a non-standard name to the publishing role. The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: DefaultStackSynthesizer.DEFAULT_FILE_ASSET_PUBLISHING_ROLE_ARN
        :param file_assets_bucket_name: Name of the S3 bucket to hold file assets. You must supply this if you have given a non-standard name to the staging bucket. The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: DefaultStackSynthesizer.DEFAULT_FILE_ASSETS_BUCKET_NAME
        :param generate_bootstrap_version_rule: Whether to add a Rule to the stack template verifying the bootstrap stack version. This generally should be left set to ``true``, unless you explicitly want to be able to deploy to an unbootstrapped environment. Default: true
        :param image_asset_publishing_external_id: External ID to use when assuming role for image asset publishing. Default: - No external ID
        :param image_asset_publishing_role_arn: The role to use to publish image assets to the ECR repository in this environment. You must supply this if you have given a non-standard name to the publishing role. The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: DefaultStackSynthesizer.DEFAULT_IMAGE_ASSET_PUBLISHING_ROLE_ARN
        :param image_assets_repository_name: Name of the ECR repository to hold Docker Image assets. You must supply this if you have given a non-standard name to the ECR repository. The placeholders ``${Qualifier}``, ``${AWS::AccountId}`` and ``${AWS::Region}`` will be replaced with the values of qualifier and the stack's account and region, respectively. Default: DefaultStackSynthesizer.DEFAULT_IMAGE_ASSETS_REPOSITORY_NAME
        :param lookup_role_arn: The role to use to look up values from the target AWS account during synthesis. Default: - None
        :param qualifier: Qualifier to disambiguate multiple environments in the same account. You can use this and leave the other naming properties empty if you have deployed the bootstrap environment with standard names but only differnet qualifiers. Default: - Value of context key '
        '''
        props = DefaultStackSynthesizerProps(
            bootstrap_stack_version_ssm_parameter=bootstrap_stack_version_ssm_parameter,
            bucket_prefix=bucket_prefix,
            cloud_formation_execution_role=cloud_formation_execution_role,
            deploy_role_arn=deploy_role_arn,
            file_asset_key_arn_export_name=file_asset_key_arn_export_name,
            file_asset_publishing_external_id=file_asset_publishing_external_id,
            file_asset_publishing_role_arn=file_asset_publishing_role_arn,
            file_assets_bucket_name=file_assets_bucket_name,
            generate_bootstrap_version_rule=generate_bootstrap_version_rule,
            image_asset_publishing_external_id=image_asset_publishing_external_id,
            image_asset_publishing_role_arn=image_asset_publishing_role_arn,
            image_assets_repository_name=image_assets_repository_name,
            lookup_role_arn=lookup_role_arn,
            qualifier=qualifier,
        )

        jsii.create(DefaultStackSynthesizer, self, [props])

    @jsii.member(jsii_name="addDockerImageAsset")
    def add_docker_image_asset(
        self,
        *,
        source_hash: builtins.str,
        directory_name: typing.Optional[builtins.str] = None,
        docker_build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        docker_build_target: typing.Optional[builtins.str] = None,
        docker_file: typing.Optional[builtins.str] = None,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        repository_name: typing.Optional[builtins.str] = None,
    ) -> DockerImageAssetLocation:
        '''Register a Docker Image Asset.

        Returns the parameters that can be used to refer to the asset inside the template.

        :param source_hash: The hash of the contents of the docker build context. This hash is used throughout the system to identify this image and avoid duplicate work in case the source did not change. NOTE: this means that if you wish to update your docker image, you must make a modification to the source (e.g. add some metadata to your Dockerfile).
        :param directory_name: The directory where the Dockerfile is stored, must be relative to the cloud assembly root. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param docker_build_args: Build args to pass to the ``docker build`` command. Since Docker build arguments are resolved before deployment, keys and values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or ``queue.queueUrl``). Only allowed when ``directoryName`` is specified. Default: - no build args are passed
        :param docker_build_target: Docker target to build to. Only allowed when ``directoryName`` is specified. Default: - no target
        :param docker_file: Path to the Dockerfile (relative to the directory). Only allowed when ``directoryName`` is specified. Default: - no file
        :param executable: An external command that will produce the packaged asset. The command should produce the name of a local Docker image on ``stdout``. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param repository_name: (deprecated) ECR repository name. Specify this property if you need to statically address the image, e.g. from a Kubernetes Pod. Note, this is only the repository name, without the registry and the tag parts. Default: - automatically derived from the asset's ID.
        '''
        asset = DockerImageAssetSource(
            source_hash=source_hash,
            directory_name=directory_name,
            docker_build_args=docker_build_args,
            docker_build_target=docker_build_target,
            docker_file=docker_file,
            executable=executable,
            repository_name=repository_name,
        )

        return typing.cast(DockerImageAssetLocation, jsii.invoke(self, "addDockerImageAsset", [asset]))

    @jsii.member(jsii_name="addFileAsset")
    def add_file_asset(
        self,
        *,
        source_hash: builtins.str,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_name: typing.Optional[builtins.str] = None,
        packaging: typing.Optional[FileAssetPackaging] = None,
    ) -> FileAssetLocation:
        '''Register a File Asset.

        Returns the parameters that can be used to refer to the asset inside the template.

        :param source_hash: A hash on the content source. This hash is used to uniquely identify this asset throughout the system. If this value doesn't change, the asset will not be rebuilt or republished.
        :param executable: An external command that will produce the packaged asset. The command should produce the location of a ZIP file on ``stdout``. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param file_name: The path, relative to the root of the cloud assembly, in which this asset source resides. This can be a path to a file or a directory, depending on the packaging type. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param packaging: Which type of packaging to perform. Default: - Required if ``fileName`` is specified.
        '''
        asset = FileAssetSource(
            source_hash=source_hash,
            executable=executable,
            file_name=file_name,
            packaging=packaging,
        )

        return typing.cast(FileAssetLocation, jsii.invoke(self, "addFileAsset", [asset]))

    @jsii.member(jsii_name="bind")
    def bind(self, stack: "Stack") -> None:
        '''Bind to the stack this environment is going to be used on.

        Must be called before any of the other methods are called.

        :param stack: -
        '''
        return typing.cast(None, jsii.invoke(self, "bind", [stack]))

    @jsii.member(jsii_name="synthesize")
    def synthesize(self, session: ISynthesisSession) -> None:
        '''Synthesize the associated stack to the session.

        :param session: -
        '''
        return typing.cast(None, jsii.invoke(self, "synthesize", [session]))

    @jsii.member(jsii_name="synthesizeStackTemplate")
    def _synthesize_stack_template(
        self,
        stack: "Stack",
        session: ISynthesisSession,
    ) -> None:
        '''Have the stack write out its template.

        :param stack: -
        :param session: -
        '''
        return typing.cast(None, jsii.invoke(self, "synthesizeStackTemplate", [stack, session]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="DEFAULT_BOOTSTRAP_STACK_VERSION_SSM_PARAMETER")
    def DEFAULT_BOOTSTRAP_STACK_VERSION_SSM_PARAMETER(cls) -> builtins.str:
        '''Default bootstrap stack version SSM parameter.'''
        return typing.cast(builtins.str, jsii.sget(cls, "DEFAULT_BOOTSTRAP_STACK_VERSION_SSM_PARAMETER"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="DEFAULT_CLOUDFORMATION_ROLE_ARN")
    def DEFAULT_CLOUDFORMATION_ROLE_ARN(cls) -> builtins.str:
        '''Default CloudFormation role ARN.'''
        return typing.cast(builtins.str, jsii.sget(cls, "DEFAULT_CLOUDFORMATION_ROLE_ARN"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="DEFAULT_DEPLOY_ROLE_ARN")
    def DEFAULT_DEPLOY_ROLE_ARN(cls) -> builtins.str:
        '''Default deploy role ARN.'''
        return typing.cast(builtins.str, jsii.sget(cls, "DEFAULT_DEPLOY_ROLE_ARN"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="DEFAULT_FILE_ASSET_KEY_ARN_EXPORT_NAME")
    def DEFAULT_FILE_ASSET_KEY_ARN_EXPORT_NAME(cls) -> builtins.str:
        '''Name of the CloudFormation Export with the asset key name.'''
        return typing.cast(builtins.str, jsii.sget(cls, "DEFAULT_FILE_ASSET_KEY_ARN_EXPORT_NAME"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="DEFAULT_FILE_ASSET_PREFIX")
    def DEFAULT_FILE_ASSET_PREFIX(cls) -> builtins.str:
        '''Default file asset prefix.'''
        return typing.cast(builtins.str, jsii.sget(cls, "DEFAULT_FILE_ASSET_PREFIX"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="DEFAULT_FILE_ASSET_PUBLISHING_ROLE_ARN")
    def DEFAULT_FILE_ASSET_PUBLISHING_ROLE_ARN(cls) -> builtins.str:
        '''Default asset publishing role ARN for file (S3) assets.'''
        return typing.cast(builtins.str, jsii.sget(cls, "DEFAULT_FILE_ASSET_PUBLISHING_ROLE_ARN"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="DEFAULT_FILE_ASSETS_BUCKET_NAME")
    def DEFAULT_FILE_ASSETS_BUCKET_NAME(cls) -> builtins.str:
        '''Default file assets bucket name.'''
        return typing.cast(builtins.str, jsii.sget(cls, "DEFAULT_FILE_ASSETS_BUCKET_NAME"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="DEFAULT_IMAGE_ASSET_PUBLISHING_ROLE_ARN")
    def DEFAULT_IMAGE_ASSET_PUBLISHING_ROLE_ARN(cls) -> builtins.str:
        '''Default asset publishing role ARN for image (ECR) assets.'''
        return typing.cast(builtins.str, jsii.sget(cls, "DEFAULT_IMAGE_ASSET_PUBLISHING_ROLE_ARN"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="DEFAULT_IMAGE_ASSETS_REPOSITORY_NAME")
    def DEFAULT_IMAGE_ASSETS_REPOSITORY_NAME(cls) -> builtins.str:
        '''Default image assets repository name.'''
        return typing.cast(builtins.str, jsii.sget(cls, "DEFAULT_IMAGE_ASSETS_REPOSITORY_NAME"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="DEFAULT_LOOKUP_ROLE_ARN")
    def DEFAULT_LOOKUP_ROLE_ARN(cls) -> builtins.str:
        '''Default lookup role ARN for missing values.'''
        return typing.cast(builtins.str, jsii.sget(cls, "DEFAULT_LOOKUP_ROLE_ARN"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="DEFAULT_QUALIFIER")
    def DEFAULT_QUALIFIER(cls) -> builtins.str:
        '''Default ARN qualifier.'''
        return typing.cast(builtins.str, jsii.sget(cls, "DEFAULT_QUALIFIER"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cloudFormationExecutionRoleArn")
    def cloud_formation_execution_role_arn(self) -> builtins.str:
        '''Returns the ARN of the CFN execution Role.'''
        return typing.cast(builtins.str, jsii.get(self, "cloudFormationExecutionRoleArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deployRoleArn")
    def deploy_role_arn(self) -> builtins.str:
        '''Returns the ARN of the deploy Role.'''
        return typing.cast(builtins.str, jsii.get(self, "deployRoleArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stack")
    def _stack(self) -> typing.Optional["Stack"]:
        return typing.cast(typing.Optional["Stack"], jsii.get(self, "stack"))


@jsii.implements(ITokenResolver)
class DefaultTokenResolver(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.DefaultTokenResolver",
):
    '''Default resolver implementation.'''

    def __init__(self, concat: IFragmentConcatenator) -> None:
        '''
        :param concat: -
        '''
        jsii.create(DefaultTokenResolver, self, [concat])

    @jsii.member(jsii_name="resolveList")
    def resolve_list(
        self,
        xs: typing.Sequence[builtins.str],
        context: IResolveContext,
    ) -> typing.Any:
        '''Resolve a tokenized list.

        :param xs: -
        :param context: -
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "resolveList", [xs, context]))

    @jsii.member(jsii_name="resolveString")
    def resolve_string(
        self,
        fragments: TokenizedStringFragments,
        context: IResolveContext,
    ) -> typing.Any:
        '''Resolve string fragments to Tokens.

        :param fragments: -
        :param context: -
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "resolveString", [fragments, context]))

    @jsii.member(jsii_name="resolveToken")
    def resolve_token(
        self,
        t: IResolvable,
        context: IResolveContext,
        post_processor: IPostProcessor,
    ) -> typing.Any:
        '''Default Token resolution.

        Resolve the Token, recurse into whatever it returns,
        then finally post-process it.

        :param t: -
        :param context: -
        :param post_processor: -
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "resolveToken", [t, context, post_processor]))


class DockerIgnoreStrategy(
    IgnoreStrategy,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.DockerIgnoreStrategy",
):
    '''Ignores file paths based on the ```.dockerignore specification`` <https://docs.docker.com/engine/reference/builder/#dockerignore-file>`_.'''

    def __init__(
        self,
        absolute_root_path: builtins.str,
        patterns: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param absolute_root_path: -
        :param patterns: -
        '''
        jsii.create(DockerIgnoreStrategy, self, [absolute_root_path, patterns])

    @jsii.member(jsii_name="add")
    def add(self, pattern: builtins.str) -> None:
        '''Adds another pattern.

        :param pattern: -

        :params: pattern the pattern to add
        '''
        return typing.cast(None, jsii.invoke(self, "add", [pattern]))

    @jsii.member(jsii_name="ignores")
    def ignores(self, absolute_file_path: builtins.str) -> builtins.bool:
        '''Determines whether a given file path should be ignored or not.

        :param absolute_file_path: absolute file path to be assessed against the pattern.

        :return: ``true`` if the file should be ignored
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "ignores", [absolute_file_path]))


class GitIgnoreStrategy(
    IgnoreStrategy,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.GitIgnoreStrategy",
):
    '''Ignores file paths based on the ```.gitignore specification`` <https://git-scm.com/docs/gitignore>`_.'''

    def __init__(
        self,
        absolute_root_path: builtins.str,
        patterns: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param absolute_root_path: -
        :param patterns: -
        '''
        jsii.create(GitIgnoreStrategy, self, [absolute_root_path, patterns])

    @jsii.member(jsii_name="add")
    def add(self, pattern: builtins.str) -> None:
        '''Adds another pattern.

        :param pattern: -

        :params: pattern the pattern to add
        '''
        return typing.cast(None, jsii.invoke(self, "add", [pattern]))

    @jsii.member(jsii_name="ignores")
    def ignores(self, absolute_file_path: builtins.str) -> builtins.bool:
        '''Determines whether a given file path should be ignored or not.

        :param absolute_file_path: absolute file path to be assessed against the pattern.

        :return: ``true`` if the file should be ignored
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "ignores", [absolute_file_path]))


class GlobIgnoreStrategy(
    IgnoreStrategy,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.GlobIgnoreStrategy",
):
    '''Ignores file paths based on simple glob patterns.'''

    def __init__(
        self,
        absolute_root_path: builtins.str,
        patterns: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param absolute_root_path: -
        :param patterns: -
        '''
        jsii.create(GlobIgnoreStrategy, self, [absolute_root_path, patterns])

    @jsii.member(jsii_name="add")
    def add(self, pattern: builtins.str) -> None:
        '''Adds another pattern.

        :param pattern: -

        :params: pattern the pattern to add
        '''
        return typing.cast(None, jsii.invoke(self, "add", [pattern]))

    @jsii.member(jsii_name="ignores")
    def ignores(self, absolute_file_path: builtins.str) -> builtins.bool:
        '''Determines whether a given file path should be ignored or not.

        :param absolute_file_path: absolute file path to be assessed against the pattern.

        :return: ``true`` if the file should be ignored
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "ignores", [absolute_file_path]))


@jsii.interface(jsii_type="@aws-cdk/core.ICfnConditionExpression")
class ICfnConditionExpression(IResolvable, typing_extensions.Protocol):
    '''Represents a CloudFormation element that can be used within a Condition.

    You can use intrinsic functions, such as ``Fn.conditionIf``,
    ``Fn.conditionEquals``, and ``Fn.conditionNot``, to conditionally create
    stack resources. These conditions are evaluated based on input parameters
    that you declare when you create or update a stack. After you define all your
    conditions, you can associate them with resources or resource properties in
    the Resources and Outputs sections of a template.

    You define all conditions in the Conditions section of a template except for
    ``Fn.conditionIf`` conditions. You can use the ``Fn.conditionIf`` condition
    in the metadata attribute, update policy attribute, and property values in
    the Resources section and Outputs sections of a template.

    You might use conditions when you want to reuse a template that can create
    resources in different contexts, such as a test environment versus a
    production environment. In your template, you can add an EnvironmentType
    input parameter, which accepts either prod or test as inputs. For the
    production environment, you might include Amazon EC2 instances with certain
    capabilities; however, for the test environment, you want to use less
    capabilities to save costs. With conditions, you can define which resources
    are created and how they're configured for each environment type.

    You can use ``toString`` when you wish to embed a condition expression
    in a property value that accepts a ``string``. For example::

       # Example automatically generated. See https://github.com/aws/jsii/issues/826
       sqs.Queue(self, "MyQueue",
           queue_name=Fn.condition_if("Condition", "Hello", "World").to_string()
       )
    '''

    pass


class _ICfnConditionExpressionProxy(
    jsii.proxy_for(IResolvable) # type: ignore[misc]
):
    '''Represents a CloudFormation element that can be used within a Condition.

    You can use intrinsic functions, such as ``Fn.conditionIf``,
    ``Fn.conditionEquals``, and ``Fn.conditionNot``, to conditionally create
    stack resources. These conditions are evaluated based on input parameters
    that you declare when you create or update a stack. After you define all your
    conditions, you can associate them with resources or resource properties in
    the Resources and Outputs sections of a template.

    You define all conditions in the Conditions section of a template except for
    ``Fn.conditionIf`` conditions. You can use the ``Fn.conditionIf`` condition
    in the metadata attribute, update policy attribute, and property values in
    the Resources section and Outputs sections of a template.

    You might use conditions when you want to reuse a template that can create
    resources in different contexts, such as a test environment versus a
    production environment. In your template, you can add an EnvironmentType
    input parameter, which accepts either prod or test as inputs. For the
    production environment, you might include Amazon EC2 instances with certain
    capabilities; however, for the test environment, you want to use less
    capabilities to save costs. With conditions, you can define which resources
    are created and how they're configured for each environment type.

    You can use ``toString`` when you wish to embed a condition expression
    in a property value that accepts a ``string``. For example::

       # Example automatically generated. See https://github.com/aws/jsii/issues/826
       sqs.Queue(self, "MyQueue",
           queue_name=Fn.condition_if("Condition", "Hello", "World").to_string()
       )
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.ICfnConditionExpression"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICfnConditionExpression).__jsii_proxy_class__ = lambda : _ICfnConditionExpressionProxy


@jsii.interface(jsii_type="@aws-cdk/core.IConstruct")
class IConstruct(constructs.IConstruct, IDependable, typing_extensions.Protocol):
    '''Represents a construct.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="node")
    def node(self) -> ConstructNode:
        '''The construct tree node for this construct.'''
        ...


class _IConstructProxy(
    jsii.proxy_for(constructs.IConstruct), # type: ignore[misc]
    jsii.proxy_for(IDependable), # type: ignore[misc]
):
    '''Represents a construct.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.IConstruct"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="node")
    def node(self) -> ConstructNode:
        '''The construct tree node for this construct.'''
        return typing.cast(ConstructNode, jsii.get(self, "node"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConstruct).__jsii_proxy_class__ = lambda : _IConstructProxy


@jsii.interface(jsii_type="@aws-cdk/core.IResource")
class IResource(IConstruct, typing_extensions.Protocol):
    '''Interface for the Resource construct.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="env")
    def env(self) -> ResourceEnvironment:
        '''The environment this resource belongs to.

        For resources that are created and managed by the CDK
        (generally, those created by creating new class instances like Role, Bucket, etc.),
        this is always the same as the environment of the stack they belong to;
        however, for imported resources
        (those obtained from static methods like fromRoleArn, fromBucketName, etc.),
        that might be different than the stack they were imported into.
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stack")
    def stack(self) -> "Stack":
        '''The stack in which this resource is defined.'''
        ...


class _IResourceProxy(
    jsii.proxy_for(IConstruct) # type: ignore[misc]
):
    '''Interface for the Resource construct.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/core.IResource"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="env")
    def env(self) -> ResourceEnvironment:
        '''The environment this resource belongs to.

        For resources that are created and managed by the CDK
        (generally, those created by creating new class instances like Role, Bucket, etc.),
        this is always the same as the environment of the stack they belong to;
        however, for imported resources
        (those obtained from static methods like fromRoleArn, fromBucketName, etc.),
        that might be different than the stack they were imported into.
        '''
        return typing.cast(ResourceEnvironment, jsii.get(self, "env"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stack")
    def stack(self) -> "Stack":
        '''The stack in which this resource is defined.'''
        return typing.cast("Stack", jsii.get(self, "stack"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResource).__jsii_proxy_class__ = lambda : _IResourceProxy


class LegacyStackSynthesizer(
    StackSynthesizer,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.LegacyStackSynthesizer",
):
    '''Use the original deployment environment.

    This deployment environment is restricted in cross-environment deployments,
    CI/CD deployments, and will use up CloudFormation parameters in your template.

    This is the only StackSynthesizer that supports customizing asset behavior
    by overriding ``Stack.addFileAsset()`` and ``Stack.addDockerImageAsset()``.
    '''

    def __init__(self) -> None:
        jsii.create(LegacyStackSynthesizer, self, [])

    @jsii.member(jsii_name="addDockerImageAsset")
    def add_docker_image_asset(
        self,
        *,
        source_hash: builtins.str,
        directory_name: typing.Optional[builtins.str] = None,
        docker_build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        docker_build_target: typing.Optional[builtins.str] = None,
        docker_file: typing.Optional[builtins.str] = None,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        repository_name: typing.Optional[builtins.str] = None,
    ) -> DockerImageAssetLocation:
        '''Register a Docker Image Asset.

        Returns the parameters that can be used to refer to the asset inside the template.

        :param source_hash: The hash of the contents of the docker build context. This hash is used throughout the system to identify this image and avoid duplicate work in case the source did not change. NOTE: this means that if you wish to update your docker image, you must make a modification to the source (e.g. add some metadata to your Dockerfile).
        :param directory_name: The directory where the Dockerfile is stored, must be relative to the cloud assembly root. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param docker_build_args: Build args to pass to the ``docker build`` command. Since Docker build arguments are resolved before deployment, keys and values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or ``queue.queueUrl``). Only allowed when ``directoryName`` is specified. Default: - no build args are passed
        :param docker_build_target: Docker target to build to. Only allowed when ``directoryName`` is specified. Default: - no target
        :param docker_file: Path to the Dockerfile (relative to the directory). Only allowed when ``directoryName`` is specified. Default: - no file
        :param executable: An external command that will produce the packaged asset. The command should produce the name of a local Docker image on ``stdout``. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param repository_name: (deprecated) ECR repository name. Specify this property if you need to statically address the image, e.g. from a Kubernetes Pod. Note, this is only the repository name, without the registry and the tag parts. Default: - automatically derived from the asset's ID.
        '''
        asset = DockerImageAssetSource(
            source_hash=source_hash,
            directory_name=directory_name,
            docker_build_args=docker_build_args,
            docker_build_target=docker_build_target,
            docker_file=docker_file,
            executable=executable,
            repository_name=repository_name,
        )

        return typing.cast(DockerImageAssetLocation, jsii.invoke(self, "addDockerImageAsset", [asset]))

    @jsii.member(jsii_name="addFileAsset")
    def add_file_asset(
        self,
        *,
        source_hash: builtins.str,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_name: typing.Optional[builtins.str] = None,
        packaging: typing.Optional[FileAssetPackaging] = None,
    ) -> FileAssetLocation:
        '''Register a File Asset.

        Returns the parameters that can be used to refer to the asset inside the template.

        :param source_hash: A hash on the content source. This hash is used to uniquely identify this asset throughout the system. If this value doesn't change, the asset will not be rebuilt or republished.
        :param executable: An external command that will produce the packaged asset. The command should produce the location of a ZIP file on ``stdout``. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param file_name: The path, relative to the root of the cloud assembly, in which this asset source resides. This can be a path to a file or a directory, depending on the packaging type. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param packaging: Which type of packaging to perform. Default: - Required if ``fileName`` is specified.
        '''
        asset = FileAssetSource(
            source_hash=source_hash,
            executable=executable,
            file_name=file_name,
            packaging=packaging,
        )

        return typing.cast(FileAssetLocation, jsii.invoke(self, "addFileAsset", [asset]))

    @jsii.member(jsii_name="bind")
    def bind(self, stack: "Stack") -> None:
        '''Bind to the stack this environment is going to be used on.

        Must be called before any of the other methods are called.

        :param stack: -
        '''
        return typing.cast(None, jsii.invoke(self, "bind", [stack]))

    @jsii.member(jsii_name="synthesize")
    def synthesize(self, session: ISynthesisSession) -> None:
        '''Synthesize the associated stack to the session.

        :param session: -
        '''
        return typing.cast(None, jsii.invoke(self, "synthesize", [session]))


class NestedStackSynthesizer(
    StackSynthesizer,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.NestedStackSynthesizer",
):
    '''Deployment environment for a nested stack.

    Interoperates with the StackSynthesizer of the parent stack.
    '''

    def __init__(self, parent_deployment: IStackSynthesizer) -> None:
        '''
        :param parent_deployment: -
        '''
        jsii.create(NestedStackSynthesizer, self, [parent_deployment])

    @jsii.member(jsii_name="addDockerImageAsset")
    def add_docker_image_asset(
        self,
        *,
        source_hash: builtins.str,
        directory_name: typing.Optional[builtins.str] = None,
        docker_build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        docker_build_target: typing.Optional[builtins.str] = None,
        docker_file: typing.Optional[builtins.str] = None,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        repository_name: typing.Optional[builtins.str] = None,
    ) -> DockerImageAssetLocation:
        '''Register a Docker Image Asset.

        Returns the parameters that can be used to refer to the asset inside the template.

        :param source_hash: The hash of the contents of the docker build context. This hash is used throughout the system to identify this image and avoid duplicate work in case the source did not change. NOTE: this means that if you wish to update your docker image, you must make a modification to the source (e.g. add some metadata to your Dockerfile).
        :param directory_name: The directory where the Dockerfile is stored, must be relative to the cloud assembly root. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param docker_build_args: Build args to pass to the ``docker build`` command. Since Docker build arguments are resolved before deployment, keys and values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or ``queue.queueUrl``). Only allowed when ``directoryName`` is specified. Default: - no build args are passed
        :param docker_build_target: Docker target to build to. Only allowed when ``directoryName`` is specified. Default: - no target
        :param docker_file: Path to the Dockerfile (relative to the directory). Only allowed when ``directoryName`` is specified. Default: - no file
        :param executable: An external command that will produce the packaged asset. The command should produce the name of a local Docker image on ``stdout``. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param repository_name: (deprecated) ECR repository name. Specify this property if you need to statically address the image, e.g. from a Kubernetes Pod. Note, this is only the repository name, without the registry and the tag parts. Default: - automatically derived from the asset's ID.
        '''
        asset = DockerImageAssetSource(
            source_hash=source_hash,
            directory_name=directory_name,
            docker_build_args=docker_build_args,
            docker_build_target=docker_build_target,
            docker_file=docker_file,
            executable=executable,
            repository_name=repository_name,
        )

        return typing.cast(DockerImageAssetLocation, jsii.invoke(self, "addDockerImageAsset", [asset]))

    @jsii.member(jsii_name="addFileAsset")
    def add_file_asset(
        self,
        *,
        source_hash: builtins.str,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_name: typing.Optional[builtins.str] = None,
        packaging: typing.Optional[FileAssetPackaging] = None,
    ) -> FileAssetLocation:
        '''Register a File Asset.

        Returns the parameters that can be used to refer to the asset inside the template.

        :param source_hash: A hash on the content source. This hash is used to uniquely identify this asset throughout the system. If this value doesn't change, the asset will not be rebuilt or republished.
        :param executable: An external command that will produce the packaged asset. The command should produce the location of a ZIP file on ``stdout``. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param file_name: The path, relative to the root of the cloud assembly, in which this asset source resides. This can be a path to a file or a directory, depending on the packaging type. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param packaging: Which type of packaging to perform. Default: - Required if ``fileName`` is specified.
        '''
        asset = FileAssetSource(
            source_hash=source_hash,
            executable=executable,
            file_name=file_name,
            packaging=packaging,
        )

        return typing.cast(FileAssetLocation, jsii.invoke(self, "addFileAsset", [asset]))

    @jsii.member(jsii_name="bind")
    def bind(self, stack: "Stack") -> None:
        '''Bind to the stack this environment is going to be used on.

        Must be called before any of the other methods are called.

        :param stack: -
        '''
        return typing.cast(None, jsii.invoke(self, "bind", [stack]))

    @jsii.member(jsii_name="synthesize")
    def synthesize(self, session: ISynthesisSession) -> None:
        '''Synthesize the associated stack to the session.

        :param session: -
        '''
        return typing.cast(None, jsii.invoke(self, "synthesize", [session]))


class BootstraplessSynthesizer(
    DefaultStackSynthesizer,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.BootstraplessSynthesizer",
):
    '''A special synthesizer that behaves similarly to DefaultStackSynthesizer, but doesn't require bootstrapping the environment it operates in.

    Because of that, stacks using it cannot have assets inside of them.
    Used by the CodePipeline construct for the support stacks needed for
    cross-region replication S3 buckets.
    '''

    def __init__(
        self,
        *,
        cloud_formation_execution_role_arn: typing.Optional[builtins.str] = None,
        deploy_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cloud_formation_execution_role_arn: The CFN execution Role ARN to use. Default: - No CloudFormation role (use CLI credentials)
        :param deploy_role_arn: The deploy Role ARN to use. Default: - No deploy role (use CLI credentials)
        '''
        props = BootstraplessSynthesizerProps(
            cloud_formation_execution_role_arn=cloud_formation_execution_role_arn,
            deploy_role_arn=deploy_role_arn,
        )

        jsii.create(BootstraplessSynthesizer, self, [props])

    @jsii.member(jsii_name="addDockerImageAsset")
    def add_docker_image_asset(
        self,
        *,
        source_hash: builtins.str,
        directory_name: typing.Optional[builtins.str] = None,
        docker_build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        docker_build_target: typing.Optional[builtins.str] = None,
        docker_file: typing.Optional[builtins.str] = None,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        repository_name: typing.Optional[builtins.str] = None,
    ) -> DockerImageAssetLocation:
        '''Register a Docker Image Asset.

        Returns the parameters that can be used to refer to the asset inside the template.

        :param source_hash: The hash of the contents of the docker build context. This hash is used throughout the system to identify this image and avoid duplicate work in case the source did not change. NOTE: this means that if you wish to update your docker image, you must make a modification to the source (e.g. add some metadata to your Dockerfile).
        :param directory_name: The directory where the Dockerfile is stored, must be relative to the cloud assembly root. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param docker_build_args: Build args to pass to the ``docker build`` command. Since Docker build arguments are resolved before deployment, keys and values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or ``queue.queueUrl``). Only allowed when ``directoryName`` is specified. Default: - no build args are passed
        :param docker_build_target: Docker target to build to. Only allowed when ``directoryName`` is specified. Default: - no target
        :param docker_file: Path to the Dockerfile (relative to the directory). Only allowed when ``directoryName`` is specified. Default: - no file
        :param executable: An external command that will produce the packaged asset. The command should produce the name of a local Docker image on ``stdout``. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param repository_name: (deprecated) ECR repository name. Specify this property if you need to statically address the image, e.g. from a Kubernetes Pod. Note, this is only the repository name, without the registry and the tag parts. Default: - automatically derived from the asset's ID.
        '''
        _asset = DockerImageAssetSource(
            source_hash=source_hash,
            directory_name=directory_name,
            docker_build_args=docker_build_args,
            docker_build_target=docker_build_target,
            docker_file=docker_file,
            executable=executable,
            repository_name=repository_name,
        )

        return typing.cast(DockerImageAssetLocation, jsii.invoke(self, "addDockerImageAsset", [_asset]))

    @jsii.member(jsii_name="addFileAsset")
    def add_file_asset(
        self,
        *,
        source_hash: builtins.str,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_name: typing.Optional[builtins.str] = None,
        packaging: typing.Optional[FileAssetPackaging] = None,
    ) -> FileAssetLocation:
        '''Register a File Asset.

        Returns the parameters that can be used to refer to the asset inside the template.

        :param source_hash: A hash on the content source. This hash is used to uniquely identify this asset throughout the system. If this value doesn't change, the asset will not be rebuilt or republished.
        :param executable: An external command that will produce the packaged asset. The command should produce the location of a ZIP file on ``stdout``. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param file_name: The path, relative to the root of the cloud assembly, in which this asset source resides. This can be a path to a file or a directory, depending on the packaging type. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param packaging: Which type of packaging to perform. Default: - Required if ``fileName`` is specified.
        '''
        _asset = FileAssetSource(
            source_hash=source_hash,
            executable=executable,
            file_name=file_name,
            packaging=packaging,
        )

        return typing.cast(FileAssetLocation, jsii.invoke(self, "addFileAsset", [_asset]))

    @jsii.member(jsii_name="synthesize")
    def synthesize(self, session: ISynthesisSession) -> None:
        '''Synthesize the associated stack to the session.

        :param session: -
        '''
        return typing.cast(None, jsii.invoke(self, "synthesize", [session]))


@jsii.implements(IConstruct)
class Construct(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.Construct",
):
    '''Represents the building block of the construct graph.

    All constructs besides the root construct must be created within the scope of
    another construct.
    '''

    def __init__(self, scope: constructs.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -
        '''
        jsii.create(Construct, self, [scope, id])

    @jsii.member(jsii_name="isConstruct") # type: ignore[misc]
    @builtins.classmethod
    def is_construct(cls, x: typing.Any) -> builtins.bool:
        '''Return whether the given object is a Construct.

        :param x: -
        '''
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isConstruct", [x]))

    @jsii.member(jsii_name="onPrepare")
    def _on_prepare(self) -> None:
        '''Perform final modifications before synthesis.

        This method can be implemented by derived constructs in order to perform
        final changes before synthesis. prepare() will be called after child
        constructs have been prepared.

        This is an advanced framework feature. Only use this if you
        understand the implications.
        '''
        return typing.cast(None, jsii.invoke(self, "onPrepare", []))

    @jsii.member(jsii_name="onSynthesize")
    def _on_synthesize(self, session: constructs.ISynthesisSession) -> None:
        '''Allows this construct to emit artifacts into the cloud assembly during synthesis.

        This method is usually implemented by framework-level constructs such as ``Stack`` and ``Asset``
        as they participate in synthesizing the cloud assembly.

        :param session: The synthesis session.
        '''
        return typing.cast(None, jsii.invoke(self, "onSynthesize", [session]))

    @jsii.member(jsii_name="onValidate")
    def _on_validate(self) -> typing.List[builtins.str]:
        '''Validate the current construct.

        This method can be implemented by derived constructs in order to perform
        validation logic. It is called on all constructs before synthesis.

        :return: An array of validation error messages, or an empty array if the construct is valid.
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "onValidate", []))

    @jsii.member(jsii_name="prepare")
    def _prepare(self) -> None:
        '''Perform final modifications before synthesis.

        This method can be implemented by derived constructs in order to perform
        final changes before synthesis. prepare() will be called after child
        constructs have been prepared.

        This is an advanced framework feature. Only use this if you
        understand the implications.
        '''
        return typing.cast(None, jsii.invoke(self, "prepare", []))

    @jsii.member(jsii_name="synthesize")
    def _synthesize(self, session: ISynthesisSession) -> None:
        '''Allows this construct to emit artifacts into the cloud assembly during synthesis.

        This method is usually implemented by framework-level constructs such as ``Stack`` and ``Asset``
        as they participate in synthesizing the cloud assembly.

        :param session: The synthesis session.
        '''
        return typing.cast(None, jsii.invoke(self, "synthesize", [session]))

    @jsii.member(jsii_name="validate")
    def _validate(self) -> typing.List[builtins.str]:
        '''Validate the current construct.

        This method can be implemented by derived constructs in order to perform
        validation logic. It is called on all constructs before synthesis.

        :return: An array of validation error messages, or an empty array if the construct is valid.
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "validate", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="node")
    def node(self) -> ConstructNode:
        '''The construct tree node associated with this construct.'''
        return typing.cast(ConstructNode, jsii.get(self, "node"))


class CustomResourceProvider(
    Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CustomResourceProvider",
):
    '''An AWS-Lambda backed custom resource provider.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        code_directory: builtins.str,
        runtime: CustomResourceProviderRuntime,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        memory_size: typing.Optional[Size] = None,
        policy_statements: typing.Optional[typing.Sequence[typing.Any]] = None,
        timeout: typing.Optional[Duration] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param code_directory: A local file system directory with the provider's code. The code will be bundled into a zip asset and wired to the provider's AWS Lambda function.
        :param runtime: The AWS Lambda runtime and version to use for the provider.
        :param description: A description of the function. Default: - No description.
        :param environment: Key-value pairs that are passed to Lambda as Environment. Default: - No environment variables.
        :param memory_size: The amount of memory that your function has access to. Increasing the function's memory also increases its CPU allocation. Default: Size.mebibytes(128)
        :param policy_statements: A set of IAM policy statements to include in the inline policy of the provider's lambda function. Default: - no additional inline policy
        :param timeout: AWS Lambda timeout for the provider. Default: Duration.minutes(15)
        '''
        props = CustomResourceProviderProps(
            code_directory=code_directory,
            runtime=runtime,
            description=description,
            environment=environment,
            memory_size=memory_size,
            policy_statements=policy_statements,
            timeout=timeout,
        )

        jsii.create(CustomResourceProvider, self, [scope, id, props])

    @jsii.member(jsii_name="getOrCreate") # type: ignore[misc]
    @builtins.classmethod
    def get_or_create(
        cls,
        scope: constructs.Construct,
        uniqueid: builtins.str,
        *,
        code_directory: builtins.str,
        runtime: CustomResourceProviderRuntime,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        memory_size: typing.Optional[Size] = None,
        policy_statements: typing.Optional[typing.Sequence[typing.Any]] = None,
        timeout: typing.Optional[Duration] = None,
    ) -> builtins.str:
        '''Returns a stack-level singleton ARN (service token) for the custom resource provider.

        :param scope: Construct scope.
        :param uniqueid: A globally unique id that will be used for the stack-level construct.
        :param code_directory: A local file system directory with the provider's code. The code will be bundled into a zip asset and wired to the provider's AWS Lambda function.
        :param runtime: The AWS Lambda runtime and version to use for the provider.
        :param description: A description of the function. Default: - No description.
        :param environment: Key-value pairs that are passed to Lambda as Environment. Default: - No environment variables.
        :param memory_size: The amount of memory that your function has access to. Increasing the function's memory also increases its CPU allocation. Default: Size.mebibytes(128)
        :param policy_statements: A set of IAM policy statements to include in the inline policy of the provider's lambda function. Default: - no additional inline policy
        :param timeout: AWS Lambda timeout for the provider. Default: Duration.minutes(15)

        :return:

        the service token of the custom resource provider, which should be
        used when defining a ``CustomResource``.
        '''
        props = CustomResourceProviderProps(
            code_directory=code_directory,
            runtime=runtime,
            description=description,
            environment=environment,
            memory_size=memory_size,
            policy_statements=policy_statements,
            timeout=timeout,
        )

        return typing.cast(builtins.str, jsii.sinvoke(cls, "getOrCreate", [scope, uniqueid, props]))

    @jsii.member(jsii_name="getOrCreateProvider") # type: ignore[misc]
    @builtins.classmethod
    def get_or_create_provider(
        cls,
        scope: constructs.Construct,
        uniqueid: builtins.str,
        *,
        code_directory: builtins.str,
        runtime: CustomResourceProviderRuntime,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        memory_size: typing.Optional[Size] = None,
        policy_statements: typing.Optional[typing.Sequence[typing.Any]] = None,
        timeout: typing.Optional[Duration] = None,
    ) -> "CustomResourceProvider":
        '''Returns a stack-level singleton for the custom resource provider.

        :param scope: Construct scope.
        :param uniqueid: A globally unique id that will be used for the stack-level construct.
        :param code_directory: A local file system directory with the provider's code. The code will be bundled into a zip asset and wired to the provider's AWS Lambda function.
        :param runtime: The AWS Lambda runtime and version to use for the provider.
        :param description: A description of the function. Default: - No description.
        :param environment: Key-value pairs that are passed to Lambda as Environment. Default: - No environment variables.
        :param memory_size: The amount of memory that your function has access to. Increasing the function's memory also increases its CPU allocation. Default: Size.mebibytes(128)
        :param policy_statements: A set of IAM policy statements to include in the inline policy of the provider's lambda function. Default: - no additional inline policy
        :param timeout: AWS Lambda timeout for the provider. Default: Duration.minutes(15)

        :return:

        the service token of the custom resource provider, which should be
        used when defining a ``CustomResource``.
        '''
        props = CustomResourceProviderProps(
            code_directory=code_directory,
            runtime=runtime,
            description=description,
            environment=environment,
            memory_size=memory_size,
            policy_statements=policy_statements,
            timeout=timeout,
        )

        return typing.cast("CustomResourceProvider", jsii.sinvoke(cls, "getOrCreateProvider", [scope, uniqueid, props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The ARN of the provider's AWS Lambda function role.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceToken")
    def service_token(self) -> builtins.str:
        '''The ARN of the provider's AWS Lambda function which should be used as the ``serviceToken`` when defining a custom resource.

        Example::

            # Example automatically generated. See https://github.com/aws/jsii/issues/826
            CustomResource(self, "MyCustomResource",
                # ...
                service_token=my_provider.service_token
            )
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceToken"))


@jsii.implements(IResource)
class Resource(
    Construct,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/core.Resource",
):
    '''A construct which represents an AWS resource.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        '''
        props = ResourceProps(
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(Resource, self, [scope, id, props])

    @jsii.member(jsii_name="isResource") # type: ignore[misc]
    @builtins.classmethod
    def is_resource(cls, construct: IConstruct) -> builtins.bool:
        '''Check whether the given construct is a Resource.

        :param construct: -
        '''
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isResource", [construct]))

    @jsii.member(jsii_name="applyRemovalPolicy")
    def apply_removal_policy(self, policy: RemovalPolicy) -> None:
        '''Apply the given removal policy to this resource.

        The Removal Policy controls what happens to this resource when it stops
        being managed by CloudFormation, either because you've removed it from the
        CDK application or because you've made a change that requires the resource
        to be replaced.

        The resource can be deleted (``RemovalPolicy.DELETE``), or left in your AWS
        account for data recovery and cleanup later (``RemovalPolicy.RETAIN``).

        :param policy: -
        '''
        return typing.cast(None, jsii.invoke(self, "applyRemovalPolicy", [policy]))

    @jsii.member(jsii_name="generatePhysicalName")
    def _generate_physical_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.invoke(self, "generatePhysicalName", []))

    @jsii.member(jsii_name="getResourceArnAttribute")
    def _get_resource_arn_attribute(
        self,
        arn_attr: builtins.str,
        *,
        resource: builtins.str,
        service: builtins.str,
        account: typing.Optional[builtins.str] = None,
        arn_format: typing.Optional[ArnFormat] = None,
        partition: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        resource_name: typing.Optional[builtins.str] = None,
        sep: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''Returns an environment-sensitive token that should be used for the resource's "ARN" attribute (e.g. ``bucket.bucketArn``).

        Normally, this token will resolve to ``arnAttr``, but if the resource is
        referenced across environments, ``arnComponents`` will be used to synthesize
        a concrete ARN with the resource's physical name. Make sure to reference
        ``this.physicalName`` in ``arnComponents``.

        :param arn_attr: The CFN attribute which resolves to the ARN of the resource. Commonly it will be called "Arn" (e.g. ``resource.attrArn``), but sometimes it's the CFN resource's ``ref``.
        :param resource: Resource type (e.g. "table", "autoScalingGroup", "certificate"). For some resource types, e.g. S3 buckets, this field defines the bucket name.
        :param service: The service namespace that identifies the AWS product (for example, 's3', 'iam', 'codepipline').
        :param account: The ID of the AWS account that owns the resource, without the hyphens. For example, 123456789012. Note that the ARNs for some resources don't require an account number, so this component might be omitted. Default: The account the stack is deployed to.
        :param arn_format: The specific ARN format to use for this ARN value. Default: - uses value of ``sep`` as the separator for formatting, ``ArnFormat.SLASH_RESOURCE_NAME`` if that property was also not provided
        :param partition: The partition that the resource is in. For standard AWS regions, the partition is aws. If you have resources in other partitions, the partition is aws-partitionname. For example, the partition for resources in the China (Beijing) region is aws-cn. Default: The AWS partition the stack is deployed to.
        :param region: The region the resource resides in. Note that the ARNs for some resources do not require a region, so this component might be omitted. Default: The region the stack is deployed to.
        :param resource_name: Resource name or path within the resource (i.e. S3 bucket object key) or a wildcard such as ``"*"``. This is service-dependent.
        :param sep: (deprecated) Separator between resource type and the resource. Can be either '/', ':' or an empty string. Will only be used if resourceName is defined. Default: '/'
        '''
        arn_components = ArnComponents(
            resource=resource,
            service=service,
            account=account,
            arn_format=arn_format,
            partition=partition,
            region=region,
            resource_name=resource_name,
            sep=sep,
        )

        return typing.cast(builtins.str, jsii.invoke(self, "getResourceArnAttribute", [arn_attr, arn_components]))

    @jsii.member(jsii_name="getResourceNameAttribute")
    def _get_resource_name_attribute(self, name_attr: builtins.str) -> builtins.str:
        '''Returns an environment-sensitive token that should be used for the resource's "name" attribute (e.g. ``bucket.bucketName``).

        Normally, this token will resolve to ``nameAttr``, but if the resource is
        referenced across environments, it will be resolved to ``this.physicalName``,
        which will be a concrete name.

        :param name_attr: The CFN attribute which resolves to the resource's name. Commonly this is the resource's ``ref``.
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "getResourceNameAttribute", [name_attr]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="env")
    def env(self) -> ResourceEnvironment:
        '''The environment this resource belongs to.

        For resources that are created and managed by the CDK
        (generally, those created by creating new class instances like Role, Bucket, etc.),
        this is always the same as the environment of the stack they belong to;
        however, for imported resources
        (those obtained from static methods like fromRoleArn, fromBucketName, etc.),
        that might be different than the stack they were imported into.
        '''
        return typing.cast(ResourceEnvironment, jsii.get(self, "env"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="physicalName")
    def _physical_name(self) -> builtins.str:
        '''Returns a string-encoded token that resolves to the physical name that should be passed to the CloudFormation resource.

        This value will resolve to one of the following:

        - a concrete value (e.g. ``"my-awesome-bucket"``)
        - ``undefined``, when a name should be generated by CloudFormation
        - a concrete name generated automatically during synthesis, in
          cross-environment scenarios.
        '''
        return typing.cast(builtins.str, jsii.get(self, "physicalName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stack")
    def stack(self) -> "Stack":
        '''The stack in which this resource is defined.'''
        return typing.cast("Stack", jsii.get(self, "stack"))


class _ResourceProxy(Resource):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Resource).__jsii_proxy_class__ = lambda : _ResourceProxy


@jsii.implements(ITaggable)
class Stack(Construct, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.Stack"):
    '''A root construct which represents a single CloudFormation stack.'''

    def __init__(
        self,
        scope: typing.Optional[constructs.Construct] = None,
        id: typing.Optional[builtins.str] = None,
        *,
        analytics_reporting: typing.Optional[builtins.bool] = None,
        description: typing.Optional[builtins.str] = None,
        env: typing.Optional[Environment] = None,
        stack_name: typing.Optional[builtins.str] = None,
        synthesizer: typing.Optional[IStackSynthesizer] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_protection: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Creates a new stack.

        :param scope: Parent of this stack, usually an ``App`` or a ``Stage``, but could be any construct.
        :param id: The construct ID of this stack. If ``stackName`` is not explicitly defined, this id (and any parent IDs) will be used to determine the physical ID of the stack.
        :param analytics_reporting: Include runtime versioning information in this Stack. Default: ``analyticsReporting`` setting of containing ``App``, or value of 'aws:cdk:version-reporting' context key
        :param description: A description of the stack. Default: - No description.
        :param env: The AWS environment (account/region) where this stack will be deployed. Set the ``region``/``account`` fields of ``env`` to either a concrete value to select the indicated environment (recommended for production stacks), or to the values of environment variables ``CDK_DEFAULT_REGION``/``CDK_DEFAULT_ACCOUNT`` to let the target environment depend on the AWS credentials/configuration that the CDK CLI is executed under (recommended for development stacks). If the ``Stack`` is instantiated inside a ``Stage``, any undefined ``region``/``account`` fields from ``env`` will default to the same field on the encompassing ``Stage``, if configured there. If either ``region`` or ``account`` are not set nor inherited from ``Stage``, the Stack will be considered "*environment-agnostic*"". Environment-agnostic stacks can be deployed to any environment but may not be able to take advantage of all features of the CDK. For example, they will not be able to use environmental context lookups such as ``ec2.Vpc.fromLookup`` and will not automatically translate Service Principals to the right format based on the environment's AWS partition, and other such enhancements. Default: - The environment of the containing ``Stage`` if available, otherwise create the stack will be environment-agnostic.
        :param stack_name: Name to deploy the stack with. Default: - Derived from construct path.
        :param synthesizer: Synthesis method to use while deploying this stack. Default: - ``DefaultStackSynthesizer`` if the ``@aws-cdk/core:newStyleStackSynthesis`` feature flag is set, ``LegacyStackSynthesizer`` otherwise.
        :param tags: Stack tags that will be applied to all the taggable resources and the stack itself. Default: {}
        :param termination_protection: Whether to enable termination protection for this stack. Default: false
        '''
        props = StackProps(
            analytics_reporting=analytics_reporting,
            description=description,
            env=env,
            stack_name=stack_name,
            synthesizer=synthesizer,
            tags=tags,
            termination_protection=termination_protection,
        )

        jsii.create(Stack, self, [scope, id, props])

    @jsii.member(jsii_name="isStack") # type: ignore[misc]
    @builtins.classmethod
    def is_stack(cls, x: typing.Any) -> builtins.bool:
        '''Return whether the given object is a Stack.

        We do attribute detection since we can't reliably use 'instanceof'.

        :param x: -
        '''
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isStack", [x]))

    @jsii.member(jsii_name="of") # type: ignore[misc]
    @builtins.classmethod
    def of(cls, construct: constructs.IConstruct) -> "Stack":
        '''Looks up the first stack scope in which ``construct`` is defined.

        Fails if there is no stack up the tree.

        :param construct: The construct to start the search from.
        '''
        return typing.cast("Stack", jsii.sinvoke(cls, "of", [construct]))

    @jsii.member(jsii_name="addDependency")
    def add_dependency(
        self,
        target: "Stack",
        reason: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Add a dependency between this stack and another stack.

        This can be used to define dependencies between any two stacks within an
        app, and also supports nested stacks.

        :param target: -
        :param reason: -
        '''
        return typing.cast(None, jsii.invoke(self, "addDependency", [target, reason]))

    @jsii.member(jsii_name="addDockerImageAsset")
    def add_docker_image_asset(
        self,
        *,
        source_hash: builtins.str,
        directory_name: typing.Optional[builtins.str] = None,
        docker_build_args: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        docker_build_target: typing.Optional[builtins.str] = None,
        docker_file: typing.Optional[builtins.str] = None,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        repository_name: typing.Optional[builtins.str] = None,
    ) -> DockerImageAssetLocation:
        '''(deprecated) Register a docker image asset on this Stack.

        :param source_hash: The hash of the contents of the docker build context. This hash is used throughout the system to identify this image and avoid duplicate work in case the source did not change. NOTE: this means that if you wish to update your docker image, you must make a modification to the source (e.g. add some metadata to your Dockerfile).
        :param directory_name: The directory where the Dockerfile is stored, must be relative to the cloud assembly root. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param docker_build_args: Build args to pass to the ``docker build`` command. Since Docker build arguments are resolved before deployment, keys and values cannot refer to unresolved tokens (such as ``lambda.functionArn`` or ``queue.queueUrl``). Only allowed when ``directoryName`` is specified. Default: - no build args are passed
        :param docker_build_target: Docker target to build to. Only allowed when ``directoryName`` is specified. Default: - no target
        :param docker_file: Path to the Dockerfile (relative to the directory). Only allowed when ``directoryName`` is specified. Default: - no file
        :param executable: An external command that will produce the packaged asset. The command should produce the name of a local Docker image on ``stdout``. Default: - Exactly one of ``directoryName`` and ``executable`` is required
        :param repository_name: (deprecated) ECR repository name. Specify this property if you need to statically address the image, e.g. from a Kubernetes Pod. Note, this is only the repository name, without the registry and the tag parts. Default: - automatically derived from the asset's ID.

        :deprecated:

        Use ``stack.synthesizer.addDockerImageAsset()`` if you are calling,
        and a different ``IStackSynthesizer`` class if you are implementing.

        :stability: deprecated
        '''
        asset = DockerImageAssetSource(
            source_hash=source_hash,
            directory_name=directory_name,
            docker_build_args=docker_build_args,
            docker_build_target=docker_build_target,
            docker_file=docker_file,
            executable=executable,
            repository_name=repository_name,
        )

        return typing.cast(DockerImageAssetLocation, jsii.invoke(self, "addDockerImageAsset", [asset]))

    @jsii.member(jsii_name="addFileAsset")
    def add_file_asset(
        self,
        *,
        source_hash: builtins.str,
        executable: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_name: typing.Optional[builtins.str] = None,
        packaging: typing.Optional[FileAssetPackaging] = None,
    ) -> FileAssetLocation:
        '''(deprecated) Register a file asset on this Stack.

        :param source_hash: A hash on the content source. This hash is used to uniquely identify this asset throughout the system. If this value doesn't change, the asset will not be rebuilt or republished.
        :param executable: An external command that will produce the packaged asset. The command should produce the location of a ZIP file on ``stdout``. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param file_name: The path, relative to the root of the cloud assembly, in which this asset source resides. This can be a path to a file or a directory, depending on the packaging type. Default: - Exactly one of ``directory`` and ``executable`` is required
        :param packaging: Which type of packaging to perform. Default: - Required if ``fileName`` is specified.

        :deprecated:

        Use ``stack.synthesizer.addFileAsset()`` if you are calling,
        and a different IStackSynthesizer class if you are implementing.

        :stability: deprecated
        '''
        asset = FileAssetSource(
            source_hash=source_hash,
            executable=executable,
            file_name=file_name,
            packaging=packaging,
        )

        return typing.cast(FileAssetLocation, jsii.invoke(self, "addFileAsset", [asset]))

    @jsii.member(jsii_name="addTransform")
    def add_transform(self, transform: builtins.str) -> None:
        '''Add a Transform to this stack. A Transform is a macro that AWS CloudFormation uses to process your template.

        Duplicate values are removed when stack is synthesized.

        :param transform: The transform to add.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-section-structure.html

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            stack.add_transform("AWS::Serverless-2016-10-31")
        '''
        return typing.cast(None, jsii.invoke(self, "addTransform", [transform]))

    @jsii.member(jsii_name="allocateLogicalId")
    def _allocate_logical_id(self, cfn_element: "CfnElement") -> builtins.str:
        '''Returns the naming scheme used to allocate logical IDs.

        By default, uses
        the ``HashedAddressingScheme`` but this method can be overridden to customize
        this behavior.

        In order to make sure logical IDs are unique and stable, we hash the resource
        construct tree path (i.e. toplevel/secondlevel/.../myresource) and add it as
        a suffix to the path components joined without a separator (CloudFormation
        IDs only allow alphanumeric characters).

        The result will be:

        <path.join('')><md5(path.join('/')>
        "human"      "hash"

        If the "human" part of the ID exceeds 240 characters, we simply trim it so
        the total ID doesn't exceed CloudFormation's 255 character limit.

        We only take 8 characters from the md5 hash (0.000005 chance of collision).

        Special cases:

        - If the path only contains a single component (i.e. it's a top-level
          resource), we won't add the hash to it. The hash is not needed for
          disamiguation and also, it allows for a more straightforward migration an
          existing CloudFormation template to a CDK stack without logical ID changes
          (or renames).
        - For aesthetic reasons, if the last components of the path are the same
          (i.e. ``L1/L2/Pipeline/Pipeline``), they will be de-duplicated to make the
          resulting human portion of the ID more pleasing: ``L1L2Pipeline<HASH>``
          instead of ``L1L2PipelinePipeline<HASH>``
        - If a component is named "Default" it will be omitted from the path. This
          allows refactoring higher level abstractions around constructs without affecting
          the IDs of already deployed resources.
        - If a component is named "Resource" it will be omitted from the user-visible
          path, but included in the hash. This reduces visual noise in the human readable
          part of the identifier.

        :param cfn_element: The element for which the logical ID is allocated.
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "allocateLogicalId", [cfn_element]))

    @jsii.member(jsii_name="exportValue")
    def export_value(
        self,
        exported_value: typing.Any,
        *,
        name: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''Create a CloudFormation Export for a value.

        Returns a string representing the corresponding ``Fn.importValue()``
        expression for this Export. You can control the name for the export by
        passing the ``name`` option.

        If you don't supply a value for ``name``, the value you're exporting must be
        a Resource attribute (for example: ``bucket.bucketName``) and it will be
        given the same name as the automatic cross-stack reference that would be created
        if you used the attribute in another Stack.

        One of the uses for this method is to *remove* the relationship between
        two Stacks established by automatic cross-stack references. It will
        temporarily ensure that the CloudFormation Export still exists while you
        remove the reference from the consuming stack. After that, you can remove
        the resource and the manual export.


        Example

        Here is how the process works. Let's say there are two stacks,
        ``producerStack`` and ``consumerStack``, and ``producerStack`` has a bucket
        called ``bucket``, which is referenced by ``consumerStack`` (perhaps because
        an AWS Lambda Function writes into it, or something like that).

        It is not safe to remove ``producerStack.bucket`` because as the bucket is being
        deleted, ``consumerStack`` might still be using it.

        Instead, the process takes two deployments:


        Deployment 1: break the relationship

        - Make sure ``consumerStack`` no longer references ``bucket.bucketName`` (maybe the consumer
          stack now uses its own bucket, or it writes to an AWS DynamoDB table, or maybe you just
          remove the Lambda Function altogether).
        - In the ``ProducerStack`` class, call ``this.exportValue(this.bucket.bucketName)``. This
          will make sure the CloudFormation Export continues to exist while the relationship
          between the two stacks is being broken.
        - Deploy (this will effectively only change the ``consumerStack``, but it's safe to deploy both).



        Deployment 2: remove the bucket resource

        - You are now free to remove the ``bucket`` resource from ``producerStack``.
        - Don't forget to remove the ``exportValue()`` call as well.
        - Deploy again (this time only the ``producerStack`` will be changed -- the bucket will be deleted).

        :param exported_value: -
        :param name: The name of the export to create. Default: - A name is automatically chosen
        '''
        options = ExportValueOptions(name=name)

        return typing.cast(builtins.str, jsii.invoke(self, "exportValue", [exported_value, options]))

    @jsii.member(jsii_name="formatArn")
    def format_arn(
        self,
        *,
        resource: builtins.str,
        service: builtins.str,
        account: typing.Optional[builtins.str] = None,
        arn_format: typing.Optional[ArnFormat] = None,
        partition: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        resource_name: typing.Optional[builtins.str] = None,
        sep: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''Creates an ARN from components.

        If ``partition``, ``region`` or ``account`` are not specified, the stack's
        partition, region and account will be used.

        If any component is the empty string, an empty string will be inserted
        into the generated ARN at the location that component corresponds to.

        The ARN will be formatted as follows:

        arn:{partition}:{service}:{region}:{account}:{resource}{sep}}{resource-name}

        The required ARN pieces that are omitted will be taken from the stack that
        the 'scope' is attached to. If all ARN pieces are supplied, the supplied scope
        can be 'undefined'.

        :param resource: Resource type (e.g. "table", "autoScalingGroup", "certificate"). For some resource types, e.g. S3 buckets, this field defines the bucket name.
        :param service: The service namespace that identifies the AWS product (for example, 's3', 'iam', 'codepipline').
        :param account: The ID of the AWS account that owns the resource, without the hyphens. For example, 123456789012. Note that the ARNs for some resources don't require an account number, so this component might be omitted. Default: The account the stack is deployed to.
        :param arn_format: The specific ARN format to use for this ARN value. Default: - uses value of ``sep`` as the separator for formatting, ``ArnFormat.SLASH_RESOURCE_NAME`` if that property was also not provided
        :param partition: The partition that the resource is in. For standard AWS regions, the partition is aws. If you have resources in other partitions, the partition is aws-partitionname. For example, the partition for resources in the China (Beijing) region is aws-cn. Default: The AWS partition the stack is deployed to.
        :param region: The region the resource resides in. Note that the ARNs for some resources do not require a region, so this component might be omitted. Default: The region the stack is deployed to.
        :param resource_name: Resource name or path within the resource (i.e. S3 bucket object key) or a wildcard such as ``"*"``. This is service-dependent.
        :param sep: (deprecated) Separator between resource type and the resource. Can be either '/', ':' or an empty string. Will only be used if resourceName is defined. Default: '/'
        '''
        components = ArnComponents(
            resource=resource,
            service=service,
            account=account,
            arn_format=arn_format,
            partition=partition,
            region=region,
            resource_name=resource_name,
            sep=sep,
        )

        return typing.cast(builtins.str, jsii.invoke(self, "formatArn", [components]))

    @jsii.member(jsii_name="getLogicalId")
    def get_logical_id(self, element: "CfnElement") -> builtins.str:
        '''Allocates a stack-unique CloudFormation-compatible logical identity for a specific resource.

        This method is called when a ``CfnElement`` is created and used to render the
        initial logical identity of resources. Logical ID renames are applied at
        this stage.

        This method uses the protected method ``allocateLogicalId`` to render the
        logical ID for an element. To modify the naming scheme, extend the ``Stack``
        class and override this method.

        :param element: The CloudFormation element for which a logical identity is needed.
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "getLogicalId", [element]))

    @jsii.member(jsii_name="parseArn")
    def parse_arn(
        self,
        arn: builtins.str,
        sep_if_token: typing.Optional[builtins.str] = None,
        has_name: typing.Optional[builtins.bool] = None,
    ) -> ArnComponents:
        '''(deprecated) Given an ARN, parses it and returns components.

        IF THE ARN IS A CONCRETE STRING...

        ...it will be parsed and validated. The separator (``sep``) will be set to '/'
        if the 6th component includes a '/', in which case, ``resource`` will be set
        to the value before the '/' and ``resourceName`` will be the rest. In case
        there is no '/', ``resource`` will be set to the 6th components and
        ``resourceName`` will be set to the rest of the string.

        IF THE ARN IS A TOKEN...

        ...it cannot be validated, since we don't have the actual value yet at the
        time of this function call. You will have to supply ``sepIfToken`` and
        whether or not ARNs of the expected format usually have resource names
        in order to parse it properly. The resulting ``ArnComponents`` object will
        contain tokens for the subexpressions of the ARN, not string literals.

        If the resource name could possibly contain the separator char, the actual
        resource name cannot be properly parsed. This only occurs if the separator
        char is '/', and happens for example for S3 object ARNs, IAM Role ARNs,
        IAM OIDC Provider ARNs, etc. To properly extract the resource name from a
        Tokenized ARN, you must know the resource type and call
        ``Arn.extractResourceName``.

        :param arn: The ARN string to parse.
        :param sep_if_token: The separator used to separate resource from resourceName.
        :param has_name: Whether there is a name component in the ARN at all. For example, SNS Topics ARNs have the 'resource' component contain the topic name, and no 'resourceName' component.

        :return:

        an ArnComponents object which allows access to the various
        components of the ARN.

        :deprecated: use splitArn instead

        :stability: deprecated
        '''
        return typing.cast(ArnComponents, jsii.invoke(self, "parseArn", [arn, sep_if_token, has_name]))

    @jsii.member(jsii_name="prepareCrossReference")
    def _prepare_cross_reference(
        self,
        _source_stack: "Stack",
        reference: Reference,
    ) -> IResolvable:
        '''(deprecated) Deprecated.

        :param _source_stack: -
        :param reference: -

        :return: reference itself without any change

        :deprecated: cross reference handling has been moved to ``App.prepare()``.

        :see: https://github.com/aws/aws-cdk/pull/7187
        :stability: deprecated
        '''
        return typing.cast(IResolvable, jsii.invoke(self, "prepareCrossReference", [_source_stack, reference]))

    @jsii.member(jsii_name="renameLogicalId")
    def rename_logical_id(self, old_id: builtins.str, new_id: builtins.str) -> None:
        '''Rename a generated logical identities.

        To modify the naming scheme strategy, extend the ``Stack`` class and
        override the ``allocateLogicalId`` method.

        :param old_id: -
        :param new_id: -
        '''
        return typing.cast(None, jsii.invoke(self, "renameLogicalId", [old_id, new_id]))

    @jsii.member(jsii_name="reportMissingContext")
    def report_missing_context(
        self,
        *,
        key: builtins.str,
        props: typing.Mapping[builtins.str, typing.Any],
        provider: builtins.str,
    ) -> None:
        '''(deprecated) DEPRECATED.

        :param key: (deprecated) The missing context key.
        :param props: (deprecated) A set of provider-specific options. (This is the old untyped definition, which is necessary for backwards compatibility. See cxschema for a type definition.)
        :param provider: (deprecated) The provider from which we expect this context key to be obtained. (This is the old untyped definition, which is necessary for backwards compatibility. See cxschema for a type definition.)

        :deprecated: use ``reportMissingContextKey()``

        :stability: deprecated
        '''
        report = aws_cdk.cx_api.MissingContext(key=key, props=props, provider=provider)

        return typing.cast(None, jsii.invoke(self, "reportMissingContext", [report]))

    @jsii.member(jsii_name="reportMissingContextKey")
    def report_missing_context_key(
        self,
        *,
        key: builtins.str,
        props: typing.Union[aws_cdk.cloud_assembly_schema.AmiContextQuery, aws_cdk.cloud_assembly_schema.AvailabilityZonesContextQuery, aws_cdk.cloud_assembly_schema.HostedZoneContextQuery, aws_cdk.cloud_assembly_schema.SSMParameterContextQuery, aws_cdk.cloud_assembly_schema.VpcContextQuery, aws_cdk.cloud_assembly_schema.EndpointServiceAvailabilityZonesContextQuery, aws_cdk.cloud_assembly_schema.LoadBalancerContextQuery, aws_cdk.cloud_assembly_schema.LoadBalancerListenerContextQuery, aws_cdk.cloud_assembly_schema.SecurityGroupContextQuery],
        provider: aws_cdk.cloud_assembly_schema.ContextProvider,
    ) -> None:
        '''Indicate that a context key was expected.

        Contains instructions which will be emitted into the cloud assembly on how
        the key should be supplied.

        :param key: The missing context key.
        :param props: A set of provider-specific options.
        :param provider: The provider from which we expect this context key to be obtained.
        '''
        report = aws_cdk.cloud_assembly_schema.MissingContext(
            key=key, props=props, provider=provider
        )

        return typing.cast(None, jsii.invoke(self, "reportMissingContextKey", [report]))

    @jsii.member(jsii_name="resolve")
    def resolve(self, obj: typing.Any) -> typing.Any:
        '''Resolve a tokenized value in the context of the current stack.

        :param obj: -
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "resolve", [obj]))

    @jsii.member(jsii_name="splitArn")
    def split_arn(self, arn: builtins.str, arn_format: ArnFormat) -> ArnComponents:
        '''Splits the provided ARN into its components.

        Works both if 'arn' is a string like 'arn:aws:s3:::bucket',
        and a Token representing a dynamic CloudFormation expression
        (in which case the returned components will also be dynamic CloudFormation expressions,
        encoded as Tokens).

        :param arn: the ARN to split into its components.
        :param arn_format: the expected format of 'arn' - depends on what format the service 'arn' represents uses.
        '''
        return typing.cast(ArnComponents, jsii.invoke(self, "splitArn", [arn, arn_format]))

    @jsii.member(jsii_name="toJsonString")
    def to_json_string(
        self,
        obj: typing.Any,
        space: typing.Optional[jsii.Number] = None,
    ) -> builtins.str:
        '''Convert an object, potentially containing tokens, to a JSON string.

        :param obj: -
        :param space: -
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toJsonString", [obj, space]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="account")
    def account(self) -> builtins.str:
        '''The AWS account into which this stack will be deployed.

        This value is resolved according to the following rules:

        1. The value provided to ``env.account`` when the stack is defined. This can
           either be a concerete account (e.g. ``585695031111``) or the
           ``Aws.accountId`` token.
        2. ``Aws.accountId``, which represents the CloudFormation intrinsic reference
           ``{ "Ref": "AWS::AccountId" }`` encoded as a string token.

        Preferably, you should use the return value as an opaque string and not
        attempt to parse it to implement your logic. If you do, you must first
        check that it is a concerete value an not an unresolved token. If this
        value is an unresolved token (``Token.isUnresolved(stack.account)`` returns
        ``true``), this implies that the user wishes that this stack will synthesize
        into a **account-agnostic template**. In this case, your code should either
        fail (throw an error, emit a synth error using ``Annotations.of(construct).addError()``) or
        implement some other region-agnostic behavior.
        '''
        return typing.cast(builtins.str, jsii.get(self, "account"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="artifactId")
    def artifact_id(self) -> builtins.str:
        '''The ID of the cloud assembly artifact for this stack.'''
        return typing.cast(builtins.str, jsii.get(self, "artifactId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.List[builtins.str]:
        '''Returns the list of AZs that are available in the AWS environment (account/region) associated with this stack.

        If the stack is environment-agnostic (either account and/or region are
        tokens), this property will return an array with 2 tokens that will resolve
        at deploy-time to the first two availability zones returned from CloudFormation's
        ``Fn::GetAZs`` intrinsic function.

        If they are not available in the context, returns a set of dummy values and
        reports them as missing, and let the CLI resolve them by calling EC2
        ``DescribeAvailabilityZones`` on the target environment.

        To specify a different strategy for selecting availability zones override this method.
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "availabilityZones"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dependencies")
    def dependencies(self) -> typing.List["Stack"]:
        '''Return the stacks this stack depends on.'''
        return typing.cast(typing.List["Stack"], jsii.get(self, "dependencies"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="environment")
    def environment(self) -> builtins.str:
        '''The environment coordinates in which this stack is deployed.

        In the form
        ``aws://account/region``. Use ``stack.account`` and ``stack.region`` to obtain
        the specific values, no need to parse.

        You can use this value to determine if two stacks are targeting the same
        environment.

        If either ``stack.account`` or ``stack.region`` are not concrete values (e.g.
        ``Aws.account`` or ``Aws.region``) the special strings ``unknown-account`` and/or
        ``unknown-region`` will be used respectively to indicate this stack is
        region/account-agnostic.
        '''
        return typing.cast(builtins.str, jsii.get(self, "environment"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nested")
    def nested(self) -> builtins.bool:
        '''Indicates if this is a nested stack, in which case ``parentStack`` will include a reference to it's parent.'''
        return typing.cast(builtins.bool, jsii.get(self, "nested"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="notificationArns")
    def notification_arns(self) -> typing.List[builtins.str]:
        '''Returns the list of notification Amazon Resource Names (ARNs) for the current stack.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notificationArns"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="partition")
    def partition(self) -> builtins.str:
        '''The partition in which this stack is defined.'''
        return typing.cast(builtins.str, jsii.get(self, "partition"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        '''The AWS region into which this stack will be deployed (e.g. ``us-west-2``).

        This value is resolved according to the following rules:

        1. The value provided to ``env.region`` when the stack is defined. This can
           either be a concerete region (e.g. ``us-west-2``) or the ``Aws.region``
           token.
        2. ``Aws.region``, which is represents the CloudFormation intrinsic reference
           ``{ "Ref": "AWS::Region" }`` encoded as a string token.

        Preferably, you should use the return value as an opaque string and not
        attempt to parse it to implement your logic. If you do, you must first
        check that it is a concerete value an not an unresolved token. If this
        value is an unresolved token (``Token.isUnresolved(stack.region)`` returns
        ``true``), this implies that the user wishes that this stack will synthesize
        into a **region-agnostic template**. In this case, your code should either
        fail (throw an error, emit a synth error using ``Annotations.of(construct).addError()``) or
        implement some other region-agnostic behavior.
        '''
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stackId")
    def stack_id(self) -> builtins.str:
        '''The ID of the stack.

        Example::

            # Example automatically generated. See https://github.com/aws/jsii/issues/826
            # After resolving, looks like
            "arn:aws:cloudformation:us-west-2:123456789012:stack/teststack/51af3dc0-da77-11e4-872e-1234567db123"
        '''
        return typing.cast(builtins.str, jsii.get(self, "stackId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stackName")
    def stack_name(self) -> builtins.str:
        '''The concrete CloudFormation physical stack name.

        This is either the name defined explicitly in the ``stackName`` prop or
        allocated based on the stack's location in the construct tree. Stacks that
        are directly defined under the app use their construct ``id`` as their stack
        name. Stacks that are defined deeper within the tree will use a hashed naming
        scheme based on the construct path to ensure uniqueness.

        If you wish to obtain the deploy-time AWS::StackName intrinsic,
        you can use ``Aws.stackName`` directly.
        '''
        return typing.cast(builtins.str, jsii.get(self, "stackName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="synthesizer")
    def synthesizer(self) -> IStackSynthesizer:
        '''Synthesis method for this stack.'''
        return typing.cast(IStackSynthesizer, jsii.get(self, "synthesizer"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> TagManager:
        '''Tags to be applied to the stack.'''
        return typing.cast(TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateFile")
    def template_file(self) -> builtins.str:
        '''The name of the CloudFormation template file emitted to the output directory during synthesis.

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            "MyStack.template.json"
        '''
        return typing.cast(builtins.str, jsii.get(self, "templateFile"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateOptions")
    def template_options(self) -> ITemplateOptions:
        '''Options for CloudFormation template (like version, transform, description).'''
        return typing.cast(ITemplateOptions, jsii.get(self, "templateOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="urlSuffix")
    def url_suffix(self) -> builtins.str:
        '''The Amazon domain suffix for the region in which this stack is defined.'''
        return typing.cast(builtins.str, jsii.get(self, "urlSuffix"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nestedStackParent")
    def nested_stack_parent(self) -> typing.Optional["Stack"]:
        '''If this is a nested stack, returns it's parent stack.'''
        return typing.cast(typing.Optional["Stack"], jsii.get(self, "nestedStackParent"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nestedStackResource")
    def nested_stack_resource(self) -> typing.Optional["CfnResource"]:
        '''If this is a nested stack, this represents its ``AWS::CloudFormation::Stack`` resource.

        ``undefined`` for top-level (non-nested) stacks.
        '''
        return typing.cast(typing.Optional["CfnResource"], jsii.get(self, "nestedStackResource"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parentStack")
    def parent_stack(self) -> typing.Optional["Stack"]:
        '''(deprecated) Returns the parent of a nested stack.

        :deprecated: use ``nestedStackParent``

        :stability: deprecated
        '''
        return typing.cast(typing.Optional["Stack"], jsii.get(self, "parentStack"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="terminationProtection")
    def termination_protection(self) -> typing.Optional[builtins.bool]:
        '''Whether termination protection is enabled for this stack.'''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "terminationProtection"))


class Stage(Construct, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.Stage"):
    '''An abstract application modeling unit consisting of Stacks that should be deployed together.

    Derive a subclass of ``Stage`` and use it to model a single instance of your
    application.

    You can then instantiate your subclass multiple times to model multiple
    copies of your application which should be be deployed to different
    environments.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        env: typing.Optional[Environment] = None,
        outdir: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param env: Default AWS environment (account/region) for ``Stack``s in this ``Stage``. Stacks defined inside this ``Stage`` with either ``region`` or ``account`` missing from its env will use the corresponding field given here. If either ``region`` or ``account``is is not configured for ``Stack`` (either on the ``Stack`` itself or on the containing ``Stage``), the Stack will be *environment-agnostic*. Environment-agnostic stacks can be deployed to any environment, may not be able to take advantage of all features of the CDK. For example, they will not be able to use environmental context lookups, will not automatically translate Service Principals to the right format based on the environment's AWS partition, and other such enhancements. Default: - The environments should be configured on the ``Stack``s.
        :param outdir: The output directory into which to emit synthesized artifacts. Can only be specified if this stage is the root stage (the app). If this is specified and this stage is nested within another stage, an error will be thrown. Default: - for nested stages, outdir will be determined as a relative directory to the outdir of the app. For apps, if outdir is not specified, a temporary directory will be created.
        '''
        props = StageProps(env=env, outdir=outdir)

        jsii.create(Stage, self, [scope, id, props])

    @jsii.member(jsii_name="isStage") # type: ignore[misc]
    @builtins.classmethod
    def is_stage(cls, x: typing.Any) -> builtins.bool:
        '''Test whether the given construct is a stage.

        :param x: -
        '''
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isStage", [x]))

    @jsii.member(jsii_name="of") # type: ignore[misc]
    @builtins.classmethod
    def of(cls, construct: constructs.IConstruct) -> typing.Optional["Stage"]:
        '''Return the stage this construct is contained with, if available.

        If called
        on a nested stage, returns its parent.

        :param construct: -
        '''
        return typing.cast(typing.Optional["Stage"], jsii.sinvoke(cls, "of", [construct]))

    @jsii.member(jsii_name="synth")
    def synth(
        self,
        *,
        force: typing.Optional[builtins.bool] = None,
        skip_validation: typing.Optional[builtins.bool] = None,
        validate_on_synthesis: typing.Optional[builtins.bool] = None,
    ) -> aws_cdk.cx_api.CloudAssembly:
        '''Synthesize this stage into a cloud assembly.

        Once an assembly has been synthesized, it cannot be modified. Subsequent
        calls will return the same assembly.

        :param force: Force a re-synth, even if the stage has already been synthesized. This is used by tests to allow for incremental verification of the output. Do not use in production. Default: false
        :param skip_validation: Should we skip construct validation. Default: - false
        :param validate_on_synthesis: Whether the stack should be validated after synthesis to check for error metadata. Default: - false
        '''
        options = StageSynthesisOptions(
            force=force,
            skip_validation=skip_validation,
            validate_on_synthesis=validate_on_synthesis,
        )

        return typing.cast(aws_cdk.cx_api.CloudAssembly, jsii.invoke(self, "synth", [options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="artifactId")
    def artifact_id(self) -> builtins.str:
        '''Artifact ID of the assembly if it is a nested stage. The root stage (app) will return an empty string.

        Derived from the construct path.
        '''
        return typing.cast(builtins.str, jsii.get(self, "artifactId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assetOutdir")
    def asset_outdir(self) -> builtins.str:
        '''The cloud assembly asset output directory.'''
        return typing.cast(builtins.str, jsii.get(self, "assetOutdir"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outdir")
    def outdir(self) -> builtins.str:
        '''The cloud assembly output directory.'''
        return typing.cast(builtins.str, jsii.get(self, "outdir"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stageName")
    def stage_name(self) -> builtins.str:
        '''The name of the stage.

        Based on names of the parent stages separated by
        hypens.
        '''
        return typing.cast(builtins.str, jsii.get(self, "stageName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="account")
    def account(self) -> typing.Optional[builtins.str]:
        '''The default account for all resources defined within this stage.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "account"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parentStage")
    def parent_stage(self) -> typing.Optional["Stage"]:
        '''The parent stage or ``undefined`` if this is the app.

        -
        '''
        return typing.cast(typing.Optional["Stage"], jsii.get(self, "parentStage"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        '''The default region for all resources defined within this stage.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))


class App(Stage, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.App"):
    '''A construct which represents an entire CDK app. This construct is normally the root of the construct tree.

    You would normally define an ``App`` instance in your program's entrypoint,
    then define constructs where the app is used as the parent scope.

    After all the child constructs are defined within the app, you should call
    ``app.synth()`` which will emit a "cloud assembly" from this app into the
    directory specified by ``outdir``. Cloud assemblies includes artifacts such as
    CloudFormation templates and assets that are needed to deploy this app into
    the AWS cloud.

    :see: https://docs.aws.amazon.com/cdk/latest/guide/apps.html
    '''

    def __init__(
        self,
        *,
        analytics_reporting: typing.Optional[builtins.bool] = None,
        auto_synth: typing.Optional[builtins.bool] = None,
        context: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        outdir: typing.Optional[builtins.str] = None,
        runtime_info: typing.Optional[builtins.bool] = None,
        stack_traces: typing.Optional[builtins.bool] = None,
        tree_metadata: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Initializes a CDK application.

        :param analytics_reporting: Include runtime versioning information in the Stacks of this app. Default: Value of 'aws:cdk:version-reporting' context key
        :param auto_synth: Automatically call ``synth()`` before the program exits. If you set this, you don't have to call ``synth()`` explicitly. Note that this feature is only available for certain programming languages, and calling ``synth()`` is still recommended. Default: true if running via CDK CLI (``CDK_OUTDIR`` is set), ``false`` otherwise
        :param context: Additional context values for the application. Context set by the CLI or the ``context`` key in ``cdk.json`` has precedence. Context can be read from any construct using ``node.getContext(key)``. Default: - no additional context
        :param outdir: The output directory into which to emit synthesized artifacts. Default: - If this value is *not* set, considers the environment variable ``CDK_OUTDIR``. If ``CDK_OUTDIR`` is not defined, uses a temp directory.
        :param runtime_info: (deprecated) Include runtime versioning information in the Stacks of this app. Default: Value of 'aws:cdk:version-reporting' context key
        :param stack_traces: Include construct creation stack trace in the ``aws:cdk:trace`` metadata key of all constructs. Default: true stack traces are included unless ``aws:cdk:disable-stack-trace`` is set in the context.
        :param tree_metadata: Include construct tree metadata as part of the Cloud Assembly. Default: true
        '''
        props = AppProps(
            analytics_reporting=analytics_reporting,
            auto_synth=auto_synth,
            context=context,
            outdir=outdir,
            runtime_info=runtime_info,
            stack_traces=stack_traces,
            tree_metadata=tree_metadata,
        )

        jsii.create(App, self, [props])

    @jsii.member(jsii_name="isApp") # type: ignore[misc]
    @builtins.classmethod
    def is_app(cls, obj: typing.Any) -> builtins.bool:
        '''Checks if an object is an instance of the ``App`` class.

        :param obj: The object to evaluate.

        :return: ``true`` if ``obj`` is an ``App``.
        '''
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isApp", [obj]))


class AssetStaging(
    Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.AssetStaging",
):
    '''Stages a file or directory from a location on the file system into a staging directory.

    This is controlled by the context key 'aws:cdk:asset-staging' and enabled
    by the CLI by default in order to ensure that when the CDK app exists, all
    assets are available for deployment. Otherwise, if an app references assets
    in temporary locations, those will not be available when it exists (see
    https://github.com/aws/aws-cdk/issues/1716).

    The ``stagedPath`` property is a stringified token that represents the location
    of the file or directory after staging. It will be resolved only during the
    "prepare" stage and may be either the original path or the staged path
    depending on the context setting.

    The file/directory are staged based on their content hash (fingerprint). This
    means that only if content was changed, copy will happen.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        source_path: builtins.str,
        extra_hash: typing.Optional[builtins.str] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[AssetHashType] = None,
        bundling: typing.Optional[BundlingOptions] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow: typing.Optional[SymlinkFollowMode] = None,
        ignore_mode: typing.Optional[IgnoreMode] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param source_path: The source file or directory to copy from.
        :param extra_hash: Extra information to encode into the fingerprint (e.g. build instructions and other inputs). Default: - hash is only based on source content
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container or a custom bundling provider. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        :param exclude: Glob patterns to exclude from the copy. Default: - nothing is excluded
        :param follow: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for exclude patterns. Default: IgnoreMode.GLOB
        '''
        props = AssetStagingProps(
            source_path=source_path,
            extra_hash=extra_hash,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
            exclude=exclude,
            follow=follow,
            ignore_mode=ignore_mode,
        )

        jsii.create(AssetStaging, self, [scope, id, props])

    @jsii.member(jsii_name="clearAssetHashCache") # type: ignore[misc]
    @builtins.classmethod
    def clear_asset_hash_cache(cls) -> None:
        '''Clears the asset hash cache.'''
        return typing.cast(None, jsii.sinvoke(cls, "clearAssetHashCache", []))

    @jsii.member(jsii_name="relativeStagedPath")
    def relative_staged_path(self, stack: Stack) -> builtins.str:
        '''Return the path to the staged asset, relative to the Cloud Assembly (manifest) directory of the given stack.

        Only returns a relative path if the asset was staged, returns an absolute path if
        it was not staged.

        A bundled asset might end up in the outDir and still not count as
        "staged"; if asset staging is disabled we're technically expected to
        reference source directories, but we don't have a source directory for the
        bundled outputs (as the bundle output is written to a temporary
        directory). Nevertheless, we will still return an absolute path.

        A non-obvious directory layout may look like this::

              CLOUD ASSEMBLY ROOT
                +-- asset.12345abcdef/
                +-- assembly-Stage
                      +-- MyStack.template.json
                      +-- MyStack.assets.json <- will contain { "path": "../asset.12345abcdef" }

        :param stack: -
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "relativeStagedPath", [stack]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="BUNDLING_INPUT_DIR")
    def BUNDLING_INPUT_DIR(cls) -> builtins.str:
        '''The directory inside the bundling container into which the asset sources will be mounted.'''
        return typing.cast(builtins.str, jsii.sget(cls, "BUNDLING_INPUT_DIR"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="BUNDLING_OUTPUT_DIR")
    def BUNDLING_OUTPUT_DIR(cls) -> builtins.str:
        '''The directory inside the bundling container into which the bundled output should be written.'''
        return typing.cast(builtins.str, jsii.sget(cls, "BUNDLING_OUTPUT_DIR"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="absoluteStagedPath")
    def absolute_staged_path(self) -> builtins.str:
        '''Absolute path to the asset data.

        If asset staging is disabled, this will just be the source path or
        a temporary directory used for bundling.

        If asset staging is enabled it will be the staged path.

        IMPORTANT: If you are going to call ``addFileAsset()``, use
        ``relativeStagedPath()`` instead.
        '''
        return typing.cast(builtins.str, jsii.get(self, "absoluteStagedPath"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assetHash")
    def asset_hash(self) -> builtins.str:
        '''A cryptographic hash of the asset.'''
        return typing.cast(builtins.str, jsii.get(self, "assetHash"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="isArchive")
    def is_archive(self) -> builtins.bool:
        '''Whether this asset is an archive (zip or jar).'''
        return typing.cast(builtins.bool, jsii.get(self, "isArchive"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="packaging")
    def packaging(self) -> FileAssetPackaging:
        '''How this asset should be packaged.'''
        return typing.cast(FileAssetPackaging, jsii.get(self, "packaging"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceHash")
    def source_hash(self) -> builtins.str:
        '''(deprecated) A cryptographic hash of the asset.

        :deprecated: see ``assetHash``.

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.get(self, "sourceHash"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourcePath")
    def source_path(self) -> builtins.str:
        '''The absolute path of the asset as it was referenced by the user.'''
        return typing.cast(builtins.str, jsii.get(self, "sourcePath"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stagedPath")
    def staged_path(self) -> builtins.str:
        '''(deprecated) Absolute path to the asset data.

        If asset staging is disabled, this will just be the source path or
        a temporary directory used for bundling.

        If asset staging is enabled it will be the staged path.

        IMPORTANT: If you are going to call ``addFileAsset()``, use
        ``relativeStagedPath()`` instead.

        :deprecated: - Use ``absoluteStagedPath`` instead.

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.get(self, "stagedPath"))


class CfnElement(
    Construct,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/core.CfnElement",
):
    '''An element of a CloudFormation stack.'''

    def __init__(self, scope: constructs.Construct, id: builtins.str) -> None:
        '''Creates an entity and binds it to a tree.

        Note that the root of the tree must be a Stack object (not just any Root).

        :param scope: The parent construct.
        :param id: -
        '''
        jsii.create(CfnElement, self, [scope, id])

    @jsii.member(jsii_name="isCfnElement") # type: ignore[misc]
    @builtins.classmethod
    def is_cfn_element(cls, x: typing.Any) -> builtins.bool:
        '''Returns ``true`` if a construct is a stack element (i.e. part of the synthesized cloudformation template).

        Uses duck-typing instead of ``instanceof`` to allow stack elements from different
        versions of this library to be included in the same stack.

        :param x: -

        :return: The construct as a stack element or undefined if it is not a stack element.
        '''
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnElement", [x]))

    @jsii.member(jsii_name="overrideLogicalId")
    def override_logical_id(self, new_logical_id: builtins.str) -> None:
        '''Overrides the auto-generated logical ID with a specific ID.

        :param new_logical_id: The new logical ID to use for this stack element.
        '''
        return typing.cast(None, jsii.invoke(self, "overrideLogicalId", [new_logical_id]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="creationStack")
    def creation_stack(self) -> typing.List[builtins.str]:
        '''
        :return:

        the stack trace of the point where this Resource was created from, sourced
        from the +metadata+ entry typed +aws:cdk:logicalId+, and with the bottom-most
        node +internal+ entries filtered.
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "creationStack"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logicalId")
    def logical_id(self) -> builtins.str:
        '''The logical ID for this CloudFormation stack element.

        The logical ID of the element
        is calculated from the path of the resource node in the construct tree.

        To override this value, use ``overrideLogicalId(newLogicalId)``.

        :return:

        the logical ID as a stringified token. This value will only get
        resolved during synthesis.
        '''
        return typing.cast(builtins.str, jsii.get(self, "logicalId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stack")
    def stack(self) -> Stack:
        '''The stack in which this element is defined.

        CfnElements must be defined within a stack scope (directly or indirectly).
        '''
        return typing.cast(Stack, jsii.get(self, "stack"))


class _CfnElementProxy(CfnElement):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, CfnElement).__jsii_proxy_class__ = lambda : _CfnElementProxy


class CfnHook(CfnElement, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.CfnHook"):
    '''Represents a CloudFormation resource.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        type: builtins.str,
        properties: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''Creates a new Hook object.

        :param scope: -
        :param id: -
        :param type: The type of the hook (for example, "AWS::CodeDeploy::BlueGreen").
        :param properties: The properties of the hook. Default: - no properties
        '''
        props = CfnHookProps(type=type, properties=properties)

        jsii.create(CfnHook, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], jsii.invoke(self, "renderProperties", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of the hook (for example, "AWS::CodeDeploy::BlueGreen").'''
        return typing.cast(builtins.str, jsii.get(self, "type"))


class CfnInclude(
    CfnElement,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnInclude",
):
    '''(deprecated) Includes a CloudFormation template into a stack.

    All elements of the template will be merged into
    the current stack, together with any elements created programmatically.

    :deprecated: use the CfnInclude class from the cloudformation-include module instead

    :stability: deprecated
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        template: typing.Mapping[typing.Any, typing.Any],
    ) -> None:
        '''(deprecated) Creates an adopted template construct.

        The template will be incorporated into the stack as-is with no changes at all.
        This means that logical IDs of entities within this template may conflict with logical IDs of entities that are part of the
        stack.

        :param scope: The parent construct of this template.
        :param id: The ID of this construct.
        :param template: (deprecated) The CloudFormation template to include in the stack (as is).

        :stability: deprecated
        '''
        props = CfnIncludeProps(template=template)

        jsii.create(CfnInclude, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="template")
    def template(self) -> typing.Mapping[typing.Any, typing.Any]:
        '''(deprecated) The included template.

        :stability: deprecated
        '''
        return typing.cast(typing.Mapping[typing.Any, typing.Any], jsii.get(self, "template"))


@jsii.implements(IResolvable)
class CfnJson(Construct, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/core.CfnJson"):
    '''Captures a synthesis-time JSON object a CloudFormation reference which resolves during deployment to the resolved values of the JSON object.

    The main use case for this is to overcome a limitation in CloudFormation that
    does not allow using intrinsic functions as dictionary keys (because
    dictionary keys in JSON must be strings). Specifically this is common in IAM
    conditions such as ``StringEquals: { lhs: "rhs" }`` where you want "lhs" to be
    a reference.

    This object is resolvable, so it can be used as a value.

    This construct is backed by a custom resource.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        value: typing.Any,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param value: The value to resolve. Can be any JavaScript object, including tokens and references in keys or values.
        '''
        props = CfnJsonProps(value=value)

        jsii.create(CfnJson, self, [scope, id, props])

    @jsii.member(jsii_name="resolve")
    def resolve(self, _: IResolveContext) -> typing.Any:
        '''Produce the Token's value at resolution time.

        :param _: -
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "resolve", [_]))

    @jsii.member(jsii_name="toJSON")
    def to_json(self) -> builtins.str:
        '''This is required in case someone JSON.stringifys an object which refrences this object. Otherwise, we'll get a cyclic JSON reference.'''
        return typing.cast(builtins.str, jsii.invoke(self, "toJSON", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="creationStack")
    def creation_stack(self) -> typing.List[builtins.str]:
        '''The creation stack of this resolvable which will be appended to errors thrown during resolution.

        This may return an array with a single informational element indicating how
        to get this property populated, if it was skipped for performance reasons.
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "creationStack"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> Reference:
        '''An Fn::GetAtt to the JSON object passed through ``value`` and resolved during synthesis.

        Normally there is no need to use this property since ``CfnJson`` is an
        IResolvable, so it can be simply used as a value.
        '''
        return typing.cast(Reference, jsii.get(self, "value"))


class CfnOutput(
    CfnElement,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnOutput",
):
    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        value: builtins.str,
        condition: typing.Optional["CfnCondition"] = None,
        description: typing.Optional[builtins.str] = None,
        export_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Creates an CfnOutput value for this stack.

        :param scope: The parent construct.
        :param id: -
        :param value: The value of the property returned by the aws cloudformation describe-stacks command. The value of an output can include literals, parameter references, pseudo-parameters, a mapping value, or intrinsic functions.
        :param condition: A condition to associate with this output value. If the condition evaluates to ``false``, this output value will not be included in the stack. Default: - No condition is associated with the output.
        :param description: A String type that describes the output value. The description can be a maximum of 4 K in length. Default: - No description.
        :param export_name: The name used to export the value of this output across stacks. To import the value from another stack, use ``Fn.importValue(exportName)``. Default: - the output is not exported
        '''
        props = CfnOutputProps(
            value=value,
            condition=condition,
            description=description,
            export_name=export_name,
        )

        jsii.create(CfnOutput, self, [scope, id, props])

    @jsii.member(jsii_name="validate")
    def _validate(self) -> typing.List[builtins.str]:
        '''Validate the current construct.

        This method can be implemented by derived constructs in order to perform
        validation logic. It is called on all constructs before synthesis.
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "validate", []))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="importValue")
    def import_value(self) -> builtins.str:
        '''Return the ``Fn.importValue`` expression to import this value into another stack.

        The returned value should not be used in the same stack, but in a
        different one. It must be deployed to the same environment, as
        CloudFormation exports can only be imported in the same Region and
        account.

        The is no automatic registration of dependencies between stacks when using
        this mechanism, so you should make sure to deploy them in the right order
        yourself.

        You can use this mechanism to share values across Stacks in different
        Stages. If you intend to share the value to another Stack inside the same
        Stage, the automatic cross-stack referencing mechanism is more convenient.
        '''
        return typing.cast(builtins.str, jsii.get(self, "importValue"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Any:
        '''The value of the property returned by the aws cloudformation describe-stacks command.

        The value of an output can include literals, parameter references, pseudo-parameters,
        a mapping value, or intrinsic functions.
        '''
        return typing.cast(typing.Any, jsii.get(self, "value"))

    @value.setter
    def value(self, value: typing.Any) -> None:
        jsii.set(self, "value", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="condition")
    def condition(self) -> typing.Optional["CfnCondition"]:
        '''A condition to associate with this output value.

        If the condition evaluates
        to ``false``, this output value will not be included in the stack.

        :default: - No condition is associated with the output.
        '''
        return typing.cast(typing.Optional["CfnCondition"], jsii.get(self, "condition"))

    @condition.setter
    def condition(self, value: typing.Optional["CfnCondition"]) -> None:
        jsii.set(self, "condition", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A String type that describes the output value.

        The description can be a maximum of 4 K in length.

        :default: - No description.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="exportName")
    def export_name(self) -> typing.Optional[builtins.str]:
        '''The name used to export the value of this output across stacks.

        To use the value in another stack, pass the value of
        ``output.importValue`` to it.

        :default: - the output is not exported
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exportName"))

    @export_name.setter
    def export_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "exportName", value)


class CfnParameter(
    CfnElement,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnParameter",
):
    '''A CloudFormation parameter.

    Use the optional Parameters section to customize your templates.
    Parameters enable you to input custom values to your template each time you create or
    update a stack.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        allowed_pattern: typing.Optional[builtins.str] = None,
        allowed_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        constraint_description: typing.Optional[builtins.str] = None,
        default: typing.Any = None,
        description: typing.Optional[builtins.str] = None,
        max_length: typing.Optional[jsii.Number] = None,
        max_value: typing.Optional[jsii.Number] = None,
        min_length: typing.Optional[jsii.Number] = None,
        min_value: typing.Optional[jsii.Number] = None,
        no_echo: typing.Optional[builtins.bool] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Creates a parameter construct.

        Note that the name (logical ID) of the parameter will derive from it's ``coname`` and location
        within the stack. Therefore, it is recommended that parameters are defined at the stack level.

        :param scope: The parent construct.
        :param id: -
        :param allowed_pattern: A regular expression that represents the patterns to allow for String types. Default: - No constraints on patterns allowed for parameter.
        :param allowed_values: An array containing the list of values allowed for the parameter. Default: - No constraints on values allowed for parameter.
        :param constraint_description: A string that explains a constraint when the constraint is violated. For example, without a constraint description, a parameter that has an allowed pattern of [A-Za-z0-9]+ displays the following error message when the user specifies an invalid value: Default: - No description with customized error message when user specifies invalid values.
        :param default: A value of the appropriate type for the template to use if no value is specified when a stack is created. If you define constraints for the parameter, you must specify a value that adheres to those constraints. Default: - No default value for parameter.
        :param description: A string of up to 4000 characters that describes the parameter. Default: - No description for the parameter.
        :param max_length: An integer value that determines the largest number of characters you want to allow for String types. Default: - None.
        :param max_value: A numeric value that determines the largest numeric value you want to allow for Number types. Default: - None.
        :param min_length: An integer value that determines the smallest number of characters you want to allow for String types. Default: - None.
        :param min_value: A numeric value that determines the smallest numeric value you want to allow for Number types. Default: - None.
        :param no_echo: Whether to mask the parameter value when anyone makes a call that describes the stack. If you set the value to ``true``, the parameter value is masked with asterisks (``*****``). Default: - Parameter values are not masked.
        :param type: The data type for the parameter (DataType). Default: String
        '''
        props = CfnParameterProps(
            allowed_pattern=allowed_pattern,
            allowed_values=allowed_values,
            constraint_description=constraint_description,
            default=default,
            description=description,
            max_length=max_length,
            max_value=max_value,
            min_length=min_length,
            min_value=min_value,
            no_echo=no_echo,
            type=type,
        )

        jsii.create(CfnParameter, self, [scope, id, props])

    @jsii.member(jsii_name="resolve")
    def resolve(self, _context: IResolveContext) -> typing.Any:
        '''
        :param _context: -
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "resolve", [_context]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="value")
    def value(self) -> IResolvable:
        '''The parameter value as a Token.'''
        return typing.cast(IResolvable, jsii.get(self, "value"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="valueAsList")
    def value_as_list(self) -> typing.List[builtins.str]:
        '''The parameter value, if it represents a string list.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "valueAsList"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="valueAsNumber")
    def value_as_number(self) -> jsii.Number:
        '''The parameter value, if it represents a number.'''
        return typing.cast(jsii.Number, jsii.get(self, "valueAsNumber"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="valueAsString")
    def value_as_string(self) -> builtins.str:
        '''The parameter value, if it represents a string.'''
        return typing.cast(builtins.str, jsii.get(self, "valueAsString"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="default")
    def default(self) -> typing.Any:
        '''A value of the appropriate type for the template to use if no value is specified when a stack is created.

        If you define constraints for the parameter, you must specify
        a value that adheres to those constraints.

        :default: - No default value for parameter.
        '''
        return typing.cast(typing.Any, jsii.get(self, "default"))

    @default.setter
    def default(self, value: typing.Any) -> None:
        jsii.set(self, "default", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="noEcho")
    def no_echo(self) -> builtins.bool:
        '''Indicates if this parameter is configured with "NoEcho" enabled.'''
        return typing.cast(builtins.bool, jsii.get(self, "noEcho"))

    @no_echo.setter
    def no_echo(self, value: builtins.bool) -> None:
        jsii.set(self, "noEcho", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The data type for the parameter (DataType).

        :default: String
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="allowedPattern")
    def allowed_pattern(self) -> typing.Optional[builtins.str]:
        '''A regular expression that represents the patterns to allow for String types.

        :default: - No constraints on patterns allowed for parameter.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allowedPattern"))

    @allowed_pattern.setter
    def allowed_pattern(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "allowedPattern", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="allowedValues")
    def allowed_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array containing the list of values allowed for the parameter.

        :default: - No constraints on values allowed for parameter.
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedValues"))

    @allowed_values.setter
    def allowed_values(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "allowedValues", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="constraintDescription")
    def constraint_description(self) -> typing.Optional[builtins.str]:
        '''A string that explains a constraint when the constraint is violated.

        For example, without a constraint description, a parameter that has an allowed
        pattern of [A-Za-z0-9]+ displays the following error message when the user specifies
        an invalid value:

        :default: - No description with customized error message when user specifies invalid values.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "constraintDescription"))

    @constraint_description.setter
    def constraint_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "constraintDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A string of up to 4000 characters that describes the parameter.

        :default: - No description for the parameter.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxLength")
    def max_length(self) -> typing.Optional[jsii.Number]:
        '''An integer value that determines the largest number of characters you want to allow for String types.

        :default: - None.
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxLength"))

    @max_length.setter
    def max_length(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "maxLength", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maxValue")
    def max_value(self) -> typing.Optional[jsii.Number]:
        '''A numeric value that determines the largest numeric value you want to allow for Number types.

        :default: - None.
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxValue"))

    @max_value.setter
    def max_value(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "maxValue", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="minLength")
    def min_length(self) -> typing.Optional[jsii.Number]:
        '''An integer value that determines the smallest number of characters you want to allow for String types.

        :default: - None.
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minLength"))

    @min_length.setter
    def min_length(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "minLength", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="minValue")
    def min_value(self) -> typing.Optional[jsii.Number]:
        '''A numeric value that determines the smallest numeric value you want to allow for Number types.

        :default: - None.
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minValue"))

    @min_value.setter
    def min_value(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "minValue", value)


class CfnRefElement(
    CfnElement,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/core.CfnRefElement",
):
    '''Base class for referenceable CloudFormation constructs which are not Resources.

    These constructs are things like Conditions and Parameters, can be
    referenced by taking the ``.ref`` attribute.

    Resource constructs do not inherit from CfnRefElement because they have their
    own, more specific types returned from the .ref attribute. Also, some
    resources aren't referenceable at all (such as BucketPolicies or GatewayAttachments).
    '''

    def __init__(self, scope: constructs.Construct, id: builtins.str) -> None:
        '''Creates an entity and binds it to a tree.

        Note that the root of the tree must be a Stack object (not just any Root).

        :param scope: The parent construct.
        :param id: -
        '''
        jsii.create(CfnRefElement, self, [scope, id])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ref")
    def ref(self) -> builtins.str:
        '''Return a string that will be resolved to a CloudFormation ``{ Ref }`` for this element.

        If, by any chance, the intrinsic reference of a resource is not a string, you could
        coerce it to an IResolvable through ``Lazy.any({ produce: resource.ref })``.
        '''
        return typing.cast(builtins.str, jsii.get(self, "ref"))


class _CfnRefElementProxy(
    CfnRefElement, jsii.proxy_for(CfnElement) # type: ignore[misc]
):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, CfnRefElement).__jsii_proxy_class__ = lambda : _CfnRefElementProxy


class CfnResource(
    CfnRefElement,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnResource",
):
    '''Represents a CloudFormation resource.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        type: builtins.str,
        properties: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> None:
        '''Creates a resource construct.

        :param scope: -
        :param id: -
        :param type: CloudFormation resource type (e.g. ``AWS::S3::Bucket``).
        :param properties: Resource properties. Default: - No resource properties.
        '''
        props = CfnResourceProps(type=type, properties=properties)

        jsii.create(CfnResource, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnResource") # type: ignore[misc]
    @builtins.classmethod
    def is_cfn_resource(cls, construct: constructs.IConstruct) -> builtins.bool:
        '''Check whether the given construct is a CfnResource.

        :param construct: -
        '''
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnResource", [construct]))

    @jsii.member(jsii_name="addDeletionOverride")
    def add_deletion_override(self, path: builtins.str) -> None:
        '''Syntactic sugar for ``addOverride(path, undefined)``.

        :param path: The path of the value to delete.
        '''
        return typing.cast(None, jsii.invoke(self, "addDeletionOverride", [path]))

    @jsii.member(jsii_name="addDependsOn")
    def add_depends_on(self, target: "CfnResource") -> None:
        '''Indicates that this resource depends on another resource and cannot be provisioned unless the other resource has been successfully provisioned.

        This can be used for resources across stacks (or nested stack) boundaries
        and the dependency will automatically be transferred to the relevant scope.

        :param target: -
        '''
        return typing.cast(None, jsii.invoke(self, "addDependsOn", [target]))

    @jsii.member(jsii_name="addMetadata")
    def add_metadata(self, key: builtins.str, value: typing.Any) -> None:
        '''Add a value to the CloudFormation Resource Metadata.

        :param key: -
        :param value: -

        :see:

        https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html

        Note that this is a different set of metadata from CDK node metadata; this
        metadata ends up in the stack template under the resource, whereas CDK
        node metadata ends up in the Cloud Assembly.
        '''
        return typing.cast(None, jsii.invoke(self, "addMetadata", [key, value]))

    @jsii.member(jsii_name="addOverride")
    def add_override(self, path: builtins.str, value: typing.Any) -> None:
        '''Adds an override to the synthesized CloudFormation resource.

        To add a
        property override, either use ``addPropertyOverride`` or prefix ``path`` with
        "Properties." (i.e. ``Properties.TopicName``).

        If the override is nested, separate each nested level using a dot (.) in the path parameter.
        If there is an array as part of the nesting, specify the index in the path.

        To include a literal ``.`` in the property name, prefix with a ``\\``. In most
        programming languages you will need to write this as ``"\\\\."`` because the
        ``\\`` itself will need to be escaped.

        For example::

           # Example automatically generated. See https://github.com/aws/jsii/issues/826
           cfn_resource.add_override("Properties.GlobalSecondaryIndexes.0.Projection.NonKeyAttributes", ["myattribute"])
           cfn_resource.add_override("Properties.GlobalSecondaryIndexes.1.ProjectionType", "INCLUDE")

        would add the overrides Example::

           "Properties": {
              "GlobalSecondaryIndexes": [
                {
                  "Projection": {
                    "NonKeyAttributes": [ "myattribute" ]
                    ...
                  }
                  ...
                },
                {
                  "ProjectionType": "INCLUDE"
                  ...
                },
              ]
              ...
           }

        :param path: - The path of the property, you can use dot notation to override values in complex types. Any intermdediate keys will be created as needed.
        :param value: - The value. Could be primitive or complex.
        '''
        return typing.cast(None, jsii.invoke(self, "addOverride", [path, value]))

    @jsii.member(jsii_name="addPropertyDeletionOverride")
    def add_property_deletion_override(self, property_path: builtins.str) -> None:
        '''Adds an override that deletes the value of a property from the resource definition.

        :param property_path: The path to the property.
        '''
        return typing.cast(None, jsii.invoke(self, "addPropertyDeletionOverride", [property_path]))

    @jsii.member(jsii_name="addPropertyOverride")
    def add_property_override(
        self,
        property_path: builtins.str,
        value: typing.Any,
    ) -> None:
        '''Adds an override to a resource property.

        Syntactic sugar for ``addOverride("Properties.<...>", value)``.

        :param property_path: The path of the property.
        :param value: The value.
        '''
        return typing.cast(None, jsii.invoke(self, "addPropertyOverride", [property_path, value]))

    @jsii.member(jsii_name="applyRemovalPolicy")
    def apply_removal_policy(
        self,
        policy: typing.Optional[RemovalPolicy] = None,
        *,
        apply_to_update_replace_policy: typing.Optional[builtins.bool] = None,
        default: typing.Optional[RemovalPolicy] = None,
    ) -> None:
        '''Sets the deletion policy of the resource based on the removal policy specified.

        :param policy: -
        :param apply_to_update_replace_policy: Apply the same deletion policy to the resource's "UpdateReplacePolicy". Default: true
        :param default: The default policy to apply in case the removal policy is not defined. Default: - Default value is resource specific. To determine the default value for a resoure, please consult that specific resource's documentation.
        '''
        options = RemovalPolicyOptions(
            apply_to_update_replace_policy=apply_to_update_replace_policy,
            default=default,
        )

        return typing.cast(None, jsii.invoke(self, "applyRemovalPolicy", [policy, options]))

    @jsii.member(jsii_name="getAtt")
    def get_att(self, attribute_name: builtins.str) -> Reference:
        '''Returns a token for an runtime attribute of this resource.

        Ideally, use generated attribute accessors (e.g. ``resource.arn``), but this can be used for future compatibility
        in case there is no generated attribute.

        :param attribute_name: The name of the attribute.
        '''
        return typing.cast(Reference, jsii.invoke(self, "getAtt", [attribute_name]))

    @jsii.member(jsii_name="getMetadata")
    def get_metadata(self, key: builtins.str) -> typing.Any:
        '''Retrieve a value value from the CloudFormation Resource Metadata.

        :param key: -

        :see:

        https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/metadata-section-structure.html

        Note that this is a different set of metadata from CDK node metadata; this
        metadata ends up in the stack template under the resource, whereas CDK
        node metadata ends up in the Cloud Assembly.
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "getMetadata", [key]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.member(jsii_name="shouldSynthesize")
    def _should_synthesize(self) -> builtins.bool:
        '''Can be overridden by subclasses to determine if this resource will be rendered into the cloudformation template.

        :return:

        ``true`` if the resource should be included or ``false`` is the resource
        should be omitted.
        '''
        return typing.cast(builtins.bool, jsii.invoke(self, "shouldSynthesize", []))

    @jsii.member(jsii_name="toString")
    def to_string(self) -> builtins.str:
        '''Returns a string representation of this construct.

        :return: a string representation of this resource
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "toString", []))

    @jsii.member(jsii_name="validateProperties")
    def _validate_properties(self, _properties: typing.Any) -> None:
        '''
        :param _properties: -
        '''
        return typing.cast(None, jsii.invoke(self, "validateProperties", [_properties]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnOptions")
    def cfn_options(self) -> ICfnResourceOptions:
        '''Options for this resource, such as condition, update policy etc.'''
        return typing.cast(ICfnResourceOptions, jsii.get(self, "cfnOptions"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnResourceType")
    def cfn_resource_type(self) -> builtins.str:
        '''AWS resource type.'''
        return typing.cast(builtins.str, jsii.get(self, "cfnResourceType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="updatedProperites")
    def _updated_properites(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''Return properties modified after initiation.

        Resources that expose mutable properties should override this function to
        collect and return the properties object for this resource.
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "updatedProperites"))


@jsii.implements(IInspectable)
class CfnResourceDefaultVersion(
    CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnResourceDefaultVersion",
):
    '''A CloudFormation ``AWS::CloudFormation::ResourceDefaultVersion``.

    :cloudformationResource: AWS::CloudFormation::ResourceDefaultVersion
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html
    '''

    def __init__(
        self,
        scope: Construct,
        id: builtins.str,
        *,
        type_name: typing.Optional[builtins.str] = None,
        type_version_arn: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::ResourceDefaultVersion``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param type_name: ``AWS::CloudFormation::ResourceDefaultVersion.TypeName``.
        :param type_version_arn: ``AWS::CloudFormation::ResourceDefaultVersion.TypeVersionArn``.
        :param version_id: ``AWS::CloudFormation::ResourceDefaultVersion.VersionId``.
        '''
        props = CfnResourceDefaultVersionProps(
            type_name=type_name,
            type_version_arn=type_version_arn,
            version_id=version_id,
        )

        jsii.create(CfnResourceDefaultVersion, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ResourceDefaultVersion.TypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html#cfn-cloudformation-resourcedefaultversion-typename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "typeName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="typeVersionArn")
    def type_version_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ResourceDefaultVersion.TypeVersionArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html#cfn-cloudformation-resourcedefaultversion-typeversionarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeVersionArn"))

    @type_version_arn.setter
    def type_version_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "typeVersionArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ResourceDefaultVersion.VersionId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourcedefaultversion.html#cfn-cloudformation-resourcedefaultversion-versionid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionId"))

    @version_id.setter
    def version_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "versionId", value)


@jsii.implements(IInspectable)
class CfnResourceVersion(
    CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnResourceVersion",
):
    '''A CloudFormation ``AWS::CloudFormation::ResourceVersion``.

    :cloudformationResource: AWS::CloudFormation::ResourceVersion
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html
    '''

    def __init__(
        self,
        scope: Construct,
        id: builtins.str,
        *,
        schema_handler_package: builtins.str,
        type_name: builtins.str,
        execution_role_arn: typing.Optional[builtins.str] = None,
        logging_config: typing.Optional[typing.Union[IResolvable, "CfnResourceVersion.LoggingConfigProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::ResourceVersion``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param schema_handler_package: ``AWS::CloudFormation::ResourceVersion.SchemaHandlerPackage``.
        :param type_name: ``AWS::CloudFormation::ResourceVersion.TypeName``.
        :param execution_role_arn: ``AWS::CloudFormation::ResourceVersion.ExecutionRoleArn``.
        :param logging_config: ``AWS::CloudFormation::ResourceVersion.LoggingConfig``.
        '''
        props = CfnResourceVersionProps(
            schema_handler_package=schema_handler_package,
            type_name=type_name,
            execution_role_arn=execution_role_arn,
            logging_config=logging_config,
        )

        jsii.create(CfnResourceVersion, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIsDefaultVersion")
    def attr_is_default_version(self) -> IResolvable:
        '''
        :cloudformationAttribute: IsDefaultVersion
        '''
        return typing.cast(IResolvable, jsii.get(self, "attrIsDefaultVersion"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrProvisioningType")
    def attr_provisioning_type(self) -> builtins.str:
        '''
        :cloudformationAttribute: ProvisioningType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProvisioningType"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrTypeArn")
    def attr_type_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: TypeArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTypeArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVersionId")
    def attr_version_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: VersionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersionId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVisibility")
    def attr_visibility(self) -> builtins.str:
        '''
        :cloudformationAttribute: Visibility
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVisibility"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="schemaHandlerPackage")
    def schema_handler_package(self) -> builtins.str:
        '''``AWS::CloudFormation::ResourceVersion.SchemaHandlerPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-schemahandlerpackage
        '''
        return typing.cast(builtins.str, jsii.get(self, "schemaHandlerPackage"))

    @schema_handler_package.setter
    def schema_handler_package(self, value: builtins.str) -> None:
        jsii.set(self, "schemaHandlerPackage", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> builtins.str:
        '''``AWS::CloudFormation::ResourceVersion.TypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-typename
        '''
        return typing.cast(builtins.str, jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: builtins.str) -> None:
        jsii.set(self, "typeName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ResourceVersion.ExecutionRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-executionrolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "executionRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(
        self,
    ) -> typing.Optional[typing.Union[IResolvable, "CfnResourceVersion.LoggingConfigProperty"]]:
        '''``AWS::CloudFormation::ResourceVersion.LoggingConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-resourceversion.html#cfn-cloudformation-resourceversion-loggingconfig
        '''
        return typing.cast(typing.Optional[typing.Union[IResolvable, "CfnResourceVersion.LoggingConfigProperty"]], jsii.get(self, "loggingConfig"))

    @logging_config.setter
    def logging_config(
        self,
        value: typing.Optional[typing.Union[IResolvable, "CfnResourceVersion.LoggingConfigProperty"]],
    ) -> None:
        jsii.set(self, "loggingConfig", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/core.CfnResourceVersion.LoggingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_name": "logGroupName", "log_role_arn": "logRoleArn"},
    )
    class LoggingConfigProperty:
        def __init__(
            self,
            *,
            log_group_name: typing.Optional[builtins.str] = None,
            log_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param log_group_name: ``CfnResourceVersion.LoggingConfigProperty.LogGroupName``.
            :param log_role_arn: ``CfnResourceVersion.LoggingConfigProperty.LogRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-resourceversion-loggingconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if log_group_name is not None:
                self._values["log_group_name"] = log_group_name
            if log_role_arn is not None:
                self._values["log_role_arn"] = log_role_arn

        @builtins.property
        def log_group_name(self) -> typing.Optional[builtins.str]:
            '''``CfnResourceVersion.LoggingConfigProperty.LogGroupName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-resourceversion-loggingconfig.html#cfn-cloudformation-resourceversion-loggingconfig-loggroupname
            '''
            result = self._values.get("log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_role_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnResourceVersion.LoggingConfigProperty.LogRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-resourceversion-loggingconfig.html#cfn-cloudformation-resourceversion-loggingconfig-logrolearn
            '''
            result = self._values.get("log_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


class CfnRule(
    CfnRefElement,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnRule",
):
    '''The Rules that define template constraints in an AWS Service Catalog portfolio describe when end users can use the template and which values they can specify for parameters that are declared in the AWS CloudFormation template used to create the product they are attempting to use.

    Rules
    are useful for preventing end users from inadvertently specifying an incorrect value.
    For example, you can add a rule to verify whether end users specified a valid subnet in a
    given VPC or used m1.small instance types for test environments. AWS CloudFormation uses
    rules to validate parameter values before it creates the resources for the product.

    A rule can include a RuleCondition property and must include an Assertions property.
    For each rule, you can define only one rule condition; you can define one or more asserts within the Assertions property.
    You define a rule condition and assertions by using rule-specific intrinsic functions.

    :link: https://docs.aws.amazon.com/servicecatalog/latest/adminguide/reference-template_constraint_rules.html
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        assertions: typing.Optional[typing.Sequence[CfnRuleAssertion]] = None,
        rule_condition: typing.Optional[ICfnConditionExpression] = None,
    ) -> None:
        '''Creates and adds a rule.

        :param scope: The parent construct.
        :param id: -
        :param assertions: Assertions which define the rule. Default: - No assertions for the rule.
        :param rule_condition: If the rule condition evaluates to false, the rule doesn't take effect. If the function in the rule condition evaluates to true, expressions in each assert are evaluated and applied. Default: - Rule's assertions will always take effect.
        '''
        props = CfnRuleProps(assertions=assertions, rule_condition=rule_condition)

        jsii.create(CfnRule, self, [scope, id, props])

    @jsii.member(jsii_name="addAssertion")
    def add_assertion(
        self,
        condition: ICfnConditionExpression,
        description: builtins.str,
    ) -> None:
        '''Adds an assertion to the rule.

        :param condition: The expression to evaluation.
        :param description: The description of the assertion.
        '''
        return typing.cast(None, jsii.invoke(self, "addAssertion", [condition, description]))


@jsii.implements(IInspectable)
class CfnStack(
    CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnStack",
):
    '''A CloudFormation ``AWS::CloudFormation::Stack``.

    :cloudformationResource: AWS::CloudFormation::Stack
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html
    '''

    def __init__(
        self,
        scope: Construct,
        id: builtins.str,
        *,
        template_url: builtins.str,
        notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Optional[typing.Union[IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[CfnTag]] = None,
        timeout_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::Stack``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param template_url: ``AWS::CloudFormation::Stack.TemplateURL``.
        :param notification_arns: ``AWS::CloudFormation::Stack.NotificationARNs``.
        :param parameters: ``AWS::CloudFormation::Stack.Parameters``.
        :param tags: ``AWS::CloudFormation::Stack.Tags``.
        :param timeout_in_minutes: ``AWS::CloudFormation::Stack.TimeoutInMinutes``.
        '''
        props = CfnStackProps(
            template_url=template_url,
            notification_arns=notification_arns,
            parameters=parameters,
            tags=tags,
            timeout_in_minutes=timeout_in_minutes,
        )

        jsii.create(CfnStack, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> TagManager:
        '''``AWS::CloudFormation::Stack.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-tags
        '''
        return typing.cast(TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateUrl")
    def template_url(self) -> builtins.str:
        '''``AWS::CloudFormation::Stack.TemplateURL``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-templateurl
        '''
        return typing.cast(builtins.str, jsii.get(self, "templateUrl"))

    @template_url.setter
    def template_url(self, value: builtins.str) -> None:
        jsii.set(self, "templateUrl", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="notificationArns")
    def notification_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::CloudFormation::Stack.NotificationARNs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-notificationarns
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notificationArns"))

    @notification_arns.setter
    def notification_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "notificationArns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''``AWS::CloudFormation::Stack.Parameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-parameters
        '''
        return typing.cast(typing.Optional[typing.Union[IResolvable, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[IResolvable, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        jsii.set(self, "parameters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeoutInMinutes")
    def timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''``AWS::CloudFormation::Stack.TimeoutInMinutes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-timeoutinminutes
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInMinutes"))

    @timeout_in_minutes.setter
    def timeout_in_minutes(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "timeoutInMinutes", value)


@jsii.implements(IInspectable)
class CfnStackSet(
    CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnStackSet",
):
    '''A CloudFormation ``AWS::CloudFormation::StackSet``.

    :cloudformationResource: AWS::CloudFormation::StackSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html
    '''

    def __init__(
        self,
        scope: Construct,
        id: builtins.str,
        *,
        permission_model: builtins.str,
        stack_set_name: builtins.str,
        administration_role_arn: typing.Optional[builtins.str] = None,
        auto_deployment: typing.Optional[typing.Union[IResolvable, "CfnStackSet.AutoDeploymentProperty"]] = None,
        call_as: typing.Optional[builtins.str] = None,
        capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        execution_role_name: typing.Optional[builtins.str] = None,
        operation_preferences: typing.Optional[typing.Union[IResolvable, "CfnStackSet.OperationPreferencesProperty"]] = None,
        parameters: typing.Optional[typing.Union[IResolvable, typing.Sequence[typing.Union[IResolvable, "CfnStackSet.ParameterProperty"]]]] = None,
        stack_instances_group: typing.Optional[typing.Union[IResolvable, typing.Sequence[typing.Union[IResolvable, "CfnStackSet.StackInstancesProperty"]]]] = None,
        tags: typing.Optional[typing.Sequence[CfnTag]] = None,
        template_body: typing.Optional[builtins.str] = None,
        template_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::StackSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param permission_model: ``AWS::CloudFormation::StackSet.PermissionModel``.
        :param stack_set_name: ``AWS::CloudFormation::StackSet.StackSetName``.
        :param administration_role_arn: ``AWS::CloudFormation::StackSet.AdministrationRoleARN``.
        :param auto_deployment: ``AWS::CloudFormation::StackSet.AutoDeployment``.
        :param call_as: ``AWS::CloudFormation::StackSet.CallAs``.
        :param capabilities: ``AWS::CloudFormation::StackSet.Capabilities``.
        :param description: ``AWS::CloudFormation::StackSet.Description``.
        :param execution_role_name: ``AWS::CloudFormation::StackSet.ExecutionRoleName``.
        :param operation_preferences: ``AWS::CloudFormation::StackSet.OperationPreferences``.
        :param parameters: ``AWS::CloudFormation::StackSet.Parameters``.
        :param stack_instances_group: ``AWS::CloudFormation::StackSet.StackInstancesGroup``.
        :param tags: ``AWS::CloudFormation::StackSet.Tags``.
        :param template_body: ``AWS::CloudFormation::StackSet.TemplateBody``.
        :param template_url: ``AWS::CloudFormation::StackSet.TemplateURL``.
        '''
        props = CfnStackSetProps(
            permission_model=permission_model,
            stack_set_name=stack_set_name,
            administration_role_arn=administration_role_arn,
            auto_deployment=auto_deployment,
            call_as=call_as,
            capabilities=capabilities,
            description=description,
            execution_role_name=execution_role_name,
            operation_preferences=operation_preferences,
            parameters=parameters,
            stack_instances_group=stack_instances_group,
            tags=tags,
            template_body=template_body,
            template_url=template_url,
        )

        jsii.create(CfnStackSet, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrStackSetId")
    def attr_stack_set_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: StackSetId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStackSetId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> TagManager:
        '''``AWS::CloudFormation::StackSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-tags
        '''
        return typing.cast(TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissionModel")
    def permission_model(self) -> builtins.str:
        '''``AWS::CloudFormation::StackSet.PermissionModel``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-permissionmodel
        '''
        return typing.cast(builtins.str, jsii.get(self, "permissionModel"))

    @permission_model.setter
    def permission_model(self, value: builtins.str) -> None:
        jsii.set(self, "permissionModel", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stackSetName")
    def stack_set_name(self) -> builtins.str:
        '''``AWS::CloudFormation::StackSet.StackSetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-stacksetname
        '''
        return typing.cast(builtins.str, jsii.get(self, "stackSetName"))

    @stack_set_name.setter
    def stack_set_name(self, value: builtins.str) -> None:
        jsii.set(self, "stackSetName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="administrationRoleArn")
    def administration_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.AdministrationRoleARN``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-administrationrolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "administrationRoleArn"))

    @administration_role_arn.setter
    def administration_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "administrationRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoDeployment")
    def auto_deployment(
        self,
    ) -> typing.Optional[typing.Union[IResolvable, "CfnStackSet.AutoDeploymentProperty"]]:
        '''``AWS::CloudFormation::StackSet.AutoDeployment``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-autodeployment
        '''
        return typing.cast(typing.Optional[typing.Union[IResolvable, "CfnStackSet.AutoDeploymentProperty"]], jsii.get(self, "autoDeployment"))

    @auto_deployment.setter
    def auto_deployment(
        self,
        value: typing.Optional[typing.Union[IResolvable, "CfnStackSet.AutoDeploymentProperty"]],
    ) -> None:
        jsii.set(self, "autoDeployment", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="callAs")
    def call_as(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.CallAs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-callas
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "callAs"))

    @call_as.setter
    def call_as(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "callAs", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="capabilities")
    def capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::CloudFormation::StackSet.Capabilities``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-capabilities
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "capabilities"))

    @capabilities.setter
    def capabilities(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "capabilities", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="executionRoleName")
    def execution_role_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.ExecutionRoleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-executionrolename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleName"))

    @execution_role_name.setter
    def execution_role_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "executionRoleName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="operationPreferences")
    def operation_preferences(
        self,
    ) -> typing.Optional[typing.Union[IResolvable, "CfnStackSet.OperationPreferencesProperty"]]:
        '''``AWS::CloudFormation::StackSet.OperationPreferences``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-operationpreferences
        '''
        return typing.cast(typing.Optional[typing.Union[IResolvable, "CfnStackSet.OperationPreferencesProperty"]], jsii.get(self, "operationPreferences"))

    @operation_preferences.setter
    def operation_preferences(
        self,
        value: typing.Optional[typing.Union[IResolvable, "CfnStackSet.OperationPreferencesProperty"]],
    ) -> None:
        jsii.set(self, "operationPreferences", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[IResolvable, typing.List[typing.Union[IResolvable, "CfnStackSet.ParameterProperty"]]]]:
        '''``AWS::CloudFormation::StackSet.Parameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-parameters
        '''
        return typing.cast(typing.Optional[typing.Union[IResolvable, typing.List[typing.Union[IResolvable, "CfnStackSet.ParameterProperty"]]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[IResolvable, typing.List[typing.Union[IResolvable, "CfnStackSet.ParameterProperty"]]]],
    ) -> None:
        jsii.set(self, "parameters", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stackInstancesGroup")
    def stack_instances_group(
        self,
    ) -> typing.Optional[typing.Union[IResolvable, typing.List[typing.Union[IResolvable, "CfnStackSet.StackInstancesProperty"]]]]:
        '''``AWS::CloudFormation::StackSet.StackInstancesGroup``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-stackinstancesgroup
        '''
        return typing.cast(typing.Optional[typing.Union[IResolvable, typing.List[typing.Union[IResolvable, "CfnStackSet.StackInstancesProperty"]]]], jsii.get(self, "stackInstancesGroup"))

    @stack_instances_group.setter
    def stack_instances_group(
        self,
        value: typing.Optional[typing.Union[IResolvable, typing.List[typing.Union[IResolvable, "CfnStackSet.StackInstancesProperty"]]]],
    ) -> None:
        jsii.set(self, "stackInstancesGroup", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateBody")
    def template_body(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.TemplateBody``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-templatebody
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateBody"))

    @template_body.setter
    def template_body(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "templateBody", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateUrl")
    def template_url(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::StackSet.TemplateURL``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-stackset.html#cfn-cloudformation-stackset-templateurl
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateUrl"))

    @template_url.setter
    def template_url(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "templateUrl", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/core.CfnStackSet.AutoDeploymentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "retain_stacks_on_account_removal": "retainStacksOnAccountRemoval",
        },
    )
    class AutoDeploymentProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, IResolvable]] = None,
            retain_stacks_on_account_removal: typing.Optional[typing.Union[builtins.bool, IResolvable]] = None,
        ) -> None:
            '''
            :param enabled: ``CfnStackSet.AutoDeploymentProperty.Enabled``.
            :param retain_stacks_on_account_removal: ``CfnStackSet.AutoDeploymentProperty.RetainStacksOnAccountRemoval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-autodeployment.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if retain_stacks_on_account_removal is not None:
                self._values["retain_stacks_on_account_removal"] = retain_stacks_on_account_removal

        @builtins.property
        def enabled(self) -> typing.Optional[typing.Union[builtins.bool, IResolvable]]:
            '''``CfnStackSet.AutoDeploymentProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-autodeployment.html#cfn-cloudformation-stackset-autodeployment-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, IResolvable]], result)

        @builtins.property
        def retain_stacks_on_account_removal(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, IResolvable]]:
            '''``CfnStackSet.AutoDeploymentProperty.RetainStacksOnAccountRemoval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-autodeployment.html#cfn-cloudformation-stackset-autodeployment-retainstacksonaccountremoval
            '''
            result = self._values.get("retain_stacks_on_account_removal")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoDeploymentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/core.CfnStackSet.DeploymentTargetsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "accounts": "accounts",
            "organizational_unit_ids": "organizationalUnitIds",
        },
    )
    class DeploymentTargetsProperty:
        def __init__(
            self,
            *,
            accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
            organizational_unit_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param accounts: ``CfnStackSet.DeploymentTargetsProperty.Accounts``.
            :param organizational_unit_ids: ``CfnStackSet.DeploymentTargetsProperty.OrganizationalUnitIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-deploymenttargets.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if accounts is not None:
                self._values["accounts"] = accounts
            if organizational_unit_ids is not None:
                self._values["organizational_unit_ids"] = organizational_unit_ids

        @builtins.property
        def accounts(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnStackSet.DeploymentTargetsProperty.Accounts``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-deploymenttargets.html#cfn-cloudformation-stackset-deploymenttargets-accounts
            '''
            result = self._values.get("accounts")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def organizational_unit_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnStackSet.DeploymentTargetsProperty.OrganizationalUnitIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-deploymenttargets.html#cfn-cloudformation-stackset-deploymenttargets-organizationalunitids
            '''
            result = self._values.get("organizational_unit_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeploymentTargetsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/core.CfnStackSet.OperationPreferencesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "failure_tolerance_count": "failureToleranceCount",
            "failure_tolerance_percentage": "failureTolerancePercentage",
            "max_concurrent_count": "maxConcurrentCount",
            "max_concurrent_percentage": "maxConcurrentPercentage",
            "region_concurrency_type": "regionConcurrencyType",
            "region_order": "regionOrder",
        },
    )
    class OperationPreferencesProperty:
        def __init__(
            self,
            *,
            failure_tolerance_count: typing.Optional[jsii.Number] = None,
            failure_tolerance_percentage: typing.Optional[jsii.Number] = None,
            max_concurrent_count: typing.Optional[jsii.Number] = None,
            max_concurrent_percentage: typing.Optional[jsii.Number] = None,
            region_concurrency_type: typing.Optional[builtins.str] = None,
            region_order: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param failure_tolerance_count: ``CfnStackSet.OperationPreferencesProperty.FailureToleranceCount``.
            :param failure_tolerance_percentage: ``CfnStackSet.OperationPreferencesProperty.FailureTolerancePercentage``.
            :param max_concurrent_count: ``CfnStackSet.OperationPreferencesProperty.MaxConcurrentCount``.
            :param max_concurrent_percentage: ``CfnStackSet.OperationPreferencesProperty.MaxConcurrentPercentage``.
            :param region_concurrency_type: ``CfnStackSet.OperationPreferencesProperty.RegionConcurrencyType``.
            :param region_order: ``CfnStackSet.OperationPreferencesProperty.RegionOrder``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if failure_tolerance_count is not None:
                self._values["failure_tolerance_count"] = failure_tolerance_count
            if failure_tolerance_percentage is not None:
                self._values["failure_tolerance_percentage"] = failure_tolerance_percentage
            if max_concurrent_count is not None:
                self._values["max_concurrent_count"] = max_concurrent_count
            if max_concurrent_percentage is not None:
                self._values["max_concurrent_percentage"] = max_concurrent_percentage
            if region_concurrency_type is not None:
                self._values["region_concurrency_type"] = region_concurrency_type
            if region_order is not None:
                self._values["region_order"] = region_order

        @builtins.property
        def failure_tolerance_count(self) -> typing.Optional[jsii.Number]:
            '''``CfnStackSet.OperationPreferencesProperty.FailureToleranceCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-failuretolerancecount
            '''
            result = self._values.get("failure_tolerance_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def failure_tolerance_percentage(self) -> typing.Optional[jsii.Number]:
            '''``CfnStackSet.OperationPreferencesProperty.FailureTolerancePercentage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-failuretolerancepercentage
            '''
            result = self._values.get("failure_tolerance_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_concurrent_count(self) -> typing.Optional[jsii.Number]:
            '''``CfnStackSet.OperationPreferencesProperty.MaxConcurrentCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-maxconcurrentcount
            '''
            result = self._values.get("max_concurrent_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_concurrent_percentage(self) -> typing.Optional[jsii.Number]:
            '''``CfnStackSet.OperationPreferencesProperty.MaxConcurrentPercentage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-maxconcurrentpercentage
            '''
            result = self._values.get("max_concurrent_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def region_concurrency_type(self) -> typing.Optional[builtins.str]:
            '''``CfnStackSet.OperationPreferencesProperty.RegionConcurrencyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-regionconcurrencytype
            '''
            result = self._values.get("region_concurrency_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region_order(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnStackSet.OperationPreferencesProperty.RegionOrder``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-operationpreferences.html#cfn-cloudformation-stackset-operationpreferences-regionorder
            '''
            result = self._values.get("region_order")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OperationPreferencesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/core.CfnStackSet.ParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameter_key": "parameterKey",
            "parameter_value": "parameterValue",
        },
    )
    class ParameterProperty:
        def __init__(
            self,
            *,
            parameter_key: builtins.str,
            parameter_value: builtins.str,
        ) -> None:
            '''
            :param parameter_key: ``CfnStackSet.ParameterProperty.ParameterKey``.
            :param parameter_value: ``CfnStackSet.ParameterProperty.ParameterValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-parameter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "parameter_key": parameter_key,
                "parameter_value": parameter_value,
            }

        @builtins.property
        def parameter_key(self) -> builtins.str:
            '''``CfnStackSet.ParameterProperty.ParameterKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-parameter.html#cfn-cloudformation-stackset-parameter-parameterkey
            '''
            result = self._values.get("parameter_key")
            assert result is not None, "Required property 'parameter_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameter_value(self) -> builtins.str:
            '''``CfnStackSet.ParameterProperty.ParameterValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-parameter.html#cfn-cloudformation-stackset-parameter-parametervalue
            '''
            result = self._values.get("parameter_value")
            assert result is not None, "Required property 'parameter_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/core.CfnStackSet.StackInstancesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "deployment_targets": "deploymentTargets",
            "regions": "regions",
            "parameter_overrides": "parameterOverrides",
        },
    )
    class StackInstancesProperty:
        def __init__(
            self,
            *,
            deployment_targets: typing.Union[IResolvable, "CfnStackSet.DeploymentTargetsProperty"],
            regions: typing.Sequence[builtins.str],
            parameter_overrides: typing.Optional[typing.Union[IResolvable, typing.Sequence[typing.Union[IResolvable, "CfnStackSet.ParameterProperty"]]]] = None,
        ) -> None:
            '''
            :param deployment_targets: ``CfnStackSet.StackInstancesProperty.DeploymentTargets``.
            :param regions: ``CfnStackSet.StackInstancesProperty.Regions``.
            :param parameter_overrides: ``CfnStackSet.StackInstancesProperty.ParameterOverrides``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-stackinstances.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "deployment_targets": deployment_targets,
                "regions": regions,
            }
            if parameter_overrides is not None:
                self._values["parameter_overrides"] = parameter_overrides

        @builtins.property
        def deployment_targets(
            self,
        ) -> typing.Union[IResolvable, "CfnStackSet.DeploymentTargetsProperty"]:
            '''``CfnStackSet.StackInstancesProperty.DeploymentTargets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-stackinstances.html#cfn-cloudformation-stackset-stackinstances-deploymenttargets
            '''
            result = self._values.get("deployment_targets")
            assert result is not None, "Required property 'deployment_targets' is missing"
            return typing.cast(typing.Union[IResolvable, "CfnStackSet.DeploymentTargetsProperty"], result)

        @builtins.property
        def regions(self) -> typing.List[builtins.str]:
            '''``CfnStackSet.StackInstancesProperty.Regions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-stackinstances.html#cfn-cloudformation-stackset-stackinstances-regions
            '''
            result = self._values.get("regions")
            assert result is not None, "Required property 'regions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def parameter_overrides(
            self,
        ) -> typing.Optional[typing.Union[IResolvable, typing.List[typing.Union[IResolvable, "CfnStackSet.ParameterProperty"]]]]:
            '''``CfnStackSet.StackInstancesProperty.ParameterOverrides``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-stackset-stackinstances.html#cfn-cloudformation-stackset-stackinstances-parameteroverrides
            '''
            result = self._values.get("parameter_overrides")
            return typing.cast(typing.Optional[typing.Union[IResolvable, typing.List[typing.Union[IResolvable, "CfnStackSet.ParameterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StackInstancesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(IInspectable)
class CfnTypeActivation(
    CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnTypeActivation",
):
    '''A CloudFormation ``AWS::CloudFormation::TypeActivation``.

    :cloudformationResource: AWS::CloudFormation::TypeActivation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html
    '''

    def __init__(
        self,
        scope: Construct,
        id: builtins.str,
        *,
        auto_update: typing.Optional[typing.Union[builtins.bool, IResolvable]] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        logging_config: typing.Optional[typing.Union[IResolvable, "CfnTypeActivation.LoggingConfigProperty"]] = None,
        major_version: typing.Optional[builtins.str] = None,
        public_type_arn: typing.Optional[builtins.str] = None,
        publisher_id: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
        type_name_alias: typing.Optional[builtins.str] = None,
        version_bump: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::TypeActivation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param auto_update: ``AWS::CloudFormation::TypeActivation.AutoUpdate``.
        :param execution_role_arn: ``AWS::CloudFormation::TypeActivation.ExecutionRoleArn``.
        :param logging_config: ``AWS::CloudFormation::TypeActivation.LoggingConfig``.
        :param major_version: ``AWS::CloudFormation::TypeActivation.MajorVersion``.
        :param public_type_arn: ``AWS::CloudFormation::TypeActivation.PublicTypeArn``.
        :param publisher_id: ``AWS::CloudFormation::TypeActivation.PublisherId``.
        :param type: ``AWS::CloudFormation::TypeActivation.Type``.
        :param type_name: ``AWS::CloudFormation::TypeActivation.TypeName``.
        :param type_name_alias: ``AWS::CloudFormation::TypeActivation.TypeNameAlias``.
        :param version_bump: ``AWS::CloudFormation::TypeActivation.VersionBump``.
        '''
        props = CfnTypeActivationProps(
            auto_update=auto_update,
            execution_role_arn=execution_role_arn,
            logging_config=logging_config,
            major_version=major_version,
            public_type_arn=public_type_arn,
            publisher_id=publisher_id,
            type=type,
            type_name=type_name,
            type_name_alias=type_name_alias,
            version_bump=version_bump,
        )

        jsii.create(CfnTypeActivation, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoUpdate")
    def auto_update(self) -> typing.Optional[typing.Union[builtins.bool, IResolvable]]:
        '''``AWS::CloudFormation::TypeActivation.AutoUpdate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-autoupdate
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, IResolvable]], jsii.get(self, "autoUpdate"))

    @auto_update.setter
    def auto_update(
        self,
        value: typing.Optional[typing.Union[builtins.bool, IResolvable]],
    ) -> None:
        jsii.set(self, "autoUpdate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.ExecutionRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-executionrolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "executionRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(
        self,
    ) -> typing.Optional[typing.Union[IResolvable, "CfnTypeActivation.LoggingConfigProperty"]]:
        '''``AWS::CloudFormation::TypeActivation.LoggingConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-loggingconfig
        '''
        return typing.cast(typing.Optional[typing.Union[IResolvable, "CfnTypeActivation.LoggingConfigProperty"]], jsii.get(self, "loggingConfig"))

    @logging_config.setter
    def logging_config(
        self,
        value: typing.Optional[typing.Union[IResolvable, "CfnTypeActivation.LoggingConfigProperty"]],
    ) -> None:
        jsii.set(self, "loggingConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="majorVersion")
    def major_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.MajorVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-majorversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "majorVersion"))

    @major_version.setter
    def major_version(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "majorVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="publicTypeArn")
    def public_type_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.PublicTypeArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-publictypearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicTypeArn"))

    @public_type_arn.setter
    def public_type_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "publicTypeArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="publisherId")
    def publisher_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.PublisherId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-publisherid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publisherId"))

    @publisher_id.setter
    def publisher_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "publisherId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-type
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.TypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-typename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "typeName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="typeNameAlias")
    def type_name_alias(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.TypeNameAlias``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-typenamealias
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeNameAlias"))

    @type_name_alias.setter
    def type_name_alias(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "typeNameAlias", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="versionBump")
    def version_bump(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::TypeActivation.VersionBump``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-typeactivation.html#cfn-cloudformation-typeactivation-versionbump
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionBump"))

    @version_bump.setter
    def version_bump(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "versionBump", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/core.CfnTypeActivation.LoggingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_name": "logGroupName", "log_role_arn": "logRoleArn"},
    )
    class LoggingConfigProperty:
        def __init__(
            self,
            *,
            log_group_name: typing.Optional[builtins.str] = None,
            log_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param log_group_name: ``CfnTypeActivation.LoggingConfigProperty.LogGroupName``.
            :param log_role_arn: ``CfnTypeActivation.LoggingConfigProperty.LogRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-typeactivation-loggingconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if log_group_name is not None:
                self._values["log_group_name"] = log_group_name
            if log_role_arn is not None:
                self._values["log_role_arn"] = log_role_arn

        @builtins.property
        def log_group_name(self) -> typing.Optional[builtins.str]:
            '''``CfnTypeActivation.LoggingConfigProperty.LogGroupName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-typeactivation-loggingconfig.html#cfn-cloudformation-typeactivation-loggingconfig-loggroupname
            '''
            result = self._values.get("log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_role_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnTypeActivation.LoggingConfigProperty.LogRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudformation-typeactivation-loggingconfig.html#cfn-cloudformation-typeactivation-loggingconfig-logrolearn
            '''
            result = self._values.get("log_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(IInspectable)
class CfnWaitCondition(
    CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnWaitCondition",
):
    '''A CloudFormation ``AWS::CloudFormation::WaitCondition``.

    :cloudformationResource: AWS::CloudFormation::WaitCondition
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html
    '''

    def __init__(
        self,
        scope: Construct,
        id: builtins.str,
        *,
        count: typing.Optional[jsii.Number] = None,
        handle: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::WaitCondition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param count: ``AWS::CloudFormation::WaitCondition.Count``.
        :param handle: ``AWS::CloudFormation::WaitCondition.Handle``.
        :param timeout: ``AWS::CloudFormation::WaitCondition.Timeout``.
        '''
        props = CfnWaitConditionProps(count=count, handle=handle, timeout=timeout)

        jsii.create(CfnWaitCondition, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrData")
    def attr_data(self) -> IResolvable:
        '''
        :cloudformationAttribute: Data
        '''
        return typing.cast(IResolvable, jsii.get(self, "attrData"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="count")
    def count(self) -> typing.Optional[jsii.Number]:
        '''``AWS::CloudFormation::WaitCondition.Count``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-count
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "count"))

    @count.setter
    def count(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "count", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="handle")
    def handle(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::WaitCondition.Handle``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-handle
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "handle"))

    @handle.setter
    def handle(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "handle", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::WaitCondition.Timeout``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-timeout
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "timeout", value)


@jsii.implements(IInspectable)
class CfnWaitConditionHandle(
    CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnWaitConditionHandle",
):
    '''A CloudFormation ``AWS::CloudFormation::WaitConditionHandle``.

    :cloudformationResource: AWS::CloudFormation::WaitConditionHandle
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitconditionhandle.html
    '''

    def __init__(self, scope: Construct, id: builtins.str) -> None:
        '''Create a new ``AWS::CloudFormation::WaitConditionHandle``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        '''
        jsii.create(CfnWaitConditionHandle, self, [scope, id])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))


class CustomResource(
    Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CustomResource",
):
    '''Custom resource that is implemented using a Lambda.

    As a custom resource author, you should be publishing a subclass of this class
    that hides the choice of provider, and accepts a strongly-typed properties
    object with the properties your provider accepts.

    :resource: AWS::CloudFormation::CustomResource
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        service_token: builtins.str,
        pascal_case_properties: typing.Optional[builtins.bool] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        removal_policy: typing.Optional[RemovalPolicy] = None,
        resource_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param service_token: The ARN of the provider which implements this custom resource type. You can implement a provider by listening to raw AWS CloudFormation events and specify the ARN of an SNS topic (``topic.topicArn``) or the ARN of an AWS Lambda function (``lambda.functionArn``) or use the CDK's custom `resource provider framework <https://docs.aws.amazon.com/cdk/api/latest/docs/custom-resources-readme.html>`_ which makes it easier to implement robust providers. Provider framework:: // use the provider framework from aws-cdk/custom-resources: const provider = new customresources.Provider(this, 'ResourceProvider', { onEventHandler, isCompleteHandler, // optional }); new CustomResource(this, 'MyResource', { serviceToken: provider.serviceToken, }); AWS Lambda function:: // invoke an AWS Lambda function when a lifecycle event occurs: new CustomResource(this, 'MyResource', { serviceToken: myFunction.functionArn, }); SNS topic:: // publish lifecycle events to an SNS topic: new CustomResource(this, 'MyResource', { serviceToken: myTopic.topicArn, });
        :param pascal_case_properties: Convert all property keys to pascal case. Default: false
        :param properties: Properties to pass to the Lambda. Default: - No properties.
        :param removal_policy: The policy to apply when this resource is removed from the application. Default: cdk.RemovalPolicy.Destroy
        :param resource_type: For custom resources, you can specify AWS::CloudFormation::CustomResource (the default) as the resource type, or you can specify your own resource type name. For example, you can use "Custom::MyCustomResourceTypeName". Custom resource type names must begin with "Custom::" and can include alphanumeric characters and the following characters: _@-. You can specify a custom resource type name up to a maximum length of 60 characters. You cannot change the type during an update. Using your own resource type names helps you quickly differentiate the types of custom resources in your stack. For example, if you had two custom resources that conduct two different ping tests, you could name their type as Custom::PingTester to make them easily identifiable as ping testers (instead of using AWS::CloudFormation::CustomResource). Default: - AWS::CloudFormation::CustomResource
        '''
        props = CustomResourceProps(
            service_token=service_token,
            pascal_case_properties=pascal_case_properties,
            properties=properties,
            removal_policy=removal_policy,
            resource_type=resource_type,
        )

        jsii.create(CustomResource, self, [scope, id, props])

    @jsii.member(jsii_name="getAtt")
    def get_att(self, attribute_name: builtins.str) -> Reference:
        '''Returns the value of an attribute of the custom resource of an arbitrary type.

        Attributes are returned from the custom resource provider through the
        ``Data`` map where the key is the attribute name.

        :param attribute_name: the name of the attribute.

        :return:

        a token for ``Fn::GetAtt``. Use ``Token.asXxx`` to encode the returned ``Reference`` as a specific type or
        use the convenience ``getAttString`` for string attributes.
        '''
        return typing.cast(Reference, jsii.invoke(self, "getAtt", [attribute_name]))

    @jsii.member(jsii_name="getAttString")
    def get_att_string(self, attribute_name: builtins.str) -> builtins.str:
        '''Returns the value of an attribute of the custom resource of type string.

        Attributes are returned from the custom resource provider through the
        ``Data`` map where the key is the attribute name.

        :param attribute_name: the name of the attribute.

        :return: a token for ``Fn::GetAtt`` encoded as a string.
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "getAttString", [attribute_name]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ref")
    def ref(self) -> builtins.str:
        '''The physical name of this custom resource.'''
        return typing.cast(builtins.str, jsii.get(self, "ref"))


class NestedStack(
    Stack,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.NestedStack",
):
    '''A CloudFormation nested stack.

    When you apply template changes to update a top-level stack, CloudFormation
    updates the top-level stack and initiates an update to its nested stacks.
    CloudFormation updates the resources of modified nested stacks, but does not
    update the resources of unmodified nested stacks.

    Furthermore, this stack will not be treated as an independent deployment
    artifact (won't be listed in "cdk list" or deployable through "cdk deploy"),
    but rather only synthesized as a template and uploaded as an asset to S3.

    Cross references of resource attributes between the parent stack and the
    nested stack will automatically be translated to stack parameters and
    outputs.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        removal_policy: typing.Optional[RemovalPolicy] = None,
        timeout: typing.Optional[Duration] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param notification_arns: The Simple Notification Service (SNS) topics to publish stack related events. Default: - notifications are not sent for this stack.
        :param parameters: The set value pairs that represent the parameters passed to CloudFormation when this nested stack is created. Each parameter has a name corresponding to a parameter defined in the embedded template and a value representing the value that you want to set for the parameter. The nested stack construct will automatically synthesize parameters in order to bind references from the parent stack(s) into the nested stack. Default: - no user-defined parameters are passed to the nested stack
        :param removal_policy: Policy to apply when the nested stack is removed. The default is ``Destroy``, because all Removal Policies of resources inside the Nested Stack should already have been set correctly. You normally should not need to set this value. Default: RemovalPolicy.DESTROY
        :param timeout: The length of time that CloudFormation waits for the nested stack to reach the CREATE_COMPLETE state. When CloudFormation detects that the nested stack has reached the CREATE_COMPLETE state, it marks the nested stack resource as CREATE_COMPLETE in the parent stack and resumes creating the parent stack. If the timeout period expires before the nested stack reaches CREATE_COMPLETE, CloudFormation marks the nested stack as failed and rolls back both the nested stack and parent stack. Default: - no timeout
        '''
        props = NestedStackProps(
            notification_arns=notification_arns,
            parameters=parameters,
            removal_policy=removal_policy,
            timeout=timeout,
        )

        jsii.create(NestedStack, self, [scope, id, props])

    @jsii.member(jsii_name="isNestedStack") # type: ignore[misc]
    @builtins.classmethod
    def is_nested_stack(cls, x: typing.Any) -> builtins.bool:
        '''Checks if ``x`` is an object of type ``NestedStack``.

        :param x: -
        '''
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isNestedStack", [x]))

    @jsii.member(jsii_name="setParameter")
    def set_parameter(self, name: builtins.str, value: builtins.str) -> None:
        '''Assign a value to one of the nested stack parameters.

        :param name: The parameter name (ID).
        :param value: The value to assign.
        '''
        return typing.cast(None, jsii.invoke(self, "setParameter", [name, value]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stackId")
    def stack_id(self) -> builtins.str:
        '''An attribute that represents the ID of the stack.

        This is a context aware attribute:

        - If this is referenced from the parent stack, it will return ``{ "Ref": "LogicalIdOfNestedStackResource" }``.
        - If this is referenced from the context of the nested stack, it will return ``{ "Ref": "AWS::StackId" }``

        :attribute: true

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            "arn:aws:cloudformation:us-east-2:123456789012:stack/mystack-mynestedstack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786"
        '''
        return typing.cast(builtins.str, jsii.get(self, "stackId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stackName")
    def stack_name(self) -> builtins.str:
        '''An attribute that represents the name of the nested stack.

        This is a context aware attribute:

        - If this is referenced from the parent stack, it will return a token that parses the name from the stack ID.
        - If this is referenced from the context of the nested stack, it will return ``{ "Ref": "AWS::StackName" }``

        :attribute: true

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            mystack - mynestedstack - sggfrhxhum7w
        '''
        return typing.cast(builtins.str, jsii.get(self, "stackName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateFile")
    def template_file(self) -> builtins.str:
        '''The name of the CloudFormation template file emitted to the output directory during synthesis.'''
        return typing.cast(builtins.str, jsii.get(self, "templateFile"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="nestedStackResource")
    def nested_stack_resource(self) -> typing.Optional[CfnResource]:
        '''If this is a nested stack, this represents its ``AWS::CloudFormation::Stack`` resource.

        ``undefined`` for top-level (non-nested) stacks.
        '''
        return typing.cast(typing.Optional[CfnResource], jsii.get(self, "nestedStackResource"))


class CfnCodeDeployBlueGreenHook(
    CfnHook,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnCodeDeployBlueGreenHook",
):
    '''A CloudFormation Hook for CodeDeploy blue-green ECS deployments.

    :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/blue-green.html#blue-green-template-reference
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        applications: typing.Sequence[CfnCodeDeployBlueGreenApplication],
        service_role: builtins.str,
        additional_options: typing.Optional[CfnCodeDeployBlueGreenAdditionalOptions] = None,
        lifecycle_event_hooks: typing.Optional[CfnCodeDeployBlueGreenLifecycleEventHooks] = None,
        traffic_routing_config: typing.Optional[CfnTrafficRoutingConfig] = None,
    ) -> None:
        '''Creates a new CodeDeploy blue-green ECS Hook.

        :param scope: the scope to create the hook in (usually the containing Stack object).
        :param id: the identifier of the construct - will be used to generate the logical ID of the Hook.
        :param applications: Properties of the Amazon ECS applications being deployed.
        :param service_role: The IAM Role for CloudFormation to use to perform blue-green deployments.
        :param additional_options: Additional options for the blue/green deployment. Default: - no additional options
        :param lifecycle_event_hooks: Use lifecycle event hooks to specify a Lambda function that CodeDeploy can call to validate a deployment. You can use the same function or a different one for deployment lifecycle events. Following completion of the validation tests, the Lambda {@link CfnCodeDeployBlueGreenLifecycleEventHooks.afterAllowTraffic} function calls back CodeDeploy and delivers a result of 'Succeeded' or 'Failed'. Default: - no lifecycle event hooks
        :param traffic_routing_config: Traffic routing configuration settings. Default: - time-based canary traffic shifting, with a 15% step percentage and a five minute bake time
        '''
        props = CfnCodeDeployBlueGreenHookProps(
            applications=applications,
            service_role=service_role,
            additional_options=additional_options,
            lifecycle_event_hooks=lifecycle_event_hooks,
            traffic_routing_config=traffic_routing_config,
        )

        jsii.create(CfnCodeDeployBlueGreenHook, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        _props: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''
        :param _props: -
        '''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], jsii.invoke(self, "renderProperties", [_props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="applications")
    def applications(self) -> typing.List[CfnCodeDeployBlueGreenApplication]:
        '''Properties of the Amazon ECS applications being deployed.'''
        return typing.cast(typing.List[CfnCodeDeployBlueGreenApplication], jsii.get(self, "applications"))

    @applications.setter
    def applications(
        self,
        value: typing.List[CfnCodeDeployBlueGreenApplication],
    ) -> None:
        jsii.set(self, "applications", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceRole")
    def service_role(self) -> builtins.str:
        '''The IAM Role for CloudFormation to use to perform blue-green deployments.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceRole"))

    @service_role.setter
    def service_role(self, value: builtins.str) -> None:
        jsii.set(self, "serviceRole", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="additionalOptions")
    def additional_options(
        self,
    ) -> typing.Optional[CfnCodeDeployBlueGreenAdditionalOptions]:
        '''Additional options for the blue/green deployment.

        :default: - no additional options
        '''
        return typing.cast(typing.Optional[CfnCodeDeployBlueGreenAdditionalOptions], jsii.get(self, "additionalOptions"))

    @additional_options.setter
    def additional_options(
        self,
        value: typing.Optional[CfnCodeDeployBlueGreenAdditionalOptions],
    ) -> None:
        jsii.set(self, "additionalOptions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lifecycleEventHooks")
    def lifecycle_event_hooks(
        self,
    ) -> typing.Optional[CfnCodeDeployBlueGreenLifecycleEventHooks]:
        '''Use lifecycle event hooks to specify a Lambda function that CodeDeploy can call to validate a deployment.

        You can use the same function or a different one for deployment lifecycle events.
        Following completion of the validation tests,
        the Lambda {@link CfnCodeDeployBlueGreenLifecycleEventHooks.afterAllowTraffic}
        function calls back CodeDeploy and delivers a result of 'Succeeded' or 'Failed'.

        :default: - no lifecycle event hooks
        '''
        return typing.cast(typing.Optional[CfnCodeDeployBlueGreenLifecycleEventHooks], jsii.get(self, "lifecycleEventHooks"))

    @lifecycle_event_hooks.setter
    def lifecycle_event_hooks(
        self,
        value: typing.Optional[CfnCodeDeployBlueGreenLifecycleEventHooks],
    ) -> None:
        jsii.set(self, "lifecycleEventHooks", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="trafficRoutingConfig")
    def traffic_routing_config(self) -> typing.Optional[CfnTrafficRoutingConfig]:
        '''Traffic routing configuration settings.

        :default: - time-based canary traffic shifting, with a 15% step percentage and a five minute bake time
        '''
        return typing.cast(typing.Optional[CfnTrafficRoutingConfig], jsii.get(self, "trafficRoutingConfig"))

    @traffic_routing_config.setter
    def traffic_routing_config(
        self,
        value: typing.Optional[CfnTrafficRoutingConfig],
    ) -> None:
        jsii.set(self, "trafficRoutingConfig", value)


@jsii.implements(ICfnConditionExpression, IResolvable)
class CfnCondition(
    CfnElement,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnCondition",
):
    '''Represents a CloudFormation condition, for resources which must be conditionally created and the determination must be made at deploy time.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        expression: typing.Optional[ICfnConditionExpression] = None,
    ) -> None:
        '''Build a new condition.

        The condition must be constructed with a condition token,
        that the condition is based on.

        :param scope: -
        :param id: -
        :param expression: The expression that the condition will evaluate. Default: - None.
        '''
        props = CfnConditionProps(expression=expression)

        jsii.create(CfnCondition, self, [scope, id, props])

    @jsii.member(jsii_name="resolve")
    def resolve(self, _context: IResolveContext) -> typing.Any:
        '''Synthesizes the condition.

        :param _context: -
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "resolve", [_context]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="expression")
    def expression(self) -> typing.Optional[ICfnConditionExpression]:
        '''The condition statement.'''
        return typing.cast(typing.Optional[ICfnConditionExpression], jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: typing.Optional[ICfnConditionExpression]) -> None:
        jsii.set(self, "expression", value)


@jsii.implements(IInspectable)
class CfnCustomResource(
    CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnCustomResource",
):
    '''A CloudFormation ``AWS::CloudFormation::CustomResource``.

    :cloudformationResource: AWS::CloudFormation::CustomResource
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html
    '''

    def __init__(
        self,
        scope: Construct,
        id: builtins.str,
        *,
        service_token: builtins.str,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::CustomResource``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param service_token: ``AWS::CloudFormation::CustomResource.ServiceToken``.
        '''
        props = CfnCustomResourceProps(service_token=service_token)

        jsii.create(CfnCustomResource, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceToken")
    def service_token(self) -> builtins.str:
        '''``AWS::CloudFormation::CustomResource.ServiceToken``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html#cfn-customresource-servicetoken
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceToken"))

    @service_token.setter
    def service_token(self, value: builtins.str) -> None:
        jsii.set(self, "serviceToken", value)


@jsii.implements(IInspectable)
class CfnMacro(
    CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnMacro",
):
    '''A CloudFormation ``AWS::CloudFormation::Macro``.

    :cloudformationResource: AWS::CloudFormation::Macro
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html
    '''

    def __init__(
        self,
        scope: Construct,
        id: builtins.str,
        *,
        function_name: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        log_group_name: typing.Optional[builtins.str] = None,
        log_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::Macro``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param function_name: ``AWS::CloudFormation::Macro.FunctionName``.
        :param name: ``AWS::CloudFormation::Macro.Name``.
        :param description: ``AWS::CloudFormation::Macro.Description``.
        :param log_group_name: ``AWS::CloudFormation::Macro.LogGroupName``.
        :param log_role_arn: ``AWS::CloudFormation::Macro.LogRoleARN``.
        '''
        props = CfnMacroProps(
            function_name=function_name,
            name=name,
            description=description,
            log_group_name=log_group_name,
            log_role_arn=log_role_arn,
        )

        jsii.create(CfnMacro, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        '''``AWS::CloudFormation::Macro.FunctionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-functionname
        '''
        return typing.cast(builtins.str, jsii.get(self, "functionName"))

    @function_name.setter
    def function_name(self, value: builtins.str) -> None:
        jsii.set(self, "functionName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::CloudFormation::Macro.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::Macro.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::Macro.LogGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-loggroupname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "logGroupName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logRoleArn")
    def log_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::Macro.LogRoleARN``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-logrolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logRoleArn"))

    @log_role_arn.setter
    def log_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "logRoleArn", value)


class CfnMapping(
    CfnRefElement,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnMapping",
):
    '''Represents a CloudFormation mapping.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        mapping: typing.Optional[typing.Mapping[builtins.str, typing.Mapping[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param mapping: Mapping of key to a set of corresponding set of named values. The key identifies a map of name-value pairs and must be unique within the mapping. For example, if you want to set values based on a region, you can create a mapping that uses the region name as a key and contains the values you want to specify for each specific region. Default: - No mapping.
        '''
        props = CfnMappingProps(mapping=mapping)

        jsii.create(CfnMapping, self, [scope, id, props])

    @jsii.member(jsii_name="findInMap")
    def find_in_map(self, key1: builtins.str, key2: builtins.str) -> builtins.str:
        '''
        :param key1: -
        :param key2: -

        :return: A reference to a value in the map based on the two keys.
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "findInMap", [key1, key2]))

    @jsii.member(jsii_name="setValue")
    def set_value(
        self,
        key1: builtins.str,
        key2: builtins.str,
        value: typing.Any,
    ) -> None:
        '''Sets a value in the map based on the two keys.

        :param key1: -
        :param key2: -
        :param value: -
        '''
        return typing.cast(None, jsii.invoke(self, "setValue", [key1, key2, value]))


@jsii.implements(IInspectable)
class CfnModuleDefaultVersion(
    CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnModuleDefaultVersion",
):
    '''A CloudFormation ``AWS::CloudFormation::ModuleDefaultVersion``.

    :cloudformationResource: AWS::CloudFormation::ModuleDefaultVersion
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html
    '''

    def __init__(
        self,
        scope: Construct,
        id: builtins.str,
        *,
        arn: typing.Optional[builtins.str] = None,
        module_name: typing.Optional[builtins.str] = None,
        version_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::ModuleDefaultVersion``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param arn: ``AWS::CloudFormation::ModuleDefaultVersion.Arn``.
        :param module_name: ``AWS::CloudFormation::ModuleDefaultVersion.ModuleName``.
        :param version_id: ``AWS::CloudFormation::ModuleDefaultVersion.VersionId``.
        '''
        props = CfnModuleDefaultVersionProps(
            arn=arn, module_name=module_name, version_id=version_id
        )

        jsii.create(CfnModuleDefaultVersion, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ModuleDefaultVersion.Arn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html#cfn-cloudformation-moduledefaultversion-arn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "arn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="moduleName")
    def module_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ModuleDefaultVersion.ModuleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html#cfn-cloudformation-moduledefaultversion-modulename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "moduleName"))

    @module_name.setter
    def module_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "moduleName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::ModuleDefaultVersion.VersionId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduledefaultversion.html#cfn-cloudformation-moduledefaultversion-versionid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionId"))

    @version_id.setter
    def version_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "versionId", value)


@jsii.implements(IInspectable)
class CfnModuleVersion(
    CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnModuleVersion",
):
    '''A CloudFormation ``AWS::CloudFormation::ModuleVersion``.

    :cloudformationResource: AWS::CloudFormation::ModuleVersion
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html
    '''

    def __init__(
        self,
        scope: Construct,
        id: builtins.str,
        *,
        module_name: builtins.str,
        module_package: builtins.str,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::ModuleVersion``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param module_name: ``AWS::CloudFormation::ModuleVersion.ModuleName``.
        :param module_package: ``AWS::CloudFormation::ModuleVersion.ModulePackage``.
        '''
        props = CfnModuleVersionProps(
            module_name=module_name, module_package=module_package
        )

        jsii.create(CfnModuleVersion, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDescription")
    def attr_description(self) -> builtins.str:
        '''
        :cloudformationAttribute: Description
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDescription"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDocumentationUrl")
    def attr_documentation_url(self) -> builtins.str:
        '''
        :cloudformationAttribute: DocumentationUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDocumentationUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIsDefaultVersion")
    def attr_is_default_version(self) -> IResolvable:
        '''
        :cloudformationAttribute: IsDefaultVersion
        '''
        return typing.cast(IResolvable, jsii.get(self, "attrIsDefaultVersion"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSchema")
    def attr_schema(self) -> builtins.str:
        '''
        :cloudformationAttribute: Schema
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSchema"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrTimeCreated")
    def attr_time_created(self) -> builtins.str:
        '''
        :cloudformationAttribute: TimeCreated
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTimeCreated"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVersionId")
    def attr_version_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: VersionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersionId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVisibility")
    def attr_visibility(self) -> builtins.str:
        '''
        :cloudformationAttribute: Visibility
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVisibility"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="moduleName")
    def module_name(self) -> builtins.str:
        '''``AWS::CloudFormation::ModuleVersion.ModuleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html#cfn-cloudformation-moduleversion-modulename
        '''
        return typing.cast(builtins.str, jsii.get(self, "moduleName"))

    @module_name.setter
    def module_name(self, value: builtins.str) -> None:
        jsii.set(self, "moduleName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modulePackage")
    def module_package(self) -> builtins.str:
        '''``AWS::CloudFormation::ModuleVersion.ModulePackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-moduleversion.html#cfn-cloudformation-moduleversion-modulepackage
        '''
        return typing.cast(builtins.str, jsii.get(self, "modulePackage"))

    @module_package.setter
    def module_package(self, value: builtins.str) -> None:
        jsii.set(self, "modulePackage", value)


@jsii.implements(IInspectable)
class CfnPublicTypeVersion(
    CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnPublicTypeVersion",
):
    '''A CloudFormation ``AWS::CloudFormation::PublicTypeVersion``.

    :cloudformationResource: AWS::CloudFormation::PublicTypeVersion
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html
    '''

    def __init__(
        self,
        scope: Construct,
        id: builtins.str,
        *,
        arn: typing.Optional[builtins.str] = None,
        log_delivery_bucket: typing.Optional[builtins.str] = None,
        public_version_number: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        type_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::PublicTypeVersion``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param arn: ``AWS::CloudFormation::PublicTypeVersion.Arn``.
        :param log_delivery_bucket: ``AWS::CloudFormation::PublicTypeVersion.LogDeliveryBucket``.
        :param public_version_number: ``AWS::CloudFormation::PublicTypeVersion.PublicVersionNumber``.
        :param type: ``AWS::CloudFormation::PublicTypeVersion.Type``.
        :param type_name: ``AWS::CloudFormation::PublicTypeVersion.TypeName``.
        '''
        props = CfnPublicTypeVersionProps(
            arn=arn,
            log_delivery_bucket=log_delivery_bucket,
            public_version_number=public_version_number,
            type=type,
            type_name=type_name,
        )

        jsii.create(CfnPublicTypeVersion, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPublicTypeArn")
    def attr_public_type_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: PublicTypeArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublicTypeArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPublisherId")
    def attr_publisher_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: PublisherId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublisherId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrTypeVersionArn")
    def attr_type_version_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: TypeVersionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTypeVersionArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="arn")
    def arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::PublicTypeVersion.Arn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-arn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "arn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logDeliveryBucket")
    def log_delivery_bucket(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::PublicTypeVersion.LogDeliveryBucket``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-logdeliverybucket
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logDeliveryBucket"))

    @log_delivery_bucket.setter
    def log_delivery_bucket(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "logDeliveryBucket", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="publicVersionNumber")
    def public_version_number(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::PublicTypeVersion.PublicVersionNumber``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-publicversionnumber
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicVersionNumber"))

    @public_version_number.setter
    def public_version_number(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "publicVersionNumber", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::PublicTypeVersion.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-type
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="typeName")
    def type_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::PublicTypeVersion.TypeName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publictypeversion.html#cfn-cloudformation-publictypeversion-typename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeName"))

    @type_name.setter
    def type_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "typeName", value)


@jsii.implements(IInspectable)
class CfnPublisher(
    CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/core.CfnPublisher",
):
    '''A CloudFormation ``AWS::CloudFormation::Publisher``.

    :cloudformationResource: AWS::CloudFormation::Publisher
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html
    '''

    def __init__(
        self,
        scope: Construct,
        id: builtins.str,
        *,
        accept_terms_and_conditions: typing.Union[builtins.bool, IResolvable],
        connection_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CloudFormation::Publisher``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param accept_terms_and_conditions: ``AWS::CloudFormation::Publisher.AcceptTermsAndConditions``.
        :param connection_arn: ``AWS::CloudFormation::Publisher.ConnectionArn``.
        '''
        props = CfnPublisherProps(
            accept_terms_and_conditions=accept_terms_and_conditions,
            connection_arn=connection_arn,
        )

        jsii.create(CfnPublisher, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrIdentityProvider")
    def attr_identity_provider(self) -> builtins.str:
        '''
        :cloudformationAttribute: IdentityProvider
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityProvider"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPublisherId")
    def attr_publisher_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: PublisherId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublisherId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPublisherProfile")
    def attr_publisher_profile(self) -> builtins.str:
        '''
        :cloudformationAttribute: PublisherProfile
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublisherProfile"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPublisherStatus")
    def attr_publisher_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: PublisherStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublisherStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="acceptTermsAndConditions")
    def accept_terms_and_conditions(self) -> typing.Union[builtins.bool, IResolvable]:
        '''``AWS::CloudFormation::Publisher.AcceptTermsAndConditions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html#cfn-cloudformation-publisher-accepttermsandconditions
        '''
        return typing.cast(typing.Union[builtins.bool, IResolvable], jsii.get(self, "acceptTermsAndConditions"))

    @accept_terms_and_conditions.setter
    def accept_terms_and_conditions(
        self,
        value: typing.Union[builtins.bool, IResolvable],
    ) -> None:
        jsii.set(self, "acceptTermsAndConditions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="connectionArn")
    def connection_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudFormation::Publisher.ConnectionArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-publisher.html#cfn-cloudformation-publisher-connectionarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionArn"))

    @connection_arn.setter
    def connection_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "connectionArn", value)


__all__ = [
    "Annotations",
    "App",
    "AppProps",
    "Arn",
    "ArnComponents",
    "ArnFormat",
    "Aspects",
    "AssetHashType",
    "AssetOptions",
    "AssetStaging",
    "AssetStagingProps",
    "Aws",
    "BootstraplessSynthesizer",
    "BootstraplessSynthesizerProps",
    "BundlingDockerImage",
    "BundlingOptions",
    "BundlingOutput",
    "CfnAutoScalingReplacingUpdate",
    "CfnAutoScalingRollingUpdate",
    "CfnAutoScalingScheduledAction",
    "CfnCapabilities",
    "CfnCodeDeployBlueGreenAdditionalOptions",
    "CfnCodeDeployBlueGreenApplication",
    "CfnCodeDeployBlueGreenApplicationTarget",
    "CfnCodeDeployBlueGreenEcsAttributes",
    "CfnCodeDeployBlueGreenHook",
    "CfnCodeDeployBlueGreenHookProps",
    "CfnCodeDeployBlueGreenLifecycleEventHooks",
    "CfnCodeDeployLambdaAliasUpdate",
    "CfnCondition",
    "CfnConditionProps",
    "CfnCreationPolicy",
    "CfnCustomResource",
    "CfnCustomResourceProps",
    "CfnDeletionPolicy",
    "CfnDynamicReference",
    "CfnDynamicReferenceProps",
    "CfnDynamicReferenceService",
    "CfnElement",
    "CfnHook",
    "CfnHookProps",
    "CfnInclude",
    "CfnIncludeProps",
    "CfnJson",
    "CfnJsonProps",
    "CfnMacro",
    "CfnMacroProps",
    "CfnMapping",
    "CfnMappingProps",
    "CfnModuleDefaultVersion",
    "CfnModuleDefaultVersionProps",
    "CfnModuleVersion",
    "CfnModuleVersionProps",
    "CfnOutput",
    "CfnOutputProps",
    "CfnParameter",
    "CfnParameterProps",
    "CfnPublicTypeVersion",
    "CfnPublicTypeVersionProps",
    "CfnPublisher",
    "CfnPublisherProps",
    "CfnRefElement",
    "CfnResource",
    "CfnResourceAutoScalingCreationPolicy",
    "CfnResourceDefaultVersion",
    "CfnResourceDefaultVersionProps",
    "CfnResourceProps",
    "CfnResourceSignal",
    "CfnResourceVersion",
    "CfnResourceVersionProps",
    "CfnRule",
    "CfnRuleAssertion",
    "CfnRuleProps",
    "CfnStack",
    "CfnStackProps",
    "CfnStackSet",
    "CfnStackSetProps",
    "CfnTag",
    "CfnTrafficRoute",
    "CfnTrafficRouting",
    "CfnTrafficRoutingConfig",
    "CfnTrafficRoutingTimeBasedCanary",
    "CfnTrafficRoutingTimeBasedLinear",
    "CfnTrafficRoutingType",
    "CfnTypeActivation",
    "CfnTypeActivationProps",
    "CfnUpdatePolicy",
    "CfnWaitCondition",
    "CfnWaitConditionHandle",
    "CfnWaitConditionProps",
    "ConcreteDependable",
    "Construct",
    "ConstructNode",
    "ConstructOrder",
    "ContextProvider",
    "CopyOptions",
    "CustomResource",
    "CustomResourceProps",
    "CustomResourceProvider",
    "CustomResourceProviderProps",
    "CustomResourceProviderRuntime",
    "DefaultStackSynthesizer",
    "DefaultStackSynthesizerProps",
    "DefaultTokenResolver",
    "DependableTrait",
    "Dependency",
    "DockerBuildOptions",
    "DockerIgnoreStrategy",
    "DockerImage",
    "DockerImageAssetLocation",
    "DockerImageAssetSource",
    "DockerRunOptions",
    "DockerVolume",
    "DockerVolumeConsistency",
    "Duration",
    "EncodingOptions",
    "Environment",
    "Expiration",
    "ExportValueOptions",
    "FeatureFlags",
    "FileAssetLocation",
    "FileAssetPackaging",
    "FileAssetSource",
    "FileCopyOptions",
    "FileFingerprintOptions",
    "FileSystem",
    "FingerprintOptions",
    "Fn",
    "GetContextKeyOptions",
    "GetContextKeyResult",
    "GetContextValueOptions",
    "GetContextValueResult",
    "GitIgnoreStrategy",
    "GlobIgnoreStrategy",
    "IAnyProducer",
    "IAspect",
    "IAsset",
    "ICfnConditionExpression",
    "ICfnResourceOptions",
    "IConstruct",
    "IDependable",
    "IFragmentConcatenator",
    "IInspectable",
    "IListProducer",
    "ILocalBundling",
    "INumberProducer",
    "IPostProcessor",
    "IResolvable",
    "IResolveContext",
    "IResource",
    "IStableAnyProducer",
    "IStableListProducer",
    "IStableNumberProducer",
    "IStableStringProducer",
    "IStackSynthesizer",
    "IStringProducer",
    "ISynthesisSession",
    "ITaggable",
    "ITemplateOptions",
    "ITokenMapper",
    "ITokenResolver",
    "IgnoreMode",
    "IgnoreStrategy",
    "Intrinsic",
    "IntrinsicProps",
    "Lazy",
    "LazyAnyValueOptions",
    "LazyListValueOptions",
    "LazyStringValueOptions",
    "LegacyStackSynthesizer",
    "Names",
    "NestedStack",
    "NestedStackProps",
    "NestedStackSynthesizer",
    "PhysicalName",
    "Reference",
    "RemovalPolicy",
    "RemovalPolicyOptions",
    "RemoveTag",
    "ResolveChangeContextOptions",
    "ResolveOptions",
    "Resource",
    "ResourceEnvironment",
    "ResourceProps",
    "ReverseOptions",
    "ScopedAws",
    "SecretValue",
    "SecretsManagerSecretOptions",
    "Size",
    "SizeConversionOptions",
    "SizeRoundingBehavior",
    "Stack",
    "StackProps",
    "StackSynthesizer",
    "Stage",
    "StageProps",
    "StageSynthesisOptions",
    "StringConcat",
    "SymlinkFollowMode",
    "SynthesisOptions",
    "SynthesizeStackArtifactOptions",
    "Tag",
    "TagManager",
    "TagManagerOptions",
    "TagProps",
    "TagType",
    "Tags",
    "TimeConversionOptions",
    "Token",
    "TokenComparison",
    "Tokenization",
    "TokenizedStringFragments",
    "TreeInspector",
    "ValidationError",
    "ValidationResult",
    "ValidationResults",
]

publication.publish()
