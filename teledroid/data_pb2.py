# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='data.proto',
  package='sfm',
  serialized_pb='\n\ndata.proto\x12\x03sfm\"+\n\rCvMatDimProto\x12\x0c\n\x04size\x18\x01 \x01(\x05\x12\x0c\n\x04step\x18\x02 \x01(\x05\"\xbb\x01\n\ncvMatProto\x12\x0e\n\x06n_dims\x18\x01 \x01(\x05\x12 \n\x04\x64ims\x18\x02 \x03(\x0b\x32\x12.sfm.CvMatDimProto\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x10\n\x08\x62ytedata\x18\x04 \x01(\x0c\x12\x30\n\x06\x66ormat\x18\x05 \x01(\x0e\x32\x19.sfm.cvMatProto.ImageType:\x05\x63vMat\")\n\tImageType\x12\t\n\x05\x63vMat\x10\x00\x12\x08\n\x04JPEG\x10\x01\x12\x07\n\x03RAW\x10\x02\"!\n\x11\x43\x61meraMatrixProto\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x02\"$\n\x14\x43\x61meraBodyTransProto\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x02\"\xc8\x02\n\rMetadataProto\x12\r\n\x05\x61ng_x\x18\x01 \x01(\x02\x12\r\n\x05\x61ng_y\x18\x02 \x01(\x02\x12\r\n\x05\x61ng_z\x18\x03 \x01(\x02\x12\r\n\x05pos_x\x18\x04 \x01(\x02\x12\r\n\x05pos_y\x18\x05 \x01(\x02\x12\r\n\x05pos_z\x18\x06 \x01(\x02\x12\x11\n\ttimestamp\x18\x07 \x01(\x06\x12\r\n\x05val_0\x18\x08 \x01(\x02\x12\r\n\x05val_1\x18\t \x01(\x02\x12\r\n\x05val_2\x18\n \x01(\x02\x12\x34\n\x04type\x18\x0b \x01(\x0e\x32\x1d.sfm.MetadataProto.SensorType:\x07GRAVITY\"g\n\nSensorType\x12\t\n\x05\x41\x43\x43\x45L\x10\x00\x12\x08\n\x04GYRO\x10\x01\x12\x0b\n\x07MAGNETO\x10\x02\x12\x0c\n\x08LINACCEL\x10\x03\x12\x0f\n\x0bORIENTATION\x10\x04\x12\x0b\n\x07GRAVITY\x10\x05\x12\x0b\n\x07ROTVECT\x10\x06\"B\n\x0b\x43vRectProto\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0e\n\x06height\x18\x04 \x01(\x05\"\xff\x01\n\nFrameProto\x12\x1f\n\x06images\x18\x01 \x03(\x0b\x32\x0f.sfm.cvMatProto\x12,\n\x0c\x63\x61meraMatrix\x18\x02 \x01(\x0b\x32\x16.sfm.CameraMatrixProto\x12\x32\n\x0f\x63\x61meraBodyTrans\x18\x03 \x01(\x0b\x32\x19.sfm.CameraBodyTransProto\x12$\n\x08metadata\x18\x04 \x01(\x0b\x32\x12.sfm.MetadataProto\x12\n\n\x02id\x18\x05 \x01(\x06\x12\x0b\n\x03seq\x18\x06 \x01(\x06\x12\x10\n\x08\x62\x61seline\x18\x08 \x01(\x02\x12\x1d\n\x03roi\x18\t \x01(\x0b\x32\x10.sfm.CvRectProtoB$\n\x18\x63vg.sfmPipeline.protoLogB\x08ProtoLog')



_CVMATPROTO_IMAGETYPE = descriptor.EnumDescriptor(
  name='ImageType',
  full_name='sfm.cvMatProto.ImageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='cvMat', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='JPEG', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RAW', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=211,
  serialized_end=252,
)

_METADATAPROTO_SENSORTYPE = descriptor.EnumDescriptor(
  name='SensorType',
  full_name='sfm.MetadataProto.SensorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='ACCEL', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='GYRO', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MAGNETO', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='LINACCEL', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ORIENTATION', index=4, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='GRAVITY', index=5, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ROTVECT', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=553,
  serialized_end=656,
)


_CVMATDIMPROTO = descriptor.Descriptor(
  name='CvMatDimProto',
  full_name='sfm.CvMatDimProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='size', full_name='sfm.CvMatDimProto.size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='step', full_name='sfm.CvMatDimProto.step', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=19,
  serialized_end=62,
)


_CVMATPROTO = descriptor.Descriptor(
  name='cvMatProto',
  full_name='sfm.cvMatProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='n_dims', full_name='sfm.cvMatProto.n_dims', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dims', full_name='sfm.cvMatProto.dims', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='sfm.cvMatProto.type', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bytedata', full_name='sfm.cvMatProto.bytedata', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='format', full_name='sfm.cvMatProto.format', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CVMATPROTO_IMAGETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=65,
  serialized_end=252,
)


_CAMERAMATRIXPROTO = descriptor.Descriptor(
  name='CameraMatrixProto',
  full_name='sfm.CameraMatrixProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='data', full_name='sfm.CameraMatrixProto.data', index=0,
      number=1, type=2, cpp_type=6, label=3,
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
  serialized_start=254,
  serialized_end=287,
)


