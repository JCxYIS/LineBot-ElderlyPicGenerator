import fileutil

from imageai.Detection import ObjectDetection
import os

# # from https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Detection/README.md
path_ai_model = fileutil.abs_path('ai_model/resnet50_coco_best_v2.0.1.h5')

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet() # 設定model類型
detector.setModelPath( path_ai_model ) # 讀取model
detector.loadModel()

def detect_objects(absPath):
    """
    使用AI來爭測物件，回傳偵測出的結果圖片位置(abs)
    """

    outputPath = fileutil.create_random_fileName_in_temp_dir('jpg');

    detections = detector.detectObjectsFromImage(
        input_image=absPath,
        output_image_path=outputPath, 
        minimum_percentage_probability=25)

    print("-----IMAGE DETECTION START-----")
    for eachObject in detections:
        print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
        print("--------------------------------")
    print("-----IMAGE DETECTION END-----", flush=True)

    return outputPath
