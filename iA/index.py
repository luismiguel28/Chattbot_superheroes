import random
import json

# Cargar la base de datos de superhéroes
with open('base.json', 'r') as f:
    heroes = json.load(f)['superheroes']

# Función para preguntar al usuario
def preguntar_caracteristica(caracteristica):
    respuesta = input('¿El superheroe en el que estas pensando tiene el poder de {}? (Si/No) '.format(caracteristica))
    if respuesta.lower() == 'si':
        return True
    elif respuesta.lower() == 'no':
        return False
    else:
        print('Lo siento, no entendi tu respuesta.')
        return preguntar_caracteristica(caracteristica)

# Función para filtrar superhéroes según una característica
def filtrar_superheroes(superheroes, caracteristica):
    return [heroe for heroe in superheroes if caracteristica in heroe['poderes']]

# Función principal del chat bot
def chat_bot():
    superheroes = heroes.copy()
    preguntas_hechas = []
    intentos = 0

    # Saludo del chat bot
    print('Hola, soy un chat bot que adivina en que superheroe estas pensando. ¿Listo para empezar?')

    # Loop principal del chat bot
    while len(superheroes) > 1 and intentos < 2:
        # Elegir una característica al azar
        caracteristica = random.choice(superheroes[0]['poderes'])
        while caracteristica in preguntas_hechas:
            caracteristica = random.choice(superheroes[0]['poderes'])
        
        # Preguntar al usuario si el superhéroe en el que está pensando tiene esa característica
        if preguntar_caracteristica(caracteristica):
            superheroes = filtrar_superheroes(superheroes, caracteristica)
        else:
            superheroes = [heroe for heroe in superheroes if caracteristica not in heroe['poderes']]
        
        # Agregar la característica preguntada a la lista de preguntas hechas
        preguntas_hechas.append(caracteristica)

        # Verificar si se ha adivinado el superhéroe
        if len(superheroes) == 1:
            respuesta = input('El superheroe en el que estas pensando es {}. ¿Es correcto? (Si/No) '.format(superheroes[0]['nombre']))
            if respuesta.lower() == 'si':
                print('¡Genial, he adivinado el superheroe!')
                return
            else:
                intentos += 1
                superheroes = heroes.copy()
                preguntas_hechas = []
                print('Vamos a intentarlo de nuevo.')

    # Si no se ha adivinado el superhéroe después de 2 intentos, agregar uno nuevo
    print('Lo siento, no pude adivinar el superheroe en el que estas pensando.')
    agregar_heroe = input('¿Quieres agregar un nuevo superheroe a la base de datos? (Si/No) ')
    if agregar_heroe.lower() == 'si':
        nombre = input('Ingresa el nombre del nuevo superheroe: ')
        poderes = input('Ingresa los poderes del nuevo superheroe (separados por comas): ').split(',')
        universe = input('Ingresa el universo del nuevo superheroe: ')
        nuevo_heroe = {'nombre': nombre, 'poderes': [poder.strip() for poder in poderes], 'universe': universe}
        heroes.append(nuevo_heroe)
        with open('base.json', 'w') as f:
            json.dump({'superheroes': heroes}, f)
        print('El nuevo superheroe ha sido agregado a la base de datos.')
    else:
        print('Gracias por jugar.')



# Ejecutar el chat bot
chat_bot()
