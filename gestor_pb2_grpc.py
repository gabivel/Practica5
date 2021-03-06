# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import gestor_pb2 as gestor__pb2


class GestorStub(object):
    """definición del servicio gestor de archivos
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.confirmaUsuario = channel.unary_unary(
                '/gestorArchivosDistribuido.Gestor/confirmaUsuario',
                request_serializer=gestor__pb2.NombreUsuario.SerializeToString,
                response_deserializer=gestor__pb2.RespuestaUsuario.FromString,
                )
        self.confirmaPassword = channel.unary_unary(
                '/gestorArchivosDistribuido.Gestor/confirmaPassword',
                request_serializer=gestor__pb2.Passwrd.SerializeToString,
                response_deserializer=gestor__pb2.RespuestaPassword.FromString,
                )
        self.listarDirectorio = channel.unary_stream(
                '/gestorArchivosDistribuido.Gestor/listarDirectorio',
                request_serializer=gestor__pb2.N_Directorio.SerializeToString,
                response_deserializer=gestor__pb2.RespuestaArchivo.FromString,
                )
        self.Create = channel.unary_unary(
                '/gestorArchivosDistribuido.Gestor/Create',
                request_serializer=gestor__pb2.NombreArchivo.SerializeToString,
                response_deserializer=gestor__pb2.RespuestaOperacion.FromString,
                )
        self.Rename = channel.unary_unary(
                '/gestorArchivosDistribuido.Gestor/Rename',
                request_serializer=gestor__pb2.NombreArchivos.SerializeToString,
                response_deserializer=gestor__pb2.RespuestaOperacion.FromString,
                )
        self.Remove = channel.unary_unary(
                '/gestorArchivosDistribuido.Gestor/Remove',
                request_serializer=gestor__pb2.NombreArchivo.SerializeToString,
                response_deserializer=gestor__pb2.RespuestaOperacion.FromString,
                )
        self.MakeDir = channel.unary_unary(
                '/gestorArchivosDistribuido.Gestor/MakeDir',
                request_serializer=gestor__pb2.N_Directorio.SerializeToString,
                response_deserializer=gestor__pb2.RespuestaOperacion.FromString,
                )
        self.RemoveDir = channel.unary_unary(
                '/gestorArchivosDistribuido.Gestor/RemoveDir',
                request_serializer=gestor__pb2.N_Directorio.SerializeToString,
                response_deserializer=gestor__pb2.RespuestaOperacion.FromString,
                )
        self.Read = channel.unary_stream(
                '/gestorArchivosDistribuido.Gestor/Read',
                request_serializer=gestor__pb2.NombreArchivo.SerializeToString,
                response_deserializer=gestor__pb2.RespuestaArchivo.FromString,
                )
        self.Write = channel.unary_unary(
                '/gestorArchivosDistribuido.Gestor/Write',
                request_serializer=gestor__pb2.InfoArchivo.SerializeToString,
                response_deserializer=gestor__pb2.RespuestaOperacion.FromString,
                )
        self.ReadDir = channel.unary_stream(
                '/gestorArchivosDistribuido.Gestor/ReadDir',
                request_serializer=gestor__pb2.N_Directorio.SerializeToString,
                response_deserializer=gestor__pb2.RespuestaArchivo.FromString,
                )


class GestorServicer(object):
    """definición del servicio gestor de archivos
    """

    def confirmaUsuario(self, request, context):
        """Confirma si el usuario existe
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def confirmaPassword(self, request, context):
        """Confirma si contraseña es correcta
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listarDirectorio(self, request, context):
        """Recibe un nombre de directorio y envia secuencia de nombres de archivos
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Crea un archivo y manda confirmacion
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Rename(self, request, context):
        """renombra un archivo
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Remove(self, request, context):
        """remueve un archivo
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MakeDir(self, request, context):
        """Crea un directorio
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveDir(self, request, context):
        """remueve un directorio
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Recibe nombre de archivo y regresa secuencia de informacion del archivo
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request, context):
        """Recibe informacion de archivo y regresa confirmacion
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadDir(self, request, context):
        """Recibe un nombre de directorio y envia secuencia de nombres de archivos
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GestorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'confirmaUsuario': grpc.unary_unary_rpc_method_handler(
                    servicer.confirmaUsuario,
                    request_deserializer=gestor__pb2.NombreUsuario.FromString,
                    response_serializer=gestor__pb2.RespuestaUsuario.SerializeToString,
            ),
            'confirmaPassword': grpc.unary_unary_rpc_method_handler(
                    servicer.confirmaPassword,
                    request_deserializer=gestor__pb2.Passwrd.FromString,
                    response_serializer=gestor__pb2.RespuestaPassword.SerializeToString,
            ),
            'listarDirectorio': grpc.unary_stream_rpc_method_handler(
                    servicer.listarDirectorio,
                    request_deserializer=gestor__pb2.N_Directorio.FromString,
                    response_serializer=gestor__pb2.RespuestaArchivo.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=gestor__pb2.NombreArchivo.FromString,
                    response_serializer=gestor__pb2.RespuestaOperacion.SerializeToString,
            ),
            'Rename': grpc.unary_unary_rpc_method_handler(
                    servicer.Rename,
                    request_deserializer=gestor__pb2.NombreArchivos.FromString,
                    response_serializer=gestor__pb2.RespuestaOperacion.SerializeToString,
            ),
            'Remove': grpc.unary_unary_rpc_method_handler(
                    servicer.Remove,
                    request_deserializer=gestor__pb2.NombreArchivo.FromString,
                    response_serializer=gestor__pb2.RespuestaOperacion.SerializeToString,
            ),
            'MakeDir': grpc.unary_unary_rpc_method_handler(
                    servicer.MakeDir,
                    request_deserializer=gestor__pb2.N_Directorio.FromString,
                    response_serializer=gestor__pb2.RespuestaOperacion.SerializeToString,
            ),
            'RemoveDir': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveDir,
                    request_deserializer=gestor__pb2.N_Directorio.FromString,
                    response_serializer=gestor__pb2.RespuestaOperacion.SerializeToString,
            ),
            'Read': grpc.unary_stream_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=gestor__pb2.NombreArchivo.FromString,
                    response_serializer=gestor__pb2.RespuestaArchivo.SerializeToString,
            ),
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=gestor__pb2.InfoArchivo.FromString,
                    response_serializer=gestor__pb2.RespuestaOperacion.SerializeToString,
            ),
            'ReadDir': grpc.unary_stream_rpc_method_handler(
                    servicer.ReadDir,
                    request_deserializer=gestor__pb2.N_Directorio.FromString,
                    response_serializer=gestor__pb2.RespuestaArchivo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gestorArchivosDistribuido.Gestor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Gestor(object):
    """definición del servicio gestor de archivos
    """

    @staticmethod
    def confirmaUsuario(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gestorArchivosDistribuido.Gestor/confirmaUsuario',
            gestor__pb2.NombreUsuario.SerializeToString,
            gestor__pb2.RespuestaUsuario.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def confirmaPassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gestorArchivosDistribuido.Gestor/confirmaPassword',
            gestor__pb2.Passwrd.SerializeToString,
            gestor__pb2.RespuestaPassword.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listarDirectorio(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/gestorArchivosDistribuido.Gestor/listarDirectorio',
            gestor__pb2.N_Directorio.SerializeToString,
            gestor__pb2.RespuestaArchivo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gestorArchivosDistribuido.Gestor/Create',
            gestor__pb2.NombreArchivo.SerializeToString,
            gestor__pb2.RespuestaOperacion.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Rename(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gestorArchivosDistribuido.Gestor/Rename',
            gestor__pb2.NombreArchivos.SerializeToString,
            gestor__pb2.RespuestaOperacion.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Remove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gestorArchivosDistribuido.Gestor/Remove',
            gestor__pb2.NombreArchivo.SerializeToString,
            gestor__pb2.RespuestaOperacion.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MakeDir(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gestorArchivosDistribuido.Gestor/MakeDir',
            gestor__pb2.N_Directorio.SerializeToString,
            gestor__pb2.RespuestaOperacion.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveDir(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gestorArchivosDistribuido.Gestor/RemoveDir',
            gestor__pb2.N_Directorio.SerializeToString,
            gestor__pb2.RespuestaOperacion.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/gestorArchivosDistribuido.Gestor/Read',
            gestor__pb2.NombreArchivo.SerializeToString,
            gestor__pb2.RespuestaArchivo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gestorArchivosDistribuido.Gestor/Write',
            gestor__pb2.InfoArchivo.SerializeToString,
            gestor__pb2.RespuestaOperacion.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadDir(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/gestorArchivosDistribuido.Gestor/ReadDir',
            gestor__pb2.N_Directorio.SerializeToString,
            gestor__pb2.RespuestaArchivo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
