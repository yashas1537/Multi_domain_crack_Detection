
from pathlib import Path
from ultralytics import YOLO


def load_crack_model(checkpoint_path):
    """
    Load the trained concrete crack segmentation model.
    """
    checkpoint = Path(checkpoint_path)

    if not checkpoint.is_file():
        raise FileNotFoundError(
            f"Model checkpoint not found: {checkpoint}"
        )

    return YOLO(str(checkpoint))


def detect_cracks(model, image_path, conf=0.25, imgsz=640):
    """
    Detect and segment cracks in an input image.
    """
    image = Path(image_path)

    if not image.is_file():
        raise FileNotFoundError(
            f"Input image not found: {image}"
        )

    results = model.predict(
        source=str(image),
        conf=conf,
        imgsz=imgsz,
        save=False,
        verbose=False
    )

    return results[0]
