import os
import pandas as pd
import subprocess
# fijar directorio de trabajo. Agregar usuario y key de Kaggle.

os.environ['KAGGLE_USERNAME'] = 'usuario'
os.environ['KAGGLE_KEY'] = "contraseña"

os.chdir("carpetaenlaquetengoaarchivos")

semillas  = ( 158771, 616523, 742499, 217981, 235439, 355537, 357755, 775733, 337753,
                       575533 )

# Defino variables
semilla = semillas[0]
experimento = "ZZ6914"

for envio in range(8000, 13501, 500):
    if envio < 10000:
        filename = f"exp_{experimento}_{experimento}_01_061_s{semilla}_0{envio}.csv"
    if envio >= 10000:
        filename = f"exp_{experimento}_{experimento}_01_061_s{semilla}_{envio}.csv"
    
    if not os.path.isfile(filename):
        print(f"No está el archivo {filename}. Revisar nombres de archivos.")
        break
    
    
    print(f"Enviando {filename} a Kaggle...")
    command = f'kaggle competitions submit -c itba-mcd-data-mining-2023a -f {filename} -m "Submission for envio {envio}"'
    subprocess.run(command, shell=True)