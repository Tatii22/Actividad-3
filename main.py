import json
import os

def limpiarConsola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def enterParaContinuar(mensaje : str = "Enter para continuar..."):
    input(mensaje)

def cargarContactos():
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):   
        return []

def guardarContactos(usuarios):
    with open('contacts.json', 'w') as file:
        json.dump(usuarios, file, indent=4)

def crearContacto(lista):
    print("=" * 40)  
    print("SECCIÓN: Crear Contacto")
    print("=" * 40)
    nombre = input("Ingrese el nombre del contacto: ")
    if not validarNombre(nombre):
        return
    telefono = input("Ingrese el teléfono del contacto: ")
    if not validarTelfono(telefono):
        return
    email = input("Ingrese el email del contacto: ")
    if not validarEmail(email):
        return
    
    nuevoId = max([contacto['ID'] for contacto in lista], default=0) + 1
    
    nuevoContacto = {
        "ID": nuevoId,
        "Nombre": nombre,
        "Telefono": telefono,
        "Email": email
    }
    
    lista.append(nuevoContacto)
    guardarContactos(lista)
    print(f"Contacto {nombre} creado con éxito.")
    enterParaContinuar("Presione enter para continuar...")
    


def listarContactos(lista):
    if not lista:
        print("No hay contactos registrados.")
    else:
        print("=" * 40) 
        print("Lista de contactos:")
        print(f"{'ID':<5} {'Nombre':<20} {'Teléfono':<15} {'Email'}")
        print("-" * 60)
        for contacto in lista:
             print(f"{contacto['ID']:<5} {contacto['Nombre']:<20} {contacto['Telefono']:<15} {contacto['Email']}")
    enterParaContinuar("Presione enter para continuar...")
    


def actualizarContacto(lista):
    listarContactos(lista)
    print("=" * 40)
    print("SECCIÓN: Actualizar Contacto")   
    print("=" * 40)
    idContacto = validarId(input("Ingrese el ID del contacto a actualizar: "))
    if not idContacto:
        return
    for contacto in lista:
        if contacto['ID'] == idContacto:
            nuevoNombre = input(f"Ingrese el nuevo nombre (actual: {contacto['Nombre']}): ")
            if not validarNombre(nuevoNombre):
                return
            nuevoTelefono = input(f"Ingrese el nuevo teléfono (actual: {contacto['Telefono']}): ")
            if not validarTelfono(nuevoTelefono):
                return
            nuevoEmail = input(f"Ingrese el nuevo email (actual: {contacto['Email']}): ")
            if not validarEmail(nuevoEmail):
                return
            
            contacto['Nombre'] = nuevoNombre
            contacto['Telefono'] = nuevoTelefono
            contacto['Email'] = nuevoEmail
            
            guardarContactos(lista)
            print(f"Contacto {contacto['ID']} actualizado con éxito.")
            enterParaContinuar("Presione enter para continuar...")
            return
    print(f"No se encontró un contacto con ID {idContacto}.")
    
    

def eliminarContacto(lista):
    listarContactos(lista)
    print("=" * 40)
    print("SECCIÓN: Eliminar Contacto")
    print("=" * 40)
    idContacto = validarId(input("Ingrese el ID del contacto a eliminar: "))
    if not idContacto:
        return          
    for contacto in lista:
        if contacto['ID'] == idContacto:
            lista.remove(contacto)
            guardarContactos(lista)
            print(f"Contacto {contacto['ID']} eliminado con éxito.")
            enterParaContinuar("Presione enter para continuar...")
            return
    print(f"No se encontró un contacto con ID {idContacto}.")

    

def validarNombre(nombre):
    if not nombre:
        print("El nombre no puede estar vacío.")
        return False
    return True
def validarTelfono(telefono):
    if not telefono.isdigit():
        print("El teléfono debe contener solo números.")
        return False
    return True
def validarEmail(email):
    email = email.strip()
    if "@" not in email or "." not in email.split('@')[-1]:
        print("El email debe contener '@' y un dominio.")
        return False
    return True
def validarId(idContacto):
    if not idContacto.isdigit():
        print("El ID debe ser un número.")
        return False
    return int(idContacto)


menu = """
   *                      
 (  `                     
 )\))(     (           (  
((_)()\   ))\  (      ))\ 
(_()((_) /((_) )\ )  /((_)
|  \/  |(_))  _(_/( (_))( 
| |\/| |/ -_)| ' \))| || |
|_|  |_|\___||_||_|  \_,_|

1. Crear usuario
2. Ver usuarios
3. Actualizar usuario
4. Eliminar usuario
5. Salir
""" 
while True:
    limpiarConsola()
    print(menu)
    opc = input("Seleccione una opción: ")
    if opc == "1":
        usuarios = cargarContactos()
        crearContacto(usuarios)
    elif opc == "2":    
        usuarios = cargarContactos()
        listarContactos(usuarios)  
        
    elif opc == "3":
        usuarios = cargarContactos()
        actualizarContacto(usuarios)    
    elif opc == "4":
        usuarios = cargarContactos()
        eliminarContacto(usuarios)
    elif opc == "5":
        enterParaContinuar("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")
