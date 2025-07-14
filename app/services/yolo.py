import base64
import io
from logging import Logger

from PIL import Image
from ultralytics import YOLO
from ultralytics.engine.results import Results


class YOLOService:
    model_name = "yolo11n.pt"

    def __init__(self, logger: Logger):
        self.model = YOLO(self.model_name)
        self.logger = logger


    @staticmethod
    def _get_image(image_str: str) -> Image:
        image_bytes = base64.b64decode(image_str)
        return Image.open(io.BytesIO(image_bytes))


    @staticmethod
    def _collect_results(results: Results) -> list[str]:
        detected_obj = []
        classes_names = results.names
        classes = results.boxes.cls.cpu().numpy()

        for class_id in classes:
            class_name = classes_names[int(class_id)]
            detected_obj.append(f"{class_name} ID:{int(class_id)}")

        return detected_obj


    def detect_image(self, image_str: str):
        image = self._get_image(image_str)
        results = self.model(image)[0]
        return self._collect_results(results)
