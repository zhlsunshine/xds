# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: udpa/annotations/status.proto
# Protobuf Python Version: 5.29.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    1,
    '',
    'udpa/annotations/status.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dudpa/annotations/status.proto\x12\x10udpa.annotations\x1a google/protobuf/descriptor.proto\"t\n\x10StatusAnnotation\x12\x18\n\x10work_in_progress\x18\x01 \x01(\x08\x12\x46\n\x16package_version_status\x18\x02 \x01(\x0e\x32&.udpa.annotations.PackageVersionStatus*]\n\x14PackageVersionStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x46ROZEN\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12 \n\x1cNEXT_MAJOR_VERSION_CANDIDATE\x10\x03:X\n\x0b\x66ile_status\x12\x1c.google.protobuf.FileOptions\x18\x87\x80\x99j \x01(\x0b\x32\".udpa.annotations.StatusAnnotationB)Z\'github.com/cncf/xds/go/udpa/annotationsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'udpa.annotations.status_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\'github.com/cncf/xds/go/udpa/annotations'
  _globals['_PACKAGEVERSIONSTATUS']._serialized_start=203
  _globals['_PACKAGEVERSIONSTATUS']._serialized_end=296
  _globals['_STATUSANNOTATION']._serialized_start=85
  _globals['_STATUSANNOTATION']._serialized_end=201
# @@protoc_insertion_point(module_scope)
