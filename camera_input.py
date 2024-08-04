import cv2
import numpy as np

class Camera_Input:
    def __init__(self):

        height = 500
        width = 500

        # Define the HSV color (Hue, Saturation, Value)
        # Hue: 0-179, Saturation: 0-255, Value: 0-255
        hsv_color = (0.9271178,  83.41741,   254.99866)  # Green color in HSV

        # Create an empty image with the defined dimensions and 3 color channels
        hsv_image = np.zeros((height, width, 3), dtype=np.uint8)

        # Fill the image with the defined HSV color
        hsv_image[:] = hsv_color

        # Convert the HSV image to BGR color space
        bgr_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

        # Display the image
        cv2.imshow('Single HSV Color Image', bgr_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # self.get_images()
        # self.get_colors()
        # print(self.avg_color(self.get_image_from_webcam("Test"), (20,20,20,20)))


    def get_images(self):
        instructions = ["White top, Green front",
                        "White top, Red front",
                        "White top, Blue front",
                        "White top, Orange front",
                        "Red top, White front",
                        "Orange top, Yellow front"]
        self.imgs = []
        for i in range(6):
            self.imgs.append(self.get_image_from_webcam(instructions[i]))

    def get_image_from_webcam(self, instruction):
        # Open the webcam
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not open webcam.")
            return None

        print("Press the spacebar to capture an image.")
        captured_image = None

        while True:
            # Read a frame from the webcam
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break

            # Display the frame
            cv2.imshow(instruction, self.with_overlay(cv2.flip(frame,1)))

            # Wait for the user to press the spacebar or 'q'
            key = cv2.waitKey(1)
            if key == ord(' '):  # Spacebar to capture image
                captured_image = frame
                print("Image captured!")
                break
            elif key == ord('q'):  # 'q' to quit
                break

        # Release the webcam and close windows
        cap.release()
        cv2.destroyAllWindows()

        return captured_image

    def with_overlay(self, img):
        height, width = img.shape[:2]

        border_width = 40

        z = min(height // 6, width // 6)
        x_pos = [width // 2 - (3 * z) + border_width, width // 2 - z + border_width, width // 2 + z + border_width]
        y_pos = [height // 2 - (3 * z) + border_width, height // 2 - z + border_width, height // 2 + z + border_width]

        square_width = (2 * z) - (2 * border_width)

        self.square_dimensions = [(x_pos[0], y_pos[0], square_width, square_width),
                                  (x_pos[1], y_pos[0], square_width, square_width),
                                  (x_pos[2], y_pos[0], square_width, square_width),
                                  (x_pos[0], y_pos[1], square_width, square_width),
                                  (x_pos[1], y_pos[1], square_width, square_width),
                                  (x_pos[2], y_pos[1], square_width, square_width),
                                  (x_pos[0], y_pos[2], square_width, square_width),
                                  (x_pos[1], y_pos[2], square_width, square_width),
                                  (x_pos[2], y_pos[2], square_width, square_width)]
        overlay = img.copy()
        overlay = cv2.addWeighted(overlay, 0.5, np.zeros_like(overlay, dtype=np.uint8), 0, 0)
        for dim in self.square_dimensions:
            x, y, w, h = dim
            overlay[y:y+h, x:x+w] = img[y:y+h, x:x+w]
        return overlay

    def get_colors(self):
        self.cube = "WWWWWWWWWRRRRRRRRRGGGGGGGGGYYYYYYYYYOOOOOOOOOBBBBBBBBB"
        color_index = [[18,19,20,21,22,23,24,25,26],
                       [9,10,11,12,13,14,15,16,17],
                       [45,46,47,48,49,50,51,52,53],
                       [36,37,38,39,40,41,42,43,44],
                       [2,5,8,1,4,7,0,3,6],
                       [33,30,27,34,31,28,35,32,29]]
        for i in range(6):
            img = self.imgs[i]
            for j in range(9):
                color = self.avg_color(img, self.square_dimensions[j])
                self.cube = self.cube[:color_index[i][j]] + color + self.cube[color_index[i][j] + 1:]
        print(self.cube)

    def avg_color(self, img, dim):
        # x, y, w, h = dim
        # rec = img[y:y+h, x:x+w]
        # hsv_image = cv2.cvtColor(rec, cv2.COLOR_BGR2HSV)
        # avg_hsv = cv2.mean(hsv_image)[:3] # (h, s, v)
        # print(avg_hsv)

        # lower = {"y": [21,50,50], "g": [70,50,50], "w": [0,0,140], "o": [5,50,50], "b":[90,50,50], "r1": [0,50,50], "r2": [140,50,50]}
        # upper = {"y": [70,255,255], "g": [90,255,255], "w": [180,60,255], "o": [21,255,255], "b":[140,255,255], "r1": [5,255,255], "r2": [180,255,255]}

        # for color in ["r","o","y","g","w","b"]:
        #     if color == "r":
        #         # Special treatment for "red" because it's hsv hue can be either high or low
        #         if self.inside_lists(avg_hsv, lower["r1"], upper["r1"]):
        #             return color
        #         if self.inside_lists(avg_hsv, lower["r2"], upper["r2"]):
        #             return color
        #     else:
        #         if self.inside_lists(avg_hsv, lower[color], upper[color]):
        #             return color
        # return "X"

        x, y, w, h = dim
        rec = img[y:y+h, x:x+w]
        hsv_image = cv2.cvtColor(rec, cv2.COLOR_BGR2HSV)
        
        # Reshape the image to be a list of pixels
        pixels = hsv_image.reshape((-1, 3))

        # Apply K-means clustering to find the dominant color
        num_clusters = 5
        kmeans = cv2.kmeans(np.float32(pixels), num_clusters, None, 
                            (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2), 
                            10, cv2.KMEANS_RANDOM_CENTERS)[2]
        
        dominant_color = np.median(kmeans, axis=0)
        print(dominant_color)

        lower = {"y": [21,50,50], "g": [70,50,50], "w": [0,0,120], "o": [0,50,50], "b":[95,50,50], "r1": [0,50,50], "r2": [140,50,50]}
        upper = {"y": [70,256,256], "g": [95,256,256], "w": [180,75,256], "o": [21,256,256], "b":[140,256,256], "r1": [0,256,256], "r2": [180,256,256]}

        for color in ["r","o","y","g","w","b"]:
            if color == "r":
                # Special treatment for "red" because its HSV hue can be either high or low
                if self.inside_lists(dominant_color, lower["r1"], upper["r1"]):
                    return color
                if self.inside_lists(dominant_color, lower["r2"], upper["r2"]):
                    return color
            else:
                if self.inside_lists(dominant_color, lower[color], upper[color]):
                    return color
        return "X"
        
    def inside_lists(self, lst, a, b):
        for i in range(len(lst)):
            if not (lst[i] >= a[i] and lst[i] <= b[i]):
                return False
        return True


def get_colors(img):
    show_img(img)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower = {"yellow": [25,80,10], "green": [40,60,10], "white": [90,0,100], "orange": [5,80,20], "blue":[100,60,10], "red1": [0,80,20], "red2": [170,120,10]}
    upper = {"yellow": [40,255,255], "green": [100,255,255], "white": [200,90,200], "orange": [25,255,255], "blue":[150,255,255], "red1": [3,255,255], "red2": [180,255,255]}
    
    colored_imgs = {}


    for color in ["red","orange","yellow","green","blue","white"]:
        if color == "red":
            # Special treatment for "red" because it's hsv hue can be either high or low
            red_mask1 = cv2.inRange(hsv, np.array(lower["red1"]), np.array(upper["red1"]))
            red_img1 = cv2.bitwise_and(img,img, mask=red_mask1)
            red_mask2 = cv2.inRange(hsv, np.array(lower["red2"]), np.array(upper["red2"]))
            red_img2 = cv2.bitwise_and(img,img, mask=red_mask2)
            colored_imgs["red"] = cv2.bitwise_or(red_img1, red_img2)
        else:
            color_mask = cv2.inRange(hsv, np.array(lower[color]), np.array(upper[color]))
            colored_imgs[color] = cv2.bitwise_and(img,img, mask=color_mask)

        # Convert the result to grayscale
        gray_img = cv2.cvtColor(colored_imgs[color], cv2.COLOR_BGR2GRAY)

        # Find contours in the grayscale image
        contours, _ = cv2.findContours(gray_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.1 * perimeter, True)
            if len (approx) == 4:
                area = cv2.contourArea(contour)
                (x, y, w, h) = cv2.boundingRect(approx)
                # Find aspect ratio of boundary rectangle around the countours.
                ratio = w / float(h)
                # Check if contour is close to a square.
                if ratio >= 0.8 and ratio <= 1.2 and w >= 30 and w <= 60 and area / (w * h) > 0.4:
                    print(contour)
                    cv2.rectangle(gray_img, (x,y), (x+w,y+h), (255, 0, 0), 2)

        # Filter contours by area (adjust the threshold as needed)
        large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 500]  # 500 is an example threshold

        blob_img = img.copy()
        cv2.drawContours(blob_img, large_contours, -1, (0, 255, 0), 2)

        show_img(blob_img, f'{color} blobs')
    
    
    # combined_img = cv2.bitwise_or(red_img, yellow_img)
    # combined_img = cv2.bitwise_or(blue_img, combined_img)
    # combined_img = cv2.bitwise_or(white_img, combined_img)
    # combined_img = cv2.bitwise_or(orange_img, combined_img)
    # combined_img = cv2.bitwise_or(green_img, combined_img)
    # show_img(combined_img)


    # Step 1/4: filter all contours to only those that are square-ish shapes.
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.1 * perimeter, True)
        if len (approx) == 4:
            area = cv2.contourArea(contour)
            (x, y, w, h) = cv2.boundingRect(approx)
            # Find aspect ratio of boundary rectangle around the countours.
            ratio = w / float(h)
            # Check if contour is close to a square.
            if ratio >= 0.8 and ratio <= 1.2 and w >= 30 and w <= 60 and area / (w * h) > 0.4:
                cv2.rectangle(gray, (x,y), (x+w,y+h), (255, 0, 0), 2)

    # for i, cnt in enumerate(contours):
    #     if cv2.contourArea(cnt) > 100:
    #         perimeter = cv2.arcLength(cnt, True)
    #         approx = cv2.approxPolyDP(cnt, 0.1 * perimeter, True)
    #         print(cv2.contourArea(cnt))
    #         # (x,y,w,h) = cv2.boundingRect(cnt)
    #         # cv2.rectangle(gray, (x,y), (x+w,y+h), (255, 0, 0), 2)
    #         # cv2.drawContours(gray, cnt, -1, (0, 255, 0), 3)

    print(len(contours))

    show_img(gray)

    # For each contour, make sure it has the correct area

    # Print the number of contours

if __name__ == "__main__":
    camera_input = Camera_Input()

    # Main execution
    # image = get_imgs()[0]

    # get_colors(image)

    # # Convert to HSV
    # hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # # Define the range for yellow color in HSV (example for one color)
    # yellow_lower = np.array([20, 100, 100])
    # yellow_upper = np.array([30, 255, 255])

    # # Create a mask for the yellow color
    # mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)

    # # Find contours in the mask
    # contours, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # # Sort contours by area and keep the largest one
    # contours = sorted(contours, key=cv2.contourArea, reverse=True)
    # largest_contour = contours[0]

    # # Get the bounding box of the largest contour
    # x, y, w, h = cv2.boundingRect(largest_contour)

    # # Extract the region of interest (ROI)
    # roi = image[y:y+h, x:x+w]

    # # Display the ROI
    # cv2.imshow('Detected Rubik\'s Cube', roi)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # segments = segment_image(roi)

    # # Display each segment
    # for i, segment in enumerate(segments):
    #     cv2.imshow(f'Segment {i+1}', segment)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()

    # # Analyze each segment
    # for i, segment in enumerate(segments):
    #     avg_color = get_average_color(segment)
    #     color_name = map_color(avg_color, colors)
    #     print(f'Segment {i+1} is {color_name}')
