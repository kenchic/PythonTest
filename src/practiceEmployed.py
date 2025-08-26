import json
import utilities

json_string = '''
{
  "id": 101,
  "nombre": "German Alvarez",
  "edad": 43,
  "cargo": "Desarrolador Web",
  "activo": true,
  "departamento": {
    "nombre": "Tecnología",
    "ubicacion": "bmanga"
  },
  "habilidades": ["Python", "C#", "Docker"],
  "salario": 2500
}
'''

empleado = json.loads(json_string)
utilities.consola(empleado["cargo"])  
