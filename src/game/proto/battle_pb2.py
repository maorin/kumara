# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: battle.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='battle.proto',
  package='msg',
  serialized_pb=_b('\n\x0c\x62\x61ttle.proto\x12\x03msg\"&\n\x11\x63\x64\x63ompleteRequest\x12\x11\n\tuser_name\x18\x01 \x02(\t\"7\n\x12\x63\x64\x63ompleteResponse\x12\x0e\n\x06result\x18\x01 \x02(\x0c\x12\x11\n\tuser_name\x18\x02 \x02(\t\"\x1e\n\tgoRequest\x12\x11\n\tuser_name\x18\x01 \x02(\t\"/\n\ngoResponse\x12\x0e\n\x06result\x18\x01 \x02(\x0c\x12\x11\n\tuser_name\x18\x02 \x02(\t\" \n\x0b\x66ireRequest\x12\x11\n\tuser_name\x18\x01 \x02(\t\"1\n\x0c\x66ireResponse\x12\x0e\n\x06result\x18\x01 \x02(\x0c\x12\x11\n\tuser_name\x18\x02 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CDCOMPLETEREQUEST = _descriptor.Descriptor(
  name='cdcompleteRequest',
  full_name='msg.cdcompleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name', full_name='msg.cdcompleteRequest.user_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=59,
)


_CDCOMPLETERESPONSE = _descriptor.Descriptor(
  name='cdcompleteResponse',
  full_name='msg.cdcompleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='msg.cdcompleteResponse.result', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='msg.cdcompleteResponse.user_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=116,
)


_GOREQUEST = _descriptor.Descriptor(
  name='goRequest',
  full_name='msg.goRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name', full_name='msg.goRequest.user_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=148,
)


_GORESPONSE = _descriptor.Descriptor(
  name='goResponse',
  full_name='msg.goResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='msg.goResponse.result', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='msg.goResponse.user_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=197,
)


_FIREREQUEST = _descriptor.Descriptor(
  name='fireRequest',
  full_name='msg.fireRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_name', full_name='msg.fireRequest.user_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=199,
  serialized_end=231,
)


_FIRERESPONSE = _descriptor.Descriptor(
  name='fireResponse',
  full_name='msg.fireResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='msg.fireResponse.result', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='msg.fireResponse.user_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=282,
)

DESCRIPTOR.message_types_by_name['cdcompleteRequest'] = _CDCOMPLETEREQUEST
DESCRIPTOR.message_types_by_name['cdcompleteResponse'] = _CDCOMPLETERESPONSE
DESCRIPTOR.message_types_by_name['goRequest'] = _GOREQUEST
DESCRIPTOR.message_types_by_name['goResponse'] = _GORESPONSE
DESCRIPTOR.message_types_by_name['fireRequest'] = _FIREREQUEST
DESCRIPTOR.message_types_by_name['fireResponse'] = _FIRERESPONSE

cdcompleteRequest = _reflection.GeneratedProtocolMessageType('cdcompleteRequest', (_message.Message,), dict(
  DESCRIPTOR = _CDCOMPLETEREQUEST,
  __module__ = 'battle_pb2'
  # @@protoc_insertion_point(class_scope:msg.cdcompleteRequest)
  ))
_sym_db.RegisterMessage(cdcompleteRequest)

cdcompleteResponse = _reflection.GeneratedProtocolMessageType('cdcompleteResponse', (_message.Message,), dict(
  DESCRIPTOR = _CDCOMPLETERESPONSE,
  __module__ = 'battle_pb2'
  # @@protoc_insertion_point(class_scope:msg.cdcompleteResponse)
  ))
_sym_db.RegisterMessage(cdcompleteResponse)

goRequest = _reflection.GeneratedProtocolMessageType('goRequest', (_message.Message,), dict(
  DESCRIPTOR = _GOREQUEST,
  __module__ = 'battle_pb2'
  # @@protoc_insertion_point(class_scope:msg.goRequest)
  ))
_sym_db.RegisterMessage(goRequest)

goResponse = _reflection.GeneratedProtocolMessageType('goResponse', (_message.Message,), dict(
  DESCRIPTOR = _GORESPONSE,
  __module__ = 'battle_pb2'
  # @@protoc_insertion_point(class_scope:msg.goResponse)
  ))
_sym_db.RegisterMessage(goResponse)

fireRequest = _reflection.GeneratedProtocolMessageType('fireRequest', (_message.Message,), dict(
  DESCRIPTOR = _FIREREQUEST,
  __module__ = 'battle_pb2'
  # @@protoc_insertion_point(class_scope:msg.fireRequest)
  ))
_sym_db.RegisterMessage(fireRequest)

fireResponse = _reflection.GeneratedProtocolMessageType('fireResponse', (_message.Message,), dict(
  DESCRIPTOR = _FIRERESPONSE,
  __module__ = 'battle_pb2'
  # @@protoc_insertion_point(class_scope:msg.fireResponse)
  ))
_sym_db.RegisterMessage(fireResponse)


# @@protoc_insertion_point(module_scope)
