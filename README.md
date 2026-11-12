# AI-Based Multi-Domain Visual Inspection Platform

An experimental AI-powered visual inspection project focused on
detecting and analyzing surface cracks in concrete. The project combines
deep-learning-based crack segmentation with scene-depth estimation,
explainability experiments, retrieval-augmented inspection guidance,
preliminary severity triage, and structured reporting.

> **Project status:** Experimental research and development. The current
> notebook primarily implements the concrete inspection workflow. A
> unified multi-domain web application is planned; the notebook should
> not be interpreted as a completed production platform.

## Overview

Conventional visual inspection can be time-consuming and depends heavily
on manual observation. This project explores an AI-assisted workflow
that can identify visible crack regions, extract image-space evidence,
retrieve relevant inspection guidance, and generate a structured report
for human review.

The system is designed to assist inspection---not replace qualified
engineering assessment.

## Implemented Workflow

``` text
Concrete Image Upload
        |
        v
YOLO Crack Detection and Segmentation
        |
        v
Pixel-space Detection / Mask Evidence
        |
        +--------------------------+
        |                          |
        v                          v
Scene-depth Estimation       Visual Results
(Depth Anything V2)          and Overlays
        |
        v
Inspection Evidence
        |
        v
FAISS-based RAG Retrieval
        |
        v
Rule-based Preliminary Triage
        |
        v
Recommendations and Sources
        |
        v
Structured JSON Inspection Report
```

## Features in the Notebook

### 1. Crack detection and segmentation

-   Uses an Ultralytics YOLO model checkpoint for concrete crack
    inference.
-   Produces bounding-box detections and segmentation masks.
-   Supports image upload and prediction in Google Colab.
-   Saves annotated prediction images and mask visualizations.
-   Records confidence values and pixel-space coordinates.

### 2. Scene-depth estimation

-   Integrates Depth Anything V2 for image-level scene-depth estimation.
-   Generates and visualizes a depth map for the input image.
-   Explores combining crack masks with the scene-depth output.

**Important limitation:** The generated depth map is relative
scene-depth information. It is not a calibrated measurement of crack
penetration depth in millimetres. The notebook also contains a simulated
visualization example; simulated values must not be presented as
measured physical depth.

### 3. Retrieval-Augmented Generation (RAG)

-   Builds a starter concrete-inspection knowledge base.
-   Uses `sentence-transformers/all-MiniLM-L6-v2` to generate text
    embeddings.
-   Uses FAISS for similarity-based retrieval.
-   Retrieves relevant inspection guidance and source metadata for a
    query.
-   Saves and restores the knowledge base, embeddings, and FAISS index.

Similarity scores indicate textual relevance, not engineering certainty.

### 4. Preliminary severity triage

A rule-based triage function evaluates explicitly supplied evidence
flags and returns preliminary categories, including:

-   Preliminary / Undetermined
-   Moderate Concern
-   High Concern
-   Insufficient Evidence
-   Urgent Safety Concern

The triage is advisory. Crack detections alone do not establish
structural severity, spalling, exposed reinforcement, or structural
safety.

### 5. Structured inspection reports

The notebook combines available outputs into JSON reports, including:

-   Image and inspection metadata
-   YOLO detection evidence
-   Confidence and pixel-space coordinates
-   Segmentation evidence
-   Scene-depth summary, where available
-   Preliminary triage result
-   Retrieved RAG guidance and source information
-   Interpretation limitations

The notebook saves project artifacts and reports to Google Drive.

### 6. Visual outputs

The notebook includes annotated detection previews, segmentation-mask
visualizations, depth-map visualizations, and inspection evidence
displays.

## Technology Stack

  Area                                Technology
  ----------------------------------- -----------------------
  Language                            Python
  Notebook environment                Google Colab
  Object detection and segmentation   Ultralytics YOLO
  Deep learning                       PyTorch
  Image processing                    OpenCV, NumPy, Pillow
  Visualization                       Matplotlib
  Scene-depth estimation              Depth Anything V2
  Text embeddings                     Sentence Transformers
  Vector search                       FAISS
  Reporting                           JSON
  Storage / backup                    Google Drive

## Running the Notebook

The main implementation is provided as a Google Colab notebook.

1.  Open the `.ipynb` notebook in Google Colab.
2.  Select a runtime with GPU support if available.
3.  Mount Google Drive when prompted.
4.  Ensure the trained YOLO checkpoint and required backup artifacts are
    available at the paths configured in the notebook.
5.  Run the setup and model-loading cells before running inference.
6.  Upload a concrete crack image when prompted.
7.  Review the detection, segmentation, depth visualization, retrieved
    guidance, and generated report.

### Expected saved artifacts

The notebook uses a Google Drive backup directory similar to:

``` text
CrackDetection_Backup/
├── best_improved.pt
├── concrete_rag_knowledge_base.json
├── concrete_rag_embeddings.npy
├── concrete_rag_faiss.index
├── concrete_inspection_rag_report.json
├── concrete_inspection_yolo_preview.jpg
└── scene_depth.npy
```

The exact files available depend on which notebook cells have been
executed successfully. Update paths in the notebook if your Drive folder
structure differs.

## Current Limitations

-   The notebook is an experimental workflow, not a packaged
    application.
-   A clean, end-to-end run from a fresh Colab runtime should be
    verified.
-   Model accuracy must be evaluated on a clearly defined held-out test
    set before making performance claims.
-   Bounding-box and mask pixel values are not physical measurements
    without camera calibration and a suitable reference scale.
-   Depth Anything V2 scene-depth output is not crack penetration depth.
-   Rule-based triage is preliminary and depends on evidence flags; it
    is not an automated structural-safety certification.
-   RAG retrieval provides supporting text, not verified engineering
    decisions.
-   Any optional vision-language-model workflow depends on the local
    model/server setup and should be checked separately.
-   A unified frontend and backend deployment are not included as
    completed features in this notebook.

## Planned Work

-   Improve and systematically evaluate the concrete segmentation model.
-   Validate the pipeline from a fresh runtime.
-   Establish calibrated measurement methods where suitable ground truth
    is available.
-   Improve and validate explainability outputs.
-   Strengthen the concrete knowledge base and source-grounded
    recommendations.
-   Package the pipeline into reusable Python modules and an API.
-   Build a web interface and integrate additional inspection domains.
-   Add reproducible tests and documentation.

## Safety and Responsible Use

This project is intended for academic experimentation and decision
support. It must not be used as the sole basis for structural-safety
decisions, repair choices, or declarations that a structure is safe. All
findings require human review and, where appropriate, assessment by
qualified structural professionals.

## Repository

Developed as an academic project exploring explainable AI-assisted
visual inspection across industrial domains.
