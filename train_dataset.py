"""La información requerida para este laboratio esta almacenada en el archivo 
"data.zip" ubicado en la carpeta raíz. Descomprima este archivo. 

Como resultado obtendra la siguiente estructura de archivos:

```
train/
    negative/
        0000.txt
        0001.txt
        ...
    positive/
        0000.txt
        0001.txt
        ...
    neutral/
        0000.txt
        0001.txt
        ...
test/
    negative/
        0000.txt
        0001.txt
        ...
    positive/
        0000.txt
        0001.txt
        ...
    neutral/
        0000.txt
        0001.txt
        ...
```

A partir de esta informacion debe generar dos archivos llamados "train_dataset.csv" y 
"test_dataset.csv". Estos archivos deben tener la siguiente estructura:

* phrase: Texto de la frase. hay una frase por cada archivo de texto.
* sentiment: Sentimiento de la frase. Puede ser "positive", "negative" o "neutral". Este corresponde al nombre del directorio donde se encuentra ubicado el archivo."""


import os
import csv

def generate_dataset(input_folder, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['phrase', 'sentiment'])

        for folder in os.listdir(input_folder):
            if os.path.isdir(os.path.join(input_folder, folder)):
                for file in os.listdir(os.path.join(input_folder, folder)):
                    if file.endswith('.txt'):
                        with open(os.path.join(input_folder, folder, file), 'r', encoding='utf-8') as f:
                            phrase = f.read().strip()
                            sentiment = folder
                            writer.writerow([phrase, sentiment])

# Rutas de entrada y salida
train_folder = 'train'
test_folder = 'test'
train_output_file = 'train_dataset.csv'
test_output_file = 'test_dataset.csv'

# Generar los conjuntos de datos
generate_dataset(train_folder, train_output_file)
generate_dataset(test_folder, test_output_file)

print("Los archivos train_dataset.csv y test_dataset.csv han sido generados correctamente.")
