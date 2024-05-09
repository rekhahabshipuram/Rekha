import cv2

# Open the webcam
cap = cv2.VideoCapture(0)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# Specify the full path where you want to save the video
output_path = '/home/rekha-habshipuram/Documents/kushi/output.avi'
out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Write the frame to the output video
    out.write(frame)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()
