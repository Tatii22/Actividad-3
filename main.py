import json
#crear una pequeña aplicación de línea de comandos que permita **Crear, Leer, Actualizar y Eliminar** registros de contactos, almacenándolos en un archivo de JSON (`contacts.json`). Cada contacto tendrá:

#- **ID** (entero único)
#- **Nombre** (cadena)
#- **Teléfono** (cadena)
#- **Email** (cadena)

def cargarUsuarios():
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:   
        return []

def guardarUsuarios(usuarios):
    with open('contacts.json', 'w') as file:
        json.dump(usuarios, file, indent=4)


# Menú de opciones          


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
    print(menu)
    opc = input("Seleccione una opción: ")
    if opc == "1":
        nombre = input("Ingrese el nombre del usuario: ")
        telefono = input("Ingrese el teléfono del usuario: ")
        email = input("Ingrese el email del usuario: ")
        
        usuarios = cargarUsuarios()
        nuevoId = max([usuario['ID'] for usuario in usuarios], default=0) + 1
        
        nuevoUsuario = {
            "ID": nuevoId,
            "Nombre": nombre,
            "Telefono": telefono,
            "Email": email
        }
        
        usuarios.append(nuevoUsuario)
        guardarUsuarios(usuarios)
        print("-------------------------------------")
        print(f"Usuario {nombre} creado con éxito.")
        print("-------------------------------------")
    elif opc == "2":    
        pass        
    elif opc == "3":
        pass
    elif opc == "4":
        pass
    elif opc == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")
