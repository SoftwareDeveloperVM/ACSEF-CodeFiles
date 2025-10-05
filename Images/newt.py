import cv2
import numpy as np

# Open the video capture (0 for webcam; or use a video file)
cap = cv2.VideoCapture(0)

# Define the HSV thresholds for a light brown color.
# These values are a starting point; they assume the fish color is roughly HSV (18, ~90, ~164).
# We allow a tolerance around these values.
lower_color = np.array([10, 50, 80])
upper_color = np.array([30, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for pixels within the specified HSV range
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Clean up the mask using morphological operations to reduce noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Assume the largest contour corresponds to the fish
        largest_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(largest_contour) > 500:  # Filter out very small regions
            x, y, w, h = cv2.boundingRect(largest_contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the results
    cv2.imshow("Fish Tracking", frame)
    cv2.imshow("Mask", mask)

    # Exit if 'ESC' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
