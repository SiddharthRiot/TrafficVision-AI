def calculate_green_time(vehicle_count):

    if vehicle_count <= 5:
        return 10

    elif vehicle_count <= 15:
        return 20

    elif vehicle_count <= 30:
        return 30

    else:
        return 45


EMERGENCY = ["ambulance", "fire truck", "police"]

def detect_emergency(labels):

    for label in labels:
        if label in EMERGENCY:
            return True

    return False