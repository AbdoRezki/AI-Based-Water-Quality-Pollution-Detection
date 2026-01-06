# AI Based Water Quality Pollution Detection

A project that combines visual waste detection in water (YOLOv8) with water potability prediction based on physico‑chemical measurements. 

---

## Project Overview

This repository contains two complementary components related to **water** quality.   
- A computer vision model based on YOLOv8 to detect floating waste (plastic, masks, gloves, etc.) in water images using the "Water Data" dataset.   
- A supervised machine learning model to classify water potability (potable / not potable) using chemical features such as pH, hardness, dissolved solids, turbidity, and others.   

The goal is to provide an end‑to‑end approach, from visual observation of a water body to quantitative assessment of its quality. 

---

## Repository Structure

- `water_detection.py`: YOLOv8 inference script that loads the model `models/60_epochs_denoised.pt` and performs object detection on `image_test.jpg`.   
- `water-detection.ipynb`: Kaggle notebook for exploring the "Water Data" dataset, preparing annotations, and training/evaluating the detection model.   
- `water-quality.ipynb`: Kaggle notebook for loading, cleaning (handling NaNs), and exploring the "Water Quality and Potability" dataset, then building potability classification models.   
- `models/60_epochs_denoised.pt`: Trained YOLOv8 weights on the water pollution dataset (add to this folder).   

---

## Datasets

- **Water Data (waste detection)**  
  URL: https://www.kaggle.com/datasets/abderrahmanrezki/water-data   
  Contains annotated images (bounding boxes) of plastics, masks, gloves, and other waste in aquatic environments.   

- **Water Quality and Potability (classification)**  
  URL: https://www.kaggle.com/datasets/uom190346a/water-quality-and-potability   
  Tabular dataset with 3276 samples and 9 features (`ph`, `Hardness`, `Solids`, `Chloramines`, `Sulfate`, `Conductivity`, `Organic_carbon`, `Trihalomethanes`, `Turbidity`) plus binary target `Potability`. 

---

## Usage

### 1. Waste Detection (YOLOv8)

- Place your test image as `image_test.jpg` at the project root or update the path in `water_detection.py`.   
- Ensure the model weights `models/60_epochs_denoised.pt` are in the `models` directory.   
- Run:  
 ```bash
python water_detection.py
```
  water_detection.py
- Output: Detection results printed, bounding box coordinates in coord list, annotated image displayed.

### 2. Water Potability Classification

- Open `water-quality.ipynb` in Jupyter or Kaggle. 
- Update CSV path if needed (default: /kaggle/input/water-quality-and-potability/water_potability.csv).
- Execute cells to:
    - Load & inspect data
    - Handle NaNs & EDA
    - Train/evaluate classification models

### 3. Full Pipeline 

- Run `water_detection.py` → detect waste → assess visual pollution
- Collect water sample → measure 9 physico-chemical parameters
- Run `water-quality.ipynb` → predict potability
- Combine results for comprehensive water quality report.