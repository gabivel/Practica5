from concurrent import futures
import logging

import grpc
import gestor_pb2
import gestor_pb2_grpc

import os

class Gestor(gestor_pb2_grpc.GestorServicer):

	def confirmaUsuario(self,request,context):
		with open('C:/Users/Velasco/Documents/Redes2/Practica5/users.txt') as temp_f:
			lineas = temp_f.readlines()
			for linea in lineas:
				if request.nombre in linea:
					return gestor_pb2.RespuestaUsuario(r_usuario=request.nombre)
			return gestor_pb2.RespuestaUsuario(r_usuario='No existe usuario')

	def confirmaPassword(self,request,context):
		with open('C:/Users/Velasco/Documents/Redes2/Practica5/users.txt') as temp_f:
			lineas = temp_f.readlines()
			for linea in lineas:
				if (request.user + ' ' + request.passwrd) in linea:
					os.chdir("C:/Users/Velasco/Documents/Redes2/Practica5/"+request.user+"/Home")
					return gestor_pb2.RespuestaPassword(r_passwrd='ok')
			return gestor_pb2.RespuestaPassword(r_passwrd='No existe password')

	def listarDirectorio(self,request,context):
		lista_archivos= os.listdir(request.directorio)
		for archivo in lista_archivos:
			yield gestor_pb2.RespuestaArchivo(archivo=archivo)
	
	def Create(self,request,context):
		try:
			file = open(request.n_archivo, "w")
			file.close()
			return gestor_pb2.RespuestaOperacion(r_operacion='se creo bien el archivo')
		except IOError:
			return gestor_pb2.RespuestaOperacion(r_operacion=IOError)

	def Rename(self,request,context):
		os.rename(request.curr_archivo, request.new_archivo)
		return gestor_pb2.RespuestaOperacion(r_operacion='se cambio nombre del archivo')


	def Remove(self,request,context):
		try:
			os.remove(request.n_archivo)
			return gestor_pb2.RespuestaOperacion(r_operacion='elimino el archivo')
		except IOError:
			return gestor_pb2.RespuestaOperacion(r_operacion=IOError)

	def MakeDir(self,request,context):
		try:
			os.mkdir(request.directorio)
			return gestor_pb2.RespuestaOperacion(r_operacion='se creo el directorio')
		except IOError:
			return gestor_pb2.RespuestaOperacion(r_operacion=IOError)


	def RemoveDir(self,request,context):
		try:
			os.rmdir(request.directorio)
			return gestor_pb2.RespuestaOperacion(r_operacion='elimino el directorio')
		except IOError:
			return gestor_pb2.RespuestaOperacion(r_operacion=IOError)

	def Read(self,request,context):
		f = open(request.n_archivo, "rb")
		lineas= f.readlines()
		for linea in lineas:
			yield gestor_pb2.RespuestaArchivo(archivo=linea)
		f.close()

	def Write(self,request,context):
		f = open(request.archivo,'a')		
		f.write('\n' + request.info)
		f.close()
		return gestor_pb2.RespuestaOperacion(r_operacion='Se ingreso todo al archivo')

	def ReadDir(self,request,context):
		lista_archivos= os.listdir(request.directorio)
		for archivo in lista_archivos:
			fullpath = os.getcwd() + "/"+ archivo
			if os.path.isdir(fullpath):
				yield gestor_pb2.RespuestaArchivo(archivo=fullpath)
	
		

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gestor_pb2_grpc.add_GestorServicer_to_server(Gestor(), server)
    server.add_insecure_port('192.168.1.89:50051')
    server.start()
    print("El servidor esta listo")
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
