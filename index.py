from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"mi nombre es (.*)",
        ["Hola %1, ¿Como estas?",]
    ],
    [
        r"cual es tu nombre ?",
        ["Mi nombre es CuscoBot, ¿Como puedo ayudarte?",]
    ],
    [
        r"(.*) (nombre|llamas|dicen) ?",
        ['Mi nombre es CuscoBot, ¿Como puedo ayudarte?',]
    ],
    [
        r"como estas ?",
        ["Yo muy bien\n¿Que hay de ti?",]
    ],
    [
        r"Disculpame (.*)",
        ["Esta bien","Esta bien, no hay problema",]
    ],
    [
        r"Yo estoy (.*) muy bien",
        ["Que gusto escuchar eso","Genial :)",]
    ],
    [
        r"Estoy bien",
        ["Que gusto escuchar esto","Alright :)",]
    ],
    [
        r"Hey|Que tal|Hola|¿estas ahi?",
        ["Hola ¿Cual es tu nombre?", "Hola que tal, ¿Como te llamas?",]
    ],
    [
        r"(.*) años tienes?|cual es tu edad?",
        ["La verdad es que soy una computadora\ny no tengo una edad definida",]
    ],
    [
        r"(.*) (años|edad) ?",
        ["La verdad es que soy una computadora\ny no tengo una edad definida",]
    ],
    [
        r"¿que (.*) gusta?|gusta|que (.*) gusta?",
        ["Proponme algo interesante",]
    ],
    [
        r"(.*) created ?",
        ["Nagesh created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (naciste|ciudad|nacer) ?",
        ['Yo nací en cusco',]
    ],
    [
        r"(.*) (chau|nos vemos|tengo que ir)",
        ["Chau, nos vemos pronto :) ","Fue un gusto hablar contigo, nos vemos pronto :)"]
    ],
    [
        r"quit",
        ["Chau, nos vemos pronto :) ","Fue un gusto hablar contigo, nos vemos pronto :)"]
    ],
]

def chatty():
    print("Hola yo soy CuscoBot ;)\nEscribe algo para iniciar una conversación y presiona quit para salir") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatty()