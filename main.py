import os
import cv2
import divide
import predict
import translate

# Define input and output directories
input_dir = "C:/Users/HP/Desktop/IEEE/chess-ai-main/input"
output_dir = "output"

# Make sure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get all image files from the input directory
image_files = [f for f in os.listdir(input_dir) if f.endswith(('.jpg', '.PNG', '.jpeg'))]

# Process each image in the input directory
for img_file in image_files:
    # Construct full path to the image
    img_full_path = os.path.join(input_dir, img_file)
    
    # Read the image
    img = cv2.imread(img_full_path)

    # Process the image (divide the board, make predictions, convert to FEN)
    images = divide.divideBoard(img)
    labels = predict.prediction(images)
    fen = translate.toFEN(labels)

    # Save the FEN result to the output/fen.txt file
    fen_output_path = os.path.join(output_dir, f"{img_file}_fen.txt")
    with open(fen_output_path, "w") as file:
        file.write(fen)

    print(f"FEN for {img_file} saved to {fen_output_path}")
