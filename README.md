# ROS2 Object Detection with YOLOv8

Real-time object detection system built with ROS2 and YOLOv8. This package provides a ROS2 node for performing real-time object detection on image streams.

## 🚀 Features

- Real-time object detection using YOLOv8
- ROS2 node integration
- Configurable confidence thresholds
- Support for various input sources (webcam, video files, ROS topics)
- Clean and modular code structure

## 🛠️ Technologies Used

- **ROS2 Humble**
- **Python 3.8+**
- **OpenCV** - Computer vision operations
- **PyTorch** - Deep learning framework
- **YOLOv8** - Object detection model
- **Ultralytics** - YOLO implementation

## 📦 Installation

### Prerequisites
- ROS2 Humble (or newer)
- Python 3.8+
- Webcam (for real-time testing)

### Setup
```bash
# Clone the repository
git clone https://github.com/samraiqbal-aiml/ros2_object_detection.git
cd ros2_object_detection

# Install Python dependencies
pip install -r requirements.txt

# Build the ROS2 package (if using ROS2)
colcon build
source install/setup.bash


## Demo
![Object Detection Demo](demo.jpg)
