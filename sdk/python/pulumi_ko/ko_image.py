# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['KoImageArgs', 'KoImage']

@pulumi.input_type
class KoImageArgs:
    def __init__(__self__, *,
                 importpath: pulumi.Input[str],
                 base_image: Optional[pulumi.Input[str]] = None,
                 platforms: Optional[pulumi.Input[str]] = None,
                 working_dir: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a KoImage resource.
        :param pulumi.Input[str] importpath: import path to build
        :param pulumi.Input[str] base_image: base image to use
        :param pulumi.Input[str] platforms: platforms to build
        :param pulumi.Input[str] working_dir: working directory for the build
        """
        pulumi.set(__self__, "importpath", importpath)
        if base_image is not None:
            pulumi.set(__self__, "base_image", base_image)
        if platforms is not None:
            pulumi.set(__self__, "platforms", platforms)
        if working_dir is not None:
            pulumi.set(__self__, "working_dir", working_dir)

    @property
    @pulumi.getter
    def importpath(self) -> pulumi.Input[str]:
        """
        import path to build
        """
        return pulumi.get(self, "importpath")

    @importpath.setter
    def importpath(self, value: pulumi.Input[str]):
        pulumi.set(self, "importpath", value)

    @property
    @pulumi.getter(name="baseImage")
    def base_image(self) -> Optional[pulumi.Input[str]]:
        """
        base image to use
        """
        return pulumi.get(self, "base_image")

    @base_image.setter
    def base_image(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_image", value)

    @property
    @pulumi.getter
    def platforms(self) -> Optional[pulumi.Input[str]]:
        """
        platforms to build
        """
        return pulumi.get(self, "platforms")

    @platforms.setter
    def platforms(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "platforms", value)

    @property
    @pulumi.getter(name="workingDir")
    def working_dir(self) -> Optional[pulumi.Input[str]]:
        """
        working directory for the build
        """
        return pulumi.get(self, "working_dir")

    @working_dir.setter
    def working_dir(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "working_dir", value)


@pulumi.input_type
class _KoImageState:
    def __init__(__self__, *,
                 base_image: Optional[pulumi.Input[str]] = None,
                 image_ref: Optional[pulumi.Input[str]] = None,
                 importpath: Optional[pulumi.Input[str]] = None,
                 platforms: Optional[pulumi.Input[str]] = None,
                 working_dir: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering KoImage resources.
        :param pulumi.Input[str] base_image: base image to use
        :param pulumi.Input[str] image_ref: built image reference by digest
        :param pulumi.Input[str] importpath: import path to build
        :param pulumi.Input[str] platforms: platforms to build
        :param pulumi.Input[str] working_dir: working directory for the build
        """
        if base_image is not None:
            pulumi.set(__self__, "base_image", base_image)
        if image_ref is not None:
            pulumi.set(__self__, "image_ref", image_ref)
        if importpath is not None:
            pulumi.set(__self__, "importpath", importpath)
        if platforms is not None:
            pulumi.set(__self__, "platforms", platforms)
        if working_dir is not None:
            pulumi.set(__self__, "working_dir", working_dir)

    @property
    @pulumi.getter(name="baseImage")
    def base_image(self) -> Optional[pulumi.Input[str]]:
        """
        base image to use
        """
        return pulumi.get(self, "base_image")

    @base_image.setter
    def base_image(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_image", value)

    @property
    @pulumi.getter(name="imageRef")
    def image_ref(self) -> Optional[pulumi.Input[str]]:
        """
        built image reference by digest
        """
        return pulumi.get(self, "image_ref")

    @image_ref.setter
    def image_ref(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_ref", value)

    @property
    @pulumi.getter
    def importpath(self) -> Optional[pulumi.Input[str]]:
        """
        import path to build
        """
        return pulumi.get(self, "importpath")

    @importpath.setter
    def importpath(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "importpath", value)

    @property
    @pulumi.getter
    def platforms(self) -> Optional[pulumi.Input[str]]:
        """
        platforms to build
        """
        return pulumi.get(self, "platforms")

    @platforms.setter
    def platforms(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "platforms", value)

    @property
    @pulumi.getter(name="workingDir")
    def working_dir(self) -> Optional[pulumi.Input[str]]:
        """
        working directory for the build
        """
        return pulumi.get(self, "working_dir")

    @working_dir.setter
    def working_dir(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "working_dir", value)


class KoImage(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_image: Optional[pulumi.Input[str]] = None,
                 importpath: Optional[pulumi.Input[str]] = None,
                 platforms: Optional[pulumi.Input[str]] = None,
                 working_dir: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a KoImage resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base_image: base image to use
        :param pulumi.Input[str] importpath: import path to build
        :param pulumi.Input[str] platforms: platforms to build
        :param pulumi.Input[str] working_dir: working directory for the build
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KoImageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a KoImage resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param KoImageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KoImageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_image: Optional[pulumi.Input[str]] = None,
                 importpath: Optional[pulumi.Input[str]] = None,
                 platforms: Optional[pulumi.Input[str]] = None,
                 working_dir: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KoImageArgs.__new__(KoImageArgs)

            __props__.__dict__["base_image"] = base_image
            if importpath is None and not opts.urn:
                raise TypeError("Missing required property 'importpath'")
            __props__.__dict__["importpath"] = importpath
            __props__.__dict__["platforms"] = platforms
            __props__.__dict__["working_dir"] = working_dir
            __props__.__dict__["image_ref"] = None
        super(KoImage, __self__).__init__(
            'ko:index/koImage:KoImage',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            base_image: Optional[pulumi.Input[str]] = None,
            image_ref: Optional[pulumi.Input[str]] = None,
            importpath: Optional[pulumi.Input[str]] = None,
            platforms: Optional[pulumi.Input[str]] = None,
            working_dir: Optional[pulumi.Input[str]] = None) -> 'KoImage':
        """
        Get an existing KoImage resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base_image: base image to use
        :param pulumi.Input[str] image_ref: built image reference by digest
        :param pulumi.Input[str] importpath: import path to build
        :param pulumi.Input[str] platforms: platforms to build
        :param pulumi.Input[str] working_dir: working directory for the build
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KoImageState.__new__(_KoImageState)

        __props__.__dict__["base_image"] = base_image
        __props__.__dict__["image_ref"] = image_ref
        __props__.__dict__["importpath"] = importpath
        __props__.__dict__["platforms"] = platforms
        __props__.__dict__["working_dir"] = working_dir
        return KoImage(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="baseImage")
    def base_image(self) -> pulumi.Output[Optional[str]]:
        """
        base image to use
        """
        return pulumi.get(self, "base_image")

    @property
    @pulumi.getter(name="imageRef")
    def image_ref(self) -> pulumi.Output[str]:
        """
        built image reference by digest
        """
        return pulumi.get(self, "image_ref")

    @property
    @pulumi.getter
    def importpath(self) -> pulumi.Output[str]:
        """
        import path to build
        """
        return pulumi.get(self, "importpath")

    @property
    @pulumi.getter
    def platforms(self) -> pulumi.Output[Optional[str]]:
        """
        platforms to build
        """
        return pulumi.get(self, "platforms")

    @property
    @pulumi.getter(name="workingDir")
    def working_dir(self) -> pulumi.Output[Optional[str]]:
        """
        working directory for the build
        """
        return pulumi.get(self, "working_dir")