_CAMERABODYTRANSPROTO = descriptor.Descriptor(
  name='CameraBodyTransProto',
  full_name='sfm.CameraBodyTransProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='data', full_name='sfm.CameraBodyTransProto.data', index=0,
      number=1, type=2, cpp_type=6, label=3,
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
  serialized_start=289,
  serialized_end=325,
)


_METADATAPROTO = descriptor.Descriptor(
  name='MetadataProto',
  full_name='sfm.MetadataProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ang_x', full_name='sfm.MetadataProto.ang_x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ang_y', full_name='sfm.MetadataProto.ang_y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ang_z', full_name='sfm.MetadataProto.ang_z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pos_x', full_name='sfm.MetadataProto.pos_x', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pos_y', full_name='sfm.MetadataProto.pos_y', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pos_z', full_name='sfm.MetadataProto.pos_z', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timestamp', full_name='sfm.MetadataProto.timestamp', index=6,
      number=7, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='val_0', full_name='sfm.MetadataProto.val_0', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='val_1', full_name='sfm.MetadataProto.val_1', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='val_2', full_name='sfm.MetadataProto.val_2', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='sfm.MetadataProto.type', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=5,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _METADATAPROTO_SENSORTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=328,
  serialized_end=656,
)


_CVRECTPROTO = descriptor.Descriptor(
  name='CvRectProto',
  full_name='sfm.CvRectProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='x', full_name='sfm.CvRectProto.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y', full_name='sfm.CvRectProto.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='width', full_name='sfm.CvRectProto.width', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='height', full_name='sfm.CvRectProto.height', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=658,
  serialized_end=724,
)


_FRAMEPROTO = descriptor.Descriptor(
  name='FrameProto',
  full_name='sfm.FrameProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='images', full_name='sfm.FrameProto.images', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cameraMatrix', full_name='sfm.FrameProto.cameraMatrix', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cameraBodyTrans', full_name='sfm.FrameProto.cameraBodyTrans', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='metadata', full_name='sfm.FrameProto.metadata', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='sfm.FrameProto.id', index=4,
      number=5, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='seq', full_name='sfm.FrameProto.seq', index=5,
      number=6, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='baseline', full_name='sfm.FrameProto.baseline', index=6,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='roi', full_name='sfm.FrameProto.roi', index=7,
      number=9, type=11, cpp_type=10, label=1,
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
  serialized_start=727,
  serialized_end=982,
)

_CVMATPROTO.fields_by_name['dims'].message_type = _CVMATDIMPROTO
_CVMATPROTO.fields_by_name['format'].enum_type = _CVMATPROTO_IMAGETYPE
_CVMATPROTO_IMAGETYPE.containing_type = _CVMATPROTO;
_METADATAPROTO.fields_by_name['type'].enum_type = _METADATAPROTO_SENSORTYPE
_METADATAPROTO_SENSORTYPE.containing_type = _METADATAPROTO;
_FRAMEPROTO.fields_by_name['images'].message_type = _CVMATPROTO
_FRAMEPROTO.fields_by_name['cameraMatrix'].message_type = _CAMERAMATRIXPROTO
_FRAMEPROTO.fields_by_name['cameraBodyTrans'].message_type = _CAMERABODYTRANSPROTO
_FRAMEPROTO.fields_by_name['metadata'].message_type = _METADATAPROTO
_FRAMEPROTO.fields_by_name['roi'].message_type = _CVRECTPROTO
DESCRIPTOR.message_types_by_name['CvMatDimProto'] = _CVMATDIMPROTO
DESCRIPTOR.message_types_by_name['cvMatProto'] = _CVMATPROTO
DESCRIPTOR.message_types_by_name['CameraMatrixProto'] = _CAMERAMATRIXPROTO
DESCRIPTOR.message_types_by_name['CameraBodyTransProto'] = _CAMERABODYTRANSPROTO
DESCRIPTOR.message_types_by_name['MetadataProto'] = _METADATAPROTO
DESCRIPTOR.message_types_by_name['CvRectProto'] = _CVRECTPROTO
DESCRIPTOR.message_types_by_name['FrameProto'] = _FRAMEPROTO

class CvMatDimProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CVMATDIMPROTO
  
  # @@protoc_insertion_point(class_scope:sfm.CvMatDimProto)

class cvMatProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CVMATPROTO
  
  # @@protoc_insertion_point(class_scope:sfm.cvMatProto)

class CameraMatrixProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CAMERAMATRIXPROTO
  
  # @@protoc_insertion_point(class_scope:sfm.CameraMatrixProto)

class CameraBodyTransProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CAMERABODYTRANSPROTO
  
  # @@protoc_insertion_point(class_scope:sfm.CameraBodyTransProto)

class MetadataProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _METADATAPROTO
  
  # @@protoc_insertion_point(class_scope:sfm.MetadataProto)

class CvRectProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CVRECTPROTO
  
  # @@protoc_insertion_point(class_scope:sfm.CvRectProto)

class FrameProto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FRAMEPROTO
  
  # @@protoc_insertion_point(class_scope:sfm.FrameProto)

# @@protoc_insertion_point(module_scope)
