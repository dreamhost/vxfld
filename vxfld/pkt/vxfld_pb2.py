# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='vxfld.proto',
  package='',
  serialized_pb='\n\x0bvxfld.proto\"\"\n\x0bIPv4Address\x12\x13\n\x07\x61\x64\x64ress\x18\x01 \x03(\rB\x02\x10\x01\"\xa6\x01\n\x05Proxy\x12\x0e\n\x03ttl\x18\x01 \x01(\r:\x01\x34\x12\x15\n\nproxy_hops\x18\x02 \x01(\r:\x01\x30\x12\x12\n\x07srcport\x18\x03 \x01(\r:\x01\x30\x12\x1d\n\x07srcip_n\x18\x04 \x01(\x0b\x32\x0c.IPv4Address\x12\x0f\n\x04\x61rea\x18\x05 \x01(\r:\x01\x30\x12\x1f\n\tproxy_ips\x18\x06 \x03(\x0b\x32\x0c.IPv4Address\x12\x11\n\tvxlan_pkt\x18\x07 \x01(\x0c\"\xf6\x01\n\x07Refresh\x12\x19\n\noriginator\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x14\n\x08holdtime\x18\x02 \x01(\r:\x02\x39\x30\x12\x18\n\rresponse_type\x18\x03 \x01(\r:\x01\x30\x12\x15\n\nidentifier\x18\x04 \x01(\x04:\x01\x30\x12\x1f\n\x05vteps\x18\x05 \x03(\x0b\x32\x10.Refresh.VniDict\x1ah\n\x07VniDict\x12\x0b\n\x03vni\x18\x01 \x02(\r\x12&\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x18.Refresh.VniDict.VniData\x1a(\n\x07VniData\x12\x1d\n\x07ip_addr\x18\x01 \x02(\x0b\x32\x0c.IPv4Address\"\xd0\x01\n\x04Sync\x12\x15\n\nidentifier\x18\x01 \x01(\x04:\x01\x30\x12\x1c\n\x05vteps\x18\x02 \x03(\x0b\x32\r.Sync.VniDict\x1a\x92\x01\n\x07VniDict\x12\x0b\n\x03vni\x18\x01 \x02(\r\x12#\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x15.Sync.VniDict.VniData\x1aU\n\x07VniData\x12\x1d\n\x07ip_addr\x18\x01 \x02(\x0b\x32\x0c.IPv4Address\x12\x14\n\x08holdtime\x18\x02 \x01(\r:\x02\x39\x30\x12\x15\n\nidentifier\x18\x03 \x01(\x04:\x01\x30')




_IPV4ADDRESS = descriptor.Descriptor(
  name='IPv4Address',
  full_name='IPv4Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='address', full_name='IPv4Address.address', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=15,
  serialized_end=49,
)


_PROXY = descriptor.Descriptor(
  name='Proxy',
  full_name='Proxy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ttl', full_name='Proxy.ttl', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=4,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='proxy_hops', full_name='Proxy.proxy_hops', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='srcport', full_name='Proxy.srcport', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='srcip_n', full_name='Proxy.srcip_n', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='area', full_name='Proxy.area', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='proxy_ips', full_name='Proxy.proxy_ips', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vxlan_pkt', full_name='Proxy.vxlan_pkt', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  serialized_start=52,
  serialized_end=218,
)


_REFRESH_VNIDICT_VNIDATA = descriptor.Descriptor(
  name='VniData',
  full_name='Refresh.VniDict.VniData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ip_addr', full_name='Refresh.VniDict.VniData.ip_addr', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=427,
  serialized_end=467,
)

_REFRESH_VNIDICT = descriptor.Descriptor(
  name='VniDict',
  full_name='Refresh.VniDict',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='vni', full_name='Refresh.VniDict.vni', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='Refresh.VniDict.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REFRESH_VNIDICT_VNIDATA, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=363,
  serialized_end=467,
)

