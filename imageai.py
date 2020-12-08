import fileutil

from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel()

def detect(absPath):
    outputPath = fileutil.create_random_fileName_in_temp_dir('jpg');

    detections = detector.detectObjectsFromImage(
        input_image=absPath,
        output_image_path=outputPath, 
        minimum_percentage_probability=25)

    for eachObject in detections:
        print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
        print("--------------------------------")
    return outputPath