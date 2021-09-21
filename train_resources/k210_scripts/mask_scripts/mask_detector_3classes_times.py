import sensor,image,lcd
import KPU as kpu
import time

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))
sensor.set_vflip(1)
sensor.run(1)
classes = ["with_mask", "mask_weared_incorrect", "without_mask"]
#task = kpu.load(0x300000) #change to "/sd/name_of_the_model_file.kmodel" if loading from SD card task = kpu.load("/sd/model.kmodel")
task = kpu.load("/sd/75_3classes.kmodel")
a = kpu.set_outputs(task, 0, 7,7,40)   #the actual shape needs to match the last layer shape of your model(before Reshape)
anchor = (0.57273, 0.677385, 1.87446, 2.06253, 3.33843, 5.47434, 7.88282, 3.52778, 9.77052, 9.16828)
a = kpu.init_yolo2(task, 0.5, 0.3, 5, anchor) #tweak the second parameter if you're getting too many false positives
while(True):
    img = sensor.snapshot().rotation_corr(z_rotation=90.0)
    a = img.pix_to_ai()
    start = time.ticks_us()
    code = kpu.run_yolo2(task, img)
    end = time.ticks_us()
    infertime = time.ticks_diff(end,start)
    strinfer = str(infertime)
    if code:
        for i in code:
            a=img.draw_rectangle(i.rect(),color = (0, 255, 0))
            a = img.draw_string(i.x(),i.y(), strinfer, color=(255,0,0), scale=3)
        a = lcd.display(img)
    else:
        a = lcd.display(img)
a = kpu.deinit(task)
