# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gestor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gestor.proto',
  package='gestorArchivosDistribuido',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cgestor.proto\x12\x19gestorArchivosDistribuido\"\x1f\n\rNombreUsuario\x12\x0e\n\x06nombre\x18\x01 \x01(\t\"%\n\x10RespuestaUsuario\x12\x11\n\tr_usuario\x18\x01 \x01(\t\"(\n\x07Passwrd\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0f\n\x07passwrd\x18\x02 \x01(\t\"&\n\x11RespuestaPassword\x12\x11\n\tr_passwrd\x18\x01 \x01(\t\"\"\n\x0cN_Directorio\x12\x12\n\ndirectorio\x18\x01 \x01(\t\"#\n\x10RespuestaArchivo\x12\x0f\n\x07\x61rchivo\x18\x01 \x01(\t\"\"\n\rNombreArchivo\x12\x11\n\tn_archivo\x18\x01 \x01(\t\")\n\x12RespuestaOperacion\x12\x13\n\x0br_operacion\x18\x01 \x01(\t\";\n\x0eNombreArchivos\x12\x14\n\x0c\x63urr_archivo\x18\x01 \x01(\t\x12\x13\n\x0bnew_archivo\x18\x02 \x01(\t\",\n\x0bInfoArchivo\x12\x0f\n\x07\x61rchivo\x18\x01 \x01(\t\x12\x0c\n\x04info\x18\x02 \x01(\t2\xf0\x08\n\x06Gestor\x12j\n\x0f\x63onfirmaUsuario\x12(.gestorArchivosDistribuido.NombreUsuario\x1a+.gestorArchivosDistribuido.RespuestaUsuario\"\x00\x12\x66\n\x10\x63onfirmaPassword\x12\".gestorArchivosDistribuido.Passwrd\x1a,.gestorArchivosDistribuido.RespuestaPassword\"\x00\x12l\n\x10listarDirectorio\x12\'.gestorArchivosDistribuido.N_Directorio\x1a+.gestorArchivosDistribuido.RespuestaArchivo\"\x00\x30\x01\x12\x63\n\x06\x43reate\x12(.gestorArchivosDistribuido.NombreArchivo\x1a-.gestorArchivosDistribuido.RespuestaOperacion\"\x00\x12\x64\n\x06Rename\x12).gestorArchivosDistribuido.NombreArchivos\x1a-.gestorArchivosDistribuido.RespuestaOperacion\"\x00\x12\x63\n\x06Remove\x12(.gestorArchivosDistribuido.NombreArchivo\x1a-.gestorArchivosDistribuido.RespuestaOperacion\"\x00\x12\x63\n\x07MakeDir\x12\'.gestorArchivosDistribuido.N_Directorio\x1a-.gestorArchivosDistribuido.RespuestaOperacion\"\x00\x12\x65\n\tRemoveDir\x12\'.gestorArchivosDistribuido.N_Directorio\x1a-.gestorArchivosDistribuido.RespuestaOperacion\"\x00\x12\x61\n\x04Read\x12(.gestorArchivosDistribuido.NombreArchivo\x1a+.gestorArchivosDistribuido.RespuestaArchivo\"\x00\x30\x01\x12`\n\x05Write\x12&.gestorArchivosDistribuido.InfoArchivo\x1a-.gestorArchivosDistribuido.RespuestaOperacion\"\x00\x12\x63\n\x07ReadDir\x12\'.gestorArchivosDistribuido.N_Directorio\x1a+.gestorArchivosDistribuido.RespuestaArchivo\"\x00\x30\x01\x62\x06proto3'
)




_NOMBREUSUARIO = _descriptor.Descriptor(
  name='NombreUsuario',
  full_name='gestorArchivosDistribuido.NombreUsuario',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nombre', full_name='gestorArchivosDistribuido.NombreUsuario.nombre', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=43,
  serialized_end=74,
)


_RESPUESTAUSUARIO = _descriptor.Descriptor(
  name='RespuestaUsuario',
  full_name='gestorArchivosDistribuido.RespuestaUsuario',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='r_usuario', full_name='gestorArchivosDistribuido.RespuestaUsuario.r_usuario', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=76,
  serialized_end=113,
)


_PASSWRD = _descriptor.Descriptor(
  name='Passwrd',
  full_name='gestorArchivosDistribuido.Passwrd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='gestorArchivosDistribuido.Passwrd.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='passwrd', full_name='gestorArchivosDistribuido.Passwrd.passwrd', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=115,
  serialized_end=155,
)


_RESPUESTAPASSWORD = _descriptor.Descriptor(
  name='RespuestaPassword',
  full_name='gestorArchivosDistribuido.RespuestaPassword',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='r_passwrd', full_name='gestorArchivosDistribuido.RespuestaPassword.r_passwrd', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=157,
  serialized_end=195,
)


