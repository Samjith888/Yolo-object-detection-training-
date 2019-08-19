# Yolo-object-detection-training-

Train Yolo


1. Download darknet-master Github repository and use Cmake and generate. Build solution by using
   Visual studio and it will generate darknet.exe and some other files.
    
       https://github.com/AlexeyAB/darknet

2. Download BBox-Label-Tool-master from Github repository.

       https://github.com/puzzledqs/BBox-Label-Tool

3. Paste the training images folder or copy the path of the training images

4. Run main.py inside 'BBox-Label-Tool-master' folder and paste the path of training images in the text box and click the load button

5. Label objects in each image using the 'BBox Label Tool'.

6. convert the text file formats into Yolov2 format by Using the convert.py.

7. Split datasets into text and train by using process.py (generate text.py and train.py)

8. Prepare Yolov2 configuration files:

   1) cfg/obj.data
     
          classes= 1  
          train  = train.txt  
          valid  = test.txt  
          names = obj.names  
          backup = backup/  

    2) cfg/obj.names
           
          NFPA

    3) cfg/yolo-obj.cfg  (edit the existing file)

          line 3: batch =64  this means we will be using 64 images for every training step
           
          line 4: subdivisions=8
  
          line 237 : set filters=(classes + 5)*5 in our case filters=30

          line 244 classes=1

9.  Download pretrained conv.23 file file. (YOLOv2 requires a set of convolutional weights)

10. Training :  (Run the following command)

         darknet.exe detector train cfg/obj.data cfg/yolo-obj.cfg darknet19_448.conv.23
         
         
   The following is the screenshot of trainining yolo by using cmd     
         
   ![yolotrain](https://user-images.githubusercontent.com/39676803/63241416-3eab0880-c271-11e9-87d2-eeab9f230d5b.PNG)
   
   
   ![yolo_train2](https://user-images.githubusercontent.com/39676803/63253452-86408d00-c28f-11e9-8248-1cba0924c6c3.PNG)
   
 
11. Stop the training when we get the avg loss  value starts with 0.0 (before stopping, confirm whether the yolo weights 
    are saved or not after getting the 0.0 avg loss values.)

12. copy the yolo text, cfg and weight file into the yolo-object-detection-training directory.

13. Run the yolo_detection.py files and start the detection.


          
