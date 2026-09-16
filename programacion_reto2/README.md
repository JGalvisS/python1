## Estudiante
- Nombre: Jessica Katherine Galvis Silva
- Grupo: 213023_493
- Programa: Ingenieria de sistemas
## Descripción del taller
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
## Descripción del proyecto
Este proyecto desarrolla un sistema de inicio de sesión y un sistema de control de lavado de autos con interfaz gráfica en Tkinter.

Antes de acceder al sistema principal, el usuario debe validar sus credenciales. La aplicación valida el usuario y la contraseña:
- Usuario: programación
- Contraseña: programación

Además, el sistema incluye una opción para crear un usuario nuevo desde la interfaz.

La clase principal del login valida que las credenciales ingresadas sean correctas y permite ingresar al sistema principal solo si la validación es exitosa.

El sistema de lavado de autos permite:
- Registrar autos con placa y hora de ingreso
- Registrar la salida del auto
- Calcular el valor a pagar
- Consultar autos registrados
- Consultar información de un auto
## Estructura del proyecto
```
programacion_reto2/
├── main.py
├── controllers/
│   ├── car_wash_controller.py
│   └── user_controller.py
├── models/
│   ├── car_wash.py
│   └── user.py
├── README.md
└── __pycache__/
```
## Cómo ejecutar
1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta:

```bash
python main.py
```

Si estás trabajando en Windows, el comando puede ser:

```bash
cd c:\programacion_reto2
python main.py
```

## Cómo usar
1. En la pantalla de inicio de sesión, ingresa las credenciales válidas:
   - Usuario: programacion
   - Contraseña: programacion
2. Presiona el botón Login.
3. Si deseas, puedes crear un usuario adicional desde la opción Create user.
4. Una vez validado, se abre la pantalla principal del sistema de lavado.
5. Desde ahí puedes registrar autos, registrar salidas y consultar información.

## Notas
El proyecto se ha organizado usando la idea de MVC:
- Models: gestionan los datos y las reglas de validación.
- Controllers: conectan la vista con el modelo.
- Main view: muestra la interfaz Tkinter.

Este proyecto está pensado como una versión básica en Python con Tkinter