# TFG Daniel Lamana García - Mochales
## Curso 2020/2021
### Recursos de entrenamiento

Aquí se encuentra los recursos necesarios para realizar el entrenamiento de un modelo.

* aXeleRate_configs: contiene los parámetros en formato .json del modelo a entrenar.
* k210_scripts: contiene el código de MicroPython necesario para ejecutar el modelo.
* raccoon_dataset: dataset para el modelo que detecta mapaches
* [Dataset de mascarillas](https://www.kaggle.com/andrewmvd/face-mask-detection): dataset para el modelo que detecta mascarillas bien puestas.
* train_results: resultados del entrenamiento con el dataset y las configuraciones contenidas en este repositorio.

El entrenamiento realizado en un Ryzen 5 3600 dura alrededor de unas 5 horas (104ms/step, 38.1s/epoch de media, más el procesamiento entre épocas)
y alrededor de una hora y media utilizando una NVidia RTX 3070 (29ms/step, 10.9s/epoch de media) con las configuraciones de este repositorio y el dataset
de mascarillas.
