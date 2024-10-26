# DataViewer

Aplicación para la visualización de data de diferentes modelos de auto. La aplicación permite graficar mediante 3 gráfico dependiendo de la necesidad del usuario:

- Histograma
- Gráfico de dispersión
- Boxplot

LINK: https://dataviewer-djvp.onrender.com/

  ¿Cómo usar la aplicación?
  
El funcionamiento de la aplicación es el siguiente: 

- Primero debes seleccionar en la barra lateral izquierda los ejes que quieres graficar paara cada gráfico dentro de los tres disponibles
- Luego, en la parte central de la pantalla encontrarás tres botones que te permiten crear el gráfico que desees en base a los parámetros


Explicación del procedimiento utilizado para la creación de la app

1. Se crea un repositorio en la cuenta de Github
   
2. Configuración del Proyecto Local:

  2.1. Crear el Entorno de Proyecto: se debe crear la carpeta en la que trabajaremos de forma local el proyecto y el entorno virtual. Para esto escribimos y ejecuramos lo siguiente en la terminal:
  
  - Crear carpeta para tu proyecto: 
      mkdir nombre_proyecto
      cd nombre_proyecto
    
  - Crear enteronovirtual:
    
                  python -m venv env  # crear entorno virtual
                  source env/bin/activate  # activar entorno en Mac/Linux
                  env\Scripts\activate  # activar entorno en Windows
    
  2.2. Instalación de Dependencias: instalación de los paquetes streamlit y plotly con pip3 install -> Estos paquetes se deben guardar en un archivo llamado requirements.txt:

                  pip3 install streamlit plotly
                  pip3 freeze > requirements.txt

3. Programación de la app -> Se creo el archivo app.py que es el que se usa para interactuar en la interfaz. Se diseñó en base a las especificaciones solicitadas.
   
4. Inicializar el repositorio GitHub y push de los cambios: se debe inicializar el repositorio en el cual alojaremos la app. Una vez se inicializa y se tienen listos los cambios a la app, se hace commit de los cambios: 

  4.1  Iniciar un Repositorio Git:
  
                      git init
                      
  4.2 Agrega el archivo README.md para describir el proyecto y crea el archivo .gitignore para excluir archivos no deseados (como el entorno virtual):
  
                    echo "# Nombre del Proyecto" > README.md
                    echo "env/" > .gitignore
  4.3 Primera Confirmación y Enlace a GitHub:
  

                    Copy code
                    git add .
                    git commit -m "Primer commit: configuración del proyecto"
  Enlaza con un repositorio remoto en GitHub:

                    git remote add origin https://github.com/usuario/nombre_proyecto.git
                    git push -u origin main
5. Testeo en el entorno local y despliegue en Render
                    streamlit run app.py
   
  Se crea un nuevo servicio web en Render, selecciona el repositorio de GitHub que contiene tu aplicación y configura el entorno (por ejemplo, seleccionando Python y estableciendo el archivo app.py como   punto de inicio).