_N_DIRECTORIO = _descriptor.Descriptor(
  name='N_Directorio',
  full_name='gestorArchivosDistribuido.N_Directorio',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='directorio', full_name='gestorArchivosDistribuido.N_Directorio.directorio', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=197,
  serialized_end=231,
)


_RESPUESTAARCHIVO = _descriptor.Descriptor(
  name='RespuestaArchivo',
  full_name='gestorArchivosDistribuido.RespuestaArchivo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='archivo', full_name='gestorArchivosDistribuido.RespuestaArchivo.archivo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=233,
  serialized_end=268,
)


_NOMBREARCHIVO = _descriptor.Descriptor(
  name='NombreArchivo',
  full_name='gestorArchivosDistribuido.NombreArchivo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='n_archivo', full_name='gestorArchivosDistribuido.NombreArchivo.n_archivo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=270,
  serialized_end=304,
)


_RESPUESTAOPERACION = _descriptor.Descriptor(
  name='RespuestaOperacion',
  full_name='gestorArchivosDistribuido.RespuestaOperacion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='r_operacion', full_name='gestorArchivosDistribuido.RespuestaOperacion.r_operacion', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=306,
  serialized_end=347,
)


_NOMBREARCHIVOS = _descriptor.Descriptor(
  name='NombreArchivos',
  full_name='gestorArchivosDistribuido.NombreArchivos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='curr_archivo', full_name='gestorArchivosDistribuido.NombreArchivos.curr_archivo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_archivo', full_name='gestorArchivosDistribuido.NombreArchivos.new_archivo', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=349,
  serialized_end=408,
)


_INFOARCHIVO = _descriptor.Descriptor(
  name='InfoArchivo',
  full_name='gestorArchivosDistribuido.InfoArchivo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='archivo', full_name='gestorArchivosDistribuido.InfoArchivo.archivo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='gestorArchivosDistribuido.InfoArchivo.info', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=410,
  serialized_end=454,
)

DESCRIPTOR.message_types_by_name['NombreUsuario'] = _NOMBREUSUARIO
DESCRIPTOR.message_types_by_name['RespuestaUsuario'] = _RESPUESTAUSUARIO
DESCRIPTOR.message_types_by_name['Passwrd'] = _PASSWRD
DESCRIPTOR.message_types_by_name['RespuestaPassword'] = _RESPUESTAPASSWORD
DESCRIPTOR.message_types_by_name['N_Directorio'] = _N_DIRECTORIO
DESCRIPTOR.message_types_by_name['RespuestaArchivo'] = _RESPUESTAARCHIVO
DESCRIPTOR.message_types_by_name['NombreArchivo'] = _NOMBREARCHIVO
DESCRIPTOR.message_types_by_name['RespuestaOperacion'] = _RESPUESTAOPERACION
DESCRIPTOR.message_types_by_name['NombreArchivos'] = _NOMBREARCHIVOS
DESCRIPTOR.message_types_by_name['InfoArchivo'] = _INFOARCHIVO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NombreUsuario = _reflection.GeneratedProtocolMessageType('NombreUsuario', (_message.Message,), {
  'DESCRIPTOR' : _NOMBREUSUARIO,
  '__module__' : 'gestor_pb2'
  # @@protoc_insertion_point(class_scope:gestorArchivosDistribuido.NombreUsuario)
  })
_sym_db.RegisterMessage(NombreUsuario)

RespuestaUsuario = _reflection.GeneratedProtocolMessageType('RespuestaUsuario', (_message.Message,), {
  'DESCRIPTOR' : _RESPUESTAUSUARIO,
  '__module__' : 'gestor_pb2'
  # @@protoc_insertion_point(class_scope:gestorArchivosDistribuido.RespuestaUsuario)
  })
_sym_db.RegisterMessage(RespuestaUsuario)

Passwrd = _reflection.GeneratedProtocolMessageType('Passwrd', (_message.Message,), {
  'DESCRIPTOR' : _PASSWRD,
  '__module__' : 'gestor_pb2'
  # @@protoc_insertion_point(class_scope:gestorArchivosDistribuido.Passwrd)
  })
_sym_db.RegisterMessage(Passwrd)

RespuestaPassword = _reflection.GeneratedProtocolMessageType('RespuestaPassword', (_message.Message,), {
  'DESCRIPTOR' : _RESPUESTAPASSWORD,
  '__module__' : 'gestor_pb2'
  # @@protoc_insertion_point(class_scope:gestorArchivosDistribuido.RespuestaPassword)
  })
_sym_db.RegisterMessage(RespuestaPassword)

N_Directorio = _reflection.GeneratedProtocolMessageType('N_Directorio', (_message.Message,), {
  'DESCRIPTOR' : _N_DIRECTORIO,
  '__module__' : 'gestor_pb2'
  # @@protoc_insertion_point(class_scope:gestorArchivosDistribuido.N_Directorio)
  })
