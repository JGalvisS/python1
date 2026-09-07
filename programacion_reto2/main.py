"""
Nombre del estudiante: Jessica Katherine Galvis Silva
Grupo: 213023_493
Programa: Ingenieria de Sistemas
Codigo fuente: autoria propia

Antes de acceder a cualquiera de los sistemas descritos en los ejercicios, el estudiante debe implementar un módulo de inicio de sesión (login) que valide un usuario que es programación y una contraseña que es programación.
Para esto, debe crearse una clase llamada Usuario, con:
•Atributos privados: _usuario y _password.
•Un método público validar(usuario_ingresado, password_ingresada) que retorne True únicamente si las credenciales coinciden.
La aplicación debe iniciar mostrando la pantalla de login en Tkinter. Solo si el usuario ingresa credenciales válidas, se desbloquea el acceso al sistema principal de cada ejercicio. Si las credenciales son incorrectas, el programa debe impedir el acceso y mostrar mensajes de error adecuados.
Sistema para Control de Lavado
Un autolavado desea controlar los autos que ingresan al servicio de lavado y calcular el costo según la cantidad de tiempo que permanezcan en el proceso.
Crear la clase AutoLavado, con:
•Atributos privados: _placa, _hora_ingreso, _tarifa_hora.
•Método registrar_ingreso(hora)
•Método registrar_salida(hora)
•Método calcular_pago(hora_salida)
•Método obtener_placa()
El sistema debe:
•Registrar autos en una lista interna.
•Permitir seleccionar un auto para registrar la salida.
•Calcular el costo automáticamente.
•Validar la hora de salida.
"""