Modelos:
  - adoptante
  - adopcion

adoptante:
  nombre, char, required
  apellidos, char, required
  animal_ids, relación one2many, es decir, un adoptante puede llegar a adoptar varios animales
  
adopcion
  animal_id, required, proviene de otro módulo de el que este depende, refugio_animales
  adoptante_id, required, proviene de el modelo adoptante
  fecha, date, fecha del día de hoy como default
  estado, una selección con las siguientes opciones:
    - pendiente, default
    - confirmado
    - facturado
    - cancelado
