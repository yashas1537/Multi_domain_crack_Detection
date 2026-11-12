# Concrete Crack Detection Module

## Overview
The Concrete module is an experimental AI-based visual inspection system designed to detect, segment, measure and analyze cracks in concrete surfaces.

## Features

- Concrete crack detection using YOLO11n segmentation.
- Crack localization using bounding boxes and segmentation masks.
- Pixel-based crack length and width estimation.
- Relative scene-depth visualization using Depth Anything V2.
- Grad-CAM-based explainability experiments.
- FAISS-based retrieval-augmented knowledge retrieval.
- Preliminary inspection recommendations.
- Structured JSON inspection reports.

## Technology Stack

- Python
- Google Colab
- Ultralytics YOLO11n
- PyTorch
- OpenCV
- Depth Anything V2
- Grad-CAM
- Sentence Transformers
- FAISS

## Project Structure

```text
Concrete/
├── notebook/
│   └── Multi_Industry_Crack_Detection (1).ipynb
├── README.md
├── DEVELOPMENT_LOG.md
└── requirements.txt
```

## Execution

1. Open the notebook using Google Colab.
2. Configure the Google Drive paths.
3. Load the trained YOLO checkpoint.
4. Upload a concrete surface image.
5. Run the detection and segmentation pipeline.
6. Review measurement, depth visualization and explainability outputs.
7. Review retrieved knowledge and preliminary recommendations.
8. Generate the inspection report.

## Current Limitations

- Model performance requires further validation and improvement.
- Pixel measurements require calibration for physical units.
- Depth Anything V2 provides relative scene-depth estimates, not calibrated crack penetration depth.
- Recommendations are preliminary and require human verification.
- The web application and backend integration are pending.

## Future Work

- Improve detection accuracy.
- Validate measurement and depth estimation.
- Improve explainability and RAG.
- Integrate the module with a web application.
- Generate downloadable inspection reports.

**Note:** This is an academic experimental system and does not replace professional structural inspection.
