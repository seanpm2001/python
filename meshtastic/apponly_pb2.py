# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apponly.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import channel_pb2 as channel__pb2
from . import config_pb2 as config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rapponly.proto\x1a\rchannel.proto\x1a\x0c\x63onfig.proto\"Y\n\nChannelSet\x12\"\n\x08settings\x18\x01 \x03(\x0b\x32\x10.ChannelSettings\x12\'\n\x0blora_config\x18\x02 \x01(\x0b\x32\x12.Config.LoRaConfigBJ\n\x13\x63om.geeksville.meshB\rAppOnlyProtosH\x03Z\"github.com/meshtastic/go/generatedb\x06proto3')



_CHANNELSET = DESCRIPTOR.message_types_by_name['ChannelSet']
ChannelSet = _reflection.GeneratedProtocolMessageType('ChannelSet', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELSET,
  '__module__' : 'apponly_pb2'
  # @@protoc_insertion_point(class_scope:ChannelSet)
  })
_sym_db.RegisterMessage(ChannelSet)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\rAppOnlyProtosH\003Z\"github.com/meshtastic/go/generated'
  _CHANNELSET._serialized_start=46
  _CHANNELSET._serialized_end=135
# @@protoc_insertion_point(module_scope)
