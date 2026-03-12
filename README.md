# 🚦 TrafficVision AI
### Dynamic AI Traffic Flow Optimizer & Emergency Grid

TrafficVision AI is an intelligent traffic management system that uses **Computer Vision and AI** to analyze live traffic conditions and dynamically optimize traffic signal timings.  
The system also provides an **AI-powered green corridor** feature to prioritize emergency vehicles such as ambulances and fire trucks.

---

# 🧠 Problem Statement

Traditional traffic signals operate on **fixed timers**, which do not adapt to real-time traffic conditions. This leads to traffic congestion, longer wait times, and delayed emergency response.

The goal of this project is to develop a **dynamic AI-based traffic control system** that can:

- Analyze traffic density using computer vision
- Adjust signal timings dynamically
- Detect emergency vehicles
- Automatically activate green corridors

---

# 🚀 Solution Overview

TrafficVision AI uses a **YOLOv8 object detection model** to analyze traffic from camera feeds. The system detects vehicles, calculates traffic density, and adjusts signal timings accordingly.

If an emergency vehicle such as an **ambulance or fire truck** is detected, the system automatically triggers a **green corridor**, ensuring a faster and uninterrupted route.

This approach enables **smart traffic management, reduced congestion, and faster emergency response times.**

---

# ⚙️ How It Works

1️⃣ Traffic cameras capture live video feed  
2️⃣ YOLOv8 detects vehicles in the video  
3️⃣ The system counts vehicles and calculates traffic density  
4️⃣ Traffic signal timing is adjusted dynamically  
5️⃣ Emergency vehicles trigger automatic **green corridor activation**

---

# 🚗 Dynamic Traffic Signal Logic

Traffic signals are controlled using adaptive timing:

| Vehicles in Lane | Green Signal Time |
|------------------|------------------|
| 0 – 5 vehicles   | 10 seconds |
| 6 – 15 vehicles  | 20 seconds |
| 16 – 30 vehicles | 30 seconds |
| 30+ vehicles     | 45 seconds |

This ensures that **lanes with heavier traffic receive longer green signals**, reducing congestion.

---

# 🚑 Emergency Vehicle Detection

The AI model detects emergency vehicles including:

- Ambulance
- Fire Truck
- Police Vehicle

When detected:

- System triggers **Green Corridor Mode**
- Traffic signals adjust automatically
- Emergency vehicle gets priority passage

---

# 📊 Dashboard Features

The system includes a **Streamlit dashboard** that displays:

- Live traffic video feed
- Vehicle detection visualization
- Traffic density level
- Current signal status
- Dynamic green signal timing
- Emergency vehicle alerts

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|--------|
| Python | Core programming language |
| YOLOv8 | Real-time object detection |
| OpenCV | Video processing |
| Streamlit | Interactive dashboard |
| NumPy | Data processing |
| Pandas | Data analysis |

---
# 👥 Team

| Name          | Institution |
| ------------- | ----------- |
| **Siddharth** | USAR        |
| **Rahul**     | NSUT        |
| **Ayushi**    | ANDC        |
| **Tarun**     | NSUT        |
| **Raman**     | NSUT        |

---
# 🔗 References

- YOLO Object Detection – https://docs.ultralytics.com
- OpenCV Computer Vision Library – https://opencv.org
- IEEE Intelligent Transportation Systems Research – https://ieeexplore.ieee.org
- NVIDIA Deep Learning Resources – https://developer.nvidia.com/deep-learning

---
# 🌍 Future Scope

- Lane-wise traffic analysis
- GPS-based emergency vehicle tracking
- Smart city traffic integration
- AI-based traffic prediction
- Multi-camera traffic monitoring systems
- Edge AI deployment for real-time traffic control

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/SiddharthRiot/TrafficVision-AI.git
cd TrafficVision-AI
```
---
## 📜 License
This project is developed for educational and hackathon purposes.


---