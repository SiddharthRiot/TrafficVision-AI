import streamlit as st
import cv2
import sys
import os
import time
import collections

# Fix module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from detection.vehicle_detector import detect_vehicles
from traffic_engine.signal_logic import calculate_green_time, detect_emergency

st.set_page_config(page_title="TrafficVision AI", layout="wide")

st.title("🚦 TrafficVision AI - Intelligent Traffic Control")

# Layout
col1, col2 = st.columns([3,1])

video = cv2.VideoCapture("demo/traffic_video.mp4")

if not video.isOpened():
    st.error("Video file not found. Please add traffic_video.mp4 inside demo folder.")
    st.stop()

frame_placeholder = col1.empty()

vehicle_metric = col2.empty()
signal_metric = col2.empty()
traffic_metric = col2.empty()
progress_bar = col2.progress(0)

signal_status = col2.empty()
alert_box = col2.empty()

# -----------------------------
# Traffic Signal State Machine
# -----------------------------

signal_state = "RED"
last_switch = time.time()

# -----------------------------
# Vehicle Stabilization
# -----------------------------

vehicle_history = collections.deque(maxlen=15)
stable_vehicle_count = 0


def get_congestion(vehicle_count):

    if vehicle_count <= 5:
        return "Low", 20

    elif vehicle_count <= 15:
        return "Medium", 60

    else:
        return "High", 100


while video.isOpened():

    ret, frame = video.read()

    if not ret:
        break

    frame = cv2.resize(frame, (640,360))

    # -----------------------------
    # YOLO detection every frame
    # -----------------------------

    vehicles, labels, frame = detect_vehicles(frame)

    vehicle_history.append(vehicles)

    stable_vehicle_count = int(sum(vehicle_history) / len(vehicle_history))

    green_time = calculate_green_time(stable_vehicle_count)

    emergency = detect_emergency(labels)

    level, density = get_congestion(stable_vehicle_count)

    # -----------------------------
    # Dynamic Traffic Signal
    # -----------------------------

    current_time = time.time()

    if current_time - last_switch > green_time:

        if signal_state == "RED":
            signal_state = "GREEN"

        elif signal_state == "GREEN":
            signal_state = "YELLOW"

        else:
            signal_state = "RED"

        last_switch = current_time

    # -----------------------------

    frame_placeholder.image(frame, channels="BGR")

    vehicle_metric.metric("🚗 Vehicles", stable_vehicle_count)
    signal_metric.metric("⏱ Green Time", f"{green_time}s")
    traffic_metric.metric("📊 Traffic Density", level)

    progress_bar.progress(density)

    signal_status.markdown(f"🚦 **Signal State: {signal_state}**")

    if emergency:
        alert_box.error("🚑 Emergency Vehicle Detected → Green Corridor Activated")

    else:
        alert_box.success("Traffic Flow Normal")

    time.sleep(0.03)