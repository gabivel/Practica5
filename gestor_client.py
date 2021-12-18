from __future__ import print_function

import logging

import grpc
import gestor_pb2
import gestor_pb2_grpc


def confirmaUser(stub,name):
    response = stub.confirmaUsuario(gestor_pb2.NombreUsuario(nombre=name))
    if response.r_usuario == name:
        return True
    else:
        return False


def confirmaPwd(stub,user,pwd):
    response = stub.confirmaPassword(gestor_pb2.Passwrd(user=user,passwrd=pwd))
    if response.r_passwrd == "ok":
        return True
    else:
        return False

def listarHome(stub,user):
    for respuesta in stub.listarDirectorio(gestor_pb2.N_Directorio(directorio='.')):
        print("- " + respuesta.archivo)

def crearArchivo(stub,user,var):
    response = stub.Create(gestor_pb2.NombreArchivo(n_archivo=var))
    print(response.r_operacion)

def renameArchivo(stub,user,var):
    curr_file = var[:var.find(' ')+1]
    print(curr_file)
    new_file = var[var.find(' ')+1:]
    print(new_file)
    response = stub.Rename(gestor_pb2.NombreArchivos(curr_archivo=curr_file,new_archivo=new_file))
    print(response.r_operacion)

def removeArchivo(stub,var):
    response = stub.Remove(gestor_pb2.NombreArchivo(n_archivo=var))
    print(response.r_operacion)

def makeDirectorio(stub,var):
    response = stub.MakeDir(gestor_pb2.N_Directorio(directorio=var))
    print(response.r_operacion)

def removeDirectorio(stub,var):
    response = stub.RemoveDir(gestor_pb2.N_Directorio(directorio=var))
    print(response.r_operacion)

def readArchivo(stub,var):
    for respuesta in stub.Read(gestor_pb2.NombreArchivo(n_archivo=var)):
        print(respuesta.archivo.rstrip('\n'))


def writeArchivo(stub,var):
    file = var[:var.find(' ')+1]
    print(file)
    texto = var[var.find(' ')+1:]
    print(texto)
    response = stub.Write(gestor_pb2.InfoArchivo(archivo=file,info=texto))
    print(response.r_operacion)

def readDir(stub):
    for respuesta in stub.ReadDir(gestor_pb2.N_Directorio(directorio='.')):
        print(respuesta.archivo)


def run():

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = gestor_pb2_grpc.GestorStub(channel)
        print("Bienvenido al gestor de archivos distrubiuido")

        user = input('Ingrese su usuario: ')

        if confirmaUser(stub,user):
            pwd = input('Ingrese contraseña: ')

            if confirmaPwd(stub,user,pwd):
                print("Puede hacer acciones en sus archivos:")
                listarHome(stub,user)

                while True:
                    comando = input("> ")
                    operacion = comando[:comando.find(' ')+1].upper()
                    var = comando[comando.find(' ')+1:]

                    if operacion.startswith("CREATE"):
                        crearArchivo(stub,user,var)
                    elif operacion.startswith("RENAME"):
                        renameArchivo(stub,user,var)
                    elif operacion.startswith("REMOVE"):
                        removeArchivo(stub,var)
                    elif operacion.startswith("MKDIR"):
                        makeDirectorio(stub,var)
                    elif operacion.startswith("RMDIR"):
                        removeDirectorio(stub,var)
                    elif operacion.startswith("READ"):
                        readArchivo(stub,var)
                    elif operacion.startswith("WRITE"):
                        writeArchivo(stub,var)
                    elif comando.upper() == "READDIR":
                        readDir(stub)
                    elif comando.upper() == "LIST":
                        listarHome(stub,var)

            else:
                print("Incorrecto, regrese pronto")
        
        else:

        	print("Incorrecto, regrese pronto")


if __name__ == '__main__':
    logging.basicConfig()
    run()