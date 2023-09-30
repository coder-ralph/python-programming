import cv2    # Import OpenCV for image and video processing.
import math   # Import the math library for mathematical functions.
import argparse   # Import argparse for command-line argument parsing.
import os   # # Import the os module for working with file paths

# Function to highlight faces in an input frame
def highlightFace(net, frame, conf_threshold=0.7):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    
    # Resize the input frame to a smaller size while preserving the aspect ratio
    # Commented out because we are not using resizing in the final version
    # newWidth = 800  # Adjust this value as needed
    # newHeight = int((frameHeight / frameWidth) * newWidth)
    # frameOpencvDnn = cv2.resize(frameOpencvDnn, (newWidth, newHeight))
    
    # Create a blob from the resized frame for the face detection model
    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    # Set the blob as input to the face detection model
    net.setInput(blob)
    
    # Forward pass to get face detections
    detections = net.forward()
    
    # Initialize a list to store the coordinates of detected faces
    faceBoxes = []
    
    # Loop through the detected faces
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        
        # If the confidence of the detection is above the threshold, consider it a valid face
        if confidence > conf_threshold:
            # Get the coordinates of the detected face and adjust for resizing
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            
            # Calculate the center of the face
            centerX = (x1 + x2) // 2
            centerY = (y1 + y2) // 2
            
            # Calculate the width and height of the rectangle
            width = x2 - x1
            height = y2 - y1
            
            # Adjust the coordinates to center the green box on the face
            x1 = centerX - width // 2
            y1 = centerY - height // 2
            x2 = centerX + width // 2
            y2 = centerY + height // 2
            
            # Append the adjusted coordinates to the list of face coordinates
            faceBoxes.append([x1, y1, x2, y2])
            
            # Draw a green rectangle around the detected face
            cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight/150)), 8)
    
    # Return the frame with green rectangles and the list of face coordinates
    return frameOpencvDnn, faceBoxes

# Create an argument parser to accept an input image file
parser = argparse.ArgumentParser()
parser.add_argument('--image')

# Add an argument for the output folder with a default value of 'Music/age/result'
parser.add_argument('--output_folder', default='result', help='Folder to save the result images')

# Parse the command-line arguments
args = parser.parse_args()

# Create the output folder if it doesn't exist
os.makedirs(args.output_folder, exist_ok=True)

# Define paths to pre-trained models and other constants
faceProto = "opencv_face_detector.pbtxt"
faceModel = "opencv_face_detector_uint8.pb"
ageProto = "age_deploy.prototxt"
ageModel = "age_net.caffemodel"
genderProto = "gender_deploy.prototxt"
genderModel = "gender_net.caffemodel"

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList = ['Male', 'Female']

# Load pre-trained models for face detection, age, and gender estimation
faceNet = cv2.dnn.readNet(faceModel, faceProto)
ageNet = cv2.dnn.readNet(ageModel, ageProto)
genderNet = cv2.dnn.readNet(genderModel, genderProto)

# Open a video capture object using the specified image file or default camera (if not specified)
video = cv2.VideoCapture(args.image if args.image else 0)

# Set padding for the face region
padding = 20

# Enter a loop to process frames and perform age and gender detection
while cv2.waitKey(1) < 0:
    hasFrame, frame = video.read()
    
    # Check if a frame was successfully captured
    if not hasFrame:
        cv2.waitKey()
        break
    
    # Call the highlightFace function to detect faces and draw green rectangles
    resultImg, faceBoxes = highlightFace(faceNet, frame)
    
    # If no faces were detected, print a message
    if not faceBoxes:
        print("No face detected")
    
    # Process each detected face
    for faceBox in faceBoxes:
        face = frame[max(0, faceBox[1] - padding): min(faceBox[3] + padding, frame.shape[0] - 1),
                     max(0, faceBox[0] - padding): min(faceBox[2] + padding, frame.shape[1] - 1)]

        # Create a blob from the face region for age and gender estimation
        blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

        # Set the blob as input to the gender estimation model
        genderNet.setInput(blob)
        
        # Forward pass to get gender predictions
        genderPreds = genderNet.forward()
        
        # Get the gender label
        gender = genderList[genderPreds[0].argmax()]
        print(f'Gender: {gender}')
        
        # Set the blob as input to the age estimation model
        ageNet.setInput(blob)
        
        # Forward pass to get age predictions
        agePreds = ageNet.forward()
        
        # Get the age label
        age = ageList[agePreds[0].argmax()]
        print(f'Age: {age[1:-1]} years')
        
        # Draw the gender and age labels on the frame
        cv2.putText(resultImg, f'{gender}, {age}', (faceBox[0], faceBox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)
        
        # Save the result image to the output folder with a unique name
        result_image_path = os.path.join(args.output_folder, f'result_{len(os.listdir(args.output_folder)) + 1}.jpg')
        cv2.imwrite(result_image_path, resultImg)
        
        # Display the frame with detected faces, age, and gender information
        cv2.imshow("Detecting age and gender", resultImg)
