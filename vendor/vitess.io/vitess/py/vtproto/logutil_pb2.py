# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logutil.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='logutil.proto',
  package='logutil',
  syntax='proto3',
  serialized_pb=_b('\n\rlogutil.proto\x12\x07logutil\",\n\x04Time\x12\x0f\n\x07seconds\x18\x01 \x01(\x03\x12\x13\n\x0bnanoseconds\x18\x02 \x01(\x05\"n\n\x05\x45vent\x12\x1b\n\x04time\x18\x01 \x01(\x0b\x32\r.logutil.Time\x12\x1d\n\x05level\x18\x02 \x01(\x0e\x32\x0e.logutil.Level\x12\x0c\n\x04\x66ile\x18\x03 \x01(\t\x12\x0c\n\x04line\x18\x04 \x01(\x03\x12\r\n\x05value\x18\x05 \x01(\t*6\n\x05Level\x12\x08\n\x04INFO\x10\x00\x12\x0b\n\x07WARNING\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\x0b\n\x07\x43ONSOLE\x10\x03\x42&Z$vitess.io/vitess/go/vt/proto/logutilb\x06proto3')
)

_LEVEL = _descriptor.EnumDescriptor(
  name='Level',
  full_name='logutil.Level',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INFO', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONSOLE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=184,
  serialized_end=238,
)
_sym_db.RegisterEnumDescriptor(_LEVEL)

Level = enum_type_wrapper.EnumTypeWrapper(_LEVEL)
INFO = 0
WARNING = 1
ERROR = 2
CONSOLE = 3



_TIME = _descriptor.Descriptor(
  name='Time',
  full_name='logutil.Time',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seconds', full_name='logutil.Time.seconds', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nanoseconds', full_name='logutil.Time.nanoseconds', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=70,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='logutil.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='logutil.Event.time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='logutil.Event.level', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file', full_name='logutil.Event.file', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='line', full_name='logutil.Event.line', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='logutil.Event.value', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=182,
)

_EVENT.fields_by_name['time'].message_type = _TIME
_EVENT.fields_by_name['level'].enum_type = _LEVEL
DESCRIPTOR.message_types_by_name['Time'] = _TIME
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.enum_types_by_name['Level'] = _LEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Time = _reflection.GeneratedProtocolMessageType('Time', (_message.Message,), dict(
  DESCRIPTOR = _TIME,
  __module__ = 'logutil_pb2'
  # @@protoc_insertion_point(class_scope:logutil.Time)
  ))
_sym_db.RegisterMessage(Time)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
  DESCRIPTOR = _EVENT,
  __module__ = 'logutil_pb2'
  # @@protoc_insertion_point(class_scope:logutil.Event)
  ))
_sym_db.RegisterMessage(Event)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z$vitess.io/vitess/go/vt/proto/logutil'))
# @@protoc_insertion_point(module_scope)
