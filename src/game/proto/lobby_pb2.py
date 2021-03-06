# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lobby.proto

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
  name='lobby.proto',
  package='msg',
  serialized_pb=_b('\n\x0blobby.proto\x12\x03msg\"\x1d\n\x0cReadyRequest\x12\r\n\x05token\x18\x01 \x02(\t\"\x1f\n\rReadyResponse\x12\x0e\n\x06result\x18\x01 \x02(\x0c\"&\n\x13\x45nterBattleResponse\x12\x0f\n\x07\x63hannel\x18\x01 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_READYREQUEST = _descriptor.Descriptor(
  name='ReadyRequest',
  full_name='msg.ReadyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='msg.ReadyRequest.token', index=0,
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
  serialized_start=20,
  serialized_end=49,
)


_READYRESPONSE = _descriptor.Descriptor(
  name='ReadyResponse',
  full_name='msg.ReadyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='msg.ReadyResponse.result', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=51,
  serialized_end=82,
)


_ENTERBATTLERESPONSE = _descriptor.Descriptor(
  name='EnterBattleResponse',
  full_name='msg.EnterBattleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='msg.EnterBattleResponse.channel', index=0,
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
  serialized_start=84,
  serialized_end=122,
)

DESCRIPTOR.message_types_by_name['ReadyRequest'] = _READYREQUEST
DESCRIPTOR.message_types_by_name['ReadyResponse'] = _READYRESPONSE
DESCRIPTOR.message_types_by_name['EnterBattleResponse'] = _ENTERBATTLERESPONSE

ReadyRequest = _reflection.GeneratedProtocolMessageType('ReadyRequest', (_message.Message,), dict(
  DESCRIPTOR = _READYREQUEST,
  __module__ = 'lobby_pb2'
  # @@protoc_insertion_point(class_scope:msg.ReadyRequest)
  ))
_sym_db.RegisterMessage(ReadyRequest)

ReadyResponse = _reflection.GeneratedProtocolMessageType('ReadyResponse', (_message.Message,), dict(
  DESCRIPTOR = _READYRESPONSE,
  __module__ = 'lobby_pb2'
  # @@protoc_insertion_point(class_scope:msg.ReadyResponse)
  ))
_sym_db.RegisterMessage(ReadyResponse)

EnterBattleResponse = _reflection.GeneratedProtocolMessageType('EnterBattleResponse', (_message.Message,), dict(
  DESCRIPTOR = _ENTERBATTLERESPONSE,
  __module__ = 'lobby_pb2'
  # @@protoc_insertion_point(class_scope:msg.EnterBattleResponse)
  ))
_sym_db.RegisterMessage(EnterBattleResponse)


# @@protoc_insertion_point(module_scope)
