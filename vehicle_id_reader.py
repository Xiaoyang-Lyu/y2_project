import cv2
import pytesseract
import re

class VehicleIdReader:
    def active_camera(self):
        pass
    def release_camera(self):
        pass
    
    def get_vehicle_id(self):
        pass
    pass



class WebCamVehicleIdreader(VehicleIdReader):
        # avtive camera
    def active_camera(self):
        self.cap = cv2.VideoCapture(0)

    def release_camera(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def get_vehicle_id(self):
        # Read the current frame
        ret, frame = self.cap.read()
        if not ret:
            # Handle the case where frame reading fails
            return "Error: Unable to read frame"
        # Convert the current frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Use pytesseract to recognize text
        text = pytesseract.image_to_string(gray_frame)
        pattern = re.compile(r'\b[A-Z0-9]{7}\b')
        
        # Use rc to find result
        matches = pattern.findall(text)
        
        if matches:
            return matches[0]# If multiple matches are found, concatenate them into a string and return
        else:
            return "No valid ID found"
     
            

class MockVehicleIdReader(VehicleIdReader):
    def __init__(self):
        self.image_path = "test_image.jpg"

    def get_vehicle_id(self):
        # Read the image from the specified path
        frame = cv2.imread(self.image_path)

        if frame is None:
            return "Error: Unable to read image"

        # Convert the image to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Use pytesseract to recognize text
        text = pytesseract.image_to_string(gray_frame)
        
        # return text.strip()
    def active_camera(self):
        pass

    def release_camera(self):
        pass