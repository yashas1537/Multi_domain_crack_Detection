Concrete Crack Detection – Development Log

Project Overview

Development activities for the Concrete Crack Detection module of the AI-Based Multi-Domain Visual Inspection Platform.

Development Activities

1. Dataset Preparation

- Prepared the concrete crack dataset.
- Cleaned and validated image annotations.
- Converted annotations into YOLO segmentation format.
- Created training, validation and testing datasets.

2. Crack Detection and Segmentation

- Implemented YOLO11n segmentation.
- Trained the model using the prepared concrete dataset.
- Generated crack detection predictions and segmentation masks.
- Evaluated model performance.

3. Crack Measurement

- Implemented pixel-based crack measurement.
- Extracted crack length and width estimates from segmentation masks.
- Generated measurement outputs for detected regions.

4. Depth Estimation

- Integrated Depth Anything V2.
- Generated relative depth maps.
- Explored depth visualization alongside crack regions.

5. Explainability

- Explored Grad-CAM-based visual explanations.
- Generated heatmaps and overlay visualizations.

6. Knowledge Retrieval

- Developed a concrete inspection knowledge base.
- Integrated Sentence Transformers for text embeddings.
- Implemented FAISS-based similarity retrieval.

7. Recommendation and Reporting

- Implemented preliminary rule-based inspection recommendations.
- Combined inspection evidence into structured JSON reports.
- Generated visual inspection outputs.

Current Development Status

- Concrete inspection pipeline: Experimental implementation.
- Model evaluation and validation: Further improvement required.
- Website integration: Pending.
- Backend integration: Pending.

Next Development Goals

- Verify reproducibility from a fresh runtime.
- Improve model performance.
- Validate measurement and depth estimation.
- Improve explainability and recommendations.
- Develop the Concrete web interface.

---
