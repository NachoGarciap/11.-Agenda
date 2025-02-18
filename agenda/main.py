import json


class Agenda:

    def __init__(self):
        self.contactos = {}
        self.id = 0
        self.cargar_contactos()  # Cargar los contactos al inicio

    def menu(self):

        while True:
            print('----- Agenda -----:')
            print('1. Agregar contacto')
            print('2. Ver lista de contactos')
            print('3. Buscar contacto')
            print('4. Eliminar contacto')
            print('5. Editar contacto')
            print('6. Salir')

            try:
                opcion = int(input("Elige una opcion: "))
            except ValueError:
                print("Por favor, introduce un número válido.")
                continue

            if opcion == 1:
                self.agregar_contacto()
            elif opcion == 2:
                self.mostrar_lista()
            elif opcion == 3:
                self.buscar_contacto()
            elif opcion == 4:
                self.eliminar_contacto()
            elif opcion == 5:
                self.editar_contacto()
            elif opcion == 6:
                print('Saliendo...')
                break
            else:
                print('Introduce una opcion valida')

    def agregar_contacto(self):
        nombre = input('Escribe el nombre: ')
        telefono = input('Escribe el telefono: ')
        email = input('Escribe el email: ')
        self.id += 1

        # crea el contacto
        contacto = {
            'Id': self.id,
            'Nombre': nombre,
            'Telefono': telefono,
            'Email': email
        }
        # Agrega el contacto
        self.contactos[self.id] = contacto
        print(f"Contacto '{nombre}' agregado correctamente.")
        self.guardar_contactos()

    def mostrar_lista(self):
        if not self.contactos:
            print('No hay contactos guardados')

        else:
            print('\nLista de contactos:')
            for contacto in self.contactos.values():
                print(
                    f"ID: {contacto['Id']}, Nombre: {contacto['Nombre']}, Teléfono: {contacto['Telefono']}, Email: {contacto['Email']}")

    def buscar_contacto(self):
        nombre = input('Introduce el nombre que quieres buscar: ').lower()
        encontrados = []  # almacenamos los contactos en la lista vacia

        for contacto in self.contactos.values():
            if contacto['Nombre'].lower() == nombre:
                encontrados.append(contacto)  # si coincide lo agrega a la lista vacia

        if encontrados:
            for listar in encontrados:
                print(
                    f"ID: {listar['Id']}, Nombre: {listar['Nombre']}, Teléfono: {listar['Telefono']}, Email: {listar['Email']}")
        else:
            print('Contacto no encontrado')

    def eliminar_contacto(self):
        nombre = input('Introduce el nombre que quieres eliminar: ').lower()

        encontrado = False
        for contacto_id, contacto in list(self.contactos.items()):
            if contacto['Nombre'].lower() == nombre:
                del self.contactos[contacto_id]
                print(f"Contacto '{nombre}' eliminado correctamente")
                encontrado = True
                break

            if not encontrado:
                print('No se encontró el contacto para borrar')

    def editar_contacto(self):
        nombre = input('Introduce el nombre del contacto que quieres editar: ').lower()
        contacto = None

        for buscar in self.contactos.values():
            if buscar['Nombre'].lower() == nombre:
                contacto = buscar
                break

        if contacto:
            print(f"Detalles actuales de {nombre}")
            print(f"Teléfono: {contacto['Telefono']}")
            print(f"Email: {contacto['Email']}")

            mod_telefono = input('Quieres modificar el telefono? (s/n): ').lower()

            if mod_telefono == 's':
                telefono = input('Introduce el nuevo telefono: ')
                contacto['Telefono'] = telefono
            else:
                print('Se mantiene el telefono')

            mod_email = input('Quieres modificar el email? (s/n): ').lower()

            if mod_email == 's':
                email = input('Introduce el nuevo email: ')
                contacto['Email'] = email
            else:
                print('Se mantiene el email')

            print(f"Contacto {nombre} actualizado correctamente.")
        else:
            print('Contacto no encontrado')

    def guardar_contactos(self):
        datos = {
            'id': self.id,
            'contactos': self.contactos
        }

        with open('contactos.json', 'w', encoding='utf8') as archivo:
            json.dump(datos, archivo, indent=4)
            print('Contacto guardado exitosamente!')

    def cargar_contactos(self):
        try:
            with open('contactos.json', 'r', encoding='utf8') as archivo:
                # Verificar si el archivo está vacío
                content = archivo.read().strip()
                if not content:
                    print("El archivo de contactos está vacío.")
                    return  # Si el archivo está vacío, no se intenta cargar datos

                datos = json.loads(content)
                print("Datos cargados:", datos)  # Agregamos una impresión para verificar el contenido cargado
                self.contactos = datos['contactos']
                self.id = datos['id']
            print("Contactos cargados exitosamente.")
        except FileNotFoundError:
            print("No se encontró el archivo de contactos. Empezando con agenda vacía.")
            self.contactos = {}  # Inicializamos la agenda vacía si no se encuentra el archivo.
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON. El archivo podría estar dañado.")
            self.contactos = {}
            self.id = 0
        except Exception as e:
            print(f"Error al cargar los contactos: {e}")


prueba = Agenda()
prueba.menu()
