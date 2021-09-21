# TFG Daniel Lamana García - Mochales
## Curso 2020/2021
### Ficheros de configuración

Estos ficheros contienen los parámetros a ajustar para el entrenamiento utilizando
aXeleRate, algunos de estoos parámetros son:

* type: Tipo de modelo, que puede ser un detector de objetos, clasificación de imágenes o segmentación semántica.
*  architecture : extractor de características a utilizar (Como Tiny Yolo \ref{par:tinyyolo  o MobileNet \ref{par:mobilenets ).
*  input_size :
*  coord_scale : magnitud en la que se penalizan las predicciones erróneas de coordenadas.
*  class_scale : magnitud en la que se penalizan las predicciones erróneas de clase (es otra clase).
*  object_scale : magnitud en la que se penalizan las predicciones erróneas de objeto (no hay objeto).
*  no_object_scale : magnitud en la que se penalizan las predicciones erróneas de no-objeto (si hay objeto).
*  actual_epoch : épocas de entrenamiento. 
*  augumentation : redimensionar, desenfocar y manipular imágenes para evitar el sobreaprendizaje.
*  valid_metric : métrica utilizada para decidir si el modelo ha mejorado respecto a la anterior época o no. (mAP: mean Average Precision)
*  train_times, validation_times : veces a repetir el dataset

La carpeta [racoon_config](link) contiene la configuración para el detector de mapaches 
y [mask_configs]() contiene las configuraciones para el detector de mascarillas.