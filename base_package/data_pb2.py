# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='data.proto',
  package='base_package',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ndata.proto\x12\x0c\x62\x61se_package\"\x1d\n\ractionrequest\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x1e\n\x0e\x61\x63tionresponse\x12\x0c\n\x04text\x18\x01 \x01(\t2U\n\nFormatData\x12G\n\x08\x44oFormat\x12\x1b.base_package.actionrequest\x1a\x1c.base_package.actionresponse\"\x00\x62\x06proto3')
)




_ACTIONREQUEST = _descriptor.Descriptor(
  name='actionrequest',
  full_name='base_package.actionrequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='base_package.actionrequest.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=57,
)


_ACTIONRESPONSE = _descriptor.Descriptor(
  name='actionresponse',
  full_name='base_package.actionresponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='base_package.actionresponse.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['actionrequest'] = _ACTIONREQUEST
DESCRIPTOR.message_types_by_name['actionresponse'] = _ACTIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

actionrequest = _reflection.GeneratedProtocolMessageType('actionrequest', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONREQUEST,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:base_package.actionrequest)
  })
_sym_db.RegisterMessage(actionrequest)

actionresponse = _reflection.GeneratedProtocolMessageType('actionresponse', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONRESPONSE,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:base_package.actionresponse)
  })
_sym_db.RegisterMessage(actionresponse)



_FORMATDATA = _descriptor.ServiceDescriptor(
  name='FormatData',
  full_name='base_package.FormatData',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=91,
  serialized_end=176,
  methods=[
  _descriptor.MethodDescriptor(
    name='DoFormat',
    full_name='base_package.FormatData.DoFormat',
    index=0,
    containing_service=None,
    input_type=_ACTIONREQUEST,
    output_type=_ACTIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FORMATDATA)

DESCRIPTOR.services_by_name['FormatData'] = _FORMATDATA

# @@protoc_insertion_point(module_scope)