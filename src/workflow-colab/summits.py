import os
import pandas as pd
import subprocess
# fijar directorio de trabajo
os.environ['KAGGLE_USERNAME'] = 'experimentos2'
os.environ['KAGGLE_KEY'] = "5a354fcb63b1264dc81c48039b104fa9"
os.chdir("C:/Users/mmgma/Downloads/Experimento14/ZZ6914")
semillas  = ( 158771, 616523, 742499, 217981, 235439, 355537, 357755, 775733, 337753,
                       575533 )
# nombres de archivos del directorio
print(os.listdir())
# Define variables
semilla = 235439
experimento = "ZZ6914"

# Create an empty DataFrame to store results
results = pd.DataFrame(columns=["experimento", "semilla", "envio", "resultado"])


for envio in range(9000, 13501, 500):
    if envio < 10000:
        filename = f"{experimento}_01_061_s{semilla}_0{envio}.csv"
    if envio >= 10000:
        filename = f"{experimento}_01_061_s{semilla}_{envio}.csv"
    
    if not os.path.isfile(filename):
        print(f"No está el archivo {filename}. Revisar nombres de archivos.")
        break
    
    
    print(f"Enviando {filename} a Kaggle...")
    command = f'kaggle competitions submit -c itba-mcd-data-mining-2023a -f {filename} -m "Submission for envio {envio}"'
    subprocess.run(command, shell=True)