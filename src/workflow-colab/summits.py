import os
import pandas as pd
import subprocess
# fijar directorio de trabajo
os.environ['KAGGLE_USERNAME'] = 'experimentos2'
os.environ['KAGGLE_KEY'] = "41233daee824c4ac25c2bcc1d3e031ad"
os.chdir("C:/Users/mmgma/Downloads/ZZ6913")
semillas  =  (158771, 616523, 742499, 217981, 235439) 
#gsutil -m cp -r gs://mia99/exp/ZZ6916    C:/Users/mmgma/Downloads/



# nombres de archivos del directorio
print(os.listdir())
# Define variables
semilla = semillas[1]
experimento = "ZZ6916"

# Create an empty DataFrame to store results
results = pd.DataFrame(columns=["experimento", "semilla", "envio", "resultado"])


for envio in range(9500, 12501, 500):
    if envio < 10000:
        filename = f"{experimento}_01_028_s{semilla}_0{envio}.csv"
    if envio >= 10000:
        filename = f"{experimento}_01_028_s{semilla}_{envio}.csv"
    
    if not os.path.isfile(filename):
        print(f"No está el archivo {filename}. Revisar nombres de archivos.")
        break
    
    
    print(f"Enviando {filename} a Kaggle...")
    command = f'kaggle competitions submit -c itba-mcd-data-mining-2023a -f {filename} -m "Submission for envio {envio}"'
    subprocess.run(command, shell=True)