_sym_db.RegisterMessage(N_Directorio)

RespuestaArchivo = _reflection.GeneratedProtocolMessageType('RespuestaArchivo', (_message.Message,), {
  'DESCRIPTOR' : _RESPUESTAARCHIVO,
  '__module__' : 'gestor_pb2'
  # @@protoc_insertion_point(class_scope:gestorArchivosDistribuido.RespuestaArchivo)
  })
_sym_db.RegisterMessage(RespuestaArchivo)

NombreArchivo = _reflection.GeneratedProtocolMessageType('NombreArchivo', (_message.Message,), {
  'DESCRIPTOR' : _NOMBREARCHIVO,
  '__module__' : 'gestor_pb2'
  # @@protoc_insertion_point(class_scope:gestorArchivosDistribuido.NombreArchivo)
  })
_sym_db.RegisterMessage(NombreArchivo)

RespuestaOperacion = _reflection.GeneratedProtocolMessageType('RespuestaOperacion', (_message.Message,), {
  'DESCRIPTOR' : _RESPUESTAOPERACION,
  '__module__' : 'gestor_pb2'
  # @@protoc_insertion_point(class_scope:gestorArchivosDistribuido.RespuestaOperacion)
  })
_sym_db.RegisterMessage(RespuestaOperacion)

NombreArchivos = _reflection.GeneratedProtocolMessageType('NombreArchivos', (_message.Message,), {
  'DESCRIPTOR' : _NOMBREARCHIVOS,
  '__module__' : 'gestor_pb2'
  # @@protoc_insertion_point(class_scope:gestorArchivosDistribuido.NombreArchivos)
  })
_sym_db.RegisterMessage(NombreArchivos)

InfoArchivo = _reflection.GeneratedProtocolMessageType('InfoArchivo', (_message.Message,), {
  'DESCRIPTOR' : _INFOARCHIVO,
  '__module__' : 'gestor_pb2'
  # @@protoc_insertion_point(class_scope:gestorArchivosDistribuido.InfoArchivo)
  })
_sym_db.RegisterMessage(InfoArchivo)



_GESTOR = _descriptor.ServiceDescriptor(
  name='Gestor',
  full_name='gestorArchivosDistribuido.Gestor',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=457,
  serialized_end=1593,
  methods=[
  _descriptor.MethodDescriptor(
    name='confirmaUsuario',
    full_name='gestorArchivosDistribuido.Gestor.confirmaUsuario',
    index=0,
    containing_service=None,
    input_type=_NOMBREUSUARIO,
    output_type=_RESPUESTAUSUARIO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='confirmaPassword',
    full_name='gestorArchivosDistribuido.Gestor.confirmaPassword',
    index=1,
    containing_service=None,
    input_type=_PASSWRD,
    output_type=_RESPUESTAPASSWORD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='listarDirectorio',
    full_name='gestorArchivosDistribuido.Gestor.listarDirectorio',
    index=2,
    containing_service=None,
    input_type=_N_DIRECTORIO,
    output_type=_RESPUESTAARCHIVO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='gestorArchivosDistribuido.Gestor.Create',
    index=3,
    containing_service=None,
    input_type=_NOMBREARCHIVO,
    output_type=_RESPUESTAOPERACION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Rename',
    full_name='gestorArchivosDistribuido.Gestor.Rename',
    index=4,
    containing_service=None,
    input_type=_NOMBREARCHIVOS,
    output_type=_RESPUESTAOPERACION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Remove',
    full_name='gestorArchivosDistribuido.Gestor.Remove',
    index=5,
    containing_service=None,
    input_type=_NOMBREARCHIVO,
    output_type=_RESPUESTAOPERACION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MakeDir',
    full_name='gestorArchivosDistribuido.Gestor.MakeDir',
    index=6,
    containing_service=None,
    input_type=_N_DIRECTORIO,
    output_type=_RESPUESTAOPERACION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveDir',
    full_name='gestorArchivosDistribuido.Gestor.RemoveDir',
    index=7,
    containing_service=None,
    input_type=_N_DIRECTORIO,
    output_type=_RESPUESTAOPERACION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Read',
    full_name='gestorArchivosDistribuido.Gestor.Read',
    index=8,
    containing_service=None,
    input_type=_NOMBREARCHIVO,
    output_type=_RESPUESTAARCHIVO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='gestorArchivosDistribuido.Gestor.Write',
    index=9,
    containing_service=None,
    input_type=_INFOARCHIVO,
    output_type=_RESPUESTAOPERACION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReadDir',
    full_name='gestorArchivosDistribuido.Gestor.ReadDir',
    index=10,
    containing_service=None,
    input_type=_N_DIRECTORIO,
    output_type=_RESPUESTAARCHIVO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GESTOR)

DESCRIPTOR.services_by_name['Gestor'] = _GESTOR

# @@protoc_insertion_point(module_scope)