# LEXPIN. Análisis de Datos con Python (I Edición)

Código producido en clases.


## ¿Cómo inicializar un nuevo proyecto de Python?

1. Crea una carpeta en la cual almacenar tu proyecto específico. Necesitarás una carpeta por cada nuevo proyecto.
2. Abre esta nueva carpeta en VSCode.
3. Ejecuta el siguiente comando en la terminal de VSCode para crear un entorno virtual:

```bash
  py -m venv .venv
```

4. Activa el entorno virtual ejecutando el siguiente comando en la terminal de VSCode:
- En Windows:
```bash
  .venv\Scripts\activate
```

- En Linux o MacOS:
```bash
  source .venv/bin/activate
```

5. Si deseas desactivar el entorno virtual, ejecuta el siguiente comando en la terminal de VSCode:
```bash
  deactivate
```

Nota: En Windows, si no puedes ejecutar el comando para activar el entorno virtual, ejecuta el siguiente comando en la terminal de VSCode:
```bash
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## ¿Cómo instalar paquetes de Python?

1. Asegúrate de que tu entorno virtual esté activado.
2. Ejecuta el siguiente comando en la terminal de VSCode para instalar un paquete de Python:
```bash
  pip install <nombre_del_paquete>
```

3. Congela las dependencias de tu proyecto ejecutando el siguiente comando en la terminal de VSCode:
```bash
  pip freeze > requirements.txt
```

Nota: Para instalar las dependencias de un proyecto existente, ejecuta el siguiente comando en la terminal de VSCode:
```bash
  pip install -r requirements.txt
```

## ¿Cómo ejecutar un proyecto de Streamlit?

1. Crea un archivo 'main.py' donde almacenar tu código.
2. Escribe el código que necesites para representar tu dashboard.
3. Ejecua el siguiente comando en la terminal:
```bash
  streamlit run main.py
```

