Para el desarrollo de este se han utilizado las siguientes tecnologías y lenguajes:
  - odoo
  - xml
  - python
Como se podrá comprobar más adelante, este módulo depende de otro con el nombre de "refugio_animales" y será imprescindible tenerle instalado antes de instalar este.

```
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
  fecha, date, fecha actual como default
  estado, una selección con las siguientes opciones:
    - pendiente, default
    - confirmado
    - facturado
    - cancelado
```
