import os
import pandas as pd
import subprocess
# fijar directorio de trabajo
os.environ['KAGGLE_USERNAME'] = 'manuelmaxgonzalez2'
os.environ['KAGGLE_KEY'] = "ee0dbdcddfaa68434b57813e31f47d53"
os.chdir("C:/Users/mmgma/Downloads/ZZ6916")
semillas  =  (158771, 616523, 742499, 217981, 235439) 
#gsutil -m cp -r gs://mia99/exp/ZZ6916    C:/Users/mmgma/Downloads/



# nombres de archivos del directorio
print(os.listdir())
# Define variables
semilla = 235439
experimento = "ZZ6916"

# Create an empty DataFrame to store results
results = pd.DataFrame(columns=["experimento", "semilla", "envio", "resultado"])


for envio in range(9500, 12501, 500):
    if envio < 10000:
        filename = f"{experimento}_01_053_s{semilla}_0{envio}.csv"
    if envio >= 10000:
        filename = f"{experimento}_01_053_s{semilla}_{envio}.csv"
    
    if not os.path.isfile(filename):
        print(f"No está el archivo {filename}. Revisar nombres de archivos.")
        break
    
    
    print(f"Enviando {filename} a Kaggle...")
    command = f'kaggle competitions submit -c itba-mcd-data-mining-2023a -f {filename} -m "Submission for envio {envio}"'
    subprocess.run(command, shell=True)