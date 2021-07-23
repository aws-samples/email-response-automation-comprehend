'''
# Amazon SageMaker Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_sagemaker as sagemaker
```
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

import aws_cdk.core


@jsii.implements(aws_cdk.core.IInspectable)
class CfnApp(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnApp",
):
    '''A CloudFormation ``AWS::SageMaker::App``.

    :cloudformationResource: AWS::SageMaker::App
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        app_name: builtins.str,
        app_type: builtins.str,
        domain_id: builtins.str,
        user_profile_name: builtins.str,
        resource_spec: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApp.ResourceSpecProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::App``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param app_name: ``AWS::SageMaker::App.AppName``.
        :param app_type: ``AWS::SageMaker::App.AppType``.
        :param domain_id: ``AWS::SageMaker::App.DomainId``.
        :param user_profile_name: ``AWS::SageMaker::App.UserProfileName``.
        :param resource_spec: ``AWS::SageMaker::App.ResourceSpec``.
        :param tags: ``AWS::SageMaker::App.Tags``.
        '''
        props = CfnAppProps(
            app_name=app_name,
            app_type=app_type,
            domain_id=domain_id,
            user_profile_name=user_profile_name,
            resource_spec=resource_spec,
            tags=tags,
        )

        jsii.create(CfnApp, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrAppArn")
    def attr_app_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AppArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAppArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::App.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="appName")
    def app_name(self) -> builtins.str:
        '''``AWS::SageMaker::App.AppName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-appname
        '''
        return typing.cast(builtins.str, jsii.get(self, "appName"))

    @app_name.setter
    def app_name(self, value: builtins.str) -> None:
        jsii.set(self, "appName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="appType")
    def app_type(self) -> builtins.str:
        '''``AWS::SageMaker::App.AppType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-apptype
        '''
        return typing.cast(builtins.str, jsii.get(self, "appType"))

    @app_type.setter
    def app_type(self, value: builtins.str) -> None:
        jsii.set(self, "appType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainId")
    def domain_id(self) -> builtins.str:
        '''``AWS::SageMaker::App.DomainId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-domainid
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainId"))

    @domain_id.setter
    def domain_id(self, value: builtins.str) -> None:
        jsii.set(self, "domainId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userProfileName")
    def user_profile_name(self) -> builtins.str:
        '''``AWS::SageMaker::App.UserProfileName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-userprofilename
        '''
        return typing.cast(builtins.str, jsii.get(self, "userProfileName"))

    @user_profile_name.setter
    def user_profile_name(self, value: builtins.str) -> None:
        jsii.set(self, "userProfileName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceSpec")
    def resource_spec(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApp.ResourceSpecProperty"]]:
        '''``AWS::SageMaker::App.ResourceSpec``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-resourcespec
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApp.ResourceSpecProperty"]], jsii.get(self, "resourceSpec"))

    @resource_spec.setter
    def resource_spec(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApp.ResourceSpecProperty"]],
    ) -> None:
        jsii.set(self, "resourceSpec", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnApp.ResourceSpecProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_type": "instanceType",
            "sage_maker_image_arn": "sageMakerImageArn",
            "sage_maker_image_version_arn": "sageMakerImageVersionArn",
        },
    )
    class ResourceSpecProperty:
        def __init__(
            self,
            *,
            instance_type: typing.Optional[builtins.str] = None,
            sage_maker_image_arn: typing.Optional[builtins.str] = None,
            sage_maker_image_version_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param instance_type: ``CfnApp.ResourceSpecProperty.InstanceType``.
            :param sage_maker_image_arn: ``CfnApp.ResourceSpecProperty.SageMakerImageArn``.
            :param sage_maker_image_version_arn: ``CfnApp.ResourceSpecProperty.SageMakerImageVersionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-app-resourcespec.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if instance_type is not None:
                self._values["instance_type"] = instance_type
            if sage_maker_image_arn is not None:
                self._values["sage_maker_image_arn"] = sage_maker_image_arn
            if sage_maker_image_version_arn is not None:
                self._values["sage_maker_image_version_arn"] = sage_maker_image_version_arn

        @builtins.property
        def instance_type(self) -> typing.Optional[builtins.str]:
            '''``CfnApp.ResourceSpecProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-app-resourcespec.html#cfn-sagemaker-app-resourcespec-instancetype
            '''
            result = self._values.get("instance_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sage_maker_image_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnApp.ResourceSpecProperty.SageMakerImageArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-app-resourcespec.html#cfn-sagemaker-app-resourcespec-sagemakerimagearn
            '''
            result = self._values.get("sage_maker_image_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sage_maker_image_version_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnApp.ResourceSpecProperty.SageMakerImageVersionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-app-resourcespec.html#cfn-sagemaker-app-resourcespec-sagemakerimageversionarn
            '''
            result = self._values.get("sage_maker_image_version_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceSpecProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnAppImageConfig(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnAppImageConfig",
):
    '''A CloudFormation ``AWS::SageMaker::AppImageConfig``.

    :cloudformationResource: AWS::SageMaker::AppImageConfig
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        app_image_config_name: builtins.str,
        kernel_gateway_image_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAppImageConfig.KernelGatewayImageConfigProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::AppImageConfig``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param app_image_config_name: ``AWS::SageMaker::AppImageConfig.AppImageConfigName``.
        :param kernel_gateway_image_config: ``AWS::SageMaker::AppImageConfig.KernelGatewayImageConfig``.
        :param tags: ``AWS::SageMaker::AppImageConfig.Tags``.
        '''
        props = CfnAppImageConfigProps(
            app_image_config_name=app_image_config_name,
            kernel_gateway_image_config=kernel_gateway_image_config,
            tags=tags,
        )

        jsii.create(CfnAppImageConfig, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrAppImageConfigArn")
    def attr_app_image_config_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: AppImageConfigArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAppImageConfigArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::AppImageConfig.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html#cfn-sagemaker-appimageconfig-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="appImageConfigName")
    def app_image_config_name(self) -> builtins.str:
        '''``AWS::SageMaker::AppImageConfig.AppImageConfigName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html#cfn-sagemaker-appimageconfig-appimageconfigname
        '''
        return typing.cast(builtins.str, jsii.get(self, "appImageConfigName"))

    @app_image_config_name.setter
    def app_image_config_name(self, value: builtins.str) -> None:
        jsii.set(self, "appImageConfigName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kernelGatewayImageConfig")
    def kernel_gateway_image_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAppImageConfig.KernelGatewayImageConfigProperty"]]:
        '''``AWS::SageMaker::AppImageConfig.KernelGatewayImageConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html#cfn-sagemaker-appimageconfig-kernelgatewayimageconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAppImageConfig.KernelGatewayImageConfigProperty"]], jsii.get(self, "kernelGatewayImageConfig"))

    @kernel_gateway_image_config.setter
    def kernel_gateway_image_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAppImageConfig.KernelGatewayImageConfigProperty"]],
    ) -> None:
        jsii.set(self, "kernelGatewayImageConfig", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnAppImageConfig.FileSystemConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "default_gid": "defaultGid",
            "default_uid": "defaultUid",
            "mount_path": "mountPath",
        },
    )
    class FileSystemConfigProperty:
        def __init__(
            self,
            *,
            default_gid: typing.Optional[jsii.Number] = None,
            default_uid: typing.Optional[jsii.Number] = None,
            mount_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param default_gid: ``CfnAppImageConfig.FileSystemConfigProperty.DefaultGid``.
            :param default_uid: ``CfnAppImageConfig.FileSystemConfigProperty.DefaultUid``.
            :param mount_path: ``CfnAppImageConfig.FileSystemConfigProperty.MountPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-filesystemconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if default_gid is not None:
                self._values["default_gid"] = default_gid
            if default_uid is not None:
                self._values["default_uid"] = default_uid
            if mount_path is not None:
                self._values["mount_path"] = mount_path

        @builtins.property
        def default_gid(self) -> typing.Optional[jsii.Number]:
            '''``CfnAppImageConfig.FileSystemConfigProperty.DefaultGid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-filesystemconfig.html#cfn-sagemaker-appimageconfig-filesystemconfig-defaultgid
            '''
            result = self._values.get("default_gid")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def default_uid(self) -> typing.Optional[jsii.Number]:
            '''``CfnAppImageConfig.FileSystemConfigProperty.DefaultUid``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-filesystemconfig.html#cfn-sagemaker-appimageconfig-filesystemconfig-defaultuid
            '''
            result = self._values.get("default_uid")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def mount_path(self) -> typing.Optional[builtins.str]:
            '''``CfnAppImageConfig.FileSystemConfigProperty.MountPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-filesystemconfig.html#cfn-sagemaker-appimageconfig-filesystemconfig-mountpath
            '''
            result = self._values.get("mount_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FileSystemConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnAppImageConfig.KernelGatewayImageConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kernel_specs": "kernelSpecs",
            "file_system_config": "fileSystemConfig",
        },
    )
    class KernelGatewayImageConfigProperty:
        def __init__(
            self,
            *,
            kernel_specs: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnAppImageConfig.KernelSpecProperty"]]],
            file_system_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAppImageConfig.FileSystemConfigProperty"]] = None,
        ) -> None:
            '''
            :param kernel_specs: ``CfnAppImageConfig.KernelGatewayImageConfigProperty.KernelSpecs``.
            :param file_system_config: ``CfnAppImageConfig.KernelGatewayImageConfigProperty.FileSystemConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-kernelgatewayimageconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "kernel_specs": kernel_specs,
            }
            if file_system_config is not None:
                self._values["file_system_config"] = file_system_config

        @builtins.property
        def kernel_specs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAppImageConfig.KernelSpecProperty"]]]:
            '''``CfnAppImageConfig.KernelGatewayImageConfigProperty.KernelSpecs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-kernelgatewayimageconfig.html#cfn-sagemaker-appimageconfig-kernelgatewayimageconfig-kernelspecs
            '''
            result = self._values.get("kernel_specs")
            assert result is not None, "Required property 'kernel_specs' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAppImageConfig.KernelSpecProperty"]]], result)

        @builtins.property
        def file_system_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAppImageConfig.FileSystemConfigProperty"]]:
            '''``CfnAppImageConfig.KernelGatewayImageConfigProperty.FileSystemConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-kernelgatewayimageconfig.html#cfn-sagemaker-appimageconfig-kernelgatewayimageconfig-filesystemconfig
            '''
            result = self._values.get("file_system_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnAppImageConfig.FileSystemConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KernelGatewayImageConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnAppImageConfig.KernelSpecProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "display_name": "displayName"},
    )
    class KernelSpecProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            display_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param name: ``CfnAppImageConfig.KernelSpecProperty.Name``.
            :param display_name: ``CfnAppImageConfig.KernelSpecProperty.DisplayName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-kernelspec.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
            }
            if display_name is not None:
                self._values["display_name"] = display_name

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnAppImageConfig.KernelSpecProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-kernelspec.html#cfn-sagemaker-appimageconfig-kernelspec-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def display_name(self) -> typing.Optional[builtins.str]:
            '''``CfnAppImageConfig.KernelSpecProperty.DisplayName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-appimageconfig-kernelspec.html#cfn-sagemaker-appimageconfig-kernelspec-displayname
            '''
            result = self._values.get("display_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KernelSpecProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnAppImageConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "app_image_config_name": "appImageConfigName",
        "kernel_gateway_image_config": "kernelGatewayImageConfig",
        "tags": "tags",
    },
)
class CfnAppImageConfigProps:
    def __init__(
        self,
        *,
        app_image_config_name: builtins.str,
        kernel_gateway_image_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnAppImageConfig.KernelGatewayImageConfigProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::AppImageConfig``.

        :param app_image_config_name: ``AWS::SageMaker::AppImageConfig.AppImageConfigName``.
        :param kernel_gateway_image_config: ``AWS::SageMaker::AppImageConfig.KernelGatewayImageConfig``.
        :param tags: ``AWS::SageMaker::AppImageConfig.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "app_image_config_name": app_image_config_name,
        }
        if kernel_gateway_image_config is not None:
            self._values["kernel_gateway_image_config"] = kernel_gateway_image_config
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def app_image_config_name(self) -> builtins.str:
        '''``AWS::SageMaker::AppImageConfig.AppImageConfigName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html#cfn-sagemaker-appimageconfig-appimageconfigname
        '''
        result = self._values.get("app_image_config_name")
        assert result is not None, "Required property 'app_image_config_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kernel_gateway_image_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnAppImageConfig.KernelGatewayImageConfigProperty]]:
        '''``AWS::SageMaker::AppImageConfig.KernelGatewayImageConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html#cfn-sagemaker-appimageconfig-kernelgatewayimageconfig
        '''
        result = self._values.get("kernel_gateway_image_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnAppImageConfig.KernelGatewayImageConfigProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::AppImageConfig.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-appimageconfig.html#cfn-sagemaker-appimageconfig-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAppImageConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnAppProps",
    jsii_struct_bases=[],
    name_mapping={
        "app_name": "appName",
        "app_type": "appType",
        "domain_id": "domainId",
        "user_profile_name": "userProfileName",
        "resource_spec": "resourceSpec",
        "tags": "tags",
    },
)
class CfnAppProps:
    def __init__(
        self,
        *,
        app_name: builtins.str,
        app_type: builtins.str,
        domain_id: builtins.str,
        user_profile_name: builtins.str,
        resource_spec: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApp.ResourceSpecProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::App``.

        :param app_name: ``AWS::SageMaker::App.AppName``.
        :param app_type: ``AWS::SageMaker::App.AppType``.
        :param domain_id: ``AWS::SageMaker::App.DomainId``.
        :param user_profile_name: ``AWS::SageMaker::App.UserProfileName``.
        :param resource_spec: ``AWS::SageMaker::App.ResourceSpec``.
        :param tags: ``AWS::SageMaker::App.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "app_name": app_name,
            "app_type": app_type,
            "domain_id": domain_id,
            "user_profile_name": user_profile_name,
        }
        if resource_spec is not None:
            self._values["resource_spec"] = resource_spec
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def app_name(self) -> builtins.str:
        '''``AWS::SageMaker::App.AppName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-appname
        '''
        result = self._values.get("app_name")
        assert result is not None, "Required property 'app_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_type(self) -> builtins.str:
        '''``AWS::SageMaker::App.AppType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-apptype
        '''
        result = self._values.get("app_type")
        assert result is not None, "Required property 'app_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_id(self) -> builtins.str:
        '''``AWS::SageMaker::App.DomainId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-domainid
        '''
        result = self._values.get("domain_id")
        assert result is not None, "Required property 'domain_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_profile_name(self) -> builtins.str:
        '''``AWS::SageMaker::App.UserProfileName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-userprofilename
        '''
        result = self._values.get("user_profile_name")
        assert result is not None, "Required property 'user_profile_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_spec(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApp.ResourceSpecProperty]]:
        '''``AWS::SageMaker::App.ResourceSpec``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-resourcespec
        '''
        result = self._values.get("resource_spec")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApp.ResourceSpecProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::App.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-app.html#cfn-sagemaker-app-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAppProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnCodeRepository(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnCodeRepository",
):
    '''A CloudFormation ``AWS::SageMaker::CodeRepository``.

    :cloudformationResource: AWS::SageMaker::CodeRepository
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        git_config: typing.Union["CfnCodeRepository.GitConfigProperty", aws_cdk.core.IResolvable],
        code_repository_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::CodeRepository``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param git_config: ``AWS::SageMaker::CodeRepository.GitConfig``.
        :param code_repository_name: ``AWS::SageMaker::CodeRepository.CodeRepositoryName``.
        :param tags: ``AWS::SageMaker::CodeRepository.Tags``.
        '''
        props = CfnCodeRepositoryProps(
            git_config=git_config, code_repository_name=code_repository_name, tags=tags
        )

        jsii.create(CfnCodeRepository, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrCodeRepositoryName")
    def attr_code_repository_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: CodeRepositoryName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCodeRepositoryName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::CodeRepository.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html#cfn-sagemaker-coderepository-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="gitConfig")
    def git_config(
        self,
    ) -> typing.Union["CfnCodeRepository.GitConfigProperty", aws_cdk.core.IResolvable]:
        '''``AWS::SageMaker::CodeRepository.GitConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html#cfn-sagemaker-coderepository-gitconfig
        '''
        return typing.cast(typing.Union["CfnCodeRepository.GitConfigProperty", aws_cdk.core.IResolvable], jsii.get(self, "gitConfig"))

    @git_config.setter
    def git_config(
        self,
        value: typing.Union["CfnCodeRepository.GitConfigProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "gitConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="codeRepositoryName")
    def code_repository_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::CodeRepository.CodeRepositoryName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html#cfn-sagemaker-coderepository-coderepositoryname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codeRepositoryName"))

    @code_repository_name.setter
    def code_repository_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "codeRepositoryName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnCodeRepository.GitConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "repository_url": "repositoryUrl",
            "branch": "branch",
            "secret_arn": "secretArn",
        },
    )
    class GitConfigProperty:
        def __init__(
            self,
            *,
            repository_url: builtins.str,
            branch: typing.Optional[builtins.str] = None,
            secret_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param repository_url: ``CfnCodeRepository.GitConfigProperty.RepositoryUrl``.
            :param branch: ``CfnCodeRepository.GitConfigProperty.Branch``.
            :param secret_arn: ``CfnCodeRepository.GitConfigProperty.SecretArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-coderepository-gitconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "repository_url": repository_url,
            }
            if branch is not None:
                self._values["branch"] = branch
            if secret_arn is not None:
                self._values["secret_arn"] = secret_arn

        @builtins.property
        def repository_url(self) -> builtins.str:
            '''``CfnCodeRepository.GitConfigProperty.RepositoryUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-coderepository-gitconfig.html#cfn-sagemaker-coderepository-gitconfig-repositoryurl
            '''
            result = self._values.get("repository_url")
            assert result is not None, "Required property 'repository_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def branch(self) -> typing.Optional[builtins.str]:
            '''``CfnCodeRepository.GitConfigProperty.Branch``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-coderepository-gitconfig.html#cfn-sagemaker-coderepository-gitconfig-branch
            '''
            result = self._values.get("branch")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secret_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnCodeRepository.GitConfigProperty.SecretArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-coderepository-gitconfig.html#cfn-sagemaker-coderepository-gitconfig-secretarn
            '''
            result = self._values.get("secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GitConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnCodeRepositoryProps",
    jsii_struct_bases=[],
    name_mapping={
        "git_config": "gitConfig",
        "code_repository_name": "codeRepositoryName",
        "tags": "tags",
    },
)
class CfnCodeRepositoryProps:
    def __init__(
        self,
        *,
        git_config: typing.Union[CfnCodeRepository.GitConfigProperty, aws_cdk.core.IResolvable],
        code_repository_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::CodeRepository``.

        :param git_config: ``AWS::SageMaker::CodeRepository.GitConfig``.
        :param code_repository_name: ``AWS::SageMaker::CodeRepository.CodeRepositoryName``.
        :param tags: ``AWS::SageMaker::CodeRepository.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "git_config": git_config,
        }
        if code_repository_name is not None:
            self._values["code_repository_name"] = code_repository_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def git_config(
        self,
    ) -> typing.Union[CfnCodeRepository.GitConfigProperty, aws_cdk.core.IResolvable]:
        '''``AWS::SageMaker::CodeRepository.GitConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html#cfn-sagemaker-coderepository-gitconfig
        '''
        result = self._values.get("git_config")
        assert result is not None, "Required property 'git_config' is missing"
        return typing.cast(typing.Union[CfnCodeRepository.GitConfigProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def code_repository_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::CodeRepository.CodeRepositoryName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html#cfn-sagemaker-coderepository-coderepositoryname
        '''
        result = self._values.get("code_repository_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::CodeRepository.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html#cfn-sagemaker-coderepository-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCodeRepositoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDataQualityJobDefinition(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition",
):
    '''A CloudFormation ``AWS::SageMaker::DataQualityJobDefinition``.

    :cloudformationResource: AWS::SageMaker::DataQualityJobDefinition
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        data_quality_app_specification: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty"],
        data_quality_job_input: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityJobInputProperty"],
        data_quality_job_output_config: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringOutputConfigProperty"],
        job_resources: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringResourcesProperty"],
        role_arn: builtins.str,
        data_quality_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty"]] = None,
        job_definition_name: typing.Optional[builtins.str] = None,
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.NetworkConfigProperty"]] = None,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.StoppingConditionProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::DataQualityJobDefinition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param data_quality_app_specification: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityAppSpecification``.
        :param data_quality_job_input: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobInput``.
        :param data_quality_job_output_config: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobOutputConfig``.
        :param job_resources: ``AWS::SageMaker::DataQualityJobDefinition.JobResources``.
        :param role_arn: ``AWS::SageMaker::DataQualityJobDefinition.RoleArn``.
        :param data_quality_baseline_config: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityBaselineConfig``.
        :param job_definition_name: ``AWS::SageMaker::DataQualityJobDefinition.JobDefinitionName``.
        :param network_config: ``AWS::SageMaker::DataQualityJobDefinition.NetworkConfig``.
        :param stopping_condition: ``AWS::SageMaker::DataQualityJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::DataQualityJobDefinition.Tags``.
        '''
        props = CfnDataQualityJobDefinitionProps(
            data_quality_app_specification=data_quality_app_specification,
            data_quality_job_input=data_quality_job_input,
            data_quality_job_output_config=data_quality_job_output_config,
            job_resources=job_resources,
            role_arn=role_arn,
            data_quality_baseline_config=data_quality_baseline_config,
            job_definition_name=job_definition_name,
            network_config=network_config,
            stopping_condition=stopping_condition,
            tags=tags,
        )

        jsii.create(CfnDataQualityJobDefinition, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrJobDefinitionArn")
    def attr_job_definition_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: JobDefinitionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrJobDefinitionArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::DataQualityJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataQualityAppSpecification")
    def data_quality_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty"]:
        '''``AWS::SageMaker::DataQualityJobDefinition.DataQualityAppSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty"], jsii.get(self, "dataQualityAppSpecification"))

    @data_quality_app_specification.setter
    def data_quality_app_specification(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty"],
    ) -> None:
        jsii.set(self, "dataQualityAppSpecification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataQualityJobInput")
    def data_quality_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityJobInputProperty"]:
        '''``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobInput``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityJobInputProperty"], jsii.get(self, "dataQualityJobInput"))

    @data_quality_job_input.setter
    def data_quality_job_input(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityJobInputProperty"],
    ) -> None:
        jsii.set(self, "dataQualityJobInput", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataQualityJobOutputConfig")
    def data_quality_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringOutputConfigProperty"]:
        '''``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobOutputConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjoboutputconfig
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringOutputConfigProperty"], jsii.get(self, "dataQualityJobOutputConfig"))

    @data_quality_job_output_config.setter
    def data_quality_job_output_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringOutputConfigProperty"],
    ) -> None:
        jsii.set(self, "dataQualityJobOutputConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobResources")
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringResourcesProperty"]:
        '''``AWS::SageMaker::DataQualityJobDefinition.JobResources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-jobresources
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringResourcesProperty"], jsii.get(self, "jobResources"))

    @job_resources.setter
    def job_resources(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringResourcesProperty"],
    ) -> None:
        jsii.set(self, "jobResources", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::DataQualityJobDefinition.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataQualityBaselineConfig")
    def data_quality_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty"]]:
        '''``AWS::SageMaker::DataQualityJobDefinition.DataQualityBaselineConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty"]], jsii.get(self, "dataQualityBaselineConfig"))

    @data_quality_baseline_config.setter
    def data_quality_baseline_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty"]],
    ) -> None:
        jsii.set(self, "dataQualityBaselineConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobDefinitionName")
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::DataQualityJobDefinition.JobDefinitionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-jobdefinitionname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobDefinitionName"))

    @job_definition_name.setter
    def job_definition_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "jobDefinitionName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="networkConfig")
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.NetworkConfigProperty"]]:
        '''``AWS::SageMaker::DataQualityJobDefinition.NetworkConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-networkconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.NetworkConfigProperty"]], jsii.get(self, "networkConfig"))

    @network_config.setter
    def network_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.NetworkConfigProperty"]],
    ) -> None:
        jsii.set(self, "networkConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stoppingCondition")
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.StoppingConditionProperty"]]:
        '''``AWS::SageMaker::DataQualityJobDefinition.StoppingCondition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-stoppingcondition
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.StoppingConditionProperty"]], jsii.get(self, "stoppingCondition"))

    @stopping_condition.setter
    def stopping_condition(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.StoppingConditionProperty"]],
    ) -> None:
        jsii.set(self, "stoppingCondition", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.ClusterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_count": "instanceCount",
            "instance_type": "instanceType",
            "volume_size_in_gb": "volumeSizeInGb",
            "volume_kms_key_id": "volumeKmsKeyId",
        },
    )
    class ClusterConfigProperty:
        def __init__(
            self,
            *,
            instance_count: jsii.Number,
            instance_type: builtins.str,
            volume_size_in_gb: jsii.Number,
            volume_kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param instance_count: ``CfnDataQualityJobDefinition.ClusterConfigProperty.InstanceCount``.
            :param instance_type: ``CfnDataQualityJobDefinition.ClusterConfigProperty.InstanceType``.
            :param volume_size_in_gb: ``CfnDataQualityJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.
            :param volume_kms_key_id: ``CfnDataQualityJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "instance_count": instance_count,
                "instance_type": instance_type,
                "volume_size_in_gb": volume_size_in_gb,
            }
            if volume_kms_key_id is not None:
                self._values["volume_kms_key_id"] = volume_kms_key_id

        @builtins.property
        def instance_count(self) -> jsii.Number:
            '''``CfnDataQualityJobDefinition.ClusterConfigProperty.InstanceCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html#cfn-sagemaker-dataqualityjobdefinition-clusterconfig-instancecount
            '''
            result = self._values.get("instance_count")
            assert result is not None, "Required property 'instance_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''``CfnDataQualityJobDefinition.ClusterConfigProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html#cfn-sagemaker-dataqualityjobdefinition-clusterconfig-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def volume_size_in_gb(self) -> jsii.Number:
            '''``CfnDataQualityJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html#cfn-sagemaker-dataqualityjobdefinition-clusterconfig-volumesizeingb
            '''
            result = self._values.get("volume_size_in_gb")
            assert result is not None, "Required property 'volume_size_in_gb' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDataQualityJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-clusterconfig.html#cfn-sagemaker-dataqualityjobdefinition-clusterconfig-volumekmskeyid
            '''
            result = self._values.get("volume_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClusterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.ConstraintsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class ConstraintsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            '''
            :param s3_uri: ``CfnDataQualityJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-constraintsresource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnDataQualityJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-constraintsresource.html#cfn-sagemaker-dataqualityjobdefinition-constraintsresource-s3uri
            '''
            result = self._values.get("s3_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConstraintsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_uri": "imageUri",
            "container_arguments": "containerArguments",
            "container_entrypoint": "containerEntrypoint",
            "environment": "environment",
            "post_analytics_processor_source_uri": "postAnalyticsProcessorSourceUri",
            "record_preprocessor_source_uri": "recordPreprocessorSourceUri",
        },
    )
    class DataQualityAppSpecificationProperty:
        def __init__(
            self,
            *,
            image_uri: builtins.str,
            container_arguments: typing.Optional[typing.Sequence[builtins.str]] = None,
            container_entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
            environment: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.EnvironmentProperty"]] = None,
            post_analytics_processor_source_uri: typing.Optional[builtins.str] = None,
            record_preprocessor_source_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param image_uri: ``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.ImageUri``.
            :param container_arguments: ``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.ContainerArguments``.
            :param container_entrypoint: ``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.ContainerEntrypoint``.
            :param environment: ``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.Environment``.
            :param post_analytics_processor_source_uri: ``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.PostAnalyticsProcessorSourceUri``.
            :param record_preprocessor_source_uri: ``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.RecordPreprocessorSourceUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "image_uri": image_uri,
            }
            if container_arguments is not None:
                self._values["container_arguments"] = container_arguments
            if container_entrypoint is not None:
                self._values["container_entrypoint"] = container_entrypoint
            if environment is not None:
                self._values["environment"] = environment
            if post_analytics_processor_source_uri is not None:
                self._values["post_analytics_processor_source_uri"] = post_analytics_processor_source_uri
            if record_preprocessor_source_uri is not None:
                self._values["record_preprocessor_source_uri"] = record_preprocessor_source_uri

        @builtins.property
        def image_uri(self) -> builtins.str:
            '''``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.ImageUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-imageuri
            '''
            result = self._values.get("image_uri")
            assert result is not None, "Required property 'image_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def container_arguments(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.ContainerArguments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-containerarguments
            '''
            result = self._values.get("container_arguments")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def container_entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.ContainerEntrypoint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-containerentrypoint
            '''
            result = self._values.get("container_entrypoint")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.EnvironmentProperty"]]:
            '''``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.Environment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-environment
            '''
            result = self._values.get("environment")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.EnvironmentProperty"]], result)

        @builtins.property
        def post_analytics_processor_source_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.PostAnalyticsProcessorSourceUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-postanalyticsprocessorsourceuri
            '''
            result = self._values.get("post_analytics_processor_source_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def record_preprocessor_source_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty.RecordPreprocessorSourceUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityappspecification.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification-recordpreprocessorsourceuri
            '''
            result = self._values.get("record_preprocessor_source_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataQualityAppSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "baselining_job_name": "baseliningJobName",
            "constraints_resource": "constraintsResource",
            "statistics_resource": "statisticsResource",
        },
    )
    class DataQualityBaselineConfigProperty:
        def __init__(
            self,
            *,
            baselining_job_name: typing.Optional[builtins.str] = None,
            constraints_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.ConstraintsResourceProperty"]] = None,
            statistics_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.StatisticsResourceProperty"]] = None,
        ) -> None:
            '''
            :param baselining_job_name: ``CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty.BaseliningJobName``.
            :param constraints_resource: ``CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty.ConstraintsResource``.
            :param statistics_resource: ``CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty.StatisticsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if baselining_job_name is not None:
                self._values["baselining_job_name"] = baselining_job_name
            if constraints_resource is not None:
                self._values["constraints_resource"] = constraints_resource
            if statistics_resource is not None:
                self._values["statistics_resource"] = statistics_resource

        @builtins.property
        def baselining_job_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty.BaseliningJobName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig.html#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig-baseliningjobname
            '''
            result = self._values.get("baselining_job_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def constraints_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.ConstraintsResourceProperty"]]:
            '''``CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty.ConstraintsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig.html#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig-constraintsresource
            '''
            result = self._values.get("constraints_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.ConstraintsResourceProperty"]], result)

        @builtins.property
        def statistics_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.StatisticsResourceProperty"]]:
            '''``CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty.StatisticsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig.html#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig-statisticsresource
            '''
            result = self._values.get("statistics_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.StatisticsResourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataQualityBaselineConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.DataQualityJobInputProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint_input": "endpointInput"},
    )
    class DataQualityJobInputProperty:
        def __init__(
            self,
            *,
            endpoint_input: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.EndpointInputProperty"],
        ) -> None:
            '''
            :param endpoint_input: ``CfnDataQualityJobDefinition.DataQualityJobInputProperty.EndpointInput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityjobinput.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_input": endpoint_input,
            }

        @builtins.property
        def endpoint_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.EndpointInputProperty"]:
            '''``CfnDataQualityJobDefinition.DataQualityJobInputProperty.EndpointInput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-dataqualityjobinput.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput-endpointinput
            '''
            result = self._values.get("endpoint_input")
            assert result is not None, "Required property 'endpoint_input' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.EndpointInputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataQualityJobInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.EndpointInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_name": "endpointName",
            "local_path": "localPath",
            "s3_data_distribution_type": "s3DataDistributionType",
            "s3_input_mode": "s3InputMode",
        },
    )
    class EndpointInputProperty:
        def __init__(
            self,
            *,
            endpoint_name: builtins.str,
            local_path: builtins.str,
            s3_data_distribution_type: typing.Optional[builtins.str] = None,
            s3_input_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param endpoint_name: ``CfnDataQualityJobDefinition.EndpointInputProperty.EndpointName``.
            :param local_path: ``CfnDataQualityJobDefinition.EndpointInputProperty.LocalPath``.
            :param s3_data_distribution_type: ``CfnDataQualityJobDefinition.EndpointInputProperty.S3DataDistributionType``.
            :param s3_input_mode: ``CfnDataQualityJobDefinition.EndpointInputProperty.S3InputMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_name": endpoint_name,
                "local_path": local_path,
            }
            if s3_data_distribution_type is not None:
                self._values["s3_data_distribution_type"] = s3_data_distribution_type
            if s3_input_mode is not None:
                self._values["s3_input_mode"] = s3_input_mode

        @builtins.property
        def endpoint_name(self) -> builtins.str:
            '''``CfnDataQualityJobDefinition.EndpointInputProperty.EndpointName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html#cfn-sagemaker-dataqualityjobdefinition-endpointinput-endpointname
            '''
            result = self._values.get("endpoint_name")
            assert result is not None, "Required property 'endpoint_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def local_path(self) -> builtins.str:
            '''``CfnDataQualityJobDefinition.EndpointInputProperty.LocalPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html#cfn-sagemaker-dataqualityjobdefinition-endpointinput-localpath
            '''
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_data_distribution_type(self) -> typing.Optional[builtins.str]:
            '''``CfnDataQualityJobDefinition.EndpointInputProperty.S3DataDistributionType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html#cfn-sagemaker-dataqualityjobdefinition-endpointinput-s3datadistributiontype
            '''
            result = self._values.get("s3_data_distribution_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_input_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnDataQualityJobDefinition.EndpointInputProperty.S3InputMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-endpointinput.html#cfn-sagemaker-dataqualityjobdefinition-endpointinput-s3inputmode
            '''
            result = self._values.get("s3_input_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.EnvironmentProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class EnvironmentProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-environment.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.MonitoringOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "monitoring_outputs": "monitoringOutputs",
            "kms_key_id": "kmsKeyId",
        },
    )
    class MonitoringOutputConfigProperty:
        def __init__(
            self,
            *,
            monitoring_outputs: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringOutputProperty"]]],
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param monitoring_outputs: ``CfnDataQualityJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.
            :param kms_key_id: ``CfnDataQualityJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutputconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "monitoring_outputs": monitoring_outputs,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def monitoring_outputs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringOutputProperty"]]]:
            '''``CfnDataQualityJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-dataqualityjobdefinition-monitoringoutputconfig-monitoringoutputs
            '''
            result = self._values.get("monitoring_outputs")
            assert result is not None, "Required property 'monitoring_outputs' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.MonitoringOutputProperty"]]], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDataQualityJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-dataqualityjobdefinition-monitoringoutputconfig-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.MonitoringOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_output": "s3Output"},
    )
    class MonitoringOutputProperty:
        def __init__(
            self,
            *,
            s3_output: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.S3OutputProperty"],
        ) -> None:
            '''
            :param s3_output: ``CfnDataQualityJobDefinition.MonitoringOutputProperty.S3Output``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutput.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "s3_output": s3_output,
            }

        @builtins.property
        def s3_output(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.S3OutputProperty"]:
            '''``CfnDataQualityJobDefinition.MonitoringOutputProperty.S3Output``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringoutput.html#cfn-sagemaker-dataqualityjobdefinition-monitoringoutput-s3output
            '''
            result = self._values.get("s3_output")
            assert result is not None, "Required property 's3_output' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.S3OutputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.MonitoringResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_config": "clusterConfig"},
    )
    class MonitoringResourcesProperty:
        def __init__(
            self,
            *,
            cluster_config: typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.ClusterConfigProperty"],
        ) -> None:
            '''
            :param cluster_config: ``CfnDataQualityJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringresources.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cluster_config": cluster_config,
            }

        @builtins.property
        def cluster_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.ClusterConfigProperty"]:
            '''``CfnDataQualityJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-monitoringresources.html#cfn-sagemaker-dataqualityjobdefinition-monitoringresources-clusterconfig
            '''
            result = self._values.get("cluster_config")
            assert result is not None, "Required property 'cluster_config' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.ClusterConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.NetworkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_inter_container_traffic_encryption": "enableInterContainerTrafficEncryption",
            "enable_network_isolation": "enableNetworkIsolation",
            "vpc_config": "vpcConfig",
        },
    )
    class NetworkConfigProperty:
        def __init__(
            self,
            *,
            enable_inter_container_traffic_encryption: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.VpcConfigProperty"]] = None,
        ) -> None:
            '''
            :param enable_inter_container_traffic_encryption: ``CfnDataQualityJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.
            :param enable_network_isolation: ``CfnDataQualityJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.
            :param vpc_config: ``CfnDataQualityJobDefinition.NetworkConfigProperty.VpcConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-networkconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if enable_inter_container_traffic_encryption is not None:
                self._values["enable_inter_container_traffic_encryption"] = enable_inter_container_traffic_encryption
            if enable_network_isolation is not None:
                self._values["enable_network_isolation"] = enable_network_isolation
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def enable_inter_container_traffic_encryption(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDataQualityJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-networkconfig.html#cfn-sagemaker-dataqualityjobdefinition-networkconfig-enableintercontainertrafficencryption
            '''
            result = self._values.get("enable_inter_container_traffic_encryption")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def enable_network_isolation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDataQualityJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-networkconfig.html#cfn-sagemaker-dataqualityjobdefinition-networkconfig-enablenetworkisolation
            '''
            result = self._values.get("enable_network_isolation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.VpcConfigProperty"]]:
            '''``CfnDataQualityJobDefinition.NetworkConfigProperty.VpcConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-networkconfig.html#cfn-sagemaker-dataqualityjobdefinition-networkconfig-vpcconfig
            '''
            result = self._values.get("vpc_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataQualityJobDefinition.VpcConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.S3OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "local_path": "localPath",
            "s3_uri": "s3Uri",
            "s3_upload_mode": "s3UploadMode",
        },
    )
    class S3OutputProperty:
        def __init__(
            self,
            *,
            local_path: builtins.str,
            s3_uri: builtins.str,
            s3_upload_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param local_path: ``CfnDataQualityJobDefinition.S3OutputProperty.LocalPath``.
            :param s3_uri: ``CfnDataQualityJobDefinition.S3OutputProperty.S3Uri``.
            :param s3_upload_mode: ``CfnDataQualityJobDefinition.S3OutputProperty.S3UploadMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-s3output.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "local_path": local_path,
                "s3_uri": s3_uri,
            }
            if s3_upload_mode is not None:
                self._values["s3_upload_mode"] = s3_upload_mode

        @builtins.property
        def local_path(self) -> builtins.str:
            '''``CfnDataQualityJobDefinition.S3OutputProperty.LocalPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-s3output.html#cfn-sagemaker-dataqualityjobdefinition-s3output-localpath
            '''
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_uri(self) -> builtins.str:
            '''``CfnDataQualityJobDefinition.S3OutputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-s3output.html#cfn-sagemaker-dataqualityjobdefinition-s3output-s3uri
            '''
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_upload_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnDataQualityJobDefinition.S3OutputProperty.S3UploadMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-s3output.html#cfn-sagemaker-dataqualityjobdefinition-s3output-s3uploadmode
            '''
            result = self._values.get("s3_upload_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.StatisticsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class StatisticsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            '''
            :param s3_uri: ``CfnDataQualityJobDefinition.StatisticsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-statisticsresource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnDataQualityJobDefinition.StatisticsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-statisticsresource.html#cfn-sagemaker-dataqualityjobdefinition-statisticsresource-s3uri
            '''
            result = self._values.get("s3_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatisticsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.StoppingConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"max_runtime_in_seconds": "maxRuntimeInSeconds"},
    )
    class StoppingConditionProperty:
        def __init__(self, *, max_runtime_in_seconds: jsii.Number) -> None:
            '''
            :param max_runtime_in_seconds: ``CfnDataQualityJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-stoppingcondition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_runtime_in_seconds": max_runtime_in_seconds,
            }

        @builtins.property
        def max_runtime_in_seconds(self) -> jsii.Number:
            '''``CfnDataQualityJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-stoppingcondition.html#cfn-sagemaker-dataqualityjobdefinition-stoppingcondition-maxruntimeinseconds
            '''
            result = self._values.get("max_runtime_in_seconds")
            assert result is not None, "Required property 'max_runtime_in_seconds' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StoppingConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinition.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param security_group_ids: ``CfnDataQualityJobDefinition.VpcConfigProperty.SecurityGroupIds``.
            :param subnets: ``CfnDataQualityJobDefinition.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-vpcconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''``CfnDataQualityJobDefinition.VpcConfigProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-vpcconfig.html#cfn-sagemaker-dataqualityjobdefinition-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''``CfnDataQualityJobDefinition.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-dataqualityjobdefinition-vpcconfig.html#cfn-sagemaker-dataqualityjobdefinition-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnDataQualityJobDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_quality_app_specification": "dataQualityAppSpecification",
        "data_quality_job_input": "dataQualityJobInput",
        "data_quality_job_output_config": "dataQualityJobOutputConfig",
        "job_resources": "jobResources",
        "role_arn": "roleArn",
        "data_quality_baseline_config": "dataQualityBaselineConfig",
        "job_definition_name": "jobDefinitionName",
        "network_config": "networkConfig",
        "stopping_condition": "stoppingCondition",
        "tags": "tags",
    },
)
class CfnDataQualityJobDefinitionProps:
    def __init__(
        self,
        *,
        data_quality_app_specification: typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty],
        data_quality_job_input: typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityJobInputProperty],
        data_quality_job_output_config: typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.MonitoringOutputConfigProperty],
        job_resources: typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.MonitoringResourcesProperty],
        role_arn: builtins.str,
        data_quality_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty]] = None,
        job_definition_name: typing.Optional[builtins.str] = None,
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.NetworkConfigProperty]] = None,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.StoppingConditionProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::DataQualityJobDefinition``.

        :param data_quality_app_specification: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityAppSpecification``.
        :param data_quality_job_input: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobInput``.
        :param data_quality_job_output_config: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobOutputConfig``.
        :param job_resources: ``AWS::SageMaker::DataQualityJobDefinition.JobResources``.
        :param role_arn: ``AWS::SageMaker::DataQualityJobDefinition.RoleArn``.
        :param data_quality_baseline_config: ``AWS::SageMaker::DataQualityJobDefinition.DataQualityBaselineConfig``.
        :param job_definition_name: ``AWS::SageMaker::DataQualityJobDefinition.JobDefinitionName``.
        :param network_config: ``AWS::SageMaker::DataQualityJobDefinition.NetworkConfig``.
        :param stopping_condition: ``AWS::SageMaker::DataQualityJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::DataQualityJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "data_quality_app_specification": data_quality_app_specification,
            "data_quality_job_input": data_quality_job_input,
            "data_quality_job_output_config": data_quality_job_output_config,
            "job_resources": job_resources,
            "role_arn": role_arn,
        }
        if data_quality_baseline_config is not None:
            self._values["data_quality_baseline_config"] = data_quality_baseline_config
        if job_definition_name is not None:
            self._values["job_definition_name"] = job_definition_name
        if network_config is not None:
            self._values["network_config"] = network_config
        if stopping_condition is not None:
            self._values["stopping_condition"] = stopping_condition
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def data_quality_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty]:
        '''``AWS::SageMaker::DataQualityJobDefinition.DataQualityAppSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityappspecification
        '''
        result = self._values.get("data_quality_app_specification")
        assert result is not None, "Required property 'data_quality_app_specification' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityAppSpecificationProperty], result)

    @builtins.property
    def data_quality_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityJobInputProperty]:
        '''``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobInput``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjobinput
        '''
        result = self._values.get("data_quality_job_input")
        assert result is not None, "Required property 'data_quality_job_input' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityJobInputProperty], result)

    @builtins.property
    def data_quality_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.MonitoringOutputConfigProperty]:
        '''``AWS::SageMaker::DataQualityJobDefinition.DataQualityJobOutputConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualityjoboutputconfig
        '''
        result = self._values.get("data_quality_job_output_config")
        assert result is not None, "Required property 'data_quality_job_output_config' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.MonitoringOutputConfigProperty], result)

    @builtins.property
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.MonitoringResourcesProperty]:
        '''``AWS::SageMaker::DataQualityJobDefinition.JobResources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-jobresources
        '''
        result = self._values.get("job_resources")
        assert result is not None, "Required property 'job_resources' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.MonitoringResourcesProperty], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::DataQualityJobDefinition.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_quality_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty]]:
        '''``AWS::SageMaker::DataQualityJobDefinition.DataQualityBaselineConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-dataqualitybaselineconfig
        '''
        result = self._values.get("data_quality_baseline_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.DataQualityBaselineConfigProperty]], result)

    @builtins.property
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::DataQualityJobDefinition.JobDefinitionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-jobdefinitionname
        '''
        result = self._values.get("job_definition_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.NetworkConfigProperty]]:
        '''``AWS::SageMaker::DataQualityJobDefinition.NetworkConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-networkconfig
        '''
        result = self._values.get("network_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.NetworkConfigProperty]], result)

    @builtins.property
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.StoppingConditionProperty]]:
        '''``AWS::SageMaker::DataQualityJobDefinition.StoppingCondition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-stoppingcondition
        '''
        result = self._values.get("stopping_condition")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataQualityJobDefinition.StoppingConditionProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::DataQualityJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-dataqualityjobdefinition.html#cfn-sagemaker-dataqualityjobdefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataQualityJobDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDevice(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnDevice",
):
    '''A CloudFormation ``AWS::SageMaker::Device``.

    :cloudformationResource: AWS::SageMaker::Device
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        device_fleet_name: builtins.str,
        device: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDevice.DeviceProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::Device``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param device_fleet_name: ``AWS::SageMaker::Device.DeviceFleetName``.
        :param device: ``AWS::SageMaker::Device.Device``.
        :param tags: ``AWS::SageMaker::Device.Tags``.
        '''
        props = CfnDeviceProps(
            device_fleet_name=device_fleet_name, device=device, tags=tags
        )

        jsii.create(CfnDevice, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::Device.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deviceFleetName")
    def device_fleet_name(self) -> builtins.str:
        '''``AWS::SageMaker::Device.DeviceFleetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-devicefleetname
        '''
        return typing.cast(builtins.str, jsii.get(self, "deviceFleetName"))

    @device_fleet_name.setter
    def device_fleet_name(self, value: builtins.str) -> None:
        jsii.set(self, "deviceFleetName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="device")
    def device(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDevice.DeviceProperty"]]:
        '''``AWS::SageMaker::Device.Device``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-device
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDevice.DeviceProperty"]], jsii.get(self, "device"))

    @device.setter
    def device(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDevice.DeviceProperty"]],
    ) -> None:
        jsii.set(self, "device", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDevice.DeviceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "device_name": "deviceName",
            "description": "description",
            "iot_thing_name": "iotThingName",
        },
    )
    class DeviceProperty:
        def __init__(
            self,
            *,
            device_name: builtins.str,
            description: typing.Optional[builtins.str] = None,
            iot_thing_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param device_name: ``CfnDevice.DeviceProperty.DeviceName``.
            :param description: ``CfnDevice.DeviceProperty.Description``.
            :param iot_thing_name: ``CfnDevice.DeviceProperty.IotThingName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-device-device.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "device_name": device_name,
            }
            if description is not None:
                self._values["description"] = description
            if iot_thing_name is not None:
                self._values["iot_thing_name"] = iot_thing_name

        @builtins.property
        def device_name(self) -> builtins.str:
            '''``CfnDevice.DeviceProperty.DeviceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-device-device.html#cfn-sagemaker-device-device-devicename
            '''
            result = self._values.get("device_name")
            assert result is not None, "Required property 'device_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnDevice.DeviceProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-device-device.html#cfn-sagemaker-device-device-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def iot_thing_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDevice.DeviceProperty.IotThingName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-device-device.html#cfn-sagemaker-device-device-iotthingname
            '''
            result = self._values.get("iot_thing_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeviceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDeviceFleet(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnDeviceFleet",
):
    '''A CloudFormation ``AWS::SageMaker::DeviceFleet``.

    :cloudformationResource: AWS::SageMaker::DeviceFleet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        device_fleet_name: builtins.str,
        output_config: typing.Union[aws_cdk.core.IResolvable, "CfnDeviceFleet.EdgeOutputConfigProperty"],
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::DeviceFleet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param device_fleet_name: ``AWS::SageMaker::DeviceFleet.DeviceFleetName``.
        :param output_config: ``AWS::SageMaker::DeviceFleet.OutputConfig``.
        :param role_arn: ``AWS::SageMaker::DeviceFleet.RoleArn``.
        :param description: ``AWS::SageMaker::DeviceFleet.Description``.
        :param tags: ``AWS::SageMaker::DeviceFleet.Tags``.
        '''
        props = CfnDeviceFleetProps(
            device_fleet_name=device_fleet_name,
            output_config=output_config,
            role_arn=role_arn,
            description=description,
            tags=tags,
        )

        jsii.create(CfnDeviceFleet, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::DeviceFleet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deviceFleetName")
    def device_fleet_name(self) -> builtins.str:
        '''``AWS::SageMaker::DeviceFleet.DeviceFleetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-devicefleetname
        '''
        return typing.cast(builtins.str, jsii.get(self, "deviceFleetName"))

    @device_fleet_name.setter
    def device_fleet_name(self, value: builtins.str) -> None:
        jsii.set(self, "deviceFleetName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="outputConfig")
    def output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDeviceFleet.EdgeOutputConfigProperty"]:
        '''``AWS::SageMaker::DeviceFleet.OutputConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-outputconfig
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDeviceFleet.EdgeOutputConfigProperty"], jsii.get(self, "outputConfig"))

    @output_config.setter
    def output_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnDeviceFleet.EdgeOutputConfigProperty"],
    ) -> None:
        jsii.set(self, "outputConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::DeviceFleet.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::DeviceFleet.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDeviceFleet.EdgeOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "s3_output_location": "s3OutputLocation",
            "kms_key_id": "kmsKeyId",
        },
    )
    class EdgeOutputConfigProperty:
        def __init__(
            self,
            *,
            s3_output_location: builtins.str,
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param s3_output_location: ``CfnDeviceFleet.EdgeOutputConfigProperty.S3OutputLocation``.
            :param kms_key_id: ``CfnDeviceFleet.EdgeOutputConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-devicefleet-edgeoutputconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "s3_output_location": s3_output_location,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def s3_output_location(self) -> builtins.str:
            '''``CfnDeviceFleet.EdgeOutputConfigProperty.S3OutputLocation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-devicefleet-edgeoutputconfig.html#cfn-sagemaker-devicefleet-edgeoutputconfig-s3outputlocation
            '''
            result = self._values.get("s3_output_location")
            assert result is not None, "Required property 's3_output_location' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDeviceFleet.EdgeOutputConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-devicefleet-edgeoutputconfig.html#cfn-sagemaker-devicefleet-edgeoutputconfig-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EdgeOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnDeviceFleetProps",
    jsii_struct_bases=[],
    name_mapping={
        "device_fleet_name": "deviceFleetName",
        "output_config": "outputConfig",
        "role_arn": "roleArn",
        "description": "description",
        "tags": "tags",
    },
)
class CfnDeviceFleetProps:
    def __init__(
        self,
        *,
        device_fleet_name: builtins.str,
        output_config: typing.Union[aws_cdk.core.IResolvable, CfnDeviceFleet.EdgeOutputConfigProperty],
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::DeviceFleet``.

        :param device_fleet_name: ``AWS::SageMaker::DeviceFleet.DeviceFleetName``.
        :param output_config: ``AWS::SageMaker::DeviceFleet.OutputConfig``.
        :param role_arn: ``AWS::SageMaker::DeviceFleet.RoleArn``.
        :param description: ``AWS::SageMaker::DeviceFleet.Description``.
        :param tags: ``AWS::SageMaker::DeviceFleet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "device_fleet_name": device_fleet_name,
            "output_config": output_config,
            "role_arn": role_arn,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def device_fleet_name(self) -> builtins.str:
        '''``AWS::SageMaker::DeviceFleet.DeviceFleetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-devicefleetname
        '''
        result = self._values.get("device_fleet_name")
        assert result is not None, "Required property 'device_fleet_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnDeviceFleet.EdgeOutputConfigProperty]:
        '''``AWS::SageMaker::DeviceFleet.OutputConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-outputconfig
        '''
        result = self._values.get("output_config")
        assert result is not None, "Required property 'output_config' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnDeviceFleet.EdgeOutputConfigProperty], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::DeviceFleet.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::DeviceFleet.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::DeviceFleet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-devicefleet.html#cfn-sagemaker-devicefleet-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeviceFleetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnDeviceProps",
    jsii_struct_bases=[],
    name_mapping={
        "device_fleet_name": "deviceFleetName",
        "device": "device",
        "tags": "tags",
    },
)
class CfnDeviceProps:
    def __init__(
        self,
        *,
        device_fleet_name: builtins.str,
        device: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDevice.DeviceProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::Device``.

        :param device_fleet_name: ``AWS::SageMaker::Device.DeviceFleetName``.
        :param device: ``AWS::SageMaker::Device.Device``.
        :param tags: ``AWS::SageMaker::Device.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "device_fleet_name": device_fleet_name,
        }
        if device is not None:
            self._values["device"] = device
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def device_fleet_name(self) -> builtins.str:
        '''``AWS::SageMaker::Device.DeviceFleetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-devicefleetname
        '''
        result = self._values.get("device_fleet_name")
        assert result is not None, "Required property 'device_fleet_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def device(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDevice.DeviceProperty]]:
        '''``AWS::SageMaker::Device.Device``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-device
        '''
        result = self._values.get("device")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDevice.DeviceProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::Device.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-device.html#cfn-sagemaker-device-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeviceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDomain(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnDomain",
):
    '''A CloudFormation ``AWS::SageMaker::Domain``.

    :cloudformationResource: AWS::SageMaker::Domain
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        auth_mode: builtins.str,
        default_user_settings: typing.Union[aws_cdk.core.IResolvable, "CfnDomain.UserSettingsProperty"],
        domain_name: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        app_network_access_type: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::Domain``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param auth_mode: ``AWS::SageMaker::Domain.AuthMode``.
        :param default_user_settings: ``AWS::SageMaker::Domain.DefaultUserSettings``.
        :param domain_name: ``AWS::SageMaker::Domain.DomainName``.
        :param subnet_ids: ``AWS::SageMaker::Domain.SubnetIds``.
        :param vpc_id: ``AWS::SageMaker::Domain.VpcId``.
        :param app_network_access_type: ``AWS::SageMaker::Domain.AppNetworkAccessType``.
        :param kms_key_id: ``AWS::SageMaker::Domain.KmsKeyId``.
        :param tags: ``AWS::SageMaker::Domain.Tags``.
        '''
        props = CfnDomainProps(
            auth_mode=auth_mode,
            default_user_settings=default_user_settings,
            domain_name=domain_name,
            subnet_ids=subnet_ids,
            vpc_id=vpc_id,
            app_network_access_type=app_network_access_type,
            kms_key_id=kms_key_id,
            tags=tags,
        )

        jsii.create(CfnDomain, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrDomainArn")
    def attr_domain_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: DomainArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrHomeEfsFileSystemId")
    def attr_home_efs_file_system_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: HomeEfsFileSystemId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHomeEfsFileSystemId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSingleSignOnManagedApplicationInstanceId")
    def attr_single_sign_on_managed_application_instance_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: SingleSignOnManagedApplicationInstanceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSingleSignOnManagedApplicationInstanceId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrUrl")
    def attr_url(self) -> builtins.str:
        '''
        :cloudformationAttribute: Url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::Domain.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="authMode")
    def auth_mode(self) -> builtins.str:
        '''``AWS::SageMaker::Domain.AuthMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-authmode
        '''
        return typing.cast(builtins.str, jsii.get(self, "authMode"))

    @auth_mode.setter
    def auth_mode(self, value: builtins.str) -> None:
        jsii.set(self, "authMode", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultUserSettings")
    def default_user_settings(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDomain.UserSettingsProperty"]:
        '''``AWS::SageMaker::Domain.DefaultUserSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-defaultusersettings
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDomain.UserSettingsProperty"], jsii.get(self, "defaultUserSettings"))

    @default_user_settings.setter
    def default_user_settings(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnDomain.UserSettingsProperty"],
    ) -> None:
        jsii.set(self, "defaultUserSettings", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''``AWS::SageMaker::Domain.DomainName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-domainname
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        jsii.set(self, "domainName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''``AWS::SageMaker::Domain.SubnetIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-subnetids
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "subnetIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''``AWS::SageMaker::Domain.VpcId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-vpcid
        '''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        jsii.set(self, "vpcId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="appNetworkAccessType")
    def app_network_access_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Domain.AppNetworkAccessType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-appnetworkaccesstype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appNetworkAccessType"))

    @app_network_access_type.setter
    def app_network_access_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "appNetworkAccessType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Domain.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyId", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDomain.CustomImageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "app_image_config_name": "appImageConfigName",
            "image_name": "imageName",
            "image_version_number": "imageVersionNumber",
        },
    )
    class CustomImageProperty:
        def __init__(
            self,
            *,
            app_image_config_name: builtins.str,
            image_name: builtins.str,
            image_version_number: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param app_image_config_name: ``CfnDomain.CustomImageProperty.AppImageConfigName``.
            :param image_name: ``CfnDomain.CustomImageProperty.ImageName``.
            :param image_version_number: ``CfnDomain.CustomImageProperty.ImageVersionNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-customimage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "app_image_config_name": app_image_config_name,
                "image_name": image_name,
            }
            if image_version_number is not None:
                self._values["image_version_number"] = image_version_number

        @builtins.property
        def app_image_config_name(self) -> builtins.str:
            '''``CfnDomain.CustomImageProperty.AppImageConfigName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-customimage.html#cfn-sagemaker-domain-customimage-appimageconfigname
            '''
            result = self._values.get("app_image_config_name")
            assert result is not None, "Required property 'app_image_config_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_name(self) -> builtins.str:
            '''``CfnDomain.CustomImageProperty.ImageName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-customimage.html#cfn-sagemaker-domain-customimage-imagename
            '''
            result = self._values.get("image_name")
            assert result is not None, "Required property 'image_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_version_number(self) -> typing.Optional[jsii.Number]:
            '''``CfnDomain.CustomImageProperty.ImageVersionNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-customimage.html#cfn-sagemaker-domain-customimage-imageversionnumber
            '''
            result = self._values.get("image_version_number")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomImageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDomain.JupyterServerAppSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"default_resource_spec": "defaultResourceSpec"},
    )
    class JupyterServerAppSettingsProperty:
        def __init__(
            self,
            *,
            default_resource_spec: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.ResourceSpecProperty"]] = None,
        ) -> None:
            '''
            :param default_resource_spec: ``CfnDomain.JupyterServerAppSettingsProperty.DefaultResourceSpec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-jupyterserverappsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if default_resource_spec is not None:
                self._values["default_resource_spec"] = default_resource_spec

        @builtins.property
        def default_resource_spec(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.ResourceSpecProperty"]]:
            '''``CfnDomain.JupyterServerAppSettingsProperty.DefaultResourceSpec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-jupyterserverappsettings.html#cfn-sagemaker-domain-jupyterserverappsettings-defaultresourcespec
            '''
            result = self._values.get("default_resource_spec")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.ResourceSpecProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JupyterServerAppSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDomain.KernelGatewayAppSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "custom_images": "customImages",
            "default_resource_spec": "defaultResourceSpec",
        },
    )
    class KernelGatewayAppSettingsProperty:
        def __init__(
            self,
            *,
            custom_images: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.CustomImageProperty"]]]] = None,
            default_resource_spec: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.ResourceSpecProperty"]] = None,
        ) -> None:
            '''
            :param custom_images: ``CfnDomain.KernelGatewayAppSettingsProperty.CustomImages``.
            :param default_resource_spec: ``CfnDomain.KernelGatewayAppSettingsProperty.DefaultResourceSpec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-kernelgatewayappsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if custom_images is not None:
                self._values["custom_images"] = custom_images
            if default_resource_spec is not None:
                self._values["default_resource_spec"] = default_resource_spec

        @builtins.property
        def custom_images(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.CustomImageProperty"]]]]:
            '''``CfnDomain.KernelGatewayAppSettingsProperty.CustomImages``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-kernelgatewayappsettings.html#cfn-sagemaker-domain-kernelgatewayappsettings-customimages
            '''
            result = self._values.get("custom_images")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.CustomImageProperty"]]]], result)

        @builtins.property
        def default_resource_spec(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.ResourceSpecProperty"]]:
            '''``CfnDomain.KernelGatewayAppSettingsProperty.DefaultResourceSpec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-kernelgatewayappsettings.html#cfn-sagemaker-domain-kernelgatewayappsettings-defaultresourcespec
            '''
            result = self._values.get("default_resource_spec")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.ResourceSpecProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KernelGatewayAppSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDomain.ResourceSpecProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_type": "instanceType",
            "sage_maker_image_arn": "sageMakerImageArn",
            "sage_maker_image_version_arn": "sageMakerImageVersionArn",
        },
    )
    class ResourceSpecProperty:
        def __init__(
            self,
            *,
            instance_type: typing.Optional[builtins.str] = None,
            sage_maker_image_arn: typing.Optional[builtins.str] = None,
            sage_maker_image_version_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param instance_type: ``CfnDomain.ResourceSpecProperty.InstanceType``.
            :param sage_maker_image_arn: ``CfnDomain.ResourceSpecProperty.SageMakerImageArn``.
            :param sage_maker_image_version_arn: ``CfnDomain.ResourceSpecProperty.SageMakerImageVersionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-resourcespec.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if instance_type is not None:
                self._values["instance_type"] = instance_type
            if sage_maker_image_arn is not None:
                self._values["sage_maker_image_arn"] = sage_maker_image_arn
            if sage_maker_image_version_arn is not None:
                self._values["sage_maker_image_version_arn"] = sage_maker_image_version_arn

        @builtins.property
        def instance_type(self) -> typing.Optional[builtins.str]:
            '''``CfnDomain.ResourceSpecProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-resourcespec.html#cfn-sagemaker-domain-resourcespec-instancetype
            '''
            result = self._values.get("instance_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sage_maker_image_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnDomain.ResourceSpecProperty.SageMakerImageArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-resourcespec.html#cfn-sagemaker-domain-resourcespec-sagemakerimagearn
            '''
            result = self._values.get("sage_maker_image_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sage_maker_image_version_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnDomain.ResourceSpecProperty.SageMakerImageVersionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-resourcespec.html#cfn-sagemaker-domain-resourcespec-sagemakerimageversionarn
            '''
            result = self._values.get("sage_maker_image_version_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceSpecProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDomain.SharingSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "notebook_output_option": "notebookOutputOption",
            "s3_kms_key_id": "s3KmsKeyId",
            "s3_output_path": "s3OutputPath",
        },
    )
    class SharingSettingsProperty:
        def __init__(
            self,
            *,
            notebook_output_option: typing.Optional[builtins.str] = None,
            s3_kms_key_id: typing.Optional[builtins.str] = None,
            s3_output_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param notebook_output_option: ``CfnDomain.SharingSettingsProperty.NotebookOutputOption``.
            :param s3_kms_key_id: ``CfnDomain.SharingSettingsProperty.S3KmsKeyId``.
            :param s3_output_path: ``CfnDomain.SharingSettingsProperty.S3OutputPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-sharingsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if notebook_output_option is not None:
                self._values["notebook_output_option"] = notebook_output_option
            if s3_kms_key_id is not None:
                self._values["s3_kms_key_id"] = s3_kms_key_id
            if s3_output_path is not None:
                self._values["s3_output_path"] = s3_output_path

        @builtins.property
        def notebook_output_option(self) -> typing.Optional[builtins.str]:
            '''``CfnDomain.SharingSettingsProperty.NotebookOutputOption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-sharingsettings.html#cfn-sagemaker-domain-sharingsettings-notebookoutputoption
            '''
            result = self._values.get("notebook_output_option")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDomain.SharingSettingsProperty.S3KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-sharingsettings.html#cfn-sagemaker-domain-sharingsettings-s3kmskeyid
            '''
            result = self._values.get("s3_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_output_path(self) -> typing.Optional[builtins.str]:
            '''``CfnDomain.SharingSettingsProperty.S3OutputPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-sharingsettings.html#cfn-sagemaker-domain-sharingsettings-s3outputpath
            '''
            result = self._values.get("s3_output_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SharingSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnDomain.UserSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "execution_role": "executionRole",
            "jupyter_server_app_settings": "jupyterServerAppSettings",
            "kernel_gateway_app_settings": "kernelGatewayAppSettings",
            "security_groups": "securityGroups",
            "sharing_settings": "sharingSettings",
        },
    )
    class UserSettingsProperty:
        def __init__(
            self,
            *,
            execution_role: typing.Optional[builtins.str] = None,
            jupyter_server_app_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.JupyterServerAppSettingsProperty"]] = None,
            kernel_gateway_app_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.KernelGatewayAppSettingsProperty"]] = None,
            security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
            sharing_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.SharingSettingsProperty"]] = None,
        ) -> None:
            '''
            :param execution_role: ``CfnDomain.UserSettingsProperty.ExecutionRole``.
            :param jupyter_server_app_settings: ``CfnDomain.UserSettingsProperty.JupyterServerAppSettings``.
            :param kernel_gateway_app_settings: ``CfnDomain.UserSettingsProperty.KernelGatewayAppSettings``.
            :param security_groups: ``CfnDomain.UserSettingsProperty.SecurityGroups``.
            :param sharing_settings: ``CfnDomain.UserSettingsProperty.SharingSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-usersettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if execution_role is not None:
                self._values["execution_role"] = execution_role
            if jupyter_server_app_settings is not None:
                self._values["jupyter_server_app_settings"] = jupyter_server_app_settings
            if kernel_gateway_app_settings is not None:
                self._values["kernel_gateway_app_settings"] = kernel_gateway_app_settings
            if security_groups is not None:
                self._values["security_groups"] = security_groups
            if sharing_settings is not None:
                self._values["sharing_settings"] = sharing_settings

        @builtins.property
        def execution_role(self) -> typing.Optional[builtins.str]:
            '''``CfnDomain.UserSettingsProperty.ExecutionRole``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-usersettings.html#cfn-sagemaker-domain-usersettings-executionrole
            '''
            result = self._values.get("execution_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def jupyter_server_app_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.JupyterServerAppSettingsProperty"]]:
            '''``CfnDomain.UserSettingsProperty.JupyterServerAppSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-usersettings.html#cfn-sagemaker-domain-usersettings-jupyterserverappsettings
            '''
            result = self._values.get("jupyter_server_app_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.JupyterServerAppSettingsProperty"]], result)

        @builtins.property
        def kernel_gateway_app_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.KernelGatewayAppSettingsProperty"]]:
            '''``CfnDomain.UserSettingsProperty.KernelGatewayAppSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-usersettings.html#cfn-sagemaker-domain-usersettings-kernelgatewayappsettings
            '''
            result = self._values.get("kernel_gateway_app_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.KernelGatewayAppSettingsProperty"]], result)

        @builtins.property
        def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDomain.UserSettingsProperty.SecurityGroups``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-usersettings.html#cfn-sagemaker-domain-usersettings-securitygroups
            '''
            result = self._values.get("security_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def sharing_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.SharingSettingsProperty"]]:
            '''``CfnDomain.UserSettingsProperty.SharingSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-domain-usersettings.html#cfn-sagemaker-domain-usersettings-sharingsettings
            '''
            result = self._values.get("sharing_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDomain.SharingSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnDomainProps",
    jsii_struct_bases=[],
    name_mapping={
        "auth_mode": "authMode",
        "default_user_settings": "defaultUserSettings",
        "domain_name": "domainName",
        "subnet_ids": "subnetIds",
        "vpc_id": "vpcId",
        "app_network_access_type": "appNetworkAccessType",
        "kms_key_id": "kmsKeyId",
        "tags": "tags",
    },
)
class CfnDomainProps:
    def __init__(
        self,
        *,
        auth_mode: builtins.str,
        default_user_settings: typing.Union[aws_cdk.core.IResolvable, CfnDomain.UserSettingsProperty],
        domain_name: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        app_network_access_type: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::Domain``.

        :param auth_mode: ``AWS::SageMaker::Domain.AuthMode``.
        :param default_user_settings: ``AWS::SageMaker::Domain.DefaultUserSettings``.
        :param domain_name: ``AWS::SageMaker::Domain.DomainName``.
        :param subnet_ids: ``AWS::SageMaker::Domain.SubnetIds``.
        :param vpc_id: ``AWS::SageMaker::Domain.VpcId``.
        :param app_network_access_type: ``AWS::SageMaker::Domain.AppNetworkAccessType``.
        :param kms_key_id: ``AWS::SageMaker::Domain.KmsKeyId``.
        :param tags: ``AWS::SageMaker::Domain.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "auth_mode": auth_mode,
            "default_user_settings": default_user_settings,
            "domain_name": domain_name,
            "subnet_ids": subnet_ids,
            "vpc_id": vpc_id,
        }
        if app_network_access_type is not None:
            self._values["app_network_access_type"] = app_network_access_type
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def auth_mode(self) -> builtins.str:
        '''``AWS::SageMaker::Domain.AuthMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-authmode
        '''
        result = self._values.get("auth_mode")
        assert result is not None, "Required property 'auth_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_user_settings(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnDomain.UserSettingsProperty]:
        '''``AWS::SageMaker::Domain.DefaultUserSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-defaultusersettings
        '''
        result = self._values.get("default_user_settings")
        assert result is not None, "Required property 'default_user_settings' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnDomain.UserSettingsProperty], result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''``AWS::SageMaker::Domain.DomainName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''``AWS::SageMaker::Domain.SubnetIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''``AWS::SageMaker::Domain.VpcId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_network_access_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Domain.AppNetworkAccessType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-appnetworkaccesstype
        '''
        result = self._values.get("app_network_access_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Domain.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::Domain.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-domain.html#cfn-sagemaker-domain-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnEndpoint(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint",
):
    '''A CloudFormation ``AWS::SageMaker::Endpoint``.

    :cloudformationResource: AWS::SageMaker::Endpoint
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        endpoint_config_name: builtins.str,
        deployment_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.DeploymentConfigProperty"]] = None,
        endpoint_name: typing.Optional[builtins.str] = None,
        exclude_retained_variant_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.VariantPropertyProperty"]]]] = None,
        retain_all_variant_properties: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::Endpoint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param endpoint_config_name: ``AWS::SageMaker::Endpoint.EndpointConfigName``.
        :param deployment_config: ``AWS::SageMaker::Endpoint.DeploymentConfig``.
        :param endpoint_name: ``AWS::SageMaker::Endpoint.EndpointName``.
        :param exclude_retained_variant_properties: ``AWS::SageMaker::Endpoint.ExcludeRetainedVariantProperties``.
        :param retain_all_variant_properties: ``AWS::SageMaker::Endpoint.RetainAllVariantProperties``.
        :param tags: ``AWS::SageMaker::Endpoint.Tags``.
        '''
        props = CfnEndpointProps(
            endpoint_config_name=endpoint_config_name,
            deployment_config=deployment_config,
            endpoint_name=endpoint_name,
            exclude_retained_variant_properties=exclude_retained_variant_properties,
            retain_all_variant_properties=retain_all_variant_properties,
            tags=tags,
        )

        jsii.create(CfnEndpoint, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrEndpointName")
    def attr_endpoint_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: EndpointName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpointName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::Endpoint.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointConfigName")
    def endpoint_config_name(self) -> builtins.str:
        '''``AWS::SageMaker::Endpoint.EndpointConfigName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-endpointconfigname
        '''
        return typing.cast(builtins.str, jsii.get(self, "endpointConfigName"))

    @endpoint_config_name.setter
    def endpoint_config_name(self, value: builtins.str) -> None:
        jsii.set(self, "endpointConfigName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.DeploymentConfigProperty"]]:
        '''``AWS::SageMaker::Endpoint.DeploymentConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-deploymentconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.DeploymentConfigProperty"]], jsii.get(self, "deploymentConfig"))

    @deployment_config.setter
    def deployment_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.DeploymentConfigProperty"]],
    ) -> None:
        jsii.set(self, "deploymentConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointName")
    def endpoint_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Endpoint.EndpointName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-endpointname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointName"))

    @endpoint_name.setter
    def endpoint_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "endpointName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="excludeRetainedVariantProperties")
    def exclude_retained_variant_properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.VariantPropertyProperty"]]]]:
        '''``AWS::SageMaker::Endpoint.ExcludeRetainedVariantProperties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-excluderetainedvariantproperties
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.VariantPropertyProperty"]]]], jsii.get(self, "excludeRetainedVariantProperties"))

    @exclude_retained_variant_properties.setter
    def exclude_retained_variant_properties(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.VariantPropertyProperty"]]]],
    ) -> None:
        jsii.set(self, "excludeRetainedVariantProperties", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="retainAllVariantProperties")
    def retain_all_variant_properties(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::SageMaker::Endpoint.RetainAllVariantProperties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-retainallvariantproperties
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "retainAllVariantProperties"))

    @retain_all_variant_properties.setter
    def retain_all_variant_properties(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "retainAllVariantProperties", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.AlarmProperty",
        jsii_struct_bases=[],
        name_mapping={"alarm_name": "alarmName"},
    )
    class AlarmProperty:
        def __init__(self, *, alarm_name: builtins.str) -> None:
            '''
            :param alarm_name: ``CfnEndpoint.AlarmProperty.AlarmName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-alarm.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "alarm_name": alarm_name,
            }

        @builtins.property
        def alarm_name(self) -> builtins.str:
            '''``CfnEndpoint.AlarmProperty.AlarmName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-alarm.html#cfn-sagemaker-endpoint-alarm-alarmname
            '''
            result = self._values.get("alarm_name")
            assert result is not None, "Required property 'alarm_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AlarmProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.AutoRollbackConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"alarms": "alarms"},
    )
    class AutoRollbackConfigProperty:
        def __init__(
            self,
            *,
            alarms: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.AlarmProperty"]]],
        ) -> None:
            '''
            :param alarms: ``CfnEndpoint.AutoRollbackConfigProperty.Alarms``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-autorollbackconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "alarms": alarms,
            }

        @builtins.property
        def alarms(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.AlarmProperty"]]]:
            '''``CfnEndpoint.AutoRollbackConfigProperty.Alarms``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-autorollbackconfig.html#cfn-sagemaker-endpoint-autorollbackconfig-alarms
            '''
            result = self._values.get("alarms")
            assert result is not None, "Required property 'alarms' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.AlarmProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoRollbackConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.BlueGreenUpdatePolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "traffic_routing_configuration": "trafficRoutingConfiguration",
            "maximum_execution_timeout_in_seconds": "maximumExecutionTimeoutInSeconds",
            "termination_wait_in_seconds": "terminationWaitInSeconds",
        },
    )
    class BlueGreenUpdatePolicyProperty:
        def __init__(
            self,
            *,
            traffic_routing_configuration: typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.TrafficRoutingConfigProperty"],
            maximum_execution_timeout_in_seconds: typing.Optional[jsii.Number] = None,
            termination_wait_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param traffic_routing_configuration: ``CfnEndpoint.BlueGreenUpdatePolicyProperty.TrafficRoutingConfiguration``.
            :param maximum_execution_timeout_in_seconds: ``CfnEndpoint.BlueGreenUpdatePolicyProperty.MaximumExecutionTimeoutInSeconds``.
            :param termination_wait_in_seconds: ``CfnEndpoint.BlueGreenUpdatePolicyProperty.TerminationWaitInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-bluegreenupdatepolicy.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "traffic_routing_configuration": traffic_routing_configuration,
            }
            if maximum_execution_timeout_in_seconds is not None:
                self._values["maximum_execution_timeout_in_seconds"] = maximum_execution_timeout_in_seconds
            if termination_wait_in_seconds is not None:
                self._values["termination_wait_in_seconds"] = termination_wait_in_seconds

        @builtins.property
        def traffic_routing_configuration(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.TrafficRoutingConfigProperty"]:
            '''``CfnEndpoint.BlueGreenUpdatePolicyProperty.TrafficRoutingConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-bluegreenupdatepolicy.html#cfn-sagemaker-endpoint-bluegreenupdatepolicy-trafficroutingconfiguration
            '''
            result = self._values.get("traffic_routing_configuration")
            assert result is not None, "Required property 'traffic_routing_configuration' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.TrafficRoutingConfigProperty"], result)

        @builtins.property
        def maximum_execution_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnEndpoint.BlueGreenUpdatePolicyProperty.MaximumExecutionTimeoutInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-bluegreenupdatepolicy.html#cfn-sagemaker-endpoint-bluegreenupdatepolicy-maximumexecutiontimeoutinseconds
            '''
            result = self._values.get("maximum_execution_timeout_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def termination_wait_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnEndpoint.BlueGreenUpdatePolicyProperty.TerminationWaitInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-bluegreenupdatepolicy.html#cfn-sagemaker-endpoint-bluegreenupdatepolicy-terminationwaitinseconds
            '''
            result = self._values.get("termination_wait_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BlueGreenUpdatePolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.CapacitySizeProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class CapacitySizeProperty:
        def __init__(self, *, type: builtins.str, value: jsii.Number) -> None:
            '''
            :param type: ``CfnEndpoint.CapacitySizeProperty.Type``.
            :param value: ``CfnEndpoint.CapacitySizeProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-capacitysize.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
                "value": value,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnEndpoint.CapacitySizeProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-capacitysize.html#cfn-sagemaker-endpoint-capacitysize-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> jsii.Number:
            '''``CfnEndpoint.CapacitySizeProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-capacitysize.html#cfn-sagemaker-endpoint-capacitysize-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CapacitySizeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.DeploymentConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "blue_green_update_policy": "blueGreenUpdatePolicy",
            "auto_rollback_configuration": "autoRollbackConfiguration",
        },
    )
    class DeploymentConfigProperty:
        def __init__(
            self,
            *,
            blue_green_update_policy: typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.BlueGreenUpdatePolicyProperty"],
            auto_rollback_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.AutoRollbackConfigProperty"]] = None,
        ) -> None:
            '''
            :param blue_green_update_policy: ``CfnEndpoint.DeploymentConfigProperty.BlueGreenUpdatePolicy``.
            :param auto_rollback_configuration: ``CfnEndpoint.DeploymentConfigProperty.AutoRollbackConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-deploymentconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "blue_green_update_policy": blue_green_update_policy,
            }
            if auto_rollback_configuration is not None:
                self._values["auto_rollback_configuration"] = auto_rollback_configuration

        @builtins.property
        def blue_green_update_policy(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.BlueGreenUpdatePolicyProperty"]:
            '''``CfnEndpoint.DeploymentConfigProperty.BlueGreenUpdatePolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-deploymentconfig.html#cfn-sagemaker-endpoint-deploymentconfig-bluegreenupdatepolicy
            '''
            result = self._values.get("blue_green_update_policy")
            assert result is not None, "Required property 'blue_green_update_policy' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.BlueGreenUpdatePolicyProperty"], result)

        @builtins.property
        def auto_rollback_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.AutoRollbackConfigProperty"]]:
            '''``CfnEndpoint.DeploymentConfigProperty.AutoRollbackConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-deploymentconfig.html#cfn-sagemaker-endpoint-deploymentconfig-autorollbackconfiguration
            '''
            result = self._values.get("auto_rollback_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.AutoRollbackConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeploymentConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.TrafficRoutingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "canary_size": "canarySize",
            "wait_interval_in_seconds": "waitIntervalInSeconds",
        },
    )
    class TrafficRoutingConfigProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            canary_size: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.CapacitySizeProperty"]] = None,
            wait_interval_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param type: ``CfnEndpoint.TrafficRoutingConfigProperty.Type``.
            :param canary_size: ``CfnEndpoint.TrafficRoutingConfigProperty.CanarySize``.
            :param wait_interval_in_seconds: ``CfnEndpoint.TrafficRoutingConfigProperty.WaitIntervalInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
            }
            if canary_size is not None:
                self._values["canary_size"] = canary_size
            if wait_interval_in_seconds is not None:
                self._values["wait_interval_in_seconds"] = wait_interval_in_seconds

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnEndpoint.TrafficRoutingConfigProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html#cfn-sagemaker-endpoint-trafficroutingconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def canary_size(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.CapacitySizeProperty"]]:
            '''``CfnEndpoint.TrafficRoutingConfigProperty.CanarySize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html#cfn-sagemaker-endpoint-trafficroutingconfig-canarysize
            '''
            result = self._values.get("canary_size")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpoint.CapacitySizeProperty"]], result)

        @builtins.property
        def wait_interval_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnEndpoint.TrafficRoutingConfigProperty.WaitIntervalInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-trafficroutingconfig.html#cfn-sagemaker-endpoint-trafficroutingconfig-waitintervalinseconds
            '''
            result = self._values.get("wait_interval_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrafficRoutingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpoint.VariantPropertyProperty",
        jsii_struct_bases=[],
        name_mapping={"variant_property_type": "variantPropertyType"},
    )
    class VariantPropertyProperty:
        def __init__(
            self,
            *,
            variant_property_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param variant_property_type: ``CfnEndpoint.VariantPropertyProperty.VariantPropertyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-variantproperty.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if variant_property_type is not None:
                self._values["variant_property_type"] = variant_property_type

        @builtins.property
        def variant_property_type(self) -> typing.Optional[builtins.str]:
            '''``CfnEndpoint.VariantPropertyProperty.VariantPropertyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpoint-variantproperty.html#cfn-sagemaker-endpoint-variantproperty-variantpropertytype
            '''
            result = self._values.get("variant_property_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VariantPropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnEndpointConfig(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfig",
):
    '''A CloudFormation ``AWS::SageMaker::EndpointConfig``.

    :cloudformationResource: AWS::SageMaker::EndpointConfig
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        production_variants: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.ProductionVariantProperty"]]],
        data_capture_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.DataCaptureConfigProperty"]] = None,
        endpoint_config_name: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::EndpointConfig``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param production_variants: ``AWS::SageMaker::EndpointConfig.ProductionVariants``.
        :param data_capture_config: ``AWS::SageMaker::EndpointConfig.DataCaptureConfig``.
        :param endpoint_config_name: ``AWS::SageMaker::EndpointConfig.EndpointConfigName``.
        :param kms_key_id: ``AWS::SageMaker::EndpointConfig.KmsKeyId``.
        :param tags: ``AWS::SageMaker::EndpointConfig.Tags``.
        '''
        props = CfnEndpointConfigProps(
            production_variants=production_variants,
            data_capture_config=data_capture_config,
            endpoint_config_name=endpoint_config_name,
            kms_key_id=kms_key_id,
            tags=tags,
        )

        jsii.create(CfnEndpointConfig, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrEndpointConfigName")
    def attr_endpoint_config_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: EndpointConfigName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEndpointConfigName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::EndpointConfig.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="productionVariants")
    def production_variants(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.ProductionVariantProperty"]]]:
        '''``AWS::SageMaker::EndpointConfig.ProductionVariants``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-productionvariants
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.ProductionVariantProperty"]]], jsii.get(self, "productionVariants"))

    @production_variants.setter
    def production_variants(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.ProductionVariantProperty"]]],
    ) -> None:
        jsii.set(self, "productionVariants", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataCaptureConfig")
    def data_capture_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.DataCaptureConfigProperty"]]:
        '''``AWS::SageMaker::EndpointConfig.DataCaptureConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.DataCaptureConfigProperty"]], jsii.get(self, "dataCaptureConfig"))

    @data_capture_config.setter
    def data_capture_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.DataCaptureConfigProperty"]],
    ) -> None:
        jsii.set(self, "dataCaptureConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointConfigName")
    def endpoint_config_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::EndpointConfig.EndpointConfigName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-endpointconfigname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointConfigName"))

    @endpoint_config_name.setter
    def endpoint_config_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "endpointConfigName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::EndpointConfig.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyId", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfig.CaptureContentTypeHeaderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "csv_content_types": "csvContentTypes",
            "json_content_types": "jsonContentTypes",
        },
    )
    class CaptureContentTypeHeaderProperty:
        def __init__(
            self,
            *,
            csv_content_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            json_content_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param csv_content_types: ``CfnEndpointConfig.CaptureContentTypeHeaderProperty.CsvContentTypes``.
            :param json_content_types: ``CfnEndpointConfig.CaptureContentTypeHeaderProperty.JsonContentTypes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if csv_content_types is not None:
                self._values["csv_content_types"] = csv_content_types
            if json_content_types is not None:
                self._values["json_content_types"] = json_content_types

        @builtins.property
        def csv_content_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnEndpointConfig.CaptureContentTypeHeaderProperty.CsvContentTypes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader.html#cfn-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader-csvcontenttypes
            '''
            result = self._values.get("csv_content_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def json_content_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnEndpointConfig.CaptureContentTypeHeaderProperty.JsonContentTypes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader.html#cfn-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader-jsoncontenttypes
            '''
            result = self._values.get("json_content_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CaptureContentTypeHeaderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfig.CaptureOptionProperty",
        jsii_struct_bases=[],
        name_mapping={"capture_mode": "captureMode"},
    )
    class CaptureOptionProperty:
        def __init__(self, *, capture_mode: builtins.str) -> None:
            '''
            :param capture_mode: ``CfnEndpointConfig.CaptureOptionProperty.CaptureMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-captureoption.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "capture_mode": capture_mode,
            }

        @builtins.property
        def capture_mode(self) -> builtins.str:
            '''``CfnEndpointConfig.CaptureOptionProperty.CaptureMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-captureoption.html#cfn-sagemaker-endpointconfig-captureoption-capturemode
            '''
            result = self._values.get("capture_mode")
            assert result is not None, "Required property 'capture_mode' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CaptureOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfig.DataCaptureConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "capture_options": "captureOptions",
            "destination_s3_uri": "destinationS3Uri",
            "initial_sampling_percentage": "initialSamplingPercentage",
            "capture_content_type_header": "captureContentTypeHeader",
            "enable_capture": "enableCapture",
            "kms_key_id": "kmsKeyId",
        },
    )
    class DataCaptureConfigProperty:
        def __init__(
            self,
            *,
            capture_options: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.CaptureOptionProperty"]]],
            destination_s3_uri: builtins.str,
            initial_sampling_percentage: jsii.Number,
            capture_content_type_header: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.CaptureContentTypeHeaderProperty"]] = None,
            enable_capture: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param capture_options: ``CfnEndpointConfig.DataCaptureConfigProperty.CaptureOptions``.
            :param destination_s3_uri: ``CfnEndpointConfig.DataCaptureConfigProperty.DestinationS3Uri``.
            :param initial_sampling_percentage: ``CfnEndpointConfig.DataCaptureConfigProperty.InitialSamplingPercentage``.
            :param capture_content_type_header: ``CfnEndpointConfig.DataCaptureConfigProperty.CaptureContentTypeHeader``.
            :param enable_capture: ``CfnEndpointConfig.DataCaptureConfigProperty.EnableCapture``.
            :param kms_key_id: ``CfnEndpointConfig.DataCaptureConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "capture_options": capture_options,
                "destination_s3_uri": destination_s3_uri,
                "initial_sampling_percentage": initial_sampling_percentage,
            }
            if capture_content_type_header is not None:
                self._values["capture_content_type_header"] = capture_content_type_header
            if enable_capture is not None:
                self._values["enable_capture"] = enable_capture
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def capture_options(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.CaptureOptionProperty"]]]:
            '''``CfnEndpointConfig.DataCaptureConfigProperty.CaptureOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-captureoptions
            '''
            result = self._values.get("capture_options")
            assert result is not None, "Required property 'capture_options' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.CaptureOptionProperty"]]], result)

        @builtins.property
        def destination_s3_uri(self) -> builtins.str:
            '''``CfnEndpointConfig.DataCaptureConfigProperty.DestinationS3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-destinations3uri
            '''
            result = self._values.get("destination_s3_uri")
            assert result is not None, "Required property 'destination_s3_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def initial_sampling_percentage(self) -> jsii.Number:
            '''``CfnEndpointConfig.DataCaptureConfigProperty.InitialSamplingPercentage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-initialsamplingpercentage
            '''
            result = self._values.get("initial_sampling_percentage")
            assert result is not None, "Required property 'initial_sampling_percentage' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def capture_content_type_header(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.CaptureContentTypeHeaderProperty"]]:
            '''``CfnEndpointConfig.DataCaptureConfigProperty.CaptureContentTypeHeader``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-capturecontenttypeheader
            '''
            result = self._values.get("capture_content_type_header")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnEndpointConfig.CaptureContentTypeHeaderProperty"]], result)

        @builtins.property
        def enable_capture(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnEndpointConfig.DataCaptureConfigProperty.EnableCapture``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-enablecapture
            '''
            result = self._values.get("enable_capture")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnEndpointConfig.DataCaptureConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-datacaptureconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataCaptureConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfig.ProductionVariantProperty",
        jsii_struct_bases=[],
        name_mapping={
            "initial_instance_count": "initialInstanceCount",
            "initial_variant_weight": "initialVariantWeight",
            "instance_type": "instanceType",
            "model_name": "modelName",
            "variant_name": "variantName",
            "accelerator_type": "acceleratorType",
        },
    )
    class ProductionVariantProperty:
        def __init__(
            self,
            *,
            initial_instance_count: jsii.Number,
            initial_variant_weight: jsii.Number,
            instance_type: builtins.str,
            model_name: builtins.str,
            variant_name: builtins.str,
            accelerator_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param initial_instance_count: ``CfnEndpointConfig.ProductionVariantProperty.InitialInstanceCount``.
            :param initial_variant_weight: ``CfnEndpointConfig.ProductionVariantProperty.InitialVariantWeight``.
            :param instance_type: ``CfnEndpointConfig.ProductionVariantProperty.InstanceType``.
            :param model_name: ``CfnEndpointConfig.ProductionVariantProperty.ModelName``.
            :param variant_name: ``CfnEndpointConfig.ProductionVariantProperty.VariantName``.
            :param accelerator_type: ``CfnEndpointConfig.ProductionVariantProperty.AcceleratorType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "initial_instance_count": initial_instance_count,
                "initial_variant_weight": initial_variant_weight,
                "instance_type": instance_type,
                "model_name": model_name,
                "variant_name": variant_name,
            }
            if accelerator_type is not None:
                self._values["accelerator_type"] = accelerator_type

        @builtins.property
        def initial_instance_count(self) -> jsii.Number:
            '''``CfnEndpointConfig.ProductionVariantProperty.InitialInstanceCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-initialinstancecount
            '''
            result = self._values.get("initial_instance_count")
            assert result is not None, "Required property 'initial_instance_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def initial_variant_weight(self) -> jsii.Number:
            '''``CfnEndpointConfig.ProductionVariantProperty.InitialVariantWeight``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-initialvariantweight
            '''
            result = self._values.get("initial_variant_weight")
            assert result is not None, "Required property 'initial_variant_weight' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''``CfnEndpointConfig.ProductionVariantProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def model_name(self) -> builtins.str:
            '''``CfnEndpointConfig.ProductionVariantProperty.ModelName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-modelname
            '''
            result = self._values.get("model_name")
            assert result is not None, "Required property 'model_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def variant_name(self) -> builtins.str:
            '''``CfnEndpointConfig.ProductionVariantProperty.VariantName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-variantname
            '''
            result = self._values.get("variant_name")
            assert result is not None, "Required property 'variant_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def accelerator_type(self) -> typing.Optional[builtins.str]:
            '''``CfnEndpointConfig.ProductionVariantProperty.AcceleratorType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-endpointconfig-productionvariant.html#cfn-sagemaker-endpointconfig-productionvariant-acceleratortype
            '''
            result = self._values.get("accelerator_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProductionVariantProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "production_variants": "productionVariants",
        "data_capture_config": "dataCaptureConfig",
        "endpoint_config_name": "endpointConfigName",
        "kms_key_id": "kmsKeyId",
        "tags": "tags",
    },
)
class CfnEndpointConfigProps:
    def __init__(
        self,
        *,
        production_variants: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnEndpointConfig.ProductionVariantProperty]]],
        data_capture_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEndpointConfig.DataCaptureConfigProperty]] = None,
        endpoint_config_name: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::EndpointConfig``.

        :param production_variants: ``AWS::SageMaker::EndpointConfig.ProductionVariants``.
        :param data_capture_config: ``AWS::SageMaker::EndpointConfig.DataCaptureConfig``.
        :param endpoint_config_name: ``AWS::SageMaker::EndpointConfig.EndpointConfigName``.
        :param kms_key_id: ``AWS::SageMaker::EndpointConfig.KmsKeyId``.
        :param tags: ``AWS::SageMaker::EndpointConfig.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "production_variants": production_variants,
        }
        if data_capture_config is not None:
            self._values["data_capture_config"] = data_capture_config
        if endpoint_config_name is not None:
            self._values["endpoint_config_name"] = endpoint_config_name
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def production_variants(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnEndpointConfig.ProductionVariantProperty]]]:
        '''``AWS::SageMaker::EndpointConfig.ProductionVariants``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-productionvariants
        '''
        result = self._values.get("production_variants")
        assert result is not None, "Required property 'production_variants' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnEndpointConfig.ProductionVariantProperty]]], result)

    @builtins.property
    def data_capture_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEndpointConfig.DataCaptureConfigProperty]]:
        '''``AWS::SageMaker::EndpointConfig.DataCaptureConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-datacaptureconfig
        '''
        result = self._values.get("data_capture_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEndpointConfig.DataCaptureConfigProperty]], result)

    @builtins.property
    def endpoint_config_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::EndpointConfig.EndpointConfigName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-endpointconfigname
        '''
        result = self._values.get("endpoint_config_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::EndpointConfig.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::EndpointConfig.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html#cfn-sagemaker-endpointconfig-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEndpointConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_config_name": "endpointConfigName",
        "deployment_config": "deploymentConfig",
        "endpoint_name": "endpointName",
        "exclude_retained_variant_properties": "excludeRetainedVariantProperties",
        "retain_all_variant_properties": "retainAllVariantProperties",
        "tags": "tags",
    },
)
class CfnEndpointProps:
    def __init__(
        self,
        *,
        endpoint_config_name: builtins.str,
        deployment_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEndpoint.DeploymentConfigProperty]] = None,
        endpoint_name: typing.Optional[builtins.str] = None,
        exclude_retained_variant_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnEndpoint.VariantPropertyProperty]]]] = None,
        retain_all_variant_properties: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::Endpoint``.

        :param endpoint_config_name: ``AWS::SageMaker::Endpoint.EndpointConfigName``.
        :param deployment_config: ``AWS::SageMaker::Endpoint.DeploymentConfig``.
        :param endpoint_name: ``AWS::SageMaker::Endpoint.EndpointName``.
        :param exclude_retained_variant_properties: ``AWS::SageMaker::Endpoint.ExcludeRetainedVariantProperties``.
        :param retain_all_variant_properties: ``AWS::SageMaker::Endpoint.RetainAllVariantProperties``.
        :param tags: ``AWS::SageMaker::Endpoint.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint_config_name": endpoint_config_name,
        }
        if deployment_config is not None:
            self._values["deployment_config"] = deployment_config
        if endpoint_name is not None:
            self._values["endpoint_name"] = endpoint_name
        if exclude_retained_variant_properties is not None:
            self._values["exclude_retained_variant_properties"] = exclude_retained_variant_properties
        if retain_all_variant_properties is not None:
            self._values["retain_all_variant_properties"] = retain_all_variant_properties
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def endpoint_config_name(self) -> builtins.str:
        '''``AWS::SageMaker::Endpoint.EndpointConfigName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-endpointconfigname
        '''
        result = self._values.get("endpoint_config_name")
        assert result is not None, "Required property 'endpoint_config_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deployment_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEndpoint.DeploymentConfigProperty]]:
        '''``AWS::SageMaker::Endpoint.DeploymentConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-deploymentconfig
        '''
        result = self._values.get("deployment_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnEndpoint.DeploymentConfigProperty]], result)

    @builtins.property
    def endpoint_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Endpoint.EndpointName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-endpointname
        '''
        result = self._values.get("endpoint_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exclude_retained_variant_properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnEndpoint.VariantPropertyProperty]]]]:
        '''``AWS::SageMaker::Endpoint.ExcludeRetainedVariantProperties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-excluderetainedvariantproperties
        '''
        result = self._values.get("exclude_retained_variant_properties")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnEndpoint.VariantPropertyProperty]]]], result)

    @builtins.property
    def retain_all_variant_properties(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::SageMaker::Endpoint.RetainAllVariantProperties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-retainallvariantproperties
        '''
        result = self._values.get("retain_all_variant_properties")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::Endpoint.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html#cfn-sagemaker-endpoint-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnFeatureGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnFeatureGroup",
):
    '''A CloudFormation ``AWS::SageMaker::FeatureGroup``.

    :cloudformationResource: AWS::SageMaker::FeatureGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        event_time_feature_name: builtins.str,
        feature_definitions: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnFeatureGroup.FeatureDefinitionProperty"]]],
        feature_group_name: builtins.str,
        record_identifier_feature_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        offline_store_config: typing.Any = None,
        online_store_config: typing.Any = None,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::FeatureGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param event_time_feature_name: ``AWS::SageMaker::FeatureGroup.EventTimeFeatureName``.
        :param feature_definitions: ``AWS::SageMaker::FeatureGroup.FeatureDefinitions``.
        :param feature_group_name: ``AWS::SageMaker::FeatureGroup.FeatureGroupName``.
        :param record_identifier_feature_name: ``AWS::SageMaker::FeatureGroup.RecordIdentifierFeatureName``.
        :param description: ``AWS::SageMaker::FeatureGroup.Description``.
        :param offline_store_config: ``AWS::SageMaker::FeatureGroup.OfflineStoreConfig``.
        :param online_store_config: ``AWS::SageMaker::FeatureGroup.OnlineStoreConfig``.
        :param role_arn: ``AWS::SageMaker::FeatureGroup.RoleArn``.
        :param tags: ``AWS::SageMaker::FeatureGroup.Tags``.
        '''
        props = CfnFeatureGroupProps(
            event_time_feature_name=event_time_feature_name,
            feature_definitions=feature_definitions,
            feature_group_name=feature_group_name,
            record_identifier_feature_name=record_identifier_feature_name,
            description=description,
            offline_store_config=offline_store_config,
            online_store_config=online_store_config,
            role_arn=role_arn,
            tags=tags,
        )

        jsii.create(CfnFeatureGroup, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::FeatureGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="eventTimeFeatureName")
    def event_time_feature_name(self) -> builtins.str:
        '''``AWS::SageMaker::FeatureGroup.EventTimeFeatureName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-eventtimefeaturename
        '''
        return typing.cast(builtins.str, jsii.get(self, "eventTimeFeatureName"))

    @event_time_feature_name.setter
    def event_time_feature_name(self, value: builtins.str) -> None:
        jsii.set(self, "eventTimeFeatureName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="featureDefinitions")
    def feature_definitions(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFeatureGroup.FeatureDefinitionProperty"]]]:
        '''``AWS::SageMaker::FeatureGroup.FeatureDefinitions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-featuredefinitions
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFeatureGroup.FeatureDefinitionProperty"]]], jsii.get(self, "featureDefinitions"))

    @feature_definitions.setter
    def feature_definitions(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnFeatureGroup.FeatureDefinitionProperty"]]],
    ) -> None:
        jsii.set(self, "featureDefinitions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="featureGroupName")
    def feature_group_name(self) -> builtins.str:
        '''``AWS::SageMaker::FeatureGroup.FeatureGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-featuregroupname
        '''
        return typing.cast(builtins.str, jsii.get(self, "featureGroupName"))

    @feature_group_name.setter
    def feature_group_name(self, value: builtins.str) -> None:
        jsii.set(self, "featureGroupName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="offlineStoreConfig")
    def offline_store_config(self) -> typing.Any:
        '''``AWS::SageMaker::FeatureGroup.OfflineStoreConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-offlinestoreconfig
        '''
        return typing.cast(typing.Any, jsii.get(self, "offlineStoreConfig"))

    @offline_store_config.setter
    def offline_store_config(self, value: typing.Any) -> None:
        jsii.set(self, "offlineStoreConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="onlineStoreConfig")
    def online_store_config(self) -> typing.Any:
        '''``AWS::SageMaker::FeatureGroup.OnlineStoreConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-onlinestoreconfig
        '''
        return typing.cast(typing.Any, jsii.get(self, "onlineStoreConfig"))

    @online_store_config.setter
    def online_store_config(self, value: typing.Any) -> None:
        jsii.set(self, "onlineStoreConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="recordIdentifierFeatureName")
    def record_identifier_feature_name(self) -> builtins.str:
        '''``AWS::SageMaker::FeatureGroup.RecordIdentifierFeatureName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-recordidentifierfeaturename
        '''
        return typing.cast(builtins.str, jsii.get(self, "recordIdentifierFeatureName"))

    @record_identifier_feature_name.setter
    def record_identifier_feature_name(self, value: builtins.str) -> None:
        jsii.set(self, "recordIdentifierFeatureName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::FeatureGroup.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::FeatureGroup.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-rolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "roleArn", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnFeatureGroup.FeatureDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"feature_name": "featureName", "feature_type": "featureType"},
    )
    class FeatureDefinitionProperty:
        def __init__(
            self,
            *,
            feature_name: builtins.str,
            feature_type: builtins.str,
        ) -> None:
            '''
            :param feature_name: ``CfnFeatureGroup.FeatureDefinitionProperty.FeatureName``.
            :param feature_type: ``CfnFeatureGroup.FeatureDefinitionProperty.FeatureType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-featuredefinition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "feature_name": feature_name,
                "feature_type": feature_type,
            }

        @builtins.property
        def feature_name(self) -> builtins.str:
            '''``CfnFeatureGroup.FeatureDefinitionProperty.FeatureName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-featuredefinition.html#cfn-sagemaker-featuregroup-featuredefinition-featurename
            '''
            result = self._values.get("feature_name")
            assert result is not None, "Required property 'feature_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def feature_type(self) -> builtins.str:
            '''``CfnFeatureGroup.FeatureDefinitionProperty.FeatureType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-featuregroup-featuredefinition.html#cfn-sagemaker-featuregroup-featuredefinition-featuretype
            '''
            result = self._values.get("feature_type")
            assert result is not None, "Required property 'feature_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FeatureDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnFeatureGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "event_time_feature_name": "eventTimeFeatureName",
        "feature_definitions": "featureDefinitions",
        "feature_group_name": "featureGroupName",
        "record_identifier_feature_name": "recordIdentifierFeatureName",
        "description": "description",
        "offline_store_config": "offlineStoreConfig",
        "online_store_config": "onlineStoreConfig",
        "role_arn": "roleArn",
        "tags": "tags",
    },
)
class CfnFeatureGroupProps:
    def __init__(
        self,
        *,
        event_time_feature_name: builtins.str,
        feature_definitions: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnFeatureGroup.FeatureDefinitionProperty]]],
        feature_group_name: builtins.str,
        record_identifier_feature_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        offline_store_config: typing.Any = None,
        online_store_config: typing.Any = None,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::FeatureGroup``.

        :param event_time_feature_name: ``AWS::SageMaker::FeatureGroup.EventTimeFeatureName``.
        :param feature_definitions: ``AWS::SageMaker::FeatureGroup.FeatureDefinitions``.
        :param feature_group_name: ``AWS::SageMaker::FeatureGroup.FeatureGroupName``.
        :param record_identifier_feature_name: ``AWS::SageMaker::FeatureGroup.RecordIdentifierFeatureName``.
        :param description: ``AWS::SageMaker::FeatureGroup.Description``.
        :param offline_store_config: ``AWS::SageMaker::FeatureGroup.OfflineStoreConfig``.
        :param online_store_config: ``AWS::SageMaker::FeatureGroup.OnlineStoreConfig``.
        :param role_arn: ``AWS::SageMaker::FeatureGroup.RoleArn``.
        :param tags: ``AWS::SageMaker::FeatureGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "event_time_feature_name": event_time_feature_name,
            "feature_definitions": feature_definitions,
            "feature_group_name": feature_group_name,
            "record_identifier_feature_name": record_identifier_feature_name,
        }
        if description is not None:
            self._values["description"] = description
        if offline_store_config is not None:
            self._values["offline_store_config"] = offline_store_config
        if online_store_config is not None:
            self._values["online_store_config"] = online_store_config
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def event_time_feature_name(self) -> builtins.str:
        '''``AWS::SageMaker::FeatureGroup.EventTimeFeatureName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-eventtimefeaturename
        '''
        result = self._values.get("event_time_feature_name")
        assert result is not None, "Required property 'event_time_feature_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def feature_definitions(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnFeatureGroup.FeatureDefinitionProperty]]]:
        '''``AWS::SageMaker::FeatureGroup.FeatureDefinitions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-featuredefinitions
        '''
        result = self._values.get("feature_definitions")
        assert result is not None, "Required property 'feature_definitions' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnFeatureGroup.FeatureDefinitionProperty]]], result)

    @builtins.property
    def feature_group_name(self) -> builtins.str:
        '''``AWS::SageMaker::FeatureGroup.FeatureGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-featuregroupname
        '''
        result = self._values.get("feature_group_name")
        assert result is not None, "Required property 'feature_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def record_identifier_feature_name(self) -> builtins.str:
        '''``AWS::SageMaker::FeatureGroup.RecordIdentifierFeatureName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-recordidentifierfeaturename
        '''
        result = self._values.get("record_identifier_feature_name")
        assert result is not None, "Required property 'record_identifier_feature_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::FeatureGroup.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def offline_store_config(self) -> typing.Any:
        '''``AWS::SageMaker::FeatureGroup.OfflineStoreConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-offlinestoreconfig
        '''
        result = self._values.get("offline_store_config")
        return typing.cast(typing.Any, result)

    @builtins.property
    def online_store_config(self) -> typing.Any:
        '''``AWS::SageMaker::FeatureGroup.OnlineStoreConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-onlinestoreconfig
        '''
        result = self._values.get("online_store_config")
        return typing.cast(typing.Any, result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::FeatureGroup.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::FeatureGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-featuregroup.html#cfn-sagemaker-featuregroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFeatureGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnImage(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnImage",
):
    '''A CloudFormation ``AWS::SageMaker::Image``.

    :cloudformationResource: AWS::SageMaker::Image
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        image_name: builtins.str,
        image_role_arn: builtins.str,
        image_description: typing.Optional[builtins.str] = None,
        image_display_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::Image``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param image_name: ``AWS::SageMaker::Image.ImageName``.
        :param image_role_arn: ``AWS::SageMaker::Image.ImageRoleArn``.
        :param image_description: ``AWS::SageMaker::Image.ImageDescription``.
        :param image_display_name: ``AWS::SageMaker::Image.ImageDisplayName``.
        :param tags: ``AWS::SageMaker::Image.Tags``.
        '''
        props = CfnImageProps(
            image_name=image_name,
            image_role_arn=image_role_arn,
            image_description=image_description,
            image_display_name=image_display_name,
            tags=tags,
        )

        jsii.create(CfnImage, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrImageArn")
    def attr_image_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ImageArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrImageArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::Image.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> builtins.str:
        '''``AWS::SageMaker::Image.ImageName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-imagename
        '''
        return typing.cast(builtins.str, jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: builtins.str) -> None:
        jsii.set(self, "imageName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageRoleArn")
    def image_role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::Image.ImageRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-imagerolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "imageRoleArn"))

    @image_role_arn.setter
    def image_role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "imageRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageDescription")
    def image_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Image.ImageDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-imagedescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageDescription"))

    @image_description.setter
    def image_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "imageDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageDisplayName")
    def image_display_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Image.ImageDisplayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-imagedisplayname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageDisplayName"))

    @image_display_name.setter
    def image_display_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "imageDisplayName", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnImageProps",
    jsii_struct_bases=[],
    name_mapping={
        "image_name": "imageName",
        "image_role_arn": "imageRoleArn",
        "image_description": "imageDescription",
        "image_display_name": "imageDisplayName",
        "tags": "tags",
    },
)
class CfnImageProps:
    def __init__(
        self,
        *,
        image_name: builtins.str,
        image_role_arn: builtins.str,
        image_description: typing.Optional[builtins.str] = None,
        image_display_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::Image``.

        :param image_name: ``AWS::SageMaker::Image.ImageName``.
        :param image_role_arn: ``AWS::SageMaker::Image.ImageRoleArn``.
        :param image_description: ``AWS::SageMaker::Image.ImageDescription``.
        :param image_display_name: ``AWS::SageMaker::Image.ImageDisplayName``.
        :param tags: ``AWS::SageMaker::Image.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "image_name": image_name,
            "image_role_arn": image_role_arn,
        }
        if image_description is not None:
            self._values["image_description"] = image_description
        if image_display_name is not None:
            self._values["image_display_name"] = image_display_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def image_name(self) -> builtins.str:
        '''``AWS::SageMaker::Image.ImageName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-imagename
        '''
        result = self._values.get("image_name")
        assert result is not None, "Required property 'image_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::Image.ImageRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-imagerolearn
        '''
        result = self._values.get("image_role_arn")
        assert result is not None, "Required property 'image_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Image.ImageDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-imagedescription
        '''
        result = self._values.get("image_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_display_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Image.ImageDisplayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-imagedisplayname
        '''
        result = self._values.get("image_display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::Image.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-image.html#cfn-sagemaker-image-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnImageProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnImageVersion(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnImageVersion",
):
    '''A CloudFormation ``AWS::SageMaker::ImageVersion``.

    :cloudformationResource: AWS::SageMaker::ImageVersion
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        base_image: builtins.str,
        image_name: builtins.str,
    ) -> None:
        '''Create a new ``AWS::SageMaker::ImageVersion``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param base_image: ``AWS::SageMaker::ImageVersion.BaseImage``.
        :param image_name: ``AWS::SageMaker::ImageVersion.ImageName``.
        '''
        props = CfnImageVersionProps(base_image=base_image, image_name=image_name)

        jsii.create(CfnImageVersion, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrContainerImage")
    def attr_container_image(self) -> builtins.str:
        '''
        :cloudformationAttribute: ContainerImage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrContainerImage"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrImageArn")
    def attr_image_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ImageArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrImageArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrImageVersionArn")
    def attr_image_version_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ImageVersionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrImageVersionArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrVersion")
    def attr_version(self) -> jsii.Number:
        '''
        :cloudformationAttribute: Version
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrVersion"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="baseImage")
    def base_image(self) -> builtins.str:
        '''``AWS::SageMaker::ImageVersion.BaseImage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html#cfn-sagemaker-imageversion-baseimage
        '''
        return typing.cast(builtins.str, jsii.get(self, "baseImage"))

    @base_image.setter
    def base_image(self, value: builtins.str) -> None:
        jsii.set(self, "baseImage", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> builtins.str:
        '''``AWS::SageMaker::ImageVersion.ImageName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html#cfn-sagemaker-imageversion-imagename
        '''
        return typing.cast(builtins.str, jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: builtins.str) -> None:
        jsii.set(self, "imageName", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnImageVersionProps",
    jsii_struct_bases=[],
    name_mapping={"base_image": "baseImage", "image_name": "imageName"},
)
class CfnImageVersionProps:
    def __init__(self, *, base_image: builtins.str, image_name: builtins.str) -> None:
        '''Properties for defining a ``AWS::SageMaker::ImageVersion``.

        :param base_image: ``AWS::SageMaker::ImageVersion.BaseImage``.
        :param image_name: ``AWS::SageMaker::ImageVersion.ImageName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "base_image": base_image,
            "image_name": image_name,
        }

    @builtins.property
    def base_image(self) -> builtins.str:
        '''``AWS::SageMaker::ImageVersion.BaseImage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html#cfn-sagemaker-imageversion-baseimage
        '''
        result = self._values.get("base_image")
        assert result is not None, "Required property 'base_image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_name(self) -> builtins.str:
        '''``AWS::SageMaker::ImageVersion.ImageName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-imageversion.html#cfn-sagemaker-imageversion-imagename
        '''
        result = self._values.get("image_name")
        assert result is not None, "Required property 'image_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnImageVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnModel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnModel",
):
    '''A CloudFormation ``AWS::SageMaker::Model``.

    :cloudformationResource: AWS::SageMaker::Model
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        execution_role_arn: builtins.str,
        containers: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]]]] = None,
        enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        inference_execution_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.InferenceExecutionConfigProperty"]] = None,
        model_name: typing.Optional[builtins.str] = None,
        primary_container: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.VpcConfigProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::Model``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param execution_role_arn: ``AWS::SageMaker::Model.ExecutionRoleArn``.
        :param containers: ``AWS::SageMaker::Model.Containers``.
        :param enable_network_isolation: ``AWS::SageMaker::Model.EnableNetworkIsolation``.
        :param inference_execution_config: ``AWS::SageMaker::Model.InferenceExecutionConfig``.
        :param model_name: ``AWS::SageMaker::Model.ModelName``.
        :param primary_container: ``AWS::SageMaker::Model.PrimaryContainer``.
        :param tags: ``AWS::SageMaker::Model.Tags``.
        :param vpc_config: ``AWS::SageMaker::Model.VpcConfig``.
        '''
        props = CfnModelProps(
            execution_role_arn=execution_role_arn,
            containers=containers,
            enable_network_isolation=enable_network_isolation,
            inference_execution_config=inference_execution_config,
            model_name=model_name,
            primary_container=primary_container,
            tags=tags,
            vpc_config=vpc_config,
        )

        jsii.create(CfnModel, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrModelName")
    def attr_model_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: ModelName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModelName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::Model.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::Model.ExecutionRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-executionrolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "executionRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="containers")
    def containers(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]]]]:
        '''``AWS::SageMaker::Model.Containers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-containers
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]]]], jsii.get(self, "containers"))

    @containers.setter
    def containers(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]]]],
    ) -> None:
        jsii.set(self, "containers", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enableNetworkIsolation")
    def enable_network_isolation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::SageMaker::Model.EnableNetworkIsolation``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-enablenetworkisolation
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "enableNetworkIsolation"))

    @enable_network_isolation.setter
    def enable_network_isolation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "enableNetworkIsolation", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="inferenceExecutionConfig")
    def inference_execution_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.InferenceExecutionConfigProperty"]]:
        '''``AWS::SageMaker::Model.InferenceExecutionConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-inferenceexecutionconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.InferenceExecutionConfigProperty"]], jsii.get(self, "inferenceExecutionConfig"))

    @inference_execution_config.setter
    def inference_execution_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.InferenceExecutionConfigProperty"]],
    ) -> None:
        jsii.set(self, "inferenceExecutionConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelName")
    def model_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Model.ModelName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-modelname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelName"))

    @model_name.setter
    def model_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "modelName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="primaryContainer")
    def primary_container(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]]:
        '''``AWS::SageMaker::Model.PrimaryContainer``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-primarycontainer
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]], jsii.get(self, "primaryContainer"))

    @primary_container.setter
    def primary_container(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ContainerDefinitionProperty"]],
    ) -> None:
        jsii.set(self, "primaryContainer", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.VpcConfigProperty"]]:
        '''``AWS::SageMaker::Model.VpcConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-vpcconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.VpcConfigProperty"]], jsii.get(self, "vpcConfig"))

    @vpc_config.setter
    def vpc_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.VpcConfigProperty"]],
    ) -> None:
        jsii.set(self, "vpcConfig", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModel.ContainerDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_hostname": "containerHostname",
            "environment": "environment",
            "image": "image",
            "image_config": "imageConfig",
            "mode": "mode",
            "model_data_url": "modelDataUrl",
            "model_package_name": "modelPackageName",
            "multi_model_config": "multiModelConfig",
        },
    )
    class ContainerDefinitionProperty:
        def __init__(
            self,
            *,
            container_hostname: typing.Optional[builtins.str] = None,
            environment: typing.Any = None,
            image: typing.Optional[builtins.str] = None,
            image_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ImageConfigProperty"]] = None,
            mode: typing.Optional[builtins.str] = None,
            model_data_url: typing.Optional[builtins.str] = None,
            model_package_name: typing.Optional[builtins.str] = None,
            multi_model_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.MultiModelConfigProperty"]] = None,
        ) -> None:
            '''
            :param container_hostname: ``CfnModel.ContainerDefinitionProperty.ContainerHostname``.
            :param environment: ``CfnModel.ContainerDefinitionProperty.Environment``.
            :param image: ``CfnModel.ContainerDefinitionProperty.Image``.
            :param image_config: ``CfnModel.ContainerDefinitionProperty.ImageConfig``.
            :param mode: ``CfnModel.ContainerDefinitionProperty.Mode``.
            :param model_data_url: ``CfnModel.ContainerDefinitionProperty.ModelDataUrl``.
            :param model_package_name: ``CfnModel.ContainerDefinitionProperty.ModelPackageName``.
            :param multi_model_config: ``CfnModel.ContainerDefinitionProperty.MultiModelConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if container_hostname is not None:
                self._values["container_hostname"] = container_hostname
            if environment is not None:
                self._values["environment"] = environment
            if image is not None:
                self._values["image"] = image
            if image_config is not None:
                self._values["image_config"] = image_config
            if mode is not None:
                self._values["mode"] = mode
            if model_data_url is not None:
                self._values["model_data_url"] = model_data_url
            if model_package_name is not None:
                self._values["model_package_name"] = model_package_name
            if multi_model_config is not None:
                self._values["multi_model_config"] = multi_model_config

        @builtins.property
        def container_hostname(self) -> typing.Optional[builtins.str]:
            '''``CfnModel.ContainerDefinitionProperty.ContainerHostname``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-containerhostname
            '''
            result = self._values.get("container_hostname")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def environment(self) -> typing.Any:
            '''``CfnModel.ContainerDefinitionProperty.Environment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-environment
            '''
            result = self._values.get("environment")
            return typing.cast(typing.Any, result)

        @builtins.property
        def image(self) -> typing.Optional[builtins.str]:
            '''``CfnModel.ContainerDefinitionProperty.Image``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-image
            '''
            result = self._values.get("image")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def image_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ImageConfigProperty"]]:
            '''``CfnModel.ContainerDefinitionProperty.ImageConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-imageconfig
            '''
            result = self._values.get("image_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.ImageConfigProperty"]], result)

        @builtins.property
        def mode(self) -> typing.Optional[builtins.str]:
            '''``CfnModel.ContainerDefinitionProperty.Mode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-mode
            '''
            result = self._values.get("mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def model_data_url(self) -> typing.Optional[builtins.str]:
            '''``CfnModel.ContainerDefinitionProperty.ModelDataUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-modeldataurl
            '''
            result = self._values.get("model_data_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def model_package_name(self) -> typing.Optional[builtins.str]:
            '''``CfnModel.ContainerDefinitionProperty.ModelPackageName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-modelpackagename
            '''
            result = self._values.get("model_package_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def multi_model_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.MultiModelConfigProperty"]]:
            '''``CfnModel.ContainerDefinitionProperty.MultiModelConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition.html#cfn-sagemaker-model-containerdefinition-multimodelconfig
            '''
            result = self._values.get("multi_model_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModel.MultiModelConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModel.ImageConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"repository_access_mode": "repositoryAccessMode"},
    )
    class ImageConfigProperty:
        def __init__(self, *, repository_access_mode: builtins.str) -> None:
            '''
            :param repository_access_mode: ``CfnModel.ImageConfigProperty.RepositoryAccessMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "repository_access_mode": repository_access_mode,
            }

        @builtins.property
        def repository_access_mode(self) -> builtins.str:
            '''``CfnModel.ImageConfigProperty.RepositoryAccessMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-imageconfig.html#cfn-sagemaker-model-containerdefinition-imageconfig-repositoryaccessmode
            '''
            result = self._values.get("repository_access_mode")
            assert result is not None, "Required property 'repository_access_mode' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModel.InferenceExecutionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"mode": "mode"},
    )
    class InferenceExecutionConfigProperty:
        def __init__(self, *, mode: builtins.str) -> None:
            '''
            :param mode: ``CfnModel.InferenceExecutionConfigProperty.Mode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-inferenceexecutionconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "mode": mode,
            }

        @builtins.property
        def mode(self) -> builtins.str:
            '''``CfnModel.InferenceExecutionConfigProperty.Mode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-inferenceexecutionconfig.html#cfn-sagemaker-model-inferenceexecutionconfig-mode
            '''
            result = self._values.get("mode")
            assert result is not None, "Required property 'mode' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InferenceExecutionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModel.MultiModelConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"model_cache_setting": "modelCacheSetting"},
    )
    class MultiModelConfigProperty:
        def __init__(
            self,
            *,
            model_cache_setting: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param model_cache_setting: ``CfnModel.MultiModelConfigProperty.ModelCacheSetting``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-multimodelconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if model_cache_setting is not None:
                self._values["model_cache_setting"] = model_cache_setting

        @builtins.property
        def model_cache_setting(self) -> typing.Optional[builtins.str]:
            '''``CfnModel.MultiModelConfigProperty.ModelCacheSetting``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-containerdefinition-multimodelconfig.html#cfn-sagemaker-model-containerdefinition-multimodelconfig-modelcachesetting
            '''
            result = self._values.get("model_cache_setting")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MultiModelConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModel.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param security_group_ids: ``CfnModel.VpcConfigProperty.SecurityGroupIds``.
            :param subnets: ``CfnModel.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-vpcconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''``CfnModel.VpcConfigProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-vpcconfig.html#cfn-sagemaker-model-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''``CfnModel.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-model-vpcconfig.html#cfn-sagemaker-model-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnModelBiasJobDefinition(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition",
):
    '''A CloudFormation ``AWS::SageMaker::ModelBiasJobDefinition``.

    :cloudformationResource: AWS::SageMaker::ModelBiasJobDefinition
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        job_resources: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringResourcesProperty"],
        model_bias_app_specification: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty"],
        model_bias_job_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasJobInputProperty"],
        model_bias_job_output_config: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringOutputConfigProperty"],
        role_arn: builtins.str,
        job_definition_name: typing.Optional[builtins.str] = None,
        model_bias_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty"]] = None,
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.NetworkConfigProperty"]] = None,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.StoppingConditionProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::ModelBiasJobDefinition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param job_resources: ``AWS::SageMaker::ModelBiasJobDefinition.JobResources``.
        :param model_bias_app_specification: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasAppSpecification``.
        :param model_bias_job_input: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobInput``.
        :param model_bias_job_output_config: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobOutputConfig``.
        :param role_arn: ``AWS::SageMaker::ModelBiasJobDefinition.RoleArn``.
        :param job_definition_name: ``AWS::SageMaker::ModelBiasJobDefinition.JobDefinitionName``.
        :param model_bias_baseline_config: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasBaselineConfig``.
        :param network_config: ``AWS::SageMaker::ModelBiasJobDefinition.NetworkConfig``.
        :param stopping_condition: ``AWS::SageMaker::ModelBiasJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::ModelBiasJobDefinition.Tags``.
        '''
        props = CfnModelBiasJobDefinitionProps(
            job_resources=job_resources,
            model_bias_app_specification=model_bias_app_specification,
            model_bias_job_input=model_bias_job_input,
            model_bias_job_output_config=model_bias_job_output_config,
            role_arn=role_arn,
            job_definition_name=job_definition_name,
            model_bias_baseline_config=model_bias_baseline_config,
            network_config=network_config,
            stopping_condition=stopping_condition,
            tags=tags,
        )

        jsii.create(CfnModelBiasJobDefinition, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrJobDefinitionArn")
    def attr_job_definition_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: JobDefinitionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrJobDefinitionArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::ModelBiasJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobResources")
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringResourcesProperty"]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.JobResources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-jobresources
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringResourcesProperty"], jsii.get(self, "jobResources"))

    @job_resources.setter
    def job_resources(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringResourcesProperty"],
    ) -> None:
        jsii.set(self, "jobResources", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelBiasAppSpecification")
    def model_bias_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty"]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasAppSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty"], jsii.get(self, "modelBiasAppSpecification"))

    @model_bias_app_specification.setter
    def model_bias_app_specification(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty"],
    ) -> None:
        jsii.set(self, "modelBiasAppSpecification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelBiasJobInput")
    def model_bias_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasJobInputProperty"]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobInput``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasJobInputProperty"], jsii.get(self, "modelBiasJobInput"))

    @model_bias_job_input.setter
    def model_bias_job_input(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasJobInputProperty"],
    ) -> None:
        jsii.set(self, "modelBiasJobInput", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelBiasJobOutputConfig")
    def model_bias_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringOutputConfigProperty"]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobOutputConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjoboutputconfig
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringOutputConfigProperty"], jsii.get(self, "modelBiasJobOutputConfig"))

    @model_bias_job_output_config.setter
    def model_bias_job_output_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringOutputConfigProperty"],
    ) -> None:
        jsii.set(self, "modelBiasJobOutputConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::ModelBiasJobDefinition.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobDefinitionName")
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.JobDefinitionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-jobdefinitionname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobDefinitionName"))

    @job_definition_name.setter
    def job_definition_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "jobDefinitionName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelBiasBaselineConfig")
    def model_bias_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty"]]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasBaselineConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty"]], jsii.get(self, "modelBiasBaselineConfig"))

    @model_bias_baseline_config.setter
    def model_bias_baseline_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty"]],
    ) -> None:
        jsii.set(self, "modelBiasBaselineConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="networkConfig")
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.NetworkConfigProperty"]]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.NetworkConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.NetworkConfigProperty"]], jsii.get(self, "networkConfig"))

    @network_config.setter
    def network_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.NetworkConfigProperty"]],
    ) -> None:
        jsii.set(self, "networkConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stoppingCondition")
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.StoppingConditionProperty"]]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.StoppingCondition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-stoppingcondition
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.StoppingConditionProperty"]], jsii.get(self, "stoppingCondition"))

    @stopping_condition.setter
    def stopping_condition(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.StoppingConditionProperty"]],
    ) -> None:
        jsii.set(self, "stoppingCondition", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.ClusterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_count": "instanceCount",
            "instance_type": "instanceType",
            "volume_size_in_gb": "volumeSizeInGb",
            "volume_kms_key_id": "volumeKmsKeyId",
        },
    )
    class ClusterConfigProperty:
        def __init__(
            self,
            *,
            instance_count: jsii.Number,
            instance_type: builtins.str,
            volume_size_in_gb: jsii.Number,
            volume_kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param instance_count: ``CfnModelBiasJobDefinition.ClusterConfigProperty.InstanceCount``.
            :param instance_type: ``CfnModelBiasJobDefinition.ClusterConfigProperty.InstanceType``.
            :param volume_size_in_gb: ``CfnModelBiasJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.
            :param volume_kms_key_id: ``CfnModelBiasJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "instance_count": instance_count,
                "instance_type": instance_type,
                "volume_size_in_gb": volume_size_in_gb,
            }
            if volume_kms_key_id is not None:
                self._values["volume_kms_key_id"] = volume_kms_key_id

        @builtins.property
        def instance_count(self) -> jsii.Number:
            '''``CfnModelBiasJobDefinition.ClusterConfigProperty.InstanceCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html#cfn-sagemaker-modelbiasjobdefinition-clusterconfig-instancecount
            '''
            result = self._values.get("instance_count")
            assert result is not None, "Required property 'instance_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''``CfnModelBiasJobDefinition.ClusterConfigProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html#cfn-sagemaker-modelbiasjobdefinition-clusterconfig-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def volume_size_in_gb(self) -> jsii.Number:
            '''``CfnModelBiasJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html#cfn-sagemaker-modelbiasjobdefinition-clusterconfig-volumesizeingb
            '''
            result = self._values.get("volume_size_in_gb")
            assert result is not None, "Required property 'volume_size_in_gb' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-clusterconfig.html#cfn-sagemaker-modelbiasjobdefinition-clusterconfig-volumekmskeyid
            '''
            result = self._values.get("volume_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClusterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.ConstraintsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class ConstraintsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            '''
            :param s3_uri: ``CfnModelBiasJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-constraintsresource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-constraintsresource.html#cfn-sagemaker-modelbiasjobdefinition-constraintsresource-s3uri
            '''
            result = self._values.get("s3_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConstraintsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.EndpointInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_name": "endpointName",
            "local_path": "localPath",
            "end_time_offset": "endTimeOffset",
            "features_attribute": "featuresAttribute",
            "inference_attribute": "inferenceAttribute",
            "probability_attribute": "probabilityAttribute",
            "probability_threshold_attribute": "probabilityThresholdAttribute",
            "s3_data_distribution_type": "s3DataDistributionType",
            "s3_input_mode": "s3InputMode",
            "start_time_offset": "startTimeOffset",
        },
    )
    class EndpointInputProperty:
        def __init__(
            self,
            *,
            endpoint_name: builtins.str,
            local_path: builtins.str,
            end_time_offset: typing.Optional[builtins.str] = None,
            features_attribute: typing.Optional[builtins.str] = None,
            inference_attribute: typing.Optional[builtins.str] = None,
            probability_attribute: typing.Optional[builtins.str] = None,
            probability_threshold_attribute: typing.Optional[jsii.Number] = None,
            s3_data_distribution_type: typing.Optional[builtins.str] = None,
            s3_input_mode: typing.Optional[builtins.str] = None,
            start_time_offset: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param endpoint_name: ``CfnModelBiasJobDefinition.EndpointInputProperty.EndpointName``.
            :param local_path: ``CfnModelBiasJobDefinition.EndpointInputProperty.LocalPath``.
            :param end_time_offset: ``CfnModelBiasJobDefinition.EndpointInputProperty.EndTimeOffset``.
            :param features_attribute: ``CfnModelBiasJobDefinition.EndpointInputProperty.FeaturesAttribute``.
            :param inference_attribute: ``CfnModelBiasJobDefinition.EndpointInputProperty.InferenceAttribute``.
            :param probability_attribute: ``CfnModelBiasJobDefinition.EndpointInputProperty.ProbabilityAttribute``.
            :param probability_threshold_attribute: ``CfnModelBiasJobDefinition.EndpointInputProperty.ProbabilityThresholdAttribute``.
            :param s3_data_distribution_type: ``CfnModelBiasJobDefinition.EndpointInputProperty.S3DataDistributionType``.
            :param s3_input_mode: ``CfnModelBiasJobDefinition.EndpointInputProperty.S3InputMode``.
            :param start_time_offset: ``CfnModelBiasJobDefinition.EndpointInputProperty.StartTimeOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_name": endpoint_name,
                "local_path": local_path,
            }
            if end_time_offset is not None:
                self._values["end_time_offset"] = end_time_offset
            if features_attribute is not None:
                self._values["features_attribute"] = features_attribute
            if inference_attribute is not None:
                self._values["inference_attribute"] = inference_attribute
            if probability_attribute is not None:
                self._values["probability_attribute"] = probability_attribute
            if probability_threshold_attribute is not None:
                self._values["probability_threshold_attribute"] = probability_threshold_attribute
            if s3_data_distribution_type is not None:
                self._values["s3_data_distribution_type"] = s3_data_distribution_type
            if s3_input_mode is not None:
                self._values["s3_input_mode"] = s3_input_mode
            if start_time_offset is not None:
                self._values["start_time_offset"] = start_time_offset

        @builtins.property
        def endpoint_name(self) -> builtins.str:
            '''``CfnModelBiasJobDefinition.EndpointInputProperty.EndpointName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-endpointname
            '''
            result = self._values.get("endpoint_name")
            assert result is not None, "Required property 'endpoint_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def local_path(self) -> builtins.str:
            '''``CfnModelBiasJobDefinition.EndpointInputProperty.LocalPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-localpath
            '''
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def end_time_offset(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.EndpointInputProperty.EndTimeOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-endtimeoffset
            '''
            result = self._values.get("end_time_offset")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def features_attribute(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.EndpointInputProperty.FeaturesAttribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-featuresattribute
            '''
            result = self._values.get("features_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inference_attribute(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.EndpointInputProperty.InferenceAttribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-inferenceattribute
            '''
            result = self._values.get("inference_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def probability_attribute(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.EndpointInputProperty.ProbabilityAttribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-probabilityattribute
            '''
            result = self._values.get("probability_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def probability_threshold_attribute(self) -> typing.Optional[jsii.Number]:
            '''``CfnModelBiasJobDefinition.EndpointInputProperty.ProbabilityThresholdAttribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-probabilitythresholdattribute
            '''
            result = self._values.get("probability_threshold_attribute")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def s3_data_distribution_type(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.EndpointInputProperty.S3DataDistributionType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-s3datadistributiontype
            '''
            result = self._values.get("s3_data_distribution_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_input_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.EndpointInputProperty.S3InputMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-s3inputmode
            '''
            result = self._values.get("s3_input_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def start_time_offset(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.EndpointInputProperty.StartTimeOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-endpointinput.html#cfn-sagemaker-modelbiasjobdefinition-endpointinput-starttimeoffset
            '''
            result = self._values.get("start_time_offset")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.EnvironmentProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class EnvironmentProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-environment.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "config_uri": "configUri",
            "image_uri": "imageUri",
            "environment": "environment",
        },
    )
    class ModelBiasAppSpecificationProperty:
        def __init__(
            self,
            *,
            config_uri: builtins.str,
            image_uri: builtins.str,
            environment: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.EnvironmentProperty"]] = None,
        ) -> None:
            '''
            :param config_uri: ``CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty.ConfigUri``.
            :param image_uri: ``CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty.ImageUri``.
            :param environment: ``CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty.Environment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "config_uri": config_uri,
                "image_uri": image_uri,
            }
            if environment is not None:
                self._values["environment"] = environment

        @builtins.property
        def config_uri(self) -> builtins.str:
            '''``CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty.ConfigUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-configuri
            '''
            result = self._values.get("config_uri")
            assert result is not None, "Required property 'config_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_uri(self) -> builtins.str:
            '''``CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty.ImageUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-imageuri
            '''
            result = self._values.get("image_uri")
            assert result is not None, "Required property 'image_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.EnvironmentProperty"]]:
            '''``CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty.Environment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasappspecification.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification-environment
            '''
            result = self._values.get("environment")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.EnvironmentProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelBiasAppSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "baselining_job_name": "baseliningJobName",
            "constraints_resource": "constraintsResource",
        },
    )
    class ModelBiasBaselineConfigProperty:
        def __init__(
            self,
            *,
            baselining_job_name: typing.Optional[builtins.str] = None,
            constraints_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ConstraintsResourceProperty"]] = None,
        ) -> None:
            '''
            :param baselining_job_name: ``CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty.BaseliningJobName``.
            :param constraints_resource: ``CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty.ConstraintsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if baselining_job_name is not None:
                self._values["baselining_job_name"] = baselining_job_name
            if constraints_resource is not None:
                self._values["constraints_resource"] = constraints_resource

        @builtins.property
        def baselining_job_name(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty.BaseliningJobName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig-baseliningjobname
            '''
            result = self._values.get("baselining_job_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def constraints_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ConstraintsResourceProperty"]]:
            '''``CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty.ConstraintsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig-constraintsresource
            '''
            result = self._values.get("constraints_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ConstraintsResourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelBiasBaselineConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.ModelBiasJobInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_input": "endpointInput",
            "ground_truth_s3_input": "groundTruthS3Input",
        },
    )
    class ModelBiasJobInputProperty:
        def __init__(
            self,
            *,
            endpoint_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.EndpointInputProperty"],
            ground_truth_s3_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty"],
        ) -> None:
            '''
            :param endpoint_input: ``CfnModelBiasJobDefinition.ModelBiasJobInputProperty.EndpointInput``.
            :param ground_truth_s3_input: ``CfnModelBiasJobDefinition.ModelBiasJobInputProperty.GroundTruthS3Input``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_input": endpoint_input,
                "ground_truth_s3_input": ground_truth_s3_input,
            }

        @builtins.property
        def endpoint_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.EndpointInputProperty"]:
            '''``CfnModelBiasJobDefinition.ModelBiasJobInputProperty.EndpointInput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput-endpointinput
            '''
            result = self._values.get("endpoint_input")
            assert result is not None, "Required property 'endpoint_input' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.EndpointInputProperty"], result)

        @builtins.property
        def ground_truth_s3_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty"]:
            '''``CfnModelBiasJobDefinition.ModelBiasJobInputProperty.GroundTruthS3Input``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-modelbiasjobinput.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput-groundtruths3input
            '''
            result = self._values.get("ground_truth_s3_input")
            assert result is not None, "Required property 'ground_truth_s3_input' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelBiasJobInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class MonitoringGroundTruthS3InputProperty:
        def __init__(self, *, s3_uri: builtins.str) -> None:
            '''
            :param s3_uri: ``CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "s3_uri": s3_uri,
            }

        @builtins.property
        def s3_uri(self) -> builtins.str:
            '''``CfnModelBiasJobDefinition.MonitoringGroundTruthS3InputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input.html#cfn-sagemaker-modelbiasjobdefinition-monitoringgroundtruths3input-s3uri
            '''
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringGroundTruthS3InputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.MonitoringOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "monitoring_outputs": "monitoringOutputs",
            "kms_key_id": "kmsKeyId",
        },
    )
    class MonitoringOutputConfigProperty:
        def __init__(
            self,
            *,
            monitoring_outputs: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringOutputProperty"]]],
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param monitoring_outputs: ``CfnModelBiasJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.
            :param kms_key_id: ``CfnModelBiasJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutputconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "monitoring_outputs": monitoring_outputs,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def monitoring_outputs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringOutputProperty"]]]:
            '''``CfnModelBiasJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelbiasjobdefinition-monitoringoutputconfig-monitoringoutputs
            '''
            result = self._values.get("monitoring_outputs")
            assert result is not None, "Required property 'monitoring_outputs' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.MonitoringOutputProperty"]]], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelbiasjobdefinition-monitoringoutputconfig-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.MonitoringOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_output": "s3Output"},
    )
    class MonitoringOutputProperty:
        def __init__(
            self,
            *,
            s3_output: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.S3OutputProperty"],
        ) -> None:
            '''
            :param s3_output: ``CfnModelBiasJobDefinition.MonitoringOutputProperty.S3Output``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutput.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "s3_output": s3_output,
            }

        @builtins.property
        def s3_output(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.S3OutputProperty"]:
            '''``CfnModelBiasJobDefinition.MonitoringOutputProperty.S3Output``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringoutput.html#cfn-sagemaker-modelbiasjobdefinition-monitoringoutput-s3output
            '''
            result = self._values.get("s3_output")
            assert result is not None, "Required property 's3_output' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.S3OutputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.MonitoringResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_config": "clusterConfig"},
    )
    class MonitoringResourcesProperty:
        def __init__(
            self,
            *,
            cluster_config: typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ClusterConfigProperty"],
        ) -> None:
            '''
            :param cluster_config: ``CfnModelBiasJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringresources.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cluster_config": cluster_config,
            }

        @builtins.property
        def cluster_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ClusterConfigProperty"]:
            '''``CfnModelBiasJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-monitoringresources.html#cfn-sagemaker-modelbiasjobdefinition-monitoringresources-clusterconfig
            '''
            result = self._values.get("cluster_config")
            assert result is not None, "Required property 'cluster_config' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.ClusterConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.NetworkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_inter_container_traffic_encryption": "enableInterContainerTrafficEncryption",
            "enable_network_isolation": "enableNetworkIsolation",
            "vpc_config": "vpcConfig",
        },
    )
    class NetworkConfigProperty:
        def __init__(
            self,
            *,
            enable_inter_container_traffic_encryption: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.VpcConfigProperty"]] = None,
        ) -> None:
            '''
            :param enable_inter_container_traffic_encryption: ``CfnModelBiasJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.
            :param enable_network_isolation: ``CfnModelBiasJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.
            :param vpc_config: ``CfnModelBiasJobDefinition.NetworkConfigProperty.VpcConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-networkconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if enable_inter_container_traffic_encryption is not None:
                self._values["enable_inter_container_traffic_encryption"] = enable_inter_container_traffic_encryption
            if enable_network_isolation is not None:
                self._values["enable_network_isolation"] = enable_network_isolation
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def enable_inter_container_traffic_encryption(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnModelBiasJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-networkconfig.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig-enableintercontainertrafficencryption
            '''
            result = self._values.get("enable_inter_container_traffic_encryption")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def enable_network_isolation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnModelBiasJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-networkconfig.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig-enablenetworkisolation
            '''
            result = self._values.get("enable_network_isolation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.VpcConfigProperty"]]:
            '''``CfnModelBiasJobDefinition.NetworkConfigProperty.VpcConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-networkconfig.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig-vpcconfig
            '''
            result = self._values.get("vpc_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelBiasJobDefinition.VpcConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.S3OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "local_path": "localPath",
            "s3_uri": "s3Uri",
            "s3_upload_mode": "s3UploadMode",
        },
    )
    class S3OutputProperty:
        def __init__(
            self,
            *,
            local_path: builtins.str,
            s3_uri: builtins.str,
            s3_upload_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param local_path: ``CfnModelBiasJobDefinition.S3OutputProperty.LocalPath``.
            :param s3_uri: ``CfnModelBiasJobDefinition.S3OutputProperty.S3Uri``.
            :param s3_upload_mode: ``CfnModelBiasJobDefinition.S3OutputProperty.S3UploadMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-s3output.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "local_path": local_path,
                "s3_uri": s3_uri,
            }
            if s3_upload_mode is not None:
                self._values["s3_upload_mode"] = s3_upload_mode

        @builtins.property
        def local_path(self) -> builtins.str:
            '''``CfnModelBiasJobDefinition.S3OutputProperty.LocalPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-s3output.html#cfn-sagemaker-modelbiasjobdefinition-s3output-localpath
            '''
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_uri(self) -> builtins.str:
            '''``CfnModelBiasJobDefinition.S3OutputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-s3output.html#cfn-sagemaker-modelbiasjobdefinition-s3output-s3uri
            '''
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_upload_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnModelBiasJobDefinition.S3OutputProperty.S3UploadMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-s3output.html#cfn-sagemaker-modelbiasjobdefinition-s3output-s3uploadmode
            '''
            result = self._values.get("s3_upload_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.StoppingConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"max_runtime_in_seconds": "maxRuntimeInSeconds"},
    )
    class StoppingConditionProperty:
        def __init__(self, *, max_runtime_in_seconds: jsii.Number) -> None:
            '''
            :param max_runtime_in_seconds: ``CfnModelBiasJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-stoppingcondition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_runtime_in_seconds": max_runtime_in_seconds,
            }

        @builtins.property
        def max_runtime_in_seconds(self) -> jsii.Number:
            '''``CfnModelBiasJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-stoppingcondition.html#cfn-sagemaker-modelbiasjobdefinition-stoppingcondition-maxruntimeinseconds
            '''
            result = self._values.get("max_runtime_in_seconds")
            assert result is not None, "Required property 'max_runtime_in_seconds' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StoppingConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinition.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param security_group_ids: ``CfnModelBiasJobDefinition.VpcConfigProperty.SecurityGroupIds``.
            :param subnets: ``CfnModelBiasJobDefinition.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-vpcconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''``CfnModelBiasJobDefinition.VpcConfigProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-vpcconfig.html#cfn-sagemaker-modelbiasjobdefinition-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''``CfnModelBiasJobDefinition.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelbiasjobdefinition-vpcconfig.html#cfn-sagemaker-modelbiasjobdefinition-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelBiasJobDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "job_resources": "jobResources",
        "model_bias_app_specification": "modelBiasAppSpecification",
        "model_bias_job_input": "modelBiasJobInput",
        "model_bias_job_output_config": "modelBiasJobOutputConfig",
        "role_arn": "roleArn",
        "job_definition_name": "jobDefinitionName",
        "model_bias_baseline_config": "modelBiasBaselineConfig",
        "network_config": "networkConfig",
        "stopping_condition": "stoppingCondition",
        "tags": "tags",
    },
)
class CfnModelBiasJobDefinitionProps:
    def __init__(
        self,
        *,
        job_resources: typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.MonitoringResourcesProperty],
        model_bias_app_specification: typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty],
        model_bias_job_input: typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasJobInputProperty],
        model_bias_job_output_config: typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.MonitoringOutputConfigProperty],
        role_arn: builtins.str,
        job_definition_name: typing.Optional[builtins.str] = None,
        model_bias_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty]] = None,
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.NetworkConfigProperty]] = None,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.StoppingConditionProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::ModelBiasJobDefinition``.

        :param job_resources: ``AWS::SageMaker::ModelBiasJobDefinition.JobResources``.
        :param model_bias_app_specification: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasAppSpecification``.
        :param model_bias_job_input: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobInput``.
        :param model_bias_job_output_config: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobOutputConfig``.
        :param role_arn: ``AWS::SageMaker::ModelBiasJobDefinition.RoleArn``.
        :param job_definition_name: ``AWS::SageMaker::ModelBiasJobDefinition.JobDefinitionName``.
        :param model_bias_baseline_config: ``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasBaselineConfig``.
        :param network_config: ``AWS::SageMaker::ModelBiasJobDefinition.NetworkConfig``.
        :param stopping_condition: ``AWS::SageMaker::ModelBiasJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::ModelBiasJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "job_resources": job_resources,
            "model_bias_app_specification": model_bias_app_specification,
            "model_bias_job_input": model_bias_job_input,
            "model_bias_job_output_config": model_bias_job_output_config,
            "role_arn": role_arn,
        }
        if job_definition_name is not None:
            self._values["job_definition_name"] = job_definition_name
        if model_bias_baseline_config is not None:
            self._values["model_bias_baseline_config"] = model_bias_baseline_config
        if network_config is not None:
            self._values["network_config"] = network_config
        if stopping_condition is not None:
            self._values["stopping_condition"] = stopping_condition
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.MonitoringResourcesProperty]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.JobResources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-jobresources
        '''
        result = self._values.get("job_resources")
        assert result is not None, "Required property 'job_resources' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.MonitoringResourcesProperty], result)

    @builtins.property
    def model_bias_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasAppSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification
        '''
        result = self._values.get("model_bias_app_specification")
        assert result is not None, "Required property 'model_bias_app_specification' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasAppSpecificationProperty], result)

    @builtins.property
    def model_bias_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasJobInputProperty]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobInput``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput
        '''
        result = self._values.get("model_bias_job_input")
        assert result is not None, "Required property 'model_bias_job_input' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasJobInputProperty], result)

    @builtins.property
    def model_bias_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.MonitoringOutputConfigProperty]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasJobOutputConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjoboutputconfig
        '''
        result = self._values.get("model_bias_job_output_config")
        assert result is not None, "Required property 'model_bias_job_output_config' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.MonitoringOutputConfigProperty], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::ModelBiasJobDefinition.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.JobDefinitionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-jobdefinitionname
        '''
        result = self._values.get("job_definition_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def model_bias_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty]]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.ModelBiasBaselineConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig
        '''
        result = self._values.get("model_bias_baseline_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.ModelBiasBaselineConfigProperty]], result)

    @builtins.property
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.NetworkConfigProperty]]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.NetworkConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig
        '''
        result = self._values.get("network_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.NetworkConfigProperty]], result)

    @builtins.property
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.StoppingConditionProperty]]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.StoppingCondition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-stoppingcondition
        '''
        result = self._values.get("stopping_condition")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelBiasJobDefinition.StoppingConditionProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::ModelBiasJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModelBiasJobDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnModelExplainabilityJobDefinition(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition",
):
    '''A CloudFormation ``AWS::SageMaker::ModelExplainabilityJobDefinition``.

    :cloudformationResource: AWS::SageMaker::ModelExplainabilityJobDefinition
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        job_resources: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty"],
        model_explainability_app_specification: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty"],
        model_explainability_job_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty"],
        model_explainability_job_output_config: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty"],
        role_arn: builtins.str,
        job_definition_name: typing.Optional[builtins.str] = None,
        model_explainability_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty"]] = None,
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.NetworkConfigProperty"]] = None,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.StoppingConditionProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::ModelExplainabilityJobDefinition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param job_resources: ``AWS::SageMaker::ModelExplainabilityJobDefinition.JobResources``.
        :param model_explainability_app_specification: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityAppSpecification``.
        :param model_explainability_job_input: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobInput``.
        :param model_explainability_job_output_config: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobOutputConfig``.
        :param role_arn: ``AWS::SageMaker::ModelExplainabilityJobDefinition.RoleArn``.
        :param job_definition_name: ``AWS::SageMaker::ModelExplainabilityJobDefinition.JobDefinitionName``.
        :param model_explainability_baseline_config: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfig``.
        :param network_config: ``AWS::SageMaker::ModelExplainabilityJobDefinition.NetworkConfig``.
        :param stopping_condition: ``AWS::SageMaker::ModelExplainabilityJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::ModelExplainabilityJobDefinition.Tags``.
        '''
        props = CfnModelExplainabilityJobDefinitionProps(
            job_resources=job_resources,
            model_explainability_app_specification=model_explainability_app_specification,
            model_explainability_job_input=model_explainability_job_input,
            model_explainability_job_output_config=model_explainability_job_output_config,
            role_arn=role_arn,
            job_definition_name=job_definition_name,
            model_explainability_baseline_config=model_explainability_baseline_config,
            network_config=network_config,
            stopping_condition=stopping_condition,
            tags=tags,
        )

        jsii.create(CfnModelExplainabilityJobDefinition, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrJobDefinitionArn")
    def attr_job_definition_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: JobDefinitionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrJobDefinitionArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobResources")
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty"]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.JobResources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-jobresources
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty"], jsii.get(self, "jobResources"))

    @job_resources.setter
    def job_resources(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty"],
    ) -> None:
        jsii.set(self, "jobResources", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelExplainabilityAppSpecification")
    def model_explainability_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty"]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityAppSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty"], jsii.get(self, "modelExplainabilityAppSpecification"))

    @model_explainability_app_specification.setter
    def model_explainability_app_specification(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty"],
    ) -> None:
        jsii.set(self, "modelExplainabilityAppSpecification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelExplainabilityJobInput")
    def model_explainability_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty"]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobInput``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty"], jsii.get(self, "modelExplainabilityJobInput"))

    @model_explainability_job_input.setter
    def model_explainability_job_input(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty"],
    ) -> None:
        jsii.set(self, "modelExplainabilityJobInput", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelExplainabilityJobOutputConfig")
    def model_explainability_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty"]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobOutputConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjoboutputconfig
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty"], jsii.get(self, "modelExplainabilityJobOutputConfig"))

    @model_explainability_job_output_config.setter
    def model_explainability_job_output_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty"],
    ) -> None:
        jsii.set(self, "modelExplainabilityJobOutputConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobDefinitionName")
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.JobDefinitionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-jobdefinitionname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobDefinitionName"))

    @job_definition_name.setter
    def job_definition_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "jobDefinitionName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelExplainabilityBaselineConfig")
    def model_explainability_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty"]]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty"]], jsii.get(self, "modelExplainabilityBaselineConfig"))

    @model_explainability_baseline_config.setter
    def model_explainability_baseline_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty"]],
    ) -> None:
        jsii.set(self, "modelExplainabilityBaselineConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="networkConfig")
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.NetworkConfigProperty"]]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.NetworkConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.NetworkConfigProperty"]], jsii.get(self, "networkConfig"))

    @network_config.setter
    def network_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.NetworkConfigProperty"]],
    ) -> None:
        jsii.set(self, "networkConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stoppingCondition")
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.StoppingConditionProperty"]]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.StoppingCondition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-stoppingcondition
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.StoppingConditionProperty"]], jsii.get(self, "stoppingCondition"))

    @stopping_condition.setter
    def stopping_condition(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.StoppingConditionProperty"]],
    ) -> None:
        jsii.set(self, "stoppingCondition", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.ClusterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_count": "instanceCount",
            "instance_type": "instanceType",
            "volume_size_in_gb": "volumeSizeInGb",
            "volume_kms_key_id": "volumeKmsKeyId",
        },
    )
    class ClusterConfigProperty:
        def __init__(
            self,
            *,
            instance_count: jsii.Number,
            instance_type: builtins.str,
            volume_size_in_gb: jsii.Number,
            volume_kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param instance_count: ``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.InstanceCount``.
            :param instance_type: ``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.InstanceType``.
            :param volume_size_in_gb: ``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.
            :param volume_kms_key_id: ``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "instance_count": instance_count,
                "instance_type": instance_type,
                "volume_size_in_gb": volume_size_in_gb,
            }
            if volume_kms_key_id is not None:
                self._values["volume_kms_key_id"] = volume_kms_key_id

        @builtins.property
        def instance_count(self) -> jsii.Number:
            '''``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.InstanceCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-clusterconfig-instancecount
            '''
            result = self._values.get("instance_count")
            assert result is not None, "Required property 'instance_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-clusterconfig-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def volume_size_in_gb(self) -> jsii.Number:
            '''``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-clusterconfig-volumesizeingb
            '''
            result = self._values.get("volume_size_in_gb")
            assert result is not None, "Required property 'volume_size_in_gb' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-clusterconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-clusterconfig-volumekmskeyid
            '''
            result = self._values.get("volume_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClusterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class ConstraintsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            '''
            :param s3_uri: ``CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-constraintsresource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-constraintsresource.html#cfn-sagemaker-modelexplainabilityjobdefinition-constraintsresource-s3uri
            '''
            result = self._values.get("s3_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConstraintsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.EndpointInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_name": "endpointName",
            "local_path": "localPath",
            "features_attribute": "featuresAttribute",
            "inference_attribute": "inferenceAttribute",
            "probability_attribute": "probabilityAttribute",
            "s3_data_distribution_type": "s3DataDistributionType",
            "s3_input_mode": "s3InputMode",
        },
    )
    class EndpointInputProperty:
        def __init__(
            self,
            *,
            endpoint_name: builtins.str,
            local_path: builtins.str,
            features_attribute: typing.Optional[builtins.str] = None,
            inference_attribute: typing.Optional[builtins.str] = None,
            probability_attribute: typing.Optional[builtins.str] = None,
            s3_data_distribution_type: typing.Optional[builtins.str] = None,
            s3_input_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param endpoint_name: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.EndpointName``.
            :param local_path: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.LocalPath``.
            :param features_attribute: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.FeaturesAttribute``.
            :param inference_attribute: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.InferenceAttribute``.
            :param probability_attribute: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.ProbabilityAttribute``.
            :param s3_data_distribution_type: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.S3DataDistributionType``.
            :param s3_input_mode: ``CfnModelExplainabilityJobDefinition.EndpointInputProperty.S3InputMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_name": endpoint_name,
                "local_path": local_path,
            }
            if features_attribute is not None:
                self._values["features_attribute"] = features_attribute
            if inference_attribute is not None:
                self._values["inference_attribute"] = inference_attribute
            if probability_attribute is not None:
                self._values["probability_attribute"] = probability_attribute
            if s3_data_distribution_type is not None:
                self._values["s3_data_distribution_type"] = s3_data_distribution_type
            if s3_input_mode is not None:
                self._values["s3_input_mode"] = s3_input_mode

        @builtins.property
        def endpoint_name(self) -> builtins.str:
            '''``CfnModelExplainabilityJobDefinition.EndpointInputProperty.EndpointName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-endpointname
            '''
            result = self._values.get("endpoint_name")
            assert result is not None, "Required property 'endpoint_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def local_path(self) -> builtins.str:
            '''``CfnModelExplainabilityJobDefinition.EndpointInputProperty.LocalPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-localpath
            '''
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def features_attribute(self) -> typing.Optional[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.EndpointInputProperty.FeaturesAttribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-featuresattribute
            '''
            result = self._values.get("features_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inference_attribute(self) -> typing.Optional[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.EndpointInputProperty.InferenceAttribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-inferenceattribute
            '''
            result = self._values.get("inference_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def probability_attribute(self) -> typing.Optional[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.EndpointInputProperty.ProbabilityAttribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-probabilityattribute
            '''
            result = self._values.get("probability_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_data_distribution_type(self) -> typing.Optional[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.EndpointInputProperty.S3DataDistributionType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-s3datadistributiontype
            '''
            result = self._values.get("s3_data_distribution_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_input_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.EndpointInputProperty.S3InputMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-endpointinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-endpointinput-s3inputmode
            '''
            result = self._values.get("s3_input_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.EnvironmentProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class EnvironmentProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-environment.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "config_uri": "configUri",
            "image_uri": "imageUri",
            "environment": "environment",
        },
    )
    class ModelExplainabilityAppSpecificationProperty:
        def __init__(
            self,
            *,
            config_uri: builtins.str,
            image_uri: builtins.str,
            environment: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.EnvironmentProperty"]] = None,
        ) -> None:
            '''
            :param config_uri: ``CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty.ConfigUri``.
            :param image_uri: ``CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty.ImageUri``.
            :param environment: ``CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty.Environment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "config_uri": config_uri,
                "image_uri": image_uri,
            }
            if environment is not None:
                self._values["environment"] = environment

        @builtins.property
        def config_uri(self) -> builtins.str:
            '''``CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty.ConfigUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-configuri
            '''
            result = self._values.get("config_uri")
            assert result is not None, "Required property 'config_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_uri(self) -> builtins.str:
            '''``CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty.ImageUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-imageuri
            '''
            result = self._values.get("image_uri")
            assert result is not None, "Required property 'image_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.EnvironmentProperty"]]:
            '''``CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty.Environment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification-environment
            '''
            result = self._values.get("environment")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.EnvironmentProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelExplainabilityAppSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "baselining_job_name": "baseliningJobName",
            "constraints_resource": "constraintsResource",
        },
    )
    class ModelExplainabilityBaselineConfigProperty:
        def __init__(
            self,
            *,
            baselining_job_name: typing.Optional[builtins.str] = None,
            constraints_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty"]] = None,
        ) -> None:
            '''
            :param baselining_job_name: ``CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty.BaseliningJobName``.
            :param constraints_resource: ``CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty.ConstraintsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if baselining_job_name is not None:
                self._values["baselining_job_name"] = baselining_job_name
            if constraints_resource is not None:
                self._values["constraints_resource"] = constraints_resource

        @builtins.property
        def baselining_job_name(self) -> typing.Optional[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty.BaseliningJobName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig-baseliningjobname
            '''
            result = self._values.get("baselining_job_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def constraints_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty"]]:
            '''``CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty.ConstraintsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig-constraintsresource
            '''
            result = self._values.get("constraints_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ConstraintsResourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelExplainabilityBaselineConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint_input": "endpointInput"},
    )
    class ModelExplainabilityJobInputProperty:
        def __init__(
            self,
            *,
            endpoint_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.EndpointInputProperty"],
        ) -> None:
            '''
            :param endpoint_input: ``CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty.EndpointInput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_input": endpoint_input,
            }

        @builtins.property
        def endpoint_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.EndpointInputProperty"]:
            '''``CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty.EndpointInput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput-endpointinput
            '''
            result = self._values.get("endpoint_input")
            assert result is not None, "Required property 'endpoint_input' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.EndpointInputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelExplainabilityJobInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "monitoring_outputs": "monitoringOutputs",
            "kms_key_id": "kmsKeyId",
        },
    )
    class MonitoringOutputConfigProperty:
        def __init__(
            self,
            *,
            monitoring_outputs: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringOutputProperty"]]],
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param monitoring_outputs: ``CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.
            :param kms_key_id: ``CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "monitoring_outputs": monitoring_outputs,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def monitoring_outputs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringOutputProperty"]]]:
            '''``CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig-monitoringoutputs
            '''
            result = self._values.get("monitoring_outputs")
            assert result is not None, "Required property 'monitoring_outputs' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.MonitoringOutputProperty"]]], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-monitoringoutputconfig-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.MonitoringOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_output": "s3Output"},
    )
    class MonitoringOutputProperty:
        def __init__(
            self,
            *,
            s3_output: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.S3OutputProperty"],
        ) -> None:
            '''
            :param s3_output: ``CfnModelExplainabilityJobDefinition.MonitoringOutputProperty.S3Output``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutput.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "s3_output": s3_output,
            }

        @builtins.property
        def s3_output(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.S3OutputProperty"]:
            '''``CfnModelExplainabilityJobDefinition.MonitoringOutputProperty.S3Output``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringoutput.html#cfn-sagemaker-modelexplainabilityjobdefinition-monitoringoutput-s3output
            '''
            result = self._values.get("s3_output")
            assert result is not None, "Required property 's3_output' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.S3OutputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_config": "clusterConfig"},
    )
    class MonitoringResourcesProperty:
        def __init__(
            self,
            *,
            cluster_config: typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ClusterConfigProperty"],
        ) -> None:
            '''
            :param cluster_config: ``CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringresources.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cluster_config": cluster_config,
            }

        @builtins.property
        def cluster_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ClusterConfigProperty"]:
            '''``CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-monitoringresources.html#cfn-sagemaker-modelexplainabilityjobdefinition-monitoringresources-clusterconfig
            '''
            result = self._values.get("cluster_config")
            assert result is not None, "Required property 'cluster_config' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.ClusterConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.NetworkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_inter_container_traffic_encryption": "enableInterContainerTrafficEncryption",
            "enable_network_isolation": "enableNetworkIsolation",
            "vpc_config": "vpcConfig",
        },
    )
    class NetworkConfigProperty:
        def __init__(
            self,
            *,
            enable_inter_container_traffic_encryption: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.VpcConfigProperty"]] = None,
        ) -> None:
            '''
            :param enable_inter_container_traffic_encryption: ``CfnModelExplainabilityJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.
            :param enable_network_isolation: ``CfnModelExplainabilityJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.
            :param vpc_config: ``CfnModelExplainabilityJobDefinition.NetworkConfigProperty.VpcConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-networkconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if enable_inter_container_traffic_encryption is not None:
                self._values["enable_inter_container_traffic_encryption"] = enable_inter_container_traffic_encryption
            if enable_network_isolation is not None:
                self._values["enable_network_isolation"] = enable_network_isolation
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def enable_inter_container_traffic_encryption(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnModelExplainabilityJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-networkconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig-enableintercontainertrafficencryption
            '''
            result = self._values.get("enable_inter_container_traffic_encryption")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def enable_network_isolation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnModelExplainabilityJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-networkconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig-enablenetworkisolation
            '''
            result = self._values.get("enable_network_isolation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.VpcConfigProperty"]]:
            '''``CfnModelExplainabilityJobDefinition.NetworkConfigProperty.VpcConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-networkconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig-vpcconfig
            '''
            result = self._values.get("vpc_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelExplainabilityJobDefinition.VpcConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.S3OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "local_path": "localPath",
            "s3_uri": "s3Uri",
            "s3_upload_mode": "s3UploadMode",
        },
    )
    class S3OutputProperty:
        def __init__(
            self,
            *,
            local_path: builtins.str,
            s3_uri: builtins.str,
            s3_upload_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param local_path: ``CfnModelExplainabilityJobDefinition.S3OutputProperty.LocalPath``.
            :param s3_uri: ``CfnModelExplainabilityJobDefinition.S3OutputProperty.S3Uri``.
            :param s3_upload_mode: ``CfnModelExplainabilityJobDefinition.S3OutputProperty.S3UploadMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-s3output.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "local_path": local_path,
                "s3_uri": s3_uri,
            }
            if s3_upload_mode is not None:
                self._values["s3_upload_mode"] = s3_upload_mode

        @builtins.property
        def local_path(self) -> builtins.str:
            '''``CfnModelExplainabilityJobDefinition.S3OutputProperty.LocalPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-s3output.html#cfn-sagemaker-modelexplainabilityjobdefinition-s3output-localpath
            '''
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_uri(self) -> builtins.str:
            '''``CfnModelExplainabilityJobDefinition.S3OutputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-s3output.html#cfn-sagemaker-modelexplainabilityjobdefinition-s3output-s3uri
            '''
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_upload_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.S3OutputProperty.S3UploadMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-s3output.html#cfn-sagemaker-modelexplainabilityjobdefinition-s3output-s3uploadmode
            '''
            result = self._values.get("s3_upload_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.StoppingConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"max_runtime_in_seconds": "maxRuntimeInSeconds"},
    )
    class StoppingConditionProperty:
        def __init__(self, *, max_runtime_in_seconds: jsii.Number) -> None:
            '''
            :param max_runtime_in_seconds: ``CfnModelExplainabilityJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-stoppingcondition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_runtime_in_seconds": max_runtime_in_seconds,
            }

        @builtins.property
        def max_runtime_in_seconds(self) -> jsii.Number:
            '''``CfnModelExplainabilityJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-stoppingcondition.html#cfn-sagemaker-modelexplainabilityjobdefinition-stoppingcondition-maxruntimeinseconds
            '''
            result = self._values.get("max_runtime_in_seconds")
            assert result is not None, "Required property 'max_runtime_in_seconds' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StoppingConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinition.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param security_group_ids: ``CfnModelExplainabilityJobDefinition.VpcConfigProperty.SecurityGroupIds``.
            :param subnets: ``CfnModelExplainabilityJobDefinition.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-vpcconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.VpcConfigProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-vpcconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''``CfnModelExplainabilityJobDefinition.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelexplainabilityjobdefinition-vpcconfig.html#cfn-sagemaker-modelexplainabilityjobdefinition-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelExplainabilityJobDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "job_resources": "jobResources",
        "model_explainability_app_specification": "modelExplainabilityAppSpecification",
        "model_explainability_job_input": "modelExplainabilityJobInput",
        "model_explainability_job_output_config": "modelExplainabilityJobOutputConfig",
        "role_arn": "roleArn",
        "job_definition_name": "jobDefinitionName",
        "model_explainability_baseline_config": "modelExplainabilityBaselineConfig",
        "network_config": "networkConfig",
        "stopping_condition": "stoppingCondition",
        "tags": "tags",
    },
)
class CfnModelExplainabilityJobDefinitionProps:
    def __init__(
        self,
        *,
        job_resources: typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty],
        model_explainability_app_specification: typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty],
        model_explainability_job_input: typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty],
        model_explainability_job_output_config: typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty],
        role_arn: builtins.str,
        job_definition_name: typing.Optional[builtins.str] = None,
        model_explainability_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty]] = None,
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.NetworkConfigProperty]] = None,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.StoppingConditionProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::ModelExplainabilityJobDefinition``.

        :param job_resources: ``AWS::SageMaker::ModelExplainabilityJobDefinition.JobResources``.
        :param model_explainability_app_specification: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityAppSpecification``.
        :param model_explainability_job_input: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobInput``.
        :param model_explainability_job_output_config: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobOutputConfig``.
        :param role_arn: ``AWS::SageMaker::ModelExplainabilityJobDefinition.RoleArn``.
        :param job_definition_name: ``AWS::SageMaker::ModelExplainabilityJobDefinition.JobDefinitionName``.
        :param model_explainability_baseline_config: ``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfig``.
        :param network_config: ``AWS::SageMaker::ModelExplainabilityJobDefinition.NetworkConfig``.
        :param stopping_condition: ``AWS::SageMaker::ModelExplainabilityJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::ModelExplainabilityJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "job_resources": job_resources,
            "model_explainability_app_specification": model_explainability_app_specification,
            "model_explainability_job_input": model_explainability_job_input,
            "model_explainability_job_output_config": model_explainability_job_output_config,
            "role_arn": role_arn,
        }
        if job_definition_name is not None:
            self._values["job_definition_name"] = job_definition_name
        if model_explainability_baseline_config is not None:
            self._values["model_explainability_baseline_config"] = model_explainability_baseline_config
        if network_config is not None:
            self._values["network_config"] = network_config
        if stopping_condition is not None:
            self._values["stopping_condition"] = stopping_condition
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.JobResources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-jobresources
        '''
        result = self._values.get("job_resources")
        assert result is not None, "Required property 'job_resources' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.MonitoringResourcesProperty], result)

    @builtins.property
    def model_explainability_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityAppSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification
        '''
        result = self._values.get("model_explainability_app_specification")
        assert result is not None, "Required property 'model_explainability_app_specification' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityAppSpecificationProperty], result)

    @builtins.property
    def model_explainability_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobInput``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput
        '''
        result = self._values.get("model_explainability_job_input")
        assert result is not None, "Required property 'model_explainability_job_input' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityJobInputProperty], result)

    @builtins.property
    def model_explainability_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityJobOutputConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjoboutputconfig
        '''
        result = self._values.get("model_explainability_job_output_config")
        assert result is not None, "Required property 'model_explainability_job_output_config' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.MonitoringOutputConfigProperty], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.JobDefinitionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-jobdefinitionname
        '''
        result = self._values.get("job_definition_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def model_explainability_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty]]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig
        '''
        result = self._values.get("model_explainability_baseline_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.ModelExplainabilityBaselineConfigProperty]], result)

    @builtins.property
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.NetworkConfigProperty]]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.NetworkConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig
        '''
        result = self._values.get("network_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.NetworkConfigProperty]], result)

    @builtins.property
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.StoppingConditionProperty]]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.StoppingCondition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-stoppingcondition
        '''
        result = self._values.get("stopping_condition")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelExplainabilityJobDefinition.StoppingConditionProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::ModelExplainabilityJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModelExplainabilityJobDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnModelPackageGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelPackageGroup",
):
    '''A CloudFormation ``AWS::SageMaker::ModelPackageGroup``.

    :cloudformationResource: AWS::SageMaker::ModelPackageGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        model_package_group_name: builtins.str,
        model_package_group_description: typing.Optional[builtins.str] = None,
        model_package_group_policy: typing.Any = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::ModelPackageGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param model_package_group_name: ``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupName``.
        :param model_package_group_description: ``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupDescription``.
        :param model_package_group_policy: ``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupPolicy``.
        :param tags: ``AWS::SageMaker::ModelPackageGroup.Tags``.
        '''
        props = CfnModelPackageGroupProps(
            model_package_group_name=model_package_group_name,
            model_package_group_description=model_package_group_description,
            model_package_group_policy=model_package_group_policy,
            tags=tags,
        )

        jsii.create(CfnModelPackageGroup, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrModelPackageGroupArn")
    def attr_model_package_group_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ModelPackageGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModelPackageGroupArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrModelPackageGroupStatus")
    def attr_model_package_group_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: ModelPackageGroupStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModelPackageGroupStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::ModelPackageGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelPackageGroupName")
    def model_package_group_name(self) -> builtins.str:
        '''``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupname
        '''
        return typing.cast(builtins.str, jsii.get(self, "modelPackageGroupName"))

    @model_package_group_name.setter
    def model_package_group_name(self, value: builtins.str) -> None:
        jsii.set(self, "modelPackageGroupName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelPackageGroupPolicy")
    def model_package_group_policy(self) -> typing.Any:
        '''``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupPolicy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegrouppolicy
        '''
        return typing.cast(typing.Any, jsii.get(self, "modelPackageGroupPolicy"))

    @model_package_group_policy.setter
    def model_package_group_policy(self, value: typing.Any) -> None:
        jsii.set(self, "modelPackageGroupPolicy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelPackageGroupDescription")
    def model_package_group_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupdescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelPackageGroupDescription"))

    @model_package_group_description.setter
    def model_package_group_description(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "modelPackageGroupDescription", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelPackageGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "model_package_group_name": "modelPackageGroupName",
        "model_package_group_description": "modelPackageGroupDescription",
        "model_package_group_policy": "modelPackageGroupPolicy",
        "tags": "tags",
    },
)
class CfnModelPackageGroupProps:
    def __init__(
        self,
        *,
        model_package_group_name: builtins.str,
        model_package_group_description: typing.Optional[builtins.str] = None,
        model_package_group_policy: typing.Any = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::ModelPackageGroup``.

        :param model_package_group_name: ``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupName``.
        :param model_package_group_description: ``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupDescription``.
        :param model_package_group_policy: ``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupPolicy``.
        :param tags: ``AWS::SageMaker::ModelPackageGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "model_package_group_name": model_package_group_name,
        }
        if model_package_group_description is not None:
            self._values["model_package_group_description"] = model_package_group_description
        if model_package_group_policy is not None:
            self._values["model_package_group_policy"] = model_package_group_policy
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def model_package_group_name(self) -> builtins.str:
        '''``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupname
        '''
        result = self._values.get("model_package_group_name")
        assert result is not None, "Required property 'model_package_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def model_package_group_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupdescription
        '''
        result = self._values.get("model_package_group_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def model_package_group_policy(self) -> typing.Any:
        '''``AWS::SageMaker::ModelPackageGroup.ModelPackageGroupPolicy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegrouppolicy
        '''
        result = self._values.get("model_package_group_policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::ModelPackageGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModelPackageGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelProps",
    jsii_struct_bases=[],
    name_mapping={
        "execution_role_arn": "executionRoleArn",
        "containers": "containers",
        "enable_network_isolation": "enableNetworkIsolation",
        "inference_execution_config": "inferenceExecutionConfig",
        "model_name": "modelName",
        "primary_container": "primaryContainer",
        "tags": "tags",
        "vpc_config": "vpcConfig",
    },
)
class CfnModelProps:
    def __init__(
        self,
        *,
        execution_role_arn: builtins.str,
        containers: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnModel.ContainerDefinitionProperty]]]] = None,
        enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        inference_execution_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.InferenceExecutionConfigProperty]] = None,
        model_name: typing.Optional[builtins.str] = None,
        primary_container: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.ContainerDefinitionProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.VpcConfigProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::Model``.

        :param execution_role_arn: ``AWS::SageMaker::Model.ExecutionRoleArn``.
        :param containers: ``AWS::SageMaker::Model.Containers``.
        :param enable_network_isolation: ``AWS::SageMaker::Model.EnableNetworkIsolation``.
        :param inference_execution_config: ``AWS::SageMaker::Model.InferenceExecutionConfig``.
        :param model_name: ``AWS::SageMaker::Model.ModelName``.
        :param primary_container: ``AWS::SageMaker::Model.PrimaryContainer``.
        :param tags: ``AWS::SageMaker::Model.Tags``.
        :param vpc_config: ``AWS::SageMaker::Model.VpcConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "execution_role_arn": execution_role_arn,
        }
        if containers is not None:
            self._values["containers"] = containers
        if enable_network_isolation is not None:
            self._values["enable_network_isolation"] = enable_network_isolation
        if inference_execution_config is not None:
            self._values["inference_execution_config"] = inference_execution_config
        if model_name is not None:
            self._values["model_name"] = model_name
        if primary_container is not None:
            self._values["primary_container"] = primary_container
        if tags is not None:
            self._values["tags"] = tags
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

    @builtins.property
    def execution_role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::Model.ExecutionRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        assert result is not None, "Required property 'execution_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def containers(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnModel.ContainerDefinitionProperty]]]]:
        '''``AWS::SageMaker::Model.Containers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-containers
        '''
        result = self._values.get("containers")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnModel.ContainerDefinitionProperty]]]], result)

    @builtins.property
    def enable_network_isolation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::SageMaker::Model.EnableNetworkIsolation``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-enablenetworkisolation
        '''
        result = self._values.get("enable_network_isolation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def inference_execution_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.InferenceExecutionConfigProperty]]:
        '''``AWS::SageMaker::Model.InferenceExecutionConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-inferenceexecutionconfig
        '''
        result = self._values.get("inference_execution_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.InferenceExecutionConfigProperty]], result)

    @builtins.property
    def model_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Model.ModelName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-modelname
        '''
        result = self._values.get("model_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary_container(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.ContainerDefinitionProperty]]:
        '''``AWS::SageMaker::Model.PrimaryContainer``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-primarycontainer
        '''
        result = self._values.get("primary_container")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.ContainerDefinitionProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::Model.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.VpcConfigProperty]]:
        '''``AWS::SageMaker::Model.VpcConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#cfn-sagemaker-model-vpcconfig
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModel.VpcConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnModelQualityJobDefinition(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition",
):
    '''A CloudFormation ``AWS::SageMaker::ModelQualityJobDefinition``.

    :cloudformationResource: AWS::SageMaker::ModelQualityJobDefinition
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        job_resources: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringResourcesProperty"],
        model_quality_app_specification: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty"],
        model_quality_job_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityJobInputProperty"],
        model_quality_job_output_config: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringOutputConfigProperty"],
        role_arn: builtins.str,
        job_definition_name: typing.Optional[builtins.str] = None,
        model_quality_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty"]] = None,
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.NetworkConfigProperty"]] = None,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.StoppingConditionProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::ModelQualityJobDefinition``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param job_resources: ``AWS::SageMaker::ModelQualityJobDefinition.JobResources``.
        :param model_quality_app_specification: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityAppSpecification``.
        :param model_quality_job_input: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobInput``.
        :param model_quality_job_output_config: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobOutputConfig``.
        :param role_arn: ``AWS::SageMaker::ModelQualityJobDefinition.RoleArn``.
        :param job_definition_name: ``AWS::SageMaker::ModelQualityJobDefinition.JobDefinitionName``.
        :param model_quality_baseline_config: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityBaselineConfig``.
        :param network_config: ``AWS::SageMaker::ModelQualityJobDefinition.NetworkConfig``.
        :param stopping_condition: ``AWS::SageMaker::ModelQualityJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::ModelQualityJobDefinition.Tags``.
        '''
        props = CfnModelQualityJobDefinitionProps(
            job_resources=job_resources,
            model_quality_app_specification=model_quality_app_specification,
            model_quality_job_input=model_quality_job_input,
            model_quality_job_output_config=model_quality_job_output_config,
            role_arn=role_arn,
            job_definition_name=job_definition_name,
            model_quality_baseline_config=model_quality_baseline_config,
            network_config=network_config,
            stopping_condition=stopping_condition,
            tags=tags,
        )

        jsii.create(CfnModelQualityJobDefinition, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrJobDefinitionArn")
    def attr_job_definition_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: JobDefinitionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrJobDefinitionArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::ModelQualityJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobResources")
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringResourcesProperty"]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.JobResources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-jobresources
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringResourcesProperty"], jsii.get(self, "jobResources"))

    @job_resources.setter
    def job_resources(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringResourcesProperty"],
    ) -> None:
        jsii.set(self, "jobResources", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelQualityAppSpecification")
    def model_quality_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty"]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityAppSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty"], jsii.get(self, "modelQualityAppSpecification"))

    @model_quality_app_specification.setter
    def model_quality_app_specification(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty"],
    ) -> None:
        jsii.set(self, "modelQualityAppSpecification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelQualityJobInput")
    def model_quality_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityJobInputProperty"]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobInput``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityJobInputProperty"], jsii.get(self, "modelQualityJobInput"))

    @model_quality_job_input.setter
    def model_quality_job_input(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityJobInputProperty"],
    ) -> None:
        jsii.set(self, "modelQualityJobInput", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelQualityJobOutputConfig")
    def model_quality_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringOutputConfigProperty"]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobOutputConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjoboutputconfig
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringOutputConfigProperty"], jsii.get(self, "modelQualityJobOutputConfig"))

    @model_quality_job_output_config.setter
    def model_quality_job_output_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringOutputConfigProperty"],
    ) -> None:
        jsii.set(self, "modelQualityJobOutputConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::ModelQualityJobDefinition.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="jobDefinitionName")
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.JobDefinitionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-jobdefinitionname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobDefinitionName"))

    @job_definition_name.setter
    def job_definition_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "jobDefinitionName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="modelQualityBaselineConfig")
    def model_quality_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty"]]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityBaselineConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty"]], jsii.get(self, "modelQualityBaselineConfig"))

    @model_quality_baseline_config.setter
    def model_quality_baseline_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty"]],
    ) -> None:
        jsii.set(self, "modelQualityBaselineConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="networkConfig")
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.NetworkConfigProperty"]]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.NetworkConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-networkconfig
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.NetworkConfigProperty"]], jsii.get(self, "networkConfig"))

    @network_config.setter
    def network_config(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.NetworkConfigProperty"]],
    ) -> None:
        jsii.set(self, "networkConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stoppingCondition")
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.StoppingConditionProperty"]]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.StoppingCondition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-stoppingcondition
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.StoppingConditionProperty"]], jsii.get(self, "stoppingCondition"))

    @stopping_condition.setter
    def stopping_condition(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.StoppingConditionProperty"]],
    ) -> None:
        jsii.set(self, "stoppingCondition", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.ClusterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_count": "instanceCount",
            "instance_type": "instanceType",
            "volume_size_in_gb": "volumeSizeInGb",
            "volume_kms_key_id": "volumeKmsKeyId",
        },
    )
    class ClusterConfigProperty:
        def __init__(
            self,
            *,
            instance_count: jsii.Number,
            instance_type: builtins.str,
            volume_size_in_gb: jsii.Number,
            volume_kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param instance_count: ``CfnModelQualityJobDefinition.ClusterConfigProperty.InstanceCount``.
            :param instance_type: ``CfnModelQualityJobDefinition.ClusterConfigProperty.InstanceType``.
            :param volume_size_in_gb: ``CfnModelQualityJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.
            :param volume_kms_key_id: ``CfnModelQualityJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "instance_count": instance_count,
                "instance_type": instance_type,
                "volume_size_in_gb": volume_size_in_gb,
            }
            if volume_kms_key_id is not None:
                self._values["volume_kms_key_id"] = volume_kms_key_id

        @builtins.property
        def instance_count(self) -> jsii.Number:
            '''``CfnModelQualityJobDefinition.ClusterConfigProperty.InstanceCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-instancecount
            '''
            result = self._values.get("instance_count")
            assert result is not None, "Required property 'instance_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''``CfnModelQualityJobDefinition.ClusterConfigProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def volume_size_in_gb(self) -> jsii.Number:
            '''``CfnModelQualityJobDefinition.ClusterConfigProperty.VolumeSizeInGB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-volumesizeingb
            '''
            result = self._values.get("volume_size_in_gb")
            assert result is not None, "Required property 'volume_size_in_gb' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.ClusterConfigProperty.VolumeKmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-clusterconfig.html#cfn-sagemaker-modelqualityjobdefinition-clusterconfig-volumekmskeyid
            '''
            result = self._values.get("volume_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClusterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.ConstraintsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class ConstraintsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            '''
            :param s3_uri: ``CfnModelQualityJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-constraintsresource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.ConstraintsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-constraintsresource.html#cfn-sagemaker-modelqualityjobdefinition-constraintsresource-s3uri
            '''
            result = self._values.get("s3_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConstraintsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.EndpointInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_name": "endpointName",
            "local_path": "localPath",
            "end_time_offset": "endTimeOffset",
            "inference_attribute": "inferenceAttribute",
            "probability_attribute": "probabilityAttribute",
            "probability_threshold_attribute": "probabilityThresholdAttribute",
            "s3_data_distribution_type": "s3DataDistributionType",
            "s3_input_mode": "s3InputMode",
            "start_time_offset": "startTimeOffset",
        },
    )
    class EndpointInputProperty:
        def __init__(
            self,
            *,
            endpoint_name: builtins.str,
            local_path: builtins.str,
            end_time_offset: typing.Optional[builtins.str] = None,
            inference_attribute: typing.Optional[builtins.str] = None,
            probability_attribute: typing.Optional[builtins.str] = None,
            probability_threshold_attribute: typing.Optional[jsii.Number] = None,
            s3_data_distribution_type: typing.Optional[builtins.str] = None,
            s3_input_mode: typing.Optional[builtins.str] = None,
            start_time_offset: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param endpoint_name: ``CfnModelQualityJobDefinition.EndpointInputProperty.EndpointName``.
            :param local_path: ``CfnModelQualityJobDefinition.EndpointInputProperty.LocalPath``.
            :param end_time_offset: ``CfnModelQualityJobDefinition.EndpointInputProperty.EndTimeOffset``.
            :param inference_attribute: ``CfnModelQualityJobDefinition.EndpointInputProperty.InferenceAttribute``.
            :param probability_attribute: ``CfnModelQualityJobDefinition.EndpointInputProperty.ProbabilityAttribute``.
            :param probability_threshold_attribute: ``CfnModelQualityJobDefinition.EndpointInputProperty.ProbabilityThresholdAttribute``.
            :param s3_data_distribution_type: ``CfnModelQualityJobDefinition.EndpointInputProperty.S3DataDistributionType``.
            :param s3_input_mode: ``CfnModelQualityJobDefinition.EndpointInputProperty.S3InputMode``.
            :param start_time_offset: ``CfnModelQualityJobDefinition.EndpointInputProperty.StartTimeOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_name": endpoint_name,
                "local_path": local_path,
            }
            if end_time_offset is not None:
                self._values["end_time_offset"] = end_time_offset
            if inference_attribute is not None:
                self._values["inference_attribute"] = inference_attribute
            if probability_attribute is not None:
                self._values["probability_attribute"] = probability_attribute
            if probability_threshold_attribute is not None:
                self._values["probability_threshold_attribute"] = probability_threshold_attribute
            if s3_data_distribution_type is not None:
                self._values["s3_data_distribution_type"] = s3_data_distribution_type
            if s3_input_mode is not None:
                self._values["s3_input_mode"] = s3_input_mode
            if start_time_offset is not None:
                self._values["start_time_offset"] = start_time_offset

        @builtins.property
        def endpoint_name(self) -> builtins.str:
            '''``CfnModelQualityJobDefinition.EndpointInputProperty.EndpointName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-endpointname
            '''
            result = self._values.get("endpoint_name")
            assert result is not None, "Required property 'endpoint_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def local_path(self) -> builtins.str:
            '''``CfnModelQualityJobDefinition.EndpointInputProperty.LocalPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-localpath
            '''
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def end_time_offset(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.EndpointInputProperty.EndTimeOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-endtimeoffset
            '''
            result = self._values.get("end_time_offset")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inference_attribute(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.EndpointInputProperty.InferenceAttribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-inferenceattribute
            '''
            result = self._values.get("inference_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def probability_attribute(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.EndpointInputProperty.ProbabilityAttribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-probabilityattribute
            '''
            result = self._values.get("probability_attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def probability_threshold_attribute(self) -> typing.Optional[jsii.Number]:
            '''``CfnModelQualityJobDefinition.EndpointInputProperty.ProbabilityThresholdAttribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-probabilitythresholdattribute
            '''
            result = self._values.get("probability_threshold_attribute")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def s3_data_distribution_type(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.EndpointInputProperty.S3DataDistributionType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-s3datadistributiontype
            '''
            result = self._values.get("s3_data_distribution_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_input_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.EndpointInputProperty.S3InputMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-s3inputmode
            '''
            result = self._values.get("s3_input_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def start_time_offset(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.EndpointInputProperty.StartTimeOffset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-endpointinput.html#cfn-sagemaker-modelqualityjobdefinition-endpointinput-starttimeoffset
            '''
            result = self._values.get("start_time_offset")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.EnvironmentProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class EnvironmentProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-environment.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_uri": "imageUri",
            "problem_type": "problemType",
            "container_arguments": "containerArguments",
            "container_entrypoint": "containerEntrypoint",
            "environment": "environment",
            "post_analytics_processor_source_uri": "postAnalyticsProcessorSourceUri",
            "record_preprocessor_source_uri": "recordPreprocessorSourceUri",
        },
    )
    class ModelQualityAppSpecificationProperty:
        def __init__(
            self,
            *,
            image_uri: builtins.str,
            problem_type: builtins.str,
            container_arguments: typing.Optional[typing.Sequence[builtins.str]] = None,
            container_entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
            environment: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.EnvironmentProperty"]] = None,
            post_analytics_processor_source_uri: typing.Optional[builtins.str] = None,
            record_preprocessor_source_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param image_uri: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ImageUri``.
            :param problem_type: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ProblemType``.
            :param container_arguments: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ContainerArguments``.
            :param container_entrypoint: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ContainerEntrypoint``.
            :param environment: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.Environment``.
            :param post_analytics_processor_source_uri: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.PostAnalyticsProcessorSourceUri``.
            :param record_preprocessor_source_uri: ``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.RecordPreprocessorSourceUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "image_uri": image_uri,
                "problem_type": problem_type,
            }
            if container_arguments is not None:
                self._values["container_arguments"] = container_arguments
            if container_entrypoint is not None:
                self._values["container_entrypoint"] = container_entrypoint
            if environment is not None:
                self._values["environment"] = environment
            if post_analytics_processor_source_uri is not None:
                self._values["post_analytics_processor_source_uri"] = post_analytics_processor_source_uri
            if record_preprocessor_source_uri is not None:
                self._values["record_preprocessor_source_uri"] = record_preprocessor_source_uri

        @builtins.property
        def image_uri(self) -> builtins.str:
            '''``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ImageUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-imageuri
            '''
            result = self._values.get("image_uri")
            assert result is not None, "Required property 'image_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def problem_type(self) -> builtins.str:
            '''``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ProblemType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-problemtype
            '''
            result = self._values.get("problem_type")
            assert result is not None, "Required property 'problem_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def container_arguments(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ContainerArguments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-containerarguments
            '''
            result = self._values.get("container_arguments")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def container_entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.ContainerEntrypoint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-containerentrypoint
            '''
            result = self._values.get("container_entrypoint")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.EnvironmentProperty"]]:
            '''``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.Environment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-environment
            '''
            result = self._values.get("environment")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.EnvironmentProperty"]], result)

        @builtins.property
        def post_analytics_processor_source_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.PostAnalyticsProcessorSourceUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-postanalyticsprocessorsourceuri
            '''
            result = self._values.get("post_analytics_processor_source_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def record_preprocessor_source_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty.RecordPreprocessorSourceUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityappspecification.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification-recordpreprocessorsourceuri
            '''
            result = self._values.get("record_preprocessor_source_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelQualityAppSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "baselining_job_name": "baseliningJobName",
            "constraints_resource": "constraintsResource",
        },
    )
    class ModelQualityBaselineConfigProperty:
        def __init__(
            self,
            *,
            baselining_job_name: typing.Optional[builtins.str] = None,
            constraints_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ConstraintsResourceProperty"]] = None,
        ) -> None:
            '''
            :param baselining_job_name: ``CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty.BaseliningJobName``.
            :param constraints_resource: ``CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty.ConstraintsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if baselining_job_name is not None:
                self._values["baselining_job_name"] = baselining_job_name
            if constraints_resource is not None:
                self._values["constraints_resource"] = constraints_resource

        @builtins.property
        def baselining_job_name(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty.BaseliningJobName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig.html#cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig-baseliningjobname
            '''
            result = self._values.get("baselining_job_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def constraints_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ConstraintsResourceProperty"]]:
            '''``CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty.ConstraintsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig.html#cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig-constraintsresource
            '''
            result = self._values.get("constraints_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ConstraintsResourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelQualityBaselineConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.ModelQualityJobInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_input": "endpointInput",
            "ground_truth_s3_input": "groundTruthS3Input",
        },
    )
    class ModelQualityJobInputProperty:
        def __init__(
            self,
            *,
            endpoint_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.EndpointInputProperty"],
            ground_truth_s3_input: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty"],
        ) -> None:
            '''
            :param endpoint_input: ``CfnModelQualityJobDefinition.ModelQualityJobInputProperty.EndpointInput``.
            :param ground_truth_s3_input: ``CfnModelQualityJobDefinition.ModelQualityJobInputProperty.GroundTruthS3Input``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_input": endpoint_input,
                "ground_truth_s3_input": ground_truth_s3_input,
            }

        @builtins.property
        def endpoint_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.EndpointInputProperty"]:
            '''``CfnModelQualityJobDefinition.ModelQualityJobInputProperty.EndpointInput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput-endpointinput
            '''
            result = self._values.get("endpoint_input")
            assert result is not None, "Required property 'endpoint_input' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.EndpointInputProperty"], result)

        @builtins.property
        def ground_truth_s3_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty"]:
            '''``CfnModelQualityJobDefinition.ModelQualityJobInputProperty.GroundTruthS3Input``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-modelqualityjobinput.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput-groundtruths3input
            '''
            result = self._values.get("ground_truth_s3_input")
            assert result is not None, "Required property 'ground_truth_s3_input' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelQualityJobInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class MonitoringGroundTruthS3InputProperty:
        def __init__(self, *, s3_uri: builtins.str) -> None:
            '''
            :param s3_uri: ``CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "s3_uri": s3_uri,
            }

        @builtins.property
        def s3_uri(self) -> builtins.str:
            '''``CfnModelQualityJobDefinition.MonitoringGroundTruthS3InputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input.html#cfn-sagemaker-modelqualityjobdefinition-monitoringgroundtruths3input-s3uri
            '''
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringGroundTruthS3InputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.MonitoringOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "monitoring_outputs": "monitoringOutputs",
            "kms_key_id": "kmsKeyId",
        },
    )
    class MonitoringOutputConfigProperty:
        def __init__(
            self,
            *,
            monitoring_outputs: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringOutputProperty"]]],
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param monitoring_outputs: ``CfnModelQualityJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.
            :param kms_key_id: ``CfnModelQualityJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutputconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "monitoring_outputs": monitoring_outputs,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def monitoring_outputs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringOutputProperty"]]]:
            '''``CfnModelQualityJobDefinition.MonitoringOutputConfigProperty.MonitoringOutputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelqualityjobdefinition-monitoringoutputconfig-monitoringoutputs
            '''
            result = self._values.get("monitoring_outputs")
            assert result is not None, "Required property 'monitoring_outputs' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.MonitoringOutputProperty"]]], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.MonitoringOutputConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutputconfig.html#cfn-sagemaker-modelqualityjobdefinition-monitoringoutputconfig-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.MonitoringOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_output": "s3Output"},
    )
    class MonitoringOutputProperty:
        def __init__(
            self,
            *,
            s3_output: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.S3OutputProperty"],
        ) -> None:
            '''
            :param s3_output: ``CfnModelQualityJobDefinition.MonitoringOutputProperty.S3Output``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutput.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "s3_output": s3_output,
            }

        @builtins.property
        def s3_output(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.S3OutputProperty"]:
            '''``CfnModelQualityJobDefinition.MonitoringOutputProperty.S3Output``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringoutput.html#cfn-sagemaker-modelqualityjobdefinition-monitoringoutput-s3output
            '''
            result = self._values.get("s3_output")
            assert result is not None, "Required property 's3_output' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.S3OutputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.MonitoringResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_config": "clusterConfig"},
    )
    class MonitoringResourcesProperty:
        def __init__(
            self,
            *,
            cluster_config: typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ClusterConfigProperty"],
        ) -> None:
            '''
            :param cluster_config: ``CfnModelQualityJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringresources.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cluster_config": cluster_config,
            }

        @builtins.property
        def cluster_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ClusterConfigProperty"]:
            '''``CfnModelQualityJobDefinition.MonitoringResourcesProperty.ClusterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-monitoringresources.html#cfn-sagemaker-modelqualityjobdefinition-monitoringresources-clusterconfig
            '''
            result = self._values.get("cluster_config")
            assert result is not None, "Required property 'cluster_config' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.ClusterConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.NetworkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_inter_container_traffic_encryption": "enableInterContainerTrafficEncryption",
            "enable_network_isolation": "enableNetworkIsolation",
            "vpc_config": "vpcConfig",
        },
    )
    class NetworkConfigProperty:
        def __init__(
            self,
            *,
            enable_inter_container_traffic_encryption: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.VpcConfigProperty"]] = None,
        ) -> None:
            '''
            :param enable_inter_container_traffic_encryption: ``CfnModelQualityJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.
            :param enable_network_isolation: ``CfnModelQualityJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.
            :param vpc_config: ``CfnModelQualityJobDefinition.NetworkConfigProperty.VpcConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-networkconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if enable_inter_container_traffic_encryption is not None:
                self._values["enable_inter_container_traffic_encryption"] = enable_inter_container_traffic_encryption
            if enable_network_isolation is not None:
                self._values["enable_network_isolation"] = enable_network_isolation
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def enable_inter_container_traffic_encryption(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnModelQualityJobDefinition.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-networkconfig.html#cfn-sagemaker-modelqualityjobdefinition-networkconfig-enableintercontainertrafficencryption
            '''
            result = self._values.get("enable_inter_container_traffic_encryption")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def enable_network_isolation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnModelQualityJobDefinition.NetworkConfigProperty.EnableNetworkIsolation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-networkconfig.html#cfn-sagemaker-modelqualityjobdefinition-networkconfig-enablenetworkisolation
            '''
            result = self._values.get("enable_network_isolation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.VpcConfigProperty"]]:
            '''``CfnModelQualityJobDefinition.NetworkConfigProperty.VpcConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-networkconfig.html#cfn-sagemaker-modelqualityjobdefinition-networkconfig-vpcconfig
            '''
            result = self._values.get("vpc_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnModelQualityJobDefinition.VpcConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.S3OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "local_path": "localPath",
            "s3_uri": "s3Uri",
            "s3_upload_mode": "s3UploadMode",
        },
    )
    class S3OutputProperty:
        def __init__(
            self,
            *,
            local_path: builtins.str,
            s3_uri: builtins.str,
            s3_upload_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param local_path: ``CfnModelQualityJobDefinition.S3OutputProperty.LocalPath``.
            :param s3_uri: ``CfnModelQualityJobDefinition.S3OutputProperty.S3Uri``.
            :param s3_upload_mode: ``CfnModelQualityJobDefinition.S3OutputProperty.S3UploadMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-s3output.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "local_path": local_path,
                "s3_uri": s3_uri,
            }
            if s3_upload_mode is not None:
                self._values["s3_upload_mode"] = s3_upload_mode

        @builtins.property
        def local_path(self) -> builtins.str:
            '''``CfnModelQualityJobDefinition.S3OutputProperty.LocalPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-s3output.html#cfn-sagemaker-modelqualityjobdefinition-s3output-localpath
            '''
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_uri(self) -> builtins.str:
            '''``CfnModelQualityJobDefinition.S3OutputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-s3output.html#cfn-sagemaker-modelqualityjobdefinition-s3output-s3uri
            '''
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_upload_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnModelQualityJobDefinition.S3OutputProperty.S3UploadMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-s3output.html#cfn-sagemaker-modelqualityjobdefinition-s3output-s3uploadmode
            '''
            result = self._values.get("s3_upload_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.StoppingConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"max_runtime_in_seconds": "maxRuntimeInSeconds"},
    )
    class StoppingConditionProperty:
        def __init__(self, *, max_runtime_in_seconds: jsii.Number) -> None:
            '''
            :param max_runtime_in_seconds: ``CfnModelQualityJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-stoppingcondition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_runtime_in_seconds": max_runtime_in_seconds,
            }

        @builtins.property
        def max_runtime_in_seconds(self) -> jsii.Number:
            '''``CfnModelQualityJobDefinition.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-stoppingcondition.html#cfn-sagemaker-modelqualityjobdefinition-stoppingcondition-maxruntimeinseconds
            '''
            result = self._values.get("max_runtime_in_seconds")
            assert result is not None, "Required property 'max_runtime_in_seconds' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StoppingConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinition.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param security_group_ids: ``CfnModelQualityJobDefinition.VpcConfigProperty.SecurityGroupIds``.
            :param subnets: ``CfnModelQualityJobDefinition.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-vpcconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''``CfnModelQualityJobDefinition.VpcConfigProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-vpcconfig.html#cfn-sagemaker-modelqualityjobdefinition-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''``CfnModelQualityJobDefinition.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-modelqualityjobdefinition-vpcconfig.html#cfn-sagemaker-modelqualityjobdefinition-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnModelQualityJobDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "job_resources": "jobResources",
        "model_quality_app_specification": "modelQualityAppSpecification",
        "model_quality_job_input": "modelQualityJobInput",
        "model_quality_job_output_config": "modelQualityJobOutputConfig",
        "role_arn": "roleArn",
        "job_definition_name": "jobDefinitionName",
        "model_quality_baseline_config": "modelQualityBaselineConfig",
        "network_config": "networkConfig",
        "stopping_condition": "stoppingCondition",
        "tags": "tags",
    },
)
class CfnModelQualityJobDefinitionProps:
    def __init__(
        self,
        *,
        job_resources: typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.MonitoringResourcesProperty],
        model_quality_app_specification: typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty],
        model_quality_job_input: typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityJobInputProperty],
        model_quality_job_output_config: typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.MonitoringOutputConfigProperty],
        role_arn: builtins.str,
        job_definition_name: typing.Optional[builtins.str] = None,
        model_quality_baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty]] = None,
        network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.NetworkConfigProperty]] = None,
        stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.StoppingConditionProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::ModelQualityJobDefinition``.

        :param job_resources: ``AWS::SageMaker::ModelQualityJobDefinition.JobResources``.
        :param model_quality_app_specification: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityAppSpecification``.
        :param model_quality_job_input: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobInput``.
        :param model_quality_job_output_config: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobOutputConfig``.
        :param role_arn: ``AWS::SageMaker::ModelQualityJobDefinition.RoleArn``.
        :param job_definition_name: ``AWS::SageMaker::ModelQualityJobDefinition.JobDefinitionName``.
        :param model_quality_baseline_config: ``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityBaselineConfig``.
        :param network_config: ``AWS::SageMaker::ModelQualityJobDefinition.NetworkConfig``.
        :param stopping_condition: ``AWS::SageMaker::ModelQualityJobDefinition.StoppingCondition``.
        :param tags: ``AWS::SageMaker::ModelQualityJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "job_resources": job_resources,
            "model_quality_app_specification": model_quality_app_specification,
            "model_quality_job_input": model_quality_job_input,
            "model_quality_job_output_config": model_quality_job_output_config,
            "role_arn": role_arn,
        }
        if job_definition_name is not None:
            self._values["job_definition_name"] = job_definition_name
        if model_quality_baseline_config is not None:
            self._values["model_quality_baseline_config"] = model_quality_baseline_config
        if network_config is not None:
            self._values["network_config"] = network_config
        if stopping_condition is not None:
            self._values["stopping_condition"] = stopping_condition
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def job_resources(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.MonitoringResourcesProperty]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.JobResources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-jobresources
        '''
        result = self._values.get("job_resources")
        assert result is not None, "Required property 'job_resources' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.MonitoringResourcesProperty], result)

    @builtins.property
    def model_quality_app_specification(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityAppSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityappspecification
        '''
        result = self._values.get("model_quality_app_specification")
        assert result is not None, "Required property 'model_quality_app_specification' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityAppSpecificationProperty], result)

    @builtins.property
    def model_quality_job_input(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityJobInputProperty]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobInput``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjobinput
        '''
        result = self._values.get("model_quality_job_input")
        assert result is not None, "Required property 'model_quality_job_input' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityJobInputProperty], result)

    @builtins.property
    def model_quality_job_output_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.MonitoringOutputConfigProperty]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityJobOutputConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualityjoboutputconfig
        '''
        result = self._values.get("model_quality_job_output_config")
        assert result is not None, "Required property 'model_quality_job_output_config' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.MonitoringOutputConfigProperty], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::ModelQualityJobDefinition.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def job_definition_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.JobDefinitionName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-jobdefinitionname
        '''
        result = self._values.get("job_definition_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def model_quality_baseline_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty]]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.ModelQualityBaselineConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-modelqualitybaselineconfig
        '''
        result = self._values.get("model_quality_baseline_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.ModelQualityBaselineConfigProperty]], result)

    @builtins.property
    def network_config(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.NetworkConfigProperty]]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.NetworkConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-networkconfig
        '''
        result = self._values.get("network_config")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.NetworkConfigProperty]], result)

    @builtins.property
    def stopping_condition(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.StoppingConditionProperty]]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.StoppingCondition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-stoppingcondition
        '''
        result = self._values.get("stopping_condition")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnModelQualityJobDefinition.StoppingConditionProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::ModelQualityJobDefinition.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelqualityjobdefinition.html#cfn-sagemaker-modelqualityjobdefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModelQualityJobDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnMonitoringSchedule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule",
):
    '''A CloudFormation ``AWS::SageMaker::MonitoringSchedule``.

    :cloudformationResource: AWS::SageMaker::MonitoringSchedule
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        monitoring_schedule_config: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringScheduleConfigProperty"],
        monitoring_schedule_name: builtins.str,
        endpoint_name: typing.Optional[builtins.str] = None,
        failure_reason: typing.Optional[builtins.str] = None,
        last_monitoring_execution_summary: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringExecutionSummaryProperty"]] = None,
        monitoring_schedule_status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::MonitoringSchedule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param monitoring_schedule_config: ``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleConfig``.
        :param monitoring_schedule_name: ``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleName``.
        :param endpoint_name: ``AWS::SageMaker::MonitoringSchedule.EndpointName``.
        :param failure_reason: ``AWS::SageMaker::MonitoringSchedule.FailureReason``.
        :param last_monitoring_execution_summary: ``AWS::SageMaker::MonitoringSchedule.LastMonitoringExecutionSummary``.
        :param monitoring_schedule_status: ``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleStatus``.
        :param tags: ``AWS::SageMaker::MonitoringSchedule.Tags``.
        '''
        props = CfnMonitoringScheduleProps(
            monitoring_schedule_config=monitoring_schedule_config,
            monitoring_schedule_name=monitoring_schedule_name,
            endpoint_name=endpoint_name,
            failure_reason=failure_reason,
            last_monitoring_execution_summary=last_monitoring_execution_summary,
            monitoring_schedule_status=monitoring_schedule_status,
            tags=tags,
        )

        jsii.create(CfnMonitoringSchedule, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrMonitoringScheduleArn")
    def attr_monitoring_schedule_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: MonitoringScheduleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMonitoringScheduleArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::MonitoringSchedule.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="monitoringScheduleConfig")
    def monitoring_schedule_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringScheduleConfigProperty"]:
        '''``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringScheduleConfigProperty"], jsii.get(self, "monitoringScheduleConfig"))

    @monitoring_schedule_config.setter
    def monitoring_schedule_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringScheduleConfigProperty"],
    ) -> None:
        jsii.set(self, "monitoringScheduleConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="monitoringScheduleName")
    def monitoring_schedule_name(self) -> builtins.str:
        '''``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringschedulename
        '''
        return typing.cast(builtins.str, jsii.get(self, "monitoringScheduleName"))

    @monitoring_schedule_name.setter
    def monitoring_schedule_name(self, value: builtins.str) -> None:
        jsii.set(self, "monitoringScheduleName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="endpointName")
    def endpoint_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::MonitoringSchedule.EndpointName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-endpointname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointName"))

    @endpoint_name.setter
    def endpoint_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "endpointName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="failureReason")
    def failure_reason(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::MonitoringSchedule.FailureReason``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-failurereason
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "failureReason"))

    @failure_reason.setter
    def failure_reason(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "failureReason", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lastMonitoringExecutionSummary")
    def last_monitoring_execution_summary(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringExecutionSummaryProperty"]]:
        '''``AWS::SageMaker::MonitoringSchedule.LastMonitoringExecutionSummary``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-lastmonitoringexecutionsummary
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringExecutionSummaryProperty"]], jsii.get(self, "lastMonitoringExecutionSummary"))

    @last_monitoring_execution_summary.setter
    def last_monitoring_execution_summary(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringExecutionSummaryProperty"]],
    ) -> None:
        jsii.set(self, "lastMonitoringExecutionSummary", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="monitoringScheduleStatus")
    def monitoring_schedule_status(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleStatus``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringschedulestatus
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "monitoringScheduleStatus"))

    @monitoring_schedule_status.setter
    def monitoring_schedule_status(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "monitoringScheduleStatus", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.BaselineConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "constraints_resource": "constraintsResource",
            "statistics_resource": "statisticsResource",
        },
    )
    class BaselineConfigProperty:
        def __init__(
            self,
            *,
            constraints_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ConstraintsResourceProperty"]] = None,
            statistics_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.StatisticsResourceProperty"]] = None,
        ) -> None:
            '''
            :param constraints_resource: ``CfnMonitoringSchedule.BaselineConfigProperty.ConstraintsResource``.
            :param statistics_resource: ``CfnMonitoringSchedule.BaselineConfigProperty.StatisticsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-baselineconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if constraints_resource is not None:
                self._values["constraints_resource"] = constraints_resource
            if statistics_resource is not None:
                self._values["statistics_resource"] = statistics_resource

        @builtins.property
        def constraints_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ConstraintsResourceProperty"]]:
            '''``CfnMonitoringSchedule.BaselineConfigProperty.ConstraintsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-baselineconfig.html#cfn-sagemaker-monitoringschedule-baselineconfig-constraintsresource
            '''
            result = self._values.get("constraints_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ConstraintsResourceProperty"]], result)

        @builtins.property
        def statistics_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.StatisticsResourceProperty"]]:
            '''``CfnMonitoringSchedule.BaselineConfigProperty.StatisticsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-baselineconfig.html#cfn-sagemaker-monitoringschedule-baselineconfig-statisticsresource
            '''
            result = self._values.get("statistics_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.StatisticsResourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BaselineConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.ClusterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_count": "instanceCount",
            "instance_type": "instanceType",
            "volume_size_in_gb": "volumeSizeInGb",
            "volume_kms_key_id": "volumeKmsKeyId",
        },
    )
    class ClusterConfigProperty:
        def __init__(
            self,
            *,
            instance_count: jsii.Number,
            instance_type: builtins.str,
            volume_size_in_gb: jsii.Number,
            volume_kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param instance_count: ``CfnMonitoringSchedule.ClusterConfigProperty.InstanceCount``.
            :param instance_type: ``CfnMonitoringSchedule.ClusterConfigProperty.InstanceType``.
            :param volume_size_in_gb: ``CfnMonitoringSchedule.ClusterConfigProperty.VolumeSizeInGB``.
            :param volume_kms_key_id: ``CfnMonitoringSchedule.ClusterConfigProperty.VolumeKmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "instance_count": instance_count,
                "instance_type": instance_type,
                "volume_size_in_gb": volume_size_in_gb,
            }
            if volume_kms_key_id is not None:
                self._values["volume_kms_key_id"] = volume_kms_key_id

        @builtins.property
        def instance_count(self) -> jsii.Number:
            '''``CfnMonitoringSchedule.ClusterConfigProperty.InstanceCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html#cfn-sagemaker-monitoringschedule-clusterconfig-instancecount
            '''
            result = self._values.get("instance_count")
            assert result is not None, "Required property 'instance_count' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''``CfnMonitoringSchedule.ClusterConfigProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html#cfn-sagemaker-monitoringschedule-clusterconfig-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def volume_size_in_gb(self) -> jsii.Number:
            '''``CfnMonitoringSchedule.ClusterConfigProperty.VolumeSizeInGB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html#cfn-sagemaker-monitoringschedule-clusterconfig-volumesizeingb
            '''
            result = self._values.get("volume_size_in_gb")
            assert result is not None, "Required property 'volume_size_in_gb' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def volume_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.ClusterConfigProperty.VolumeKmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-clusterconfig.html#cfn-sagemaker-monitoringschedule-clusterconfig-volumekmskeyid
            '''
            result = self._values.get("volume_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClusterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.ConstraintsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class ConstraintsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            '''
            :param s3_uri: ``CfnMonitoringSchedule.ConstraintsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-constraintsresource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.ConstraintsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-constraintsresource.html#cfn-sagemaker-monitoringschedule-constraintsresource-s3uri
            '''
            result = self._values.get("s3_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConstraintsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.EndpointInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_name": "endpointName",
            "local_path": "localPath",
            "s3_data_distribution_type": "s3DataDistributionType",
            "s3_input_mode": "s3InputMode",
        },
    )
    class EndpointInputProperty:
        def __init__(
            self,
            *,
            endpoint_name: builtins.str,
            local_path: builtins.str,
            s3_data_distribution_type: typing.Optional[builtins.str] = None,
            s3_input_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param endpoint_name: ``CfnMonitoringSchedule.EndpointInputProperty.EndpointName``.
            :param local_path: ``CfnMonitoringSchedule.EndpointInputProperty.LocalPath``.
            :param s3_data_distribution_type: ``CfnMonitoringSchedule.EndpointInputProperty.S3DataDistributionType``.
            :param s3_input_mode: ``CfnMonitoringSchedule.EndpointInputProperty.S3InputMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_name": endpoint_name,
                "local_path": local_path,
            }
            if s3_data_distribution_type is not None:
                self._values["s3_data_distribution_type"] = s3_data_distribution_type
            if s3_input_mode is not None:
                self._values["s3_input_mode"] = s3_input_mode

        @builtins.property
        def endpoint_name(self) -> builtins.str:
            '''``CfnMonitoringSchedule.EndpointInputProperty.EndpointName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html#cfn-sagemaker-monitoringschedule-endpointinput-endpointname
            '''
            result = self._values.get("endpoint_name")
            assert result is not None, "Required property 'endpoint_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def local_path(self) -> builtins.str:
            '''``CfnMonitoringSchedule.EndpointInputProperty.LocalPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html#cfn-sagemaker-monitoringschedule-endpointinput-localpath
            '''
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_data_distribution_type(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.EndpointInputProperty.S3DataDistributionType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html#cfn-sagemaker-monitoringschedule-endpointinput-s3datadistributiontype
            '''
            result = self._values.get("s3_data_distribution_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_input_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.EndpointInputProperty.S3InputMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-endpointinput.html#cfn-sagemaker-monitoringschedule-endpointinput-s3inputmode
            '''
            result = self._values.get("s3_input_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.EnvironmentProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class EnvironmentProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-environment.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringAppSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_uri": "imageUri",
            "container_arguments": "containerArguments",
            "container_entrypoint": "containerEntrypoint",
            "post_analytics_processor_source_uri": "postAnalyticsProcessorSourceUri",
            "record_preprocessor_source_uri": "recordPreprocessorSourceUri",
        },
    )
    class MonitoringAppSpecificationProperty:
        def __init__(
            self,
            *,
            image_uri: builtins.str,
            container_arguments: typing.Optional[typing.Sequence[builtins.str]] = None,
            container_entrypoint: typing.Optional[typing.Sequence[builtins.str]] = None,
            post_analytics_processor_source_uri: typing.Optional[builtins.str] = None,
            record_preprocessor_source_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param image_uri: ``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.ImageUri``.
            :param container_arguments: ``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.ContainerArguments``.
            :param container_entrypoint: ``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.ContainerEntrypoint``.
            :param post_analytics_processor_source_uri: ``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.PostAnalyticsProcessorSourceUri``.
            :param record_preprocessor_source_uri: ``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.RecordPreprocessorSourceUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "image_uri": image_uri,
            }
            if container_arguments is not None:
                self._values["container_arguments"] = container_arguments
            if container_entrypoint is not None:
                self._values["container_entrypoint"] = container_entrypoint
            if post_analytics_processor_source_uri is not None:
                self._values["post_analytics_processor_source_uri"] = post_analytics_processor_source_uri
            if record_preprocessor_source_uri is not None:
                self._values["record_preprocessor_source_uri"] = record_preprocessor_source_uri

        @builtins.property
        def image_uri(self) -> builtins.str:
            '''``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.ImageUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html#cfn-sagemaker-monitoringschedule-monitoringappspecification-imageuri
            '''
            result = self._values.get("image_uri")
            assert result is not None, "Required property 'image_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def container_arguments(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.ContainerArguments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html#cfn-sagemaker-monitoringschedule-monitoringappspecification-containerarguments
            '''
            result = self._values.get("container_arguments")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def container_entrypoint(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.ContainerEntrypoint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html#cfn-sagemaker-monitoringschedule-monitoringappspecification-containerentrypoint
            '''
            result = self._values.get("container_entrypoint")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def post_analytics_processor_source_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.PostAnalyticsProcessorSourceUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html#cfn-sagemaker-monitoringschedule-monitoringappspecification-postanalyticsprocessorsourceuri
            '''
            result = self._values.get("post_analytics_processor_source_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def record_preprocessor_source_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.MonitoringAppSpecificationProperty.RecordPreprocessorSourceUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringappspecification.html#cfn-sagemaker-monitoringschedule-monitoringappspecification-recordpreprocessorsourceuri
            '''
            result = self._values.get("record_preprocessor_source_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringAppSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringExecutionSummaryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "creation_time": "creationTime",
            "last_modified_time": "lastModifiedTime",
            "monitoring_execution_status": "monitoringExecutionStatus",
            "monitoring_schedule_name": "monitoringScheduleName",
            "scheduled_time": "scheduledTime",
            "endpoint_name": "endpointName",
            "failure_reason": "failureReason",
            "processing_job_arn": "processingJobArn",
        },
    )
    class MonitoringExecutionSummaryProperty:
        def __init__(
            self,
            *,
            creation_time: builtins.str,
            last_modified_time: builtins.str,
            monitoring_execution_status: builtins.str,
            monitoring_schedule_name: builtins.str,
            scheduled_time: builtins.str,
            endpoint_name: typing.Optional[builtins.str] = None,
            failure_reason: typing.Optional[builtins.str] = None,
            processing_job_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param creation_time: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.CreationTime``.
            :param last_modified_time: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.LastModifiedTime``.
            :param monitoring_execution_status: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.MonitoringExecutionStatus``.
            :param monitoring_schedule_name: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.MonitoringScheduleName``.
            :param scheduled_time: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.ScheduledTime``.
            :param endpoint_name: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.EndpointName``.
            :param failure_reason: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.FailureReason``.
            :param processing_job_arn: ``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.ProcessingJobArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "creation_time": creation_time,
                "last_modified_time": last_modified_time,
                "monitoring_execution_status": monitoring_execution_status,
                "monitoring_schedule_name": monitoring_schedule_name,
                "scheduled_time": scheduled_time,
            }
            if endpoint_name is not None:
                self._values["endpoint_name"] = endpoint_name
            if failure_reason is not None:
                self._values["failure_reason"] = failure_reason
            if processing_job_arn is not None:
                self._values["processing_job_arn"] = processing_job_arn

        @builtins.property
        def creation_time(self) -> builtins.str:
            '''``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.CreationTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-creationtime
            '''
            result = self._values.get("creation_time")
            assert result is not None, "Required property 'creation_time' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def last_modified_time(self) -> builtins.str:
            '''``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.LastModifiedTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-lastmodifiedtime
            '''
            result = self._values.get("last_modified_time")
            assert result is not None, "Required property 'last_modified_time' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def monitoring_execution_status(self) -> builtins.str:
            '''``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.MonitoringExecutionStatus``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-monitoringexecutionstatus
            '''
            result = self._values.get("monitoring_execution_status")
            assert result is not None, "Required property 'monitoring_execution_status' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def monitoring_schedule_name(self) -> builtins.str:
            '''``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.MonitoringScheduleName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-monitoringschedulename
            '''
            result = self._values.get("monitoring_schedule_name")
            assert result is not None, "Required property 'monitoring_schedule_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def scheduled_time(self) -> builtins.str:
            '''``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.ScheduledTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-scheduledtime
            '''
            result = self._values.get("scheduled_time")
            assert result is not None, "Required property 'scheduled_time' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def endpoint_name(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.EndpointName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-endpointname
            '''
            result = self._values.get("endpoint_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def failure_reason(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.FailureReason``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-failurereason
            '''
            result = self._values.get("failure_reason")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def processing_job_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.MonitoringExecutionSummaryProperty.ProcessingJobArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringexecutionsummary.html#cfn-sagemaker-monitoringschedule-monitoringexecutionsummary-processingjobarn
            '''
            result = self._values.get("processing_job_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringExecutionSummaryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringInputProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint_input": "endpointInput"},
    )
    class MonitoringInputProperty:
        def __init__(
            self,
            *,
            endpoint_input: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.EndpointInputProperty"],
        ) -> None:
            '''
            :param endpoint_input: ``CfnMonitoringSchedule.MonitoringInputProperty.EndpointInput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringinput.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_input": endpoint_input,
            }

        @builtins.property
        def endpoint_input(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.EndpointInputProperty"]:
            '''``CfnMonitoringSchedule.MonitoringInputProperty.EndpointInput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringinput.html#cfn-sagemaker-monitoringschedule-monitoringinput-endpointinput
            '''
            result = self._values.get("endpoint_input")
            assert result is not None, "Required property 'endpoint_input' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.EndpointInputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringJobDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "monitoring_app_specification": "monitoringAppSpecification",
            "monitoring_inputs": "monitoringInputs",
            "monitoring_output_config": "monitoringOutputConfig",
            "monitoring_resources": "monitoringResources",
            "role_arn": "roleArn",
            "baseline_config": "baselineConfig",
            "environment": "environment",
            "network_config": "networkConfig",
            "stopping_condition": "stoppingCondition",
        },
    )
    class MonitoringJobDefinitionProperty:
        def __init__(
            self,
            *,
            monitoring_app_specification: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringAppSpecificationProperty"],
            monitoring_inputs: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringInputProperty"]]],
            monitoring_output_config: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringOutputConfigProperty"],
            monitoring_resources: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringResourcesProperty"],
            role_arn: builtins.str,
            baseline_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.BaselineConfigProperty"]] = None,
            environment: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.EnvironmentProperty"]] = None,
            network_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.NetworkConfigProperty"]] = None,
            stopping_condition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.StoppingConditionProperty"]] = None,
        ) -> None:
            '''
            :param monitoring_app_specification: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringAppSpecification``.
            :param monitoring_inputs: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringInputs``.
            :param monitoring_output_config: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringOutputConfig``.
            :param monitoring_resources: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringResources``.
            :param role_arn: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.RoleArn``.
            :param baseline_config: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.BaselineConfig``.
            :param environment: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.Environment``.
            :param network_config: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.NetworkConfig``.
            :param stopping_condition: ``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.StoppingCondition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "monitoring_app_specification": monitoring_app_specification,
                "monitoring_inputs": monitoring_inputs,
                "monitoring_output_config": monitoring_output_config,
                "monitoring_resources": monitoring_resources,
                "role_arn": role_arn,
            }
            if baseline_config is not None:
                self._values["baseline_config"] = baseline_config
            if environment is not None:
                self._values["environment"] = environment
            if network_config is not None:
                self._values["network_config"] = network_config
            if stopping_condition is not None:
                self._values["stopping_condition"] = stopping_condition

        @builtins.property
        def monitoring_app_specification(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringAppSpecificationProperty"]:
            '''``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringAppSpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-monitoringappspecification
            '''
            result = self._values.get("monitoring_app_specification")
            assert result is not None, "Required property 'monitoring_app_specification' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringAppSpecificationProperty"], result)

        @builtins.property
        def monitoring_inputs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringInputProperty"]]]:
            '''``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringInputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-monitoringinputs
            '''
            result = self._values.get("monitoring_inputs")
            assert result is not None, "Required property 'monitoring_inputs' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringInputProperty"]]], result)

        @builtins.property
        def monitoring_output_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringOutputConfigProperty"]:
            '''``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringOutputConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-monitoringoutputconfig
            '''
            result = self._values.get("monitoring_output_config")
            assert result is not None, "Required property 'monitoring_output_config' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringOutputConfigProperty"], result)

        @builtins.property
        def monitoring_resources(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringResourcesProperty"]:
            '''``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.MonitoringResources``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-monitoringresources
            '''
            result = self._values.get("monitoring_resources")
            assert result is not None, "Required property 'monitoring_resources' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringResourcesProperty"], result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def baseline_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.BaselineConfigProperty"]]:
            '''``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.BaselineConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-baselineconfig
            '''
            result = self._values.get("baseline_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.BaselineConfigProperty"]], result)

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.EnvironmentProperty"]]:
            '''``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.Environment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-environment
            '''
            result = self._values.get("environment")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.EnvironmentProperty"]], result)

        @builtins.property
        def network_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.NetworkConfigProperty"]]:
            '''``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.NetworkConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-networkconfig
            '''
            result = self._values.get("network_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.NetworkConfigProperty"]], result)

        @builtins.property
        def stopping_condition(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.StoppingConditionProperty"]]:
            '''``CfnMonitoringSchedule.MonitoringJobDefinitionProperty.StoppingCondition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringjobdefinition.html#cfn-sagemaker-monitoringschedule-monitoringjobdefinition-stoppingcondition
            '''
            result = self._values.get("stopping_condition")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.StoppingConditionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringJobDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "monitoring_outputs": "monitoringOutputs",
            "kms_key_id": "kmsKeyId",
        },
    )
    class MonitoringOutputConfigProperty:
        def __init__(
            self,
            *,
            monitoring_outputs: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringOutputProperty"]]],
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param monitoring_outputs: ``CfnMonitoringSchedule.MonitoringOutputConfigProperty.MonitoringOutputs``.
            :param kms_key_id: ``CfnMonitoringSchedule.MonitoringOutputConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutputconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "monitoring_outputs": monitoring_outputs,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def monitoring_outputs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringOutputProperty"]]]:
            '''``CfnMonitoringSchedule.MonitoringOutputConfigProperty.MonitoringOutputs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutputconfig.html#cfn-sagemaker-monitoringschedule-monitoringoutputconfig-monitoringoutputs
            '''
            result = self._values.get("monitoring_outputs")
            assert result is not None, "Required property 'monitoring_outputs' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringOutputProperty"]]], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.MonitoringOutputConfigProperty.KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutputconfig.html#cfn-sagemaker-monitoringschedule-monitoringoutputconfig-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_output": "s3Output"},
    )
    class MonitoringOutputProperty:
        def __init__(
            self,
            *,
            s3_output: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.S3OutputProperty"],
        ) -> None:
            '''
            :param s3_output: ``CfnMonitoringSchedule.MonitoringOutputProperty.S3Output``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutput.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "s3_output": s3_output,
            }

        @builtins.property
        def s3_output(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.S3OutputProperty"]:
            '''``CfnMonitoringSchedule.MonitoringOutputProperty.S3Output``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringoutput.html#cfn-sagemaker-monitoringschedule-monitoringoutput-s3output
            '''
            result = self._values.get("s3_output")
            assert result is not None, "Required property 's3_output' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.S3OutputProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_config": "clusterConfig"},
    )
    class MonitoringResourcesProperty:
        def __init__(
            self,
            *,
            cluster_config: typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ClusterConfigProperty"],
        ) -> None:
            '''
            :param cluster_config: ``CfnMonitoringSchedule.MonitoringResourcesProperty.ClusterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringresources.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cluster_config": cluster_config,
            }

        @builtins.property
        def cluster_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ClusterConfigProperty"]:
            '''``CfnMonitoringSchedule.MonitoringResourcesProperty.ClusterConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringresources.html#cfn-sagemaker-monitoringschedule-monitoringresources-clusterconfig
            '''
            result = self._values.get("cluster_config")
            assert result is not None, "Required property 'cluster_config' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ClusterConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.MonitoringScheduleConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "monitoring_job_definition": "monitoringJobDefinition",
            "monitoring_job_definition_name": "monitoringJobDefinitionName",
            "monitoring_type": "monitoringType",
            "schedule_config": "scheduleConfig",
        },
    )
    class MonitoringScheduleConfigProperty:
        def __init__(
            self,
            *,
            monitoring_job_definition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringJobDefinitionProperty"]] = None,
            monitoring_job_definition_name: typing.Optional[builtins.str] = None,
            monitoring_type: typing.Optional[builtins.str] = None,
            schedule_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ScheduleConfigProperty"]] = None,
        ) -> None:
            '''
            :param monitoring_job_definition: ``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.MonitoringJobDefinition``.
            :param monitoring_job_definition_name: ``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.MonitoringJobDefinitionName``.
            :param monitoring_type: ``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.MonitoringType``.
            :param schedule_config: ``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.ScheduleConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if monitoring_job_definition is not None:
                self._values["monitoring_job_definition"] = monitoring_job_definition
            if monitoring_job_definition_name is not None:
                self._values["monitoring_job_definition_name"] = monitoring_job_definition_name
            if monitoring_type is not None:
                self._values["monitoring_type"] = monitoring_type
            if schedule_config is not None:
                self._values["schedule_config"] = schedule_config

        @builtins.property
        def monitoring_job_definition(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringJobDefinitionProperty"]]:
            '''``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.MonitoringJobDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringjobdefinition
            '''
            result = self._values.get("monitoring_job_definition")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.MonitoringJobDefinitionProperty"]], result)

        @builtins.property
        def monitoring_job_definition_name(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.MonitoringJobDefinitionName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringjobdefinitionname
            '''
            result = self._values.get("monitoring_job_definition_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def monitoring_type(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.MonitoringType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-monitoringtype
            '''
            result = self._values.get("monitoring_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def schedule_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ScheduleConfigProperty"]]:
            '''``CfnMonitoringSchedule.MonitoringScheduleConfigProperty.ScheduleConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-monitoringscheduleconfig.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig-scheduleconfig
            '''
            result = self._values.get("schedule_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.ScheduleConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringScheduleConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.NetworkConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_inter_container_traffic_encryption": "enableInterContainerTrafficEncryption",
            "enable_network_isolation": "enableNetworkIsolation",
            "vpc_config": "vpcConfig",
        },
    )
    class NetworkConfigProperty:
        def __init__(
            self,
            *,
            enable_inter_container_traffic_encryption: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            enable_network_isolation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            vpc_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.VpcConfigProperty"]] = None,
        ) -> None:
            '''
            :param enable_inter_container_traffic_encryption: ``CfnMonitoringSchedule.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.
            :param enable_network_isolation: ``CfnMonitoringSchedule.NetworkConfigProperty.EnableNetworkIsolation``.
            :param vpc_config: ``CfnMonitoringSchedule.NetworkConfigProperty.VpcConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if enable_inter_container_traffic_encryption is not None:
                self._values["enable_inter_container_traffic_encryption"] = enable_inter_container_traffic_encryption
            if enable_network_isolation is not None:
                self._values["enable_network_isolation"] = enable_network_isolation
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def enable_inter_container_traffic_encryption(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnMonitoringSchedule.NetworkConfigProperty.EnableInterContainerTrafficEncryption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html#cfn-sagemaker-monitoringschedule-networkconfig-enableintercontainertrafficencryption
            '''
            result = self._values.get("enable_inter_container_traffic_encryption")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def enable_network_isolation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnMonitoringSchedule.NetworkConfigProperty.EnableNetworkIsolation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html#cfn-sagemaker-monitoringschedule-networkconfig-enablenetworkisolation
            '''
            result = self._values.get("enable_network_isolation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.VpcConfigProperty"]]:
            '''``CfnMonitoringSchedule.NetworkConfigProperty.VpcConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-networkconfig.html#cfn-sagemaker-monitoringschedule-networkconfig-vpcconfig
            '''
            result = self._values.get("vpc_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnMonitoringSchedule.VpcConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.S3OutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "local_path": "localPath",
            "s3_uri": "s3Uri",
            "s3_upload_mode": "s3UploadMode",
        },
    )
    class S3OutputProperty:
        def __init__(
            self,
            *,
            local_path: builtins.str,
            s3_uri: builtins.str,
            s3_upload_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param local_path: ``CfnMonitoringSchedule.S3OutputProperty.LocalPath``.
            :param s3_uri: ``CfnMonitoringSchedule.S3OutputProperty.S3Uri``.
            :param s3_upload_mode: ``CfnMonitoringSchedule.S3OutputProperty.S3UploadMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-s3output.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "local_path": local_path,
                "s3_uri": s3_uri,
            }
            if s3_upload_mode is not None:
                self._values["s3_upload_mode"] = s3_upload_mode

        @builtins.property
        def local_path(self) -> builtins.str:
            '''``CfnMonitoringSchedule.S3OutputProperty.LocalPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-s3output.html#cfn-sagemaker-monitoringschedule-s3output-localpath
            '''
            result = self._values.get("local_path")
            assert result is not None, "Required property 'local_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_uri(self) -> builtins.str:
            '''``CfnMonitoringSchedule.S3OutputProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-s3output.html#cfn-sagemaker-monitoringschedule-s3output-s3uri
            '''
            result = self._values.get("s3_uri")
            assert result is not None, "Required property 's3_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_upload_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.S3OutputProperty.S3UploadMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-s3output.html#cfn-sagemaker-monitoringschedule-s3output-s3uploadmode
            '''
            result = self._values.get("s3_upload_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.ScheduleConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"schedule_expression": "scheduleExpression"},
    )
    class ScheduleConfigProperty:
        def __init__(self, *, schedule_expression: builtins.str) -> None:
            '''
            :param schedule_expression: ``CfnMonitoringSchedule.ScheduleConfigProperty.ScheduleExpression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-scheduleconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "schedule_expression": schedule_expression,
            }

        @builtins.property
        def schedule_expression(self) -> builtins.str:
            '''``CfnMonitoringSchedule.ScheduleConfigProperty.ScheduleExpression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-scheduleconfig.html#cfn-sagemaker-monitoringschedule-scheduleconfig-scheduleexpression
            '''
            result = self._values.get("schedule_expression")
            assert result is not None, "Required property 'schedule_expression' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.StatisticsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_uri": "s3Uri"},
    )
    class StatisticsResourceProperty:
        def __init__(self, *, s3_uri: typing.Optional[builtins.str] = None) -> None:
            '''
            :param s3_uri: ``CfnMonitoringSchedule.StatisticsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-statisticsresource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_uri is not None:
                self._values["s3_uri"] = s3_uri

        @builtins.property
        def s3_uri(self) -> typing.Optional[builtins.str]:
            '''``CfnMonitoringSchedule.StatisticsResourceProperty.S3Uri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-statisticsresource.html#cfn-sagemaker-monitoringschedule-statisticsresource-s3uri
            '''
            result = self._values.get("s3_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatisticsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.StoppingConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"max_runtime_in_seconds": "maxRuntimeInSeconds"},
    )
    class StoppingConditionProperty:
        def __init__(self, *, max_runtime_in_seconds: jsii.Number) -> None:
            '''
            :param max_runtime_in_seconds: ``CfnMonitoringSchedule.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-stoppingcondition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_runtime_in_seconds": max_runtime_in_seconds,
            }

        @builtins.property
        def max_runtime_in_seconds(self) -> jsii.Number:
            '''``CfnMonitoringSchedule.StoppingConditionProperty.MaxRuntimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-stoppingcondition.html#cfn-sagemaker-monitoringschedule-stoppingcondition-maxruntimeinseconds
            '''
            result = self._values.get("max_runtime_in_seconds")
            assert result is not None, "Required property 'max_runtime_in_seconds' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StoppingConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringSchedule.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param security_group_ids: ``CfnMonitoringSchedule.VpcConfigProperty.SecurityGroupIds``.
            :param subnets: ``CfnMonitoringSchedule.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-vpcconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnets": subnets,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''``CfnMonitoringSchedule.VpcConfigProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-vpcconfig.html#cfn-sagemaker-monitoringschedule-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''``CfnMonitoringSchedule.VpcConfigProperty.Subnets``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-monitoringschedule-vpcconfig.html#cfn-sagemaker-monitoringschedule-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnMonitoringScheduleProps",
    jsii_struct_bases=[],
    name_mapping={
        "monitoring_schedule_config": "monitoringScheduleConfig",
        "monitoring_schedule_name": "monitoringScheduleName",
        "endpoint_name": "endpointName",
        "failure_reason": "failureReason",
        "last_monitoring_execution_summary": "lastMonitoringExecutionSummary",
        "monitoring_schedule_status": "monitoringScheduleStatus",
        "tags": "tags",
    },
)
class CfnMonitoringScheduleProps:
    def __init__(
        self,
        *,
        monitoring_schedule_config: typing.Union[aws_cdk.core.IResolvable, CfnMonitoringSchedule.MonitoringScheduleConfigProperty],
        monitoring_schedule_name: builtins.str,
        endpoint_name: typing.Optional[builtins.str] = None,
        failure_reason: typing.Optional[builtins.str] = None,
        last_monitoring_execution_summary: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnMonitoringSchedule.MonitoringExecutionSummaryProperty]] = None,
        monitoring_schedule_status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::MonitoringSchedule``.

        :param monitoring_schedule_config: ``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleConfig``.
        :param monitoring_schedule_name: ``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleName``.
        :param endpoint_name: ``AWS::SageMaker::MonitoringSchedule.EndpointName``.
        :param failure_reason: ``AWS::SageMaker::MonitoringSchedule.FailureReason``.
        :param last_monitoring_execution_summary: ``AWS::SageMaker::MonitoringSchedule.LastMonitoringExecutionSummary``.
        :param monitoring_schedule_status: ``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleStatus``.
        :param tags: ``AWS::SageMaker::MonitoringSchedule.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "monitoring_schedule_config": monitoring_schedule_config,
            "monitoring_schedule_name": monitoring_schedule_name,
        }
        if endpoint_name is not None:
            self._values["endpoint_name"] = endpoint_name
        if failure_reason is not None:
            self._values["failure_reason"] = failure_reason
        if last_monitoring_execution_summary is not None:
            self._values["last_monitoring_execution_summary"] = last_monitoring_execution_summary
        if monitoring_schedule_status is not None:
            self._values["monitoring_schedule_status"] = monitoring_schedule_status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def monitoring_schedule_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnMonitoringSchedule.MonitoringScheduleConfigProperty]:
        '''``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringscheduleconfig
        '''
        result = self._values.get("monitoring_schedule_config")
        assert result is not None, "Required property 'monitoring_schedule_config' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnMonitoringSchedule.MonitoringScheduleConfigProperty], result)

    @builtins.property
    def monitoring_schedule_name(self) -> builtins.str:
        '''``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringschedulename
        '''
        result = self._values.get("monitoring_schedule_name")
        assert result is not None, "Required property 'monitoring_schedule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::MonitoringSchedule.EndpointName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-endpointname
        '''
        result = self._values.get("endpoint_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def failure_reason(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::MonitoringSchedule.FailureReason``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-failurereason
        '''
        result = self._values.get("failure_reason")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_monitoring_execution_summary(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnMonitoringSchedule.MonitoringExecutionSummaryProperty]]:
        '''``AWS::SageMaker::MonitoringSchedule.LastMonitoringExecutionSummary``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-lastmonitoringexecutionsummary
        '''
        result = self._values.get("last_monitoring_execution_summary")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnMonitoringSchedule.MonitoringExecutionSummaryProperty]], result)

    @builtins.property
    def monitoring_schedule_status(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::MonitoringSchedule.MonitoringScheduleStatus``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-monitoringschedulestatus
        '''
        result = self._values.get("monitoring_schedule_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::MonitoringSchedule.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-monitoringschedule.html#cfn-sagemaker-monitoringschedule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMonitoringScheduleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnNotebookInstance(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnNotebookInstance",
):
    '''A CloudFormation ``AWS::SageMaker::NotebookInstance``.

    :cloudformationResource: AWS::SageMaker::NotebookInstance
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        instance_type: builtins.str,
        role_arn: builtins.str,
        accelerator_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        additional_code_repositories: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_code_repository: typing.Optional[builtins.str] = None,
        direct_internet_access: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        lifecycle_config_name: typing.Optional[builtins.str] = None,
        notebook_instance_name: typing.Optional[builtins.str] = None,
        root_access: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        volume_size_in_gb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::NotebookInstance``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_type: ``AWS::SageMaker::NotebookInstance.InstanceType``.
        :param role_arn: ``AWS::SageMaker::NotebookInstance.RoleArn``.
        :param accelerator_types: ``AWS::SageMaker::NotebookInstance.AcceleratorTypes``.
        :param additional_code_repositories: ``AWS::SageMaker::NotebookInstance.AdditionalCodeRepositories``.
        :param default_code_repository: ``AWS::SageMaker::NotebookInstance.DefaultCodeRepository``.
        :param direct_internet_access: ``AWS::SageMaker::NotebookInstance.DirectInternetAccess``.
        :param kms_key_id: ``AWS::SageMaker::NotebookInstance.KmsKeyId``.
        :param lifecycle_config_name: ``AWS::SageMaker::NotebookInstance.LifecycleConfigName``.
        :param notebook_instance_name: ``AWS::SageMaker::NotebookInstance.NotebookInstanceName``.
        :param root_access: ``AWS::SageMaker::NotebookInstance.RootAccess``.
        :param security_group_ids: ``AWS::SageMaker::NotebookInstance.SecurityGroupIds``.
        :param subnet_id: ``AWS::SageMaker::NotebookInstance.SubnetId``.
        :param tags: ``AWS::SageMaker::NotebookInstance.Tags``.
        :param volume_size_in_gb: ``AWS::SageMaker::NotebookInstance.VolumeSizeInGB``.
        '''
        props = CfnNotebookInstanceProps(
            instance_type=instance_type,
            role_arn=role_arn,
            accelerator_types=accelerator_types,
            additional_code_repositories=additional_code_repositories,
            default_code_repository=default_code_repository,
            direct_internet_access=direct_internet_access,
            kms_key_id=kms_key_id,
            lifecycle_config_name=lifecycle_config_name,
            notebook_instance_name=notebook_instance_name,
            root_access=root_access,
            security_group_ids=security_group_ids,
            subnet_id=subnet_id,
            tags=tags,
            volume_size_in_gb=volume_size_in_gb,
        )

        jsii.create(CfnNotebookInstance, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrNotebookInstanceName")
    def attr_notebook_instance_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: NotebookInstanceName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNotebookInstanceName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::NotebookInstance.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        '''``AWS::SageMaker::NotebookInstance.InstanceType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-instancetype
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        jsii.set(self, "instanceType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::NotebookInstance.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="acceleratorTypes")
    def accelerator_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SageMaker::NotebookInstance.AcceleratorTypes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-acceleratortypes
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "acceleratorTypes"))

    @accelerator_types.setter
    def accelerator_types(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "acceleratorTypes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="additionalCodeRepositories")
    def additional_code_repositories(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SageMaker::NotebookInstance.AdditionalCodeRepositories``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-additionalcoderepositories
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "additionalCodeRepositories"))

    @additional_code_repositories.setter
    def additional_code_repositories(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "additionalCodeRepositories", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultCodeRepository")
    def default_code_repository(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.DefaultCodeRepository``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-defaultcoderepository
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultCodeRepository"))

    @default_code_repository.setter
    def default_code_repository(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "defaultCodeRepository", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="directInternetAccess")
    def direct_internet_access(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.DirectInternetAccess``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-directinternetaccess
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directInternetAccess"))

    @direct_internet_access.setter
    def direct_internet_access(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "directInternetAccess", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lifecycleConfigName")
    def lifecycle_config_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.LifecycleConfigName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-lifecycleconfigname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleConfigName"))

    @lifecycle_config_name.setter
    def lifecycle_config_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "lifecycleConfigName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="notebookInstanceName")
    def notebook_instance_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.NotebookInstanceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-notebookinstancename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notebookInstanceName"))

    @notebook_instance_name.setter
    def notebook_instance_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "notebookInstanceName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rootAccess")
    def root_access(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.RootAccess``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-rootaccess
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootAccess"))

    @root_access.setter
    def root_access(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "rootAccess", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SageMaker::NotebookInstance.SecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-securitygroupids
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "securityGroupIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.SubnetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-subnetid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "subnetId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumeSizeInGb")
    def volume_size_in_gb(self) -> typing.Optional[jsii.Number]:
        '''``AWS::SageMaker::NotebookInstance.VolumeSizeInGB``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-volumesizeingb
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "volumeSizeInGb"))

    @volume_size_in_gb.setter
    def volume_size_in_gb(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "volumeSizeInGb", value)


@jsii.implements(aws_cdk.core.IInspectable)
class CfnNotebookInstanceLifecycleConfig(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnNotebookInstanceLifecycleConfig",
):
    '''A CloudFormation ``AWS::SageMaker::NotebookInstanceLifecycleConfig``.

    :cloudformationResource: AWS::SageMaker::NotebookInstanceLifecycleConfig
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        notebook_instance_lifecycle_config_name: typing.Optional[builtins.str] = None,
        on_create: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]] = None,
        on_start: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::NotebookInstanceLifecycleConfig``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param notebook_instance_lifecycle_config_name: ``AWS::SageMaker::NotebookInstanceLifecycleConfig.NotebookInstanceLifecycleConfigName``.
        :param on_create: ``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnCreate``.
        :param on_start: ``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnStart``.
        '''
        props = CfnNotebookInstanceLifecycleConfigProps(
            notebook_instance_lifecycle_config_name=notebook_instance_lifecycle_config_name,
            on_create=on_create,
            on_start=on_start,
        )

        jsii.create(CfnNotebookInstanceLifecycleConfig, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrNotebookInstanceLifecycleConfigName")
    def attr_notebook_instance_lifecycle_config_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: NotebookInstanceLifecycleConfigName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNotebookInstanceLifecycleConfigName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="notebookInstanceLifecycleConfigName")
    def notebook_instance_lifecycle_config_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstanceLifecycleConfig.NotebookInstanceLifecycleConfigName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecycleconfigname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notebookInstanceLifecycleConfigName"))

    @notebook_instance_lifecycle_config_name.setter
    def notebook_instance_lifecycle_config_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "notebookInstanceLifecycleConfigName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="onCreate")
    def on_create(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]]:
        '''``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnCreate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-oncreate
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]], jsii.get(self, "onCreate"))

    @on_create.setter
    def on_create(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]],
    ) -> None:
        jsii.set(self, "onCreate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="onStart")
    def on_start(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]]:
        '''``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnStart``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-onstart
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]], jsii.get(self, "onStart"))

    @on_start.setter
    def on_start(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty"]]]],
    ) -> None:
        jsii.set(self, "onStart", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty",
        jsii_struct_bases=[],
        name_mapping={"content": "content"},
    )
    class NotebookInstanceLifecycleHookProperty:
        def __init__(self, *, content: typing.Optional[builtins.str] = None) -> None:
            '''
            :param content: ``CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty.Content``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if content is not None:
                self._values["content"] = content

        @builtins.property
        def content(self) -> typing.Optional[builtins.str]:
            '''``CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty.Content``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook.html#cfn-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecyclehook-content
            '''
            result = self._values.get("content")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotebookInstanceLifecycleHookProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnNotebookInstanceLifecycleConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "notebook_instance_lifecycle_config_name": "notebookInstanceLifecycleConfigName",
        "on_create": "onCreate",
        "on_start": "onStart",
    },
)
class CfnNotebookInstanceLifecycleConfigProps:
    def __init__(
        self,
        *,
        notebook_instance_lifecycle_config_name: typing.Optional[builtins.str] = None,
        on_create: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty]]]] = None,
        on_start: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::NotebookInstanceLifecycleConfig``.

        :param notebook_instance_lifecycle_config_name: ``AWS::SageMaker::NotebookInstanceLifecycleConfig.NotebookInstanceLifecycleConfigName``.
        :param on_create: ``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnCreate``.
        :param on_start: ``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnStart``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if notebook_instance_lifecycle_config_name is not None:
            self._values["notebook_instance_lifecycle_config_name"] = notebook_instance_lifecycle_config_name
        if on_create is not None:
            self._values["on_create"] = on_create
        if on_start is not None:
            self._values["on_start"] = on_start

    @builtins.property
    def notebook_instance_lifecycle_config_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstanceLifecycleConfig.NotebookInstanceLifecycleConfigName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-notebookinstancelifecycleconfigname
        '''
        result = self._values.get("notebook_instance_lifecycle_config_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def on_create(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty]]]]:
        '''``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnCreate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-oncreate
        '''
        result = self._values.get("on_create")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty]]]], result)

    @builtins.property
    def on_start(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty]]]]:
        '''``AWS::SageMaker::NotebookInstanceLifecycleConfig.OnStart``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html#cfn-sagemaker-notebookinstancelifecycleconfig-onstart
        '''
        result = self._values.get("on_start")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnNotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHookProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNotebookInstanceLifecycleConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnNotebookInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "role_arn": "roleArn",
        "accelerator_types": "acceleratorTypes",
        "additional_code_repositories": "additionalCodeRepositories",
        "default_code_repository": "defaultCodeRepository",
        "direct_internet_access": "directInternetAccess",
        "kms_key_id": "kmsKeyId",
        "lifecycle_config_name": "lifecycleConfigName",
        "notebook_instance_name": "notebookInstanceName",
        "root_access": "rootAccess",
        "security_group_ids": "securityGroupIds",
        "subnet_id": "subnetId",
        "tags": "tags",
        "volume_size_in_gb": "volumeSizeInGb",
    },
)
class CfnNotebookInstanceProps:
    def __init__(
        self,
        *,
        instance_type: builtins.str,
        role_arn: builtins.str,
        accelerator_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        additional_code_repositories: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_code_repository: typing.Optional[builtins.str] = None,
        direct_internet_access: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        lifecycle_config_name: typing.Optional[builtins.str] = None,
        notebook_instance_name: typing.Optional[builtins.str] = None,
        root_access: typing.Optional[builtins.str] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        volume_size_in_gb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::NotebookInstance``.

        :param instance_type: ``AWS::SageMaker::NotebookInstance.InstanceType``.
        :param role_arn: ``AWS::SageMaker::NotebookInstance.RoleArn``.
        :param accelerator_types: ``AWS::SageMaker::NotebookInstance.AcceleratorTypes``.
        :param additional_code_repositories: ``AWS::SageMaker::NotebookInstance.AdditionalCodeRepositories``.
        :param default_code_repository: ``AWS::SageMaker::NotebookInstance.DefaultCodeRepository``.
        :param direct_internet_access: ``AWS::SageMaker::NotebookInstance.DirectInternetAccess``.
        :param kms_key_id: ``AWS::SageMaker::NotebookInstance.KmsKeyId``.
        :param lifecycle_config_name: ``AWS::SageMaker::NotebookInstance.LifecycleConfigName``.
        :param notebook_instance_name: ``AWS::SageMaker::NotebookInstance.NotebookInstanceName``.
        :param root_access: ``AWS::SageMaker::NotebookInstance.RootAccess``.
        :param security_group_ids: ``AWS::SageMaker::NotebookInstance.SecurityGroupIds``.
        :param subnet_id: ``AWS::SageMaker::NotebookInstance.SubnetId``.
        :param tags: ``AWS::SageMaker::NotebookInstance.Tags``.
        :param volume_size_in_gb: ``AWS::SageMaker::NotebookInstance.VolumeSizeInGB``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "instance_type": instance_type,
            "role_arn": role_arn,
        }
        if accelerator_types is not None:
            self._values["accelerator_types"] = accelerator_types
        if additional_code_repositories is not None:
            self._values["additional_code_repositories"] = additional_code_repositories
        if default_code_repository is not None:
            self._values["default_code_repository"] = default_code_repository
        if direct_internet_access is not None:
            self._values["direct_internet_access"] = direct_internet_access
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if lifecycle_config_name is not None:
            self._values["lifecycle_config_name"] = lifecycle_config_name
        if notebook_instance_name is not None:
            self._values["notebook_instance_name"] = notebook_instance_name
        if root_access is not None:
            self._values["root_access"] = root_access
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if tags is not None:
            self._values["tags"] = tags
        if volume_size_in_gb is not None:
            self._values["volume_size_in_gb"] = volume_size_in_gb

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''``AWS::SageMaker::NotebookInstance.InstanceType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-instancetype
        '''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::NotebookInstance.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accelerator_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SageMaker::NotebookInstance.AcceleratorTypes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-acceleratortypes
        '''
        result = self._values.get("accelerator_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def additional_code_repositories(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SageMaker::NotebookInstance.AdditionalCodeRepositories``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-additionalcoderepositories
        '''
        result = self._values.get("additional_code_repositories")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def default_code_repository(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.DefaultCodeRepository``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-defaultcoderepository
        '''
        result = self._values.get("default_code_repository")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def direct_internet_access(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.DirectInternetAccess``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-directinternetaccess
        '''
        result = self._values.get("direct_internet_access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.KmsKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_config_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.LifecycleConfigName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-lifecycleconfigname
        '''
        result = self._values.get("lifecycle_config_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notebook_instance_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.NotebookInstanceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-notebookinstancename
        '''
        result = self._values.get("notebook_instance_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_access(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.RootAccess``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-rootaccess
        '''
        result = self._values.get("root_access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SageMaker::NotebookInstance.SecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::NotebookInstance.SubnetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-subnetid
        '''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::NotebookInstance.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def volume_size_in_gb(self) -> typing.Optional[jsii.Number]:
        '''``AWS::SageMaker::NotebookInstance.VolumeSizeInGB``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html#cfn-sagemaker-notebookinstance-volumesizeingb
        '''
        result = self._values.get("volume_size_in_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNotebookInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPipeline(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnPipeline",
):
    '''A CloudFormation ``AWS::SageMaker::Pipeline``.

    :cloudformationResource: AWS::SageMaker::Pipeline
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        pipeline_definition: typing.Any,
        pipeline_name: builtins.str,
        role_arn: builtins.str,
        pipeline_description: typing.Optional[builtins.str] = None,
        pipeline_display_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::Pipeline``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param pipeline_definition: ``AWS::SageMaker::Pipeline.PipelineDefinition``.
        :param pipeline_name: ``AWS::SageMaker::Pipeline.PipelineName``.
        :param role_arn: ``AWS::SageMaker::Pipeline.RoleArn``.
        :param pipeline_description: ``AWS::SageMaker::Pipeline.PipelineDescription``.
        :param pipeline_display_name: ``AWS::SageMaker::Pipeline.PipelineDisplayName``.
        :param tags: ``AWS::SageMaker::Pipeline.Tags``.
        '''
        props = CfnPipelineProps(
            pipeline_definition=pipeline_definition,
            pipeline_name=pipeline_name,
            role_arn=role_arn,
            pipeline_description=pipeline_description,
            pipeline_display_name=pipeline_display_name,
            tags=tags,
        )

        jsii.create(CfnPipeline, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::Pipeline.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pipelineDefinition")
    def pipeline_definition(self) -> typing.Any:
        '''``AWS::SageMaker::Pipeline.PipelineDefinition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedefinition
        '''
        return typing.cast(typing.Any, jsii.get(self, "pipelineDefinition"))

    @pipeline_definition.setter
    def pipeline_definition(self, value: typing.Any) -> None:
        jsii.set(self, "pipelineDefinition", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pipelineName")
    def pipeline_name(self) -> builtins.str:
        '''``AWS::SageMaker::Pipeline.PipelineName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinename
        '''
        return typing.cast(builtins.str, jsii.get(self, "pipelineName"))

    @pipeline_name.setter
    def pipeline_name(self, value: builtins.str) -> None:
        jsii.set(self, "pipelineName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::Pipeline.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pipelineDescription")
    def pipeline_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Pipeline.PipelineDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pipelineDescription"))

    @pipeline_description.setter
    def pipeline_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "pipelineDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pipelineDisplayName")
    def pipeline_display_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Pipeline.PipelineDisplayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedisplayname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pipelineDisplayName"))

    @pipeline_display_name.setter
    def pipeline_display_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "pipelineDisplayName", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnPipelineProps",
    jsii_struct_bases=[],
    name_mapping={
        "pipeline_definition": "pipelineDefinition",
        "pipeline_name": "pipelineName",
        "role_arn": "roleArn",
        "pipeline_description": "pipelineDescription",
        "pipeline_display_name": "pipelineDisplayName",
        "tags": "tags",
    },
)
class CfnPipelineProps:
    def __init__(
        self,
        *,
        pipeline_definition: typing.Any,
        pipeline_name: builtins.str,
        role_arn: builtins.str,
        pipeline_description: typing.Optional[builtins.str] = None,
        pipeline_display_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::Pipeline``.

        :param pipeline_definition: ``AWS::SageMaker::Pipeline.PipelineDefinition``.
        :param pipeline_name: ``AWS::SageMaker::Pipeline.PipelineName``.
        :param role_arn: ``AWS::SageMaker::Pipeline.RoleArn``.
        :param pipeline_description: ``AWS::SageMaker::Pipeline.PipelineDescription``.
        :param pipeline_display_name: ``AWS::SageMaker::Pipeline.PipelineDisplayName``.
        :param tags: ``AWS::SageMaker::Pipeline.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "pipeline_definition": pipeline_definition,
            "pipeline_name": pipeline_name,
            "role_arn": role_arn,
        }
        if pipeline_description is not None:
            self._values["pipeline_description"] = pipeline_description
        if pipeline_display_name is not None:
            self._values["pipeline_display_name"] = pipeline_display_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def pipeline_definition(self) -> typing.Any:
        '''``AWS::SageMaker::Pipeline.PipelineDefinition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedefinition
        '''
        result = self._values.get("pipeline_definition")
        assert result is not None, "Required property 'pipeline_definition' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def pipeline_name(self) -> builtins.str:
        '''``AWS::SageMaker::Pipeline.PipelineName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinename
        '''
        result = self._values.get("pipeline_name")
        assert result is not None, "Required property 'pipeline_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::SageMaker::Pipeline.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pipeline_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Pipeline.PipelineDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedescription
        '''
        result = self._values.get("pipeline_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pipeline_display_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Pipeline.PipelineDisplayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-pipelinedisplayname
        '''
        result = self._values.get("pipeline_display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::Pipeline.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-pipeline.html#cfn-sagemaker-pipeline-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPipelineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnProject(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnProject",
):
    '''A CloudFormation ``AWS::SageMaker::Project``.

    :cloudformationResource: AWS::SageMaker::Project
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        project_name: builtins.str,
        service_catalog_provisioning_details: typing.Any,
        project_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::Project``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param project_name: ``AWS::SageMaker::Project.ProjectName``.
        :param service_catalog_provisioning_details: ``AWS::SageMaker::Project.ServiceCatalogProvisioningDetails``.
        :param project_description: ``AWS::SageMaker::Project.ProjectDescription``.
        :param tags: ``AWS::SageMaker::Project.Tags``.
        '''
        props = CfnProjectProps(
            project_name=project_name,
            service_catalog_provisioning_details=service_catalog_provisioning_details,
            project_description=project_description,
            tags=tags,
        )

        jsii.create(CfnProject, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrProjectArn")
    def attr_project_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: ProjectArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrProjectId")
    def attr_project_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ProjectId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrProjectStatus")
    def attr_project_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: ProjectStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProjectStatus"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::Project.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="projectName")
    def project_name(self) -> builtins.str:
        '''``AWS::SageMaker::Project.ProjectName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-projectname
        '''
        return typing.cast(builtins.str, jsii.get(self, "projectName"))

    @project_name.setter
    def project_name(self, value: builtins.str) -> None:
        jsii.set(self, "projectName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceCatalogProvisioningDetails")
    def service_catalog_provisioning_details(self) -> typing.Any:
        '''``AWS::SageMaker::Project.ServiceCatalogProvisioningDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-servicecatalogprovisioningdetails
        '''
        return typing.cast(typing.Any, jsii.get(self, "serviceCatalogProvisioningDetails"))

    @service_catalog_provisioning_details.setter
    def service_catalog_provisioning_details(self, value: typing.Any) -> None:
        jsii.set(self, "serviceCatalogProvisioningDetails", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="projectDescription")
    def project_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Project.ProjectDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-projectdescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectDescription"))

    @project_description.setter
    def project_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "projectDescription", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnProjectProps",
    jsii_struct_bases=[],
    name_mapping={
        "project_name": "projectName",
        "service_catalog_provisioning_details": "serviceCatalogProvisioningDetails",
        "project_description": "projectDescription",
        "tags": "tags",
    },
)
class CfnProjectProps:
    def __init__(
        self,
        *,
        project_name: builtins.str,
        service_catalog_provisioning_details: typing.Any,
        project_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::Project``.

        :param project_name: ``AWS::SageMaker::Project.ProjectName``.
        :param service_catalog_provisioning_details: ``AWS::SageMaker::Project.ServiceCatalogProvisioningDetails``.
        :param project_description: ``AWS::SageMaker::Project.ProjectDescription``.
        :param tags: ``AWS::SageMaker::Project.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "project_name": project_name,
            "service_catalog_provisioning_details": service_catalog_provisioning_details,
        }
        if project_description is not None:
            self._values["project_description"] = project_description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def project_name(self) -> builtins.str:
        '''``AWS::SageMaker::Project.ProjectName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-projectname
        '''
        result = self._values.get("project_name")
        assert result is not None, "Required property 'project_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_catalog_provisioning_details(self) -> typing.Any:
        '''``AWS::SageMaker::Project.ServiceCatalogProvisioningDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-servicecatalogprovisioningdetails
        '''
        result = self._values.get("service_catalog_provisioning_details")
        assert result is not None, "Required property 'service_catalog_provisioning_details' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def project_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Project.ProjectDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-projectdescription
        '''
        result = self._values.get("project_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::Project.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-project.html#cfn-sagemaker-project-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnUserProfile(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnUserProfile",
):
    '''A CloudFormation ``AWS::SageMaker::UserProfile``.

    :cloudformationResource: AWS::SageMaker::UserProfile
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        domain_id: builtins.str,
        user_profile_name: builtins.str,
        single_sign_on_user_identifier: typing.Optional[builtins.str] = None,
        single_sign_on_user_value: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        user_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.UserSettingsProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::UserProfile``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param domain_id: ``AWS::SageMaker::UserProfile.DomainId``.
        :param user_profile_name: ``AWS::SageMaker::UserProfile.UserProfileName``.
        :param single_sign_on_user_identifier: ``AWS::SageMaker::UserProfile.SingleSignOnUserIdentifier``.
        :param single_sign_on_user_value: ``AWS::SageMaker::UserProfile.SingleSignOnUserValue``.
        :param tags: ``AWS::SageMaker::UserProfile.Tags``.
        :param user_settings: ``AWS::SageMaker::UserProfile.UserSettings``.
        '''
        props = CfnUserProfileProps(
            domain_id=domain_id,
            user_profile_name=user_profile_name,
            single_sign_on_user_identifier=single_sign_on_user_identifier,
            single_sign_on_user_value=single_sign_on_user_value,
            tags=tags,
            user_settings=user_settings,
        )

        jsii.create(CfnUserProfile, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrUserProfileArn")
    def attr_user_profile_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: UserProfileArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserProfileArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::UserProfile.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domainId")
    def domain_id(self) -> builtins.str:
        '''``AWS::SageMaker::UserProfile.DomainId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-domainid
        '''
        return typing.cast(builtins.str, jsii.get(self, "domainId"))

    @domain_id.setter
    def domain_id(self, value: builtins.str) -> None:
        jsii.set(self, "domainId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userProfileName")
    def user_profile_name(self) -> builtins.str:
        '''``AWS::SageMaker::UserProfile.UserProfileName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-userprofilename
        '''
        return typing.cast(builtins.str, jsii.get(self, "userProfileName"))

    @user_profile_name.setter
    def user_profile_name(self, value: builtins.str) -> None:
        jsii.set(self, "userProfileName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="singleSignOnUserIdentifier")
    def single_sign_on_user_identifier(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::UserProfile.SingleSignOnUserIdentifier``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-singlesignonuseridentifier
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "singleSignOnUserIdentifier"))

    @single_sign_on_user_identifier.setter
    def single_sign_on_user_identifier(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "singleSignOnUserIdentifier", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="singleSignOnUserValue")
    def single_sign_on_user_value(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::UserProfile.SingleSignOnUserValue``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-singlesignonuservalue
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "singleSignOnUserValue"))

    @single_sign_on_user_value.setter
    def single_sign_on_user_value(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "singleSignOnUserValue", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userSettings")
    def user_settings(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.UserSettingsProperty"]]:
        '''``AWS::SageMaker::UserProfile.UserSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-usersettings
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.UserSettingsProperty"]], jsii.get(self, "userSettings"))

    @user_settings.setter
    def user_settings(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.UserSettingsProperty"]],
    ) -> None:
        jsii.set(self, "userSettings", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnUserProfile.CustomImageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "app_image_config_name": "appImageConfigName",
            "image_name": "imageName",
            "image_version_number": "imageVersionNumber",
        },
    )
    class CustomImageProperty:
        def __init__(
            self,
            *,
            app_image_config_name: builtins.str,
            image_name: builtins.str,
            image_version_number: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param app_image_config_name: ``CfnUserProfile.CustomImageProperty.AppImageConfigName``.
            :param image_name: ``CfnUserProfile.CustomImageProperty.ImageName``.
            :param image_version_number: ``CfnUserProfile.CustomImageProperty.ImageVersionNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-customimage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "app_image_config_name": app_image_config_name,
                "image_name": image_name,
            }
            if image_version_number is not None:
                self._values["image_version_number"] = image_version_number

        @builtins.property
        def app_image_config_name(self) -> builtins.str:
            '''``CfnUserProfile.CustomImageProperty.AppImageConfigName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-customimage.html#cfn-sagemaker-userprofile-customimage-appimageconfigname
            '''
            result = self._values.get("app_image_config_name")
            assert result is not None, "Required property 'app_image_config_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_name(self) -> builtins.str:
            '''``CfnUserProfile.CustomImageProperty.ImageName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-customimage.html#cfn-sagemaker-userprofile-customimage-imagename
            '''
            result = self._values.get("image_name")
            assert result is not None, "Required property 'image_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_version_number(self) -> typing.Optional[jsii.Number]:
            '''``CfnUserProfile.CustomImageProperty.ImageVersionNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-customimage.html#cfn-sagemaker-userprofile-customimage-imageversionnumber
            '''
            result = self._values.get("image_version_number")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomImageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnUserProfile.JupyterServerAppSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"default_resource_spec": "defaultResourceSpec"},
    )
    class JupyterServerAppSettingsProperty:
        def __init__(
            self,
            *,
            default_resource_spec: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.ResourceSpecProperty"]] = None,
        ) -> None:
            '''
            :param default_resource_spec: ``CfnUserProfile.JupyterServerAppSettingsProperty.DefaultResourceSpec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-jupyterserverappsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if default_resource_spec is not None:
                self._values["default_resource_spec"] = default_resource_spec

        @builtins.property
        def default_resource_spec(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.ResourceSpecProperty"]]:
            '''``CfnUserProfile.JupyterServerAppSettingsProperty.DefaultResourceSpec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-jupyterserverappsettings.html#cfn-sagemaker-userprofile-jupyterserverappsettings-defaultresourcespec
            '''
            result = self._values.get("default_resource_spec")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.ResourceSpecProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JupyterServerAppSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnUserProfile.KernelGatewayAppSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "custom_images": "customImages",
            "default_resource_spec": "defaultResourceSpec",
        },
    )
    class KernelGatewayAppSettingsProperty:
        def __init__(
            self,
            *,
            custom_images: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.CustomImageProperty"]]]] = None,
            default_resource_spec: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.ResourceSpecProperty"]] = None,
        ) -> None:
            '''
            :param custom_images: ``CfnUserProfile.KernelGatewayAppSettingsProperty.CustomImages``.
            :param default_resource_spec: ``CfnUserProfile.KernelGatewayAppSettingsProperty.DefaultResourceSpec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-kernelgatewayappsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if custom_images is not None:
                self._values["custom_images"] = custom_images
            if default_resource_spec is not None:
                self._values["default_resource_spec"] = default_resource_spec

        @builtins.property
        def custom_images(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.CustomImageProperty"]]]]:
            '''``CfnUserProfile.KernelGatewayAppSettingsProperty.CustomImages``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-kernelgatewayappsettings.html#cfn-sagemaker-userprofile-kernelgatewayappsettings-customimages
            '''
            result = self._values.get("custom_images")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.CustomImageProperty"]]]], result)

        @builtins.property
        def default_resource_spec(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.ResourceSpecProperty"]]:
            '''``CfnUserProfile.KernelGatewayAppSettingsProperty.DefaultResourceSpec``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-kernelgatewayappsettings.html#cfn-sagemaker-userprofile-kernelgatewayappsettings-defaultresourcespec
            '''
            result = self._values.get("default_resource_spec")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.ResourceSpecProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KernelGatewayAppSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnUserProfile.ResourceSpecProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_type": "instanceType",
            "sage_maker_image_arn": "sageMakerImageArn",
            "sage_maker_image_version_arn": "sageMakerImageVersionArn",
        },
    )
    class ResourceSpecProperty:
        def __init__(
            self,
            *,
            instance_type: typing.Optional[builtins.str] = None,
            sage_maker_image_arn: typing.Optional[builtins.str] = None,
            sage_maker_image_version_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param instance_type: ``CfnUserProfile.ResourceSpecProperty.InstanceType``.
            :param sage_maker_image_arn: ``CfnUserProfile.ResourceSpecProperty.SageMakerImageArn``.
            :param sage_maker_image_version_arn: ``CfnUserProfile.ResourceSpecProperty.SageMakerImageVersionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-resourcespec.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if instance_type is not None:
                self._values["instance_type"] = instance_type
            if sage_maker_image_arn is not None:
                self._values["sage_maker_image_arn"] = sage_maker_image_arn
            if sage_maker_image_version_arn is not None:
                self._values["sage_maker_image_version_arn"] = sage_maker_image_version_arn

        @builtins.property
        def instance_type(self) -> typing.Optional[builtins.str]:
            '''``CfnUserProfile.ResourceSpecProperty.InstanceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-resourcespec.html#cfn-sagemaker-userprofile-resourcespec-instancetype
            '''
            result = self._values.get("instance_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sage_maker_image_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnUserProfile.ResourceSpecProperty.SageMakerImageArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-resourcespec.html#cfn-sagemaker-userprofile-resourcespec-sagemakerimagearn
            '''
            result = self._values.get("sage_maker_image_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sage_maker_image_version_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnUserProfile.ResourceSpecProperty.SageMakerImageVersionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-resourcespec.html#cfn-sagemaker-userprofile-resourcespec-sagemakerimageversionarn
            '''
            result = self._values.get("sage_maker_image_version_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceSpecProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnUserProfile.SharingSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "notebook_output_option": "notebookOutputOption",
            "s3_kms_key_id": "s3KmsKeyId",
            "s3_output_path": "s3OutputPath",
        },
    )
    class SharingSettingsProperty:
        def __init__(
            self,
            *,
            notebook_output_option: typing.Optional[builtins.str] = None,
            s3_kms_key_id: typing.Optional[builtins.str] = None,
            s3_output_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param notebook_output_option: ``CfnUserProfile.SharingSettingsProperty.NotebookOutputOption``.
            :param s3_kms_key_id: ``CfnUserProfile.SharingSettingsProperty.S3KmsKeyId``.
            :param s3_output_path: ``CfnUserProfile.SharingSettingsProperty.S3OutputPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-sharingsettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if notebook_output_option is not None:
                self._values["notebook_output_option"] = notebook_output_option
            if s3_kms_key_id is not None:
                self._values["s3_kms_key_id"] = s3_kms_key_id
            if s3_output_path is not None:
                self._values["s3_output_path"] = s3_output_path

        @builtins.property
        def notebook_output_option(self) -> typing.Optional[builtins.str]:
            '''``CfnUserProfile.SharingSettingsProperty.NotebookOutputOption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-sharingsettings.html#cfn-sagemaker-userprofile-sharingsettings-notebookoutputoption
            '''
            result = self._values.get("notebook_output_option")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''``CfnUserProfile.SharingSettingsProperty.S3KmsKeyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-sharingsettings.html#cfn-sagemaker-userprofile-sharingsettings-s3kmskeyid
            '''
            result = self._values.get("s3_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_output_path(self) -> typing.Optional[builtins.str]:
            '''``CfnUserProfile.SharingSettingsProperty.S3OutputPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-sharingsettings.html#cfn-sagemaker-userprofile-sharingsettings-s3outputpath
            '''
            result = self._values.get("s3_output_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SharingSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnUserProfile.UserSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "execution_role": "executionRole",
            "jupyter_server_app_settings": "jupyterServerAppSettings",
            "kernel_gateway_app_settings": "kernelGatewayAppSettings",
            "security_groups": "securityGroups",
            "sharing_settings": "sharingSettings",
        },
    )
    class UserSettingsProperty:
        def __init__(
            self,
            *,
            execution_role: typing.Optional[builtins.str] = None,
            jupyter_server_app_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.JupyterServerAppSettingsProperty"]] = None,
            kernel_gateway_app_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.KernelGatewayAppSettingsProperty"]] = None,
            security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
            sharing_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.SharingSettingsProperty"]] = None,
        ) -> None:
            '''
            :param execution_role: ``CfnUserProfile.UserSettingsProperty.ExecutionRole``.
            :param jupyter_server_app_settings: ``CfnUserProfile.UserSettingsProperty.JupyterServerAppSettings``.
            :param kernel_gateway_app_settings: ``CfnUserProfile.UserSettingsProperty.KernelGatewayAppSettings``.
            :param security_groups: ``CfnUserProfile.UserSettingsProperty.SecurityGroups``.
            :param sharing_settings: ``CfnUserProfile.UserSettingsProperty.SharingSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-usersettings.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if execution_role is not None:
                self._values["execution_role"] = execution_role
            if jupyter_server_app_settings is not None:
                self._values["jupyter_server_app_settings"] = jupyter_server_app_settings
            if kernel_gateway_app_settings is not None:
                self._values["kernel_gateway_app_settings"] = kernel_gateway_app_settings
            if security_groups is not None:
                self._values["security_groups"] = security_groups
            if sharing_settings is not None:
                self._values["sharing_settings"] = sharing_settings

        @builtins.property
        def execution_role(self) -> typing.Optional[builtins.str]:
            '''``CfnUserProfile.UserSettingsProperty.ExecutionRole``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-usersettings.html#cfn-sagemaker-userprofile-usersettings-executionrole
            '''
            result = self._values.get("execution_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def jupyter_server_app_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.JupyterServerAppSettingsProperty"]]:
            '''``CfnUserProfile.UserSettingsProperty.JupyterServerAppSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-usersettings.html#cfn-sagemaker-userprofile-usersettings-jupyterserverappsettings
            '''
            result = self._values.get("jupyter_server_app_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.JupyterServerAppSettingsProperty"]], result)

        @builtins.property
        def kernel_gateway_app_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.KernelGatewayAppSettingsProperty"]]:
            '''``CfnUserProfile.UserSettingsProperty.KernelGatewayAppSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-usersettings.html#cfn-sagemaker-userprofile-usersettings-kernelgatewayappsettings
            '''
            result = self._values.get("kernel_gateway_app_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.KernelGatewayAppSettingsProperty"]], result)

        @builtins.property
        def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnUserProfile.UserSettingsProperty.SecurityGroups``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-usersettings.html#cfn-sagemaker-userprofile-usersettings-securitygroups
            '''
            result = self._values.get("security_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def sharing_settings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.SharingSettingsProperty"]]:
            '''``CfnUserProfile.UserSettingsProperty.SharingSettings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-userprofile-usersettings.html#cfn-sagemaker-userprofile-usersettings-sharingsettings
            '''
            result = self._values.get("sharing_settings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnUserProfile.SharingSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnUserProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_id": "domainId",
        "user_profile_name": "userProfileName",
        "single_sign_on_user_identifier": "singleSignOnUserIdentifier",
        "single_sign_on_user_value": "singleSignOnUserValue",
        "tags": "tags",
        "user_settings": "userSettings",
    },
)
class CfnUserProfileProps:
    def __init__(
        self,
        *,
        domain_id: builtins.str,
        user_profile_name: builtins.str,
        single_sign_on_user_identifier: typing.Optional[builtins.str] = None,
        single_sign_on_user_value: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        user_settings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnUserProfile.UserSettingsProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::UserProfile``.

        :param domain_id: ``AWS::SageMaker::UserProfile.DomainId``.
        :param user_profile_name: ``AWS::SageMaker::UserProfile.UserProfileName``.
        :param single_sign_on_user_identifier: ``AWS::SageMaker::UserProfile.SingleSignOnUserIdentifier``.
        :param single_sign_on_user_value: ``AWS::SageMaker::UserProfile.SingleSignOnUserValue``.
        :param tags: ``AWS::SageMaker::UserProfile.Tags``.
        :param user_settings: ``AWS::SageMaker::UserProfile.UserSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "domain_id": domain_id,
            "user_profile_name": user_profile_name,
        }
        if single_sign_on_user_identifier is not None:
            self._values["single_sign_on_user_identifier"] = single_sign_on_user_identifier
        if single_sign_on_user_value is not None:
            self._values["single_sign_on_user_value"] = single_sign_on_user_value
        if tags is not None:
            self._values["tags"] = tags
        if user_settings is not None:
            self._values["user_settings"] = user_settings

    @builtins.property
    def domain_id(self) -> builtins.str:
        '''``AWS::SageMaker::UserProfile.DomainId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-domainid
        '''
        result = self._values.get("domain_id")
        assert result is not None, "Required property 'domain_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_profile_name(self) -> builtins.str:
        '''``AWS::SageMaker::UserProfile.UserProfileName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-userprofilename
        '''
        result = self._values.get("user_profile_name")
        assert result is not None, "Required property 'user_profile_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def single_sign_on_user_identifier(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::UserProfile.SingleSignOnUserIdentifier``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-singlesignonuseridentifier
        '''
        result = self._values.get("single_sign_on_user_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def single_sign_on_user_value(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::UserProfile.SingleSignOnUserValue``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-singlesignonuservalue
        '''
        result = self._values.get("single_sign_on_user_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::UserProfile.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def user_settings(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnUserProfile.UserSettingsProperty]]:
        '''``AWS::SageMaker::UserProfile.UserSettings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-userprofile.html#cfn-sagemaker-userprofile-usersettings
        '''
        result = self._values.get("user_settings")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnUserProfile.UserSettingsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnWorkteam(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sagemaker.CfnWorkteam",
):
    '''A CloudFormation ``AWS::SageMaker::Workteam``.

    :cloudformationResource: AWS::SageMaker::Workteam
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        member_definitions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.MemberDefinitionProperty"]]]] = None,
        notification_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.NotificationConfigurationProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        workteam_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::SageMaker::Workteam``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::SageMaker::Workteam.Description``.
        :param member_definitions: ``AWS::SageMaker::Workteam.MemberDefinitions``.
        :param notification_configuration: ``AWS::SageMaker::Workteam.NotificationConfiguration``.
        :param tags: ``AWS::SageMaker::Workteam.Tags``.
        :param workteam_name: ``AWS::SageMaker::Workteam.WorkteamName``.
        '''
        props = CfnWorkteamProps(
            description=description,
            member_definitions=member_definitions,
            notification_configuration=notification_configuration,
            tags=tags,
            workteam_name=workteam_name,
        )

        jsii.create(CfnWorkteam, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrWorkteamName")
    def attr_workteam_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: WorkteamName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkteamName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SageMaker::Workteam.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Workteam.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="memberDefinitions")
    def member_definitions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.MemberDefinitionProperty"]]]]:
        '''``AWS::SageMaker::Workteam.MemberDefinitions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-memberdefinitions
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.MemberDefinitionProperty"]]]], jsii.get(self, "memberDefinitions"))

    @member_definitions.setter
    def member_definitions(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.MemberDefinitionProperty"]]]],
    ) -> None:
        jsii.set(self, "memberDefinitions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="notificationConfiguration")
    def notification_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.NotificationConfigurationProperty"]]:
        '''``AWS::SageMaker::Workteam.NotificationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-notificationconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.NotificationConfigurationProperty"]], jsii.get(self, "notificationConfiguration"))

    @notification_configuration.setter
    def notification_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.NotificationConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "notificationConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="workteamName")
    def workteam_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Workteam.WorkteamName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-workteamname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workteamName"))

    @workteam_name.setter
    def workteam_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "workteamName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnWorkteam.CognitoMemberDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cognito_client_id": "cognitoClientId",
            "cognito_user_group": "cognitoUserGroup",
            "cognito_user_pool": "cognitoUserPool",
        },
    )
    class CognitoMemberDefinitionProperty:
        def __init__(
            self,
            *,
            cognito_client_id: builtins.str,
            cognito_user_group: builtins.str,
            cognito_user_pool: builtins.str,
        ) -> None:
            '''
            :param cognito_client_id: ``CfnWorkteam.CognitoMemberDefinitionProperty.CognitoClientId``.
            :param cognito_user_group: ``CfnWorkteam.CognitoMemberDefinitionProperty.CognitoUserGroup``.
            :param cognito_user_pool: ``CfnWorkteam.CognitoMemberDefinitionProperty.CognitoUserPool``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-cognitomemberdefinition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cognito_client_id": cognito_client_id,
                "cognito_user_group": cognito_user_group,
                "cognito_user_pool": cognito_user_pool,
            }

        @builtins.property
        def cognito_client_id(self) -> builtins.str:
            '''``CfnWorkteam.CognitoMemberDefinitionProperty.CognitoClientId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-cognitomemberdefinition.html#cfn-sagemaker-workteam-cognitomemberdefinition-cognitoclientid
            '''
            result = self._values.get("cognito_client_id")
            assert result is not None, "Required property 'cognito_client_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def cognito_user_group(self) -> builtins.str:
            '''``CfnWorkteam.CognitoMemberDefinitionProperty.CognitoUserGroup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-cognitomemberdefinition.html#cfn-sagemaker-workteam-cognitomemberdefinition-cognitousergroup
            '''
            result = self._values.get("cognito_user_group")
            assert result is not None, "Required property 'cognito_user_group' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def cognito_user_pool(self) -> builtins.str:
            '''``CfnWorkteam.CognitoMemberDefinitionProperty.CognitoUserPool``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-cognitomemberdefinition.html#cfn-sagemaker-workteam-cognitomemberdefinition-cognitouserpool
            '''
            result = self._values.get("cognito_user_pool")
            assert result is not None, "Required property 'cognito_user_pool' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CognitoMemberDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnWorkteam.MemberDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"cognito_member_definition": "cognitoMemberDefinition"},
    )
    class MemberDefinitionProperty:
        def __init__(
            self,
            *,
            cognito_member_definition: typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.CognitoMemberDefinitionProperty"],
        ) -> None:
            '''
            :param cognito_member_definition: ``CfnWorkteam.MemberDefinitionProperty.CognitoMemberDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-memberdefinition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cognito_member_definition": cognito_member_definition,
            }

        @builtins.property
        def cognito_member_definition(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.CognitoMemberDefinitionProperty"]:
            '''``CfnWorkteam.MemberDefinitionProperty.CognitoMemberDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-memberdefinition.html#cfn-sagemaker-workteam-memberdefinition-cognitomemberdefinition
            '''
            result = self._values.get("cognito_member_definition")
            assert result is not None, "Required property 'cognito_member_definition' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnWorkteam.CognitoMemberDefinitionProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MemberDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sagemaker.CfnWorkteam.NotificationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"notification_topic_arn": "notificationTopicArn"},
    )
    class NotificationConfigurationProperty:
        def __init__(self, *, notification_topic_arn: builtins.str) -> None:
            '''
            :param notification_topic_arn: ``CfnWorkteam.NotificationConfigurationProperty.NotificationTopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-notificationconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "notification_topic_arn": notification_topic_arn,
            }

        @builtins.property
        def notification_topic_arn(self) -> builtins.str:
            '''``CfnWorkteam.NotificationConfigurationProperty.NotificationTopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sagemaker-workteam-notificationconfiguration.html#cfn-sagemaker-workteam-notificationconfiguration-notificationtopicarn
            '''
            result = self._values.get("notification_topic_arn")
            assert result is not None, "Required property 'notification_topic_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sagemaker.CfnWorkteamProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "member_definitions": "memberDefinitions",
        "notification_configuration": "notificationConfiguration",
        "tags": "tags",
        "workteam_name": "workteamName",
    },
)
class CfnWorkteamProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        member_definitions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnWorkteam.MemberDefinitionProperty]]]] = None,
        notification_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnWorkteam.NotificationConfigurationProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        workteam_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SageMaker::Workteam``.

        :param description: ``AWS::SageMaker::Workteam.Description``.
        :param member_definitions: ``AWS::SageMaker::Workteam.MemberDefinitions``.
        :param notification_configuration: ``AWS::SageMaker::Workteam.NotificationConfiguration``.
        :param tags: ``AWS::SageMaker::Workteam.Tags``.
        :param workteam_name: ``AWS::SageMaker::Workteam.WorkteamName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if member_definitions is not None:
            self._values["member_definitions"] = member_definitions
        if notification_configuration is not None:
            self._values["notification_configuration"] = notification_configuration
        if tags is not None:
            self._values["tags"] = tags
        if workteam_name is not None:
            self._values["workteam_name"] = workteam_name

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Workteam.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def member_definitions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnWorkteam.MemberDefinitionProperty]]]]:
        '''``AWS::SageMaker::Workteam.MemberDefinitions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-memberdefinitions
        '''
        result = self._values.get("member_definitions")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnWorkteam.MemberDefinitionProperty]]]], result)

    @builtins.property
    def notification_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnWorkteam.NotificationConfigurationProperty]]:
        '''``AWS::SageMaker::Workteam.NotificationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-notificationconfiguration
        '''
        result = self._values.get("notification_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnWorkteam.NotificationConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SageMaker::Workteam.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def workteam_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SageMaker::Workteam.WorkteamName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html#cfn-sagemaker-workteam-workteamname
        '''
        result = self._values.get("workteam_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkteamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApp",
    "CfnAppImageConfig",
    "CfnAppImageConfigProps",
    "CfnAppProps",
    "CfnCodeRepository",
    "CfnCodeRepositoryProps",
    "CfnDataQualityJobDefinition",
    "CfnDataQualityJobDefinitionProps",
    "CfnDevice",
    "CfnDeviceFleet",
    "CfnDeviceFleetProps",
    "CfnDeviceProps",
    "CfnDomain",
    "CfnDomainProps",
    "CfnEndpoint",
    "CfnEndpointConfig",
    "CfnEndpointConfigProps",
    "CfnEndpointProps",
    "CfnFeatureGroup",
    "CfnFeatureGroupProps",
    "CfnImage",
    "CfnImageProps",
    "CfnImageVersion",
    "CfnImageVersionProps",
    "CfnModel",
    "CfnModelBiasJobDefinition",
    "CfnModelBiasJobDefinitionProps",
    "CfnModelExplainabilityJobDefinition",
    "CfnModelExplainabilityJobDefinitionProps",
    "CfnModelPackageGroup",
    "CfnModelPackageGroupProps",
    "CfnModelProps",
    "CfnModelQualityJobDefinition",
    "CfnModelQualityJobDefinitionProps",
    "CfnMonitoringSchedule",
    "CfnMonitoringScheduleProps",
    "CfnNotebookInstance",
    "CfnNotebookInstanceLifecycleConfig",
    "CfnNotebookInstanceLifecycleConfigProps",
    "CfnNotebookInstanceProps",
    "CfnPipeline",
    "CfnPipelineProps",
    "CfnProject",
    "CfnProjectProps",
    "CfnUserProfile",
    "CfnUserProfileProps",
    "CfnWorkteam",
    "CfnWorkteamProps",
]

publication.publish()
