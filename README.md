# **Explanation of the Entity Value Extraction Script**

---

**Names:** Shashank C, Shreevathsa G P, Samar Garg 

**University:** PES University

**Team:** Watermelon Wings  

**Project:** Entity Value Extraction from Product Images

---

## **Overview**

The script performs entity value extraction from product images using Optical Character Recognition (OCR) and other image processing techniques. It involves several steps including image preprocessing, OCR, and post-processing to extract meaningful data from the images and compare it with expected values.

## **Script Breakdown**

### **0. Setting Up**

1. **Imports and Setup**:
   - The script imports necessary libraries such as `os`, `cv2`, `logging`, and `PaddleOCR`.
   - It sets up logging configurations and verifies the existence of required CSV files.

2. **Paths Configuration**:
   - Paths for dataset files (`train.csv`, `test.csv`, `sample_test.csv`) are defined.
   - It checks if these files are present in the specified paths.

### **1. Helper Functions**

1. **`display_image(image)`**:
   - Displays an image using Matplotlib.

2. **`find_all_indices(s, substring)`**:
   - Finds all indices of a substring within a string.

3. **`is_valid_representation(x)`**:
   - Checks if a value matches any of the valid unit representations.

4. **`make_clickable_path(path)`**:
   - Generates an HTML clickable path if the file exists.

5. **`display_path(path)`**:
   - Displays the clickable path in the IPython display.

6. **`extract_weights_with_units(weight_list)`**:
   - Extracts numeric weights and their units from a list of strings.

7. **`convert_to_kg(value, unit)`**:
   - Converts weight to kilograms based on the provided unit.

### **2. Training**

1. **Preprocessing**:
   - Reads and preprocesses the image using OpenCV (`cv2`).
   - Converts the image to RGB format.

2. **Text Recognition**:
   - Uses PaddleOCR to perform OCR on the preprocessed image.
   - Displays OCR results on the image.

3. **Post Processing**:
   - Extracts measurements and positions from OCR results.
   - Formats and processes numerical values.
   - Handles European number formats and unit conversions.

### **3. Naive Iteration**

1. **Imports and Setup**:
   - Imports `pandas`, `tqdm`, and `ThreadPoolExecutor` for processing.
   - Defines paths for input and output CSV files.

2. **`process_row(index, row, image_folder_in)`**:
   - Processes each row in the DataFrame:
     - Reads the image.
     - Applies OCR.
     - Extracts and processes measurements based on entity types.
     - Handles errors and debugging.

3. **Parallel Processing**:
   - Optionally uses multi-threading to speed up processing.
   - Processes rows either sequentially or in parallel depending on the `MULTI_THREADED` flag.

4. **Output**:
   - Compiles results into a DataFrame.
   - Saves the output to a CSV file.

## **Key Points**

- **Image Preprocessing**: Ensures that the images are in the correct format for OCR.
- **OCR**: Extracts text data from images using PaddleOCR.
- **Post Processing**: Processes and formats the extracted text to match expected values.
- **Error Handling**: Includes mechanisms for debugging and handling errors during processing.
- **Parallel Processing**: Optionally speeds up the process using multiple threads.

---

Feel free to modify or expand upon this explanation as needed!
