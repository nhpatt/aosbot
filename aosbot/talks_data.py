import yaml


emoji = {
    "coffee": b"",
    "alarm_clock": b"\xE2\x8F\xB0",
    "watch": b"\xE2\x8C\x9A",
    "hourglass_flowing_sand": b"\xE2\x8F\xB3",
    "calendar": b"\xF0\x9F\x93\x85",
    "fork_and_knife": b"\xF0\x9F\x8D\xB4",
    "raising_hand": b"\xF0\x9F\x99\x8B",
    "footprints": b"\xF0\x9F\x91\xA3",
    "speech_balloon": b"\xF0\x9F\x92\xAC",
    "thought_balloon": b"\xF0\x9F\x92\xAD",
    "pig": b"\xF0\x9F\x90\x96",
    "pig_nose": b"\xF0\x9F\x90\xBD",
    "ghost": b"\xF0\x9F\x91\xBB",
    "gift": b"",
    "closed_book": b"\xF0\x9F\x93\x95",
    "blue_book": b"\xF0\x9F\x93\x98",
    "orange_book": b"\xF0\x9F\x93\x99",
    "notebook": b"\xF0\x9F\x93\x93",
    "space_invader": b"",
}


# Talk types: session, general, break, extra
# Session rooms: TODO


def get_emoji(emoji_name):
    return emoji[emoji_name].decode('utf-8')


talks_data = yaml.safe_load("""
---

talks:
  # - session_type: session
  #   from_time: "2017-06-24T09:00:00+0200"
  #   to_time: "2017-06-24T10:00:00+0200"
  #   room: 
  #   icon: 
  #   title:
  #   proposer:
  #   description:

# Viernes 23

  - session_type: extra
    from_time: "2017-06-23T11:00:00+0200"
    to_time: "2017-06-23T13:00:00+0200"
    room: Campus María Zambrano
    icon: ghost
    title: Let's Play Agile Games
    proposer: Amalia Hernández y Delia Estebaranz
    description: |
        Juegos acerca de la formación de equipos y la confianza. 
        Apto para todo tipo de públicos.

  - session_type: extra
    from_time: "2017-06-23T11:00:00+0200"
    to_time: "2017-06-23T13:00:00+0200"
    room: Campus María Zambrano
    icon: ghost
    title: AOS Code Jam
    proposer: José Dova y Agustín Herranz
    description: |
        Sesión abierta sobre programación en la que practicar, plantear dudas, enseñar código, debatir... 
        podrás traer tu portátil para trabajar sobre código y aprender un montón de cosas..

  - session_type: general
    from_time: "2017-06-23T16:00:00+0200"
    to_time: "2017-06-23T17:30:00+0200"
    room: Campus María Zambrano
    icon: raising_hand
    title: Apertura del AOS 2017
    proposer: AOS
    description: |
        ¿En qué consiste el AOS 2017?
        Presentación y actividades previas.

  - session_type: general
    from_time: "2017-06-23T17:30:00+0200"
    to_time: "2017-06-23T19:30:00+0200"
    room: Campus María Zambrano
    icon: raising_hand
    title: Creación del panel y votación de las sesiones.
    proposer: AOS
    description: |
        Las personas que lo deseen proponen una sesión o un tema del que hablar explicando brevemente el contenido y enfoque de la sesión.
        Tras proponer todas las sesiones, los asistentes votan aquellas que sean de su interés.
        Las más votadas se repartirán en el panel final estableciendo la agenda del sábado.

# Sábado 24

  - session_type: general
    from_time: "2017-06-24T09:00:00+0200"
    to_time: "2017-06-24T10:00:00+0200"
    room: 
    icon: raising_hand
    title: Apertura de las sesiones
    proposer: AOS
    description:

  - session_type: session
    from_time: "2017-06-24T10:00:00+0200"
    to_time: "2017-06-24T11:00:00+0200"
    room: room
    icon: calendar
    title: Session I
    proposer: AOS
    description: ...

  - session_type: session
    from_time: "2017-06-24T11:00:00+0200"
    to_time: "2017-06-24T12:00:00+0200"
    room: room
    icon: calendar
    title: Session II
    proposer: AOS
    description: ...

  - session_type: break
    from_time: "2017-06-24T12:00:00+0200"
    to_time: "2017-06-24T12:30:00+0200"
    room: room
    icon: fork_and_knife
    title: Coffe break
    proposer: AOS
    description: ...

  - session_type: session
    from_time: "2017-06-24T12:30:00+0200"
    to_time: "2017-06-24T13:30:00+0200"
    room: room
    icon: calendar
    title: Session III
    proposer: AOS
    description: ...

  - session_type: session
    from_time: "2017-06-24T13:30:00+0200"
    to_time: "2017-06-24T14:30:00+0200"
    room: room
    icon: calendar
    title: Session IV
    proposer: AOS
    description: ...

  - session_type: break
    from_time: "2017-06-24T14:30:00+0200"
    to_time: "2017-06-24T16:00:00+0200"
    room: room
    icon: fork_and_knife
    title: Comida
    proposer: AOS
    description: ...

  - session_type: session
    from_time: "2017-06-24T16:00:00+0200"
    to_time: "2017-06-24T17:00:00+0200"
    room: room
    icon: calendar
    title: Session V
    proposer: AOS
    description: ...

  - session_type: session
    from_time: "2017-06-24T17:00:00+0200"
    to_time: "2017-06-24T18:00:00+0200"
    room: room
    icon: calendar
    title: Session VI
    proposer: AOS
    description: ...

  - session_type: general
    from_time: "2017-06-24T18:00:00+0200"
    to_time: "2017-06-24T19:00:00+0200"
    room: 
    icon: raising_hand
    title: Retrospectiva y cierre AOS 2017
    proposer: AOS
    description:

""")  # NoQA E501, W291
