import os
import pandas as pd
import subprocess
# fijar directorio de trabajo
os.environ['KAGGLE_USERNAME'] = 'manuelmaxgonzalez'
os.environ['KAGGLE_KEY'] = "09d23053576e98ff40cc1d9791bba4be"
os.chdir("C:/Users/mmgma/Downloads/Experimento14")
semillas  = ( 158771, 616523, 742499, 217981, 235439, 355537, 357755, 775733, 337753,
                       575533 )
# nombres de archivos del directorio
print(os.listdir())
# Define variables
semilla = 775733
experimento = "ZZ6914"

# Create an empty DataFrame to store results
results = pd.DataFrame(columns=["experimento", "semilla", "envio", "resultado"])


for envio in range(8000, 12001, 500):
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