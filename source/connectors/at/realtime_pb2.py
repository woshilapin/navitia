# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import type_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='realtime.proto',
  package='pbnavitia.realtime',
  serialized_pb='\n\x0erealtime.proto\x12\x12pbnavitia.realtime\x1a\ntype.proto\"K\n\x08TCObject\x12\x12\n\nobject_uri\x18\x01 \x01(\t\x12+\n\x0bobject_type\x18\x02 \x01(\x0e\x32\x16.pbnavitia.NavitiaType\"A\n\x10LocalizedMessage\x12\x10\n\x08language\x18\x01 \x02(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"\xe1\x02\n\x07Message\x12\x0b\n\x03uri\x18\x01 \x02(\t\x12,\n\x06object\x18\x02 \x02(\x0b\x32\x1c.pbnavitia.realtime.TCObject\x12\x1e\n\x16start_publication_date\x18\x03 \x01(\x04\x12\x1c\n\x14\x65nd_publication_date\x18\x04 \x01(\x04\x12\x1e\n\x16start_application_date\x18\x05 \x01(\x04\x12\x1c\n\x14\x65nd_application_date\x18\x06 \x01(\x04\x12$\n\x1cstart_application_daily_hour\x18\x07 \x01(\r\x12\"\n\x1a\x65nd_application_daily_hour\x18\x08 \x01(\r\x12\x13\n\x0b\x61\x63tive_days\x18\t \x01(\t\x12@\n\x12localized_messages\x18\n \x03(\x0b\x32$.pbnavitia.realtime.LocalizedMessage\"\xe8\x01\n\x0e\x41tPerturbation\x12\x0b\n\x03uri\x18\x01 \x02(\t\x12,\n\x06object\x18\x02 \x02(\x0b\x32\x1c.pbnavitia.realtime.TCObject\x12\x1e\n\x16start_application_date\x18\x03 \x01(\x04\x12\x1c\n\x14\x65nd_application_date\x18\x04 \x01(\x04\x12$\n\x1cstart_application_daily_hour\x18\x05 \x01(\r\x12\"\n\x1a\x65nd_application_daily_hour\x18\x06 \x01(\r\x12\x13\n\x0b\x61\x63tive_days\x18\x07 \x01(\t')




_TCOBJECT = descriptor.Descriptor(
  name='TCObject',
  full_name='pbnavitia.realtime.TCObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='object_uri', full_name='pbnavitia.realtime.TCObject.object_uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='object_type', full_name='pbnavitia.realtime.TCObject.object_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
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
  serialized_start=50,
  serialized_end=125,
)


_LOCALIZEDMESSAGE = descriptor.Descriptor(
  name='LocalizedMessage',
  full_name='pbnavitia.realtime.LocalizedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='language', full_name='pbnavitia.realtime.LocalizedMessage.language', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='body', full_name='pbnavitia.realtime.LocalizedMessage.body', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='title', full_name='pbnavitia.realtime.LocalizedMessage.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=127,
  serialized_end=192,
)


_MESSAGE = descriptor.Descriptor(
  name='Message',
  full_name='pbnavitia.realtime.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='uri', full_name='pbnavitia.realtime.Message.uri', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='object', full_name='pbnavitia.realtime.Message.object', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='start_publication_date', full_name='pbnavitia.realtime.Message.start_publication_date', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='end_publication_date', full_name='pbnavitia.realtime.Message.end_publication_date', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='start_application_date', full_name='pbnavitia.realtime.Message.start_application_date', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='end_application_date', full_name='pbnavitia.realtime.Message.end_application_date', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='start_application_daily_hour', full_name='pbnavitia.realtime.Message.start_application_daily_hour', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='end_application_daily_hour', full_name='pbnavitia.realtime.Message.end_application_daily_hour', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='active_days', full_name='pbnavitia.realtime.Message.active_days', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='localized_messages', full_name='pbnavitia.realtime.Message.localized_messages', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=195,
  serialized_end=548,
)


_ATPERTURBATION = descriptor.Descriptor(
  name='AtPerturbation',
  full_name='pbnavitia.realtime.AtPerturbation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='uri', full_name='pbnavitia.realtime.AtPerturbation.uri', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='object', full_name='pbnavitia.realtime.AtPerturbation.object', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='start_application_date', full_name='pbnavitia.realtime.AtPerturbation.start_application_date', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='end_application_date', full_name='pbnavitia.realtime.AtPerturbation.end_application_date', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='start_application_daily_hour', full_name='pbnavitia.realtime.AtPerturbation.start_application_daily_hour', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='end_application_daily_hour', full_name='pbnavitia.realtime.AtPerturbation.end_application_daily_hour', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='active_days', full_name='pbnavitia.realtime.AtPerturbation.active_days', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=551,
  serialized_end=783,
)

_TCOBJECT.fields_by_name['object_type'].enum_type = type_pb2._NAVITIATYPE
_MESSAGE.fields_by_name['object'].message_type = _TCOBJECT
_MESSAGE.fields_by_name['localized_messages'].message_type = _LOCALIZEDMESSAGE
_ATPERTURBATION.fields_by_name['object'].message_type = _TCOBJECT
DESCRIPTOR.message_types_by_name['TCObject'] = _TCOBJECT
DESCRIPTOR.message_types_by_name['LocalizedMessage'] = _LOCALIZEDMESSAGE
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['AtPerturbation'] = _ATPERTURBATION

class TCObject(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TCOBJECT
  
  # @@protoc_insertion_point(class_scope:pbnavitia.realtime.TCObject)

class LocalizedMessage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOCALIZEDMESSAGE
  
  # @@protoc_insertion_point(class_scope:pbnavitia.realtime.LocalizedMessage)

class Message(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MESSAGE
  
  # @@protoc_insertion_point(class_scope:pbnavitia.realtime.Message)

class AtPerturbation(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ATPERTURBATION
  
  # @@protoc_insertion_point(class_scope:pbnavitia.realtime.AtPerturbation)

# @@protoc_insertion_point(module_scope)