_REFRESH = descriptor.Descriptor(
  name='Refresh',
  full_name='Refresh',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='originator', full_name='Refresh.originator', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='holdtime', full_name='Refresh.holdtime', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=90,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='response_type', full_name='Refresh.response_type', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='identifier', full_name='Refresh.identifier', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vteps', full_name='Refresh.vteps', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REFRESH_VNIDICT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=221,
  serialized_end=467,
)


_SYNC_VNIDICT_VNIDATA = descriptor.Descriptor(
  name='VniData',
  full_name='Sync.VniDict.VniData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ip_addr', full_name='Sync.VniDict.VniData.ip_addr', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='holdtime', full_name='Sync.VniDict.VniData.holdtime', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=90,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='identifier', full_name='Sync.VniDict.VniData.identifier', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=593,
  serialized_end=678,
)

_SYNC_VNIDICT = descriptor.Descriptor(
  name='VniDict',
  full_name='Sync.VniDict',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='vni', full_name='Sync.VniDict.vni', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='Sync.VniDict.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SYNC_VNIDICT_VNIDATA, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=532,
  serialized_end=678,
)

_SYNC = descriptor.Descriptor(
  name='Sync',
  full_name='Sync',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='identifier', full_name='Sync.identifier', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vteps', full_name='Sync.vteps', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SYNC_VNIDICT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=470,
  serialized_end=678,
)

_PROXY.fields_by_name['srcip_n'].message_type = _IPV4ADDRESS
_PROXY.fields_by_name['proxy_ips'].message_type = _IPV4ADDRESS
_REFRESH_VNIDICT_VNIDATA.fields_by_name['ip_addr'].message_type = _IPV4ADDRESS
_REFRESH_VNIDICT_VNIDATA.containing_type = _REFRESH_VNIDICT;
_REFRESH_VNIDICT.fields_by_name['data'].message_type = _REFRESH_VNIDICT_VNIDATA
_REFRESH_VNIDICT.containing_type = _REFRESH;
_REFRESH.fields_by_name['vteps'].message_type = _REFRESH_VNIDICT
_SYNC_VNIDICT_VNIDATA.fields_by_name['ip_addr'].message_type = _IPV4ADDRESS
_SYNC_VNIDICT_VNIDATA.containing_type = _SYNC_VNIDICT;
_SYNC_VNIDICT.fields_by_name['data'].message_type = _SYNC_VNIDICT_VNIDATA
_SYNC_VNIDICT.containing_type = _SYNC;
_SYNC.fields_by_name['vteps'].message_type = _SYNC_VNIDICT
DESCRIPTOR.message_types_by_name['IPv4Address'] = _IPV4ADDRESS
DESCRIPTOR.message_types_by_name['Proxy'] = _PROXY
DESCRIPTOR.message_types_by_name['Refresh'] = _REFRESH
DESCRIPTOR.message_types_by_name['Sync'] = _SYNC

class IPv4Address(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _IPV4ADDRESS
  
  # @@protoc_insertion_point(class_scope:IPv4Address)

class Proxy(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PROXY
  
  # @@protoc_insertion_point(class_scope:Proxy)

class Refresh(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class VniDict(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    
    class VniData(message.Message):
      __metaclass__ = reflection.GeneratedProtocolMessageType
      DESCRIPTOR = _REFRESH_VNIDICT_VNIDATA
      
      # @@protoc_insertion_point(class_scope:Refresh.VniDict.VniData)
    DESCRIPTOR = _REFRESH_VNIDICT
    
    # @@protoc_insertion_point(class_scope:Refresh.VniDict)
  DESCRIPTOR = _REFRESH
  
  # @@protoc_insertion_point(class_scope:Refresh)

class Sync(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class VniDict(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    
    class VniData(message.Message):
      __metaclass__ = reflection.GeneratedProtocolMessageType
      DESCRIPTOR = _SYNC_VNIDICT_VNIDATA
      
      # @@protoc_insertion_point(class_scope:Sync.VniDict.VniData)
    DESCRIPTOR = _SYNC_VNIDICT
    
    # @@protoc_insertion_point(class_scope:Sync.VniDict)
  DESCRIPTOR = _SYNC
  
  # @@protoc_insertion_point(class_scope:Sync)

# @@protoc_insertion_point(module_scope)
