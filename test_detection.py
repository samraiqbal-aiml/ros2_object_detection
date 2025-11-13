#!/usr/bin/env python3
"""
Test script for object detection without ROS2 dependencies
Author: Samra Iqbal
"""

import cv2
import torch
from ultralytics import YOLO
import numpy as np

def test_object_detection():
    print("🚀 Testing Object Detection with YOLOv8...")
    
    # Load model
    model = YOLO('yolov8n.pt')
    print("✅ YOLO model loaded successfully!")
    
    # Test with webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ No webcam found. Using test image...")
        # Create a test image instead
        test_image = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
        results = model(test_image)
        annotated_image = results[0].plot()
        cv2.imwrite('test_output.jpg', annotated_image)
        print("✅ Test image processed and saved as 'test_output.jpg'")
        return
    
    print("✅ Webcam detected. Starting real-time detection...")
    print("Press 'q' to quit")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Run detection
        results = model(frame)
        annotated_frame = results[0].plot()
        
        # Display
        cv2.imshow('YOLO Object Detection - Samra Iqbal', annotated_frame)
        
        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print("✅ Test completed successfully!")

if __name__ == '__main__':
    test_object_detection()
