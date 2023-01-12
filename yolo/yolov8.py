"""

CLI command:

# SNOWMOBILE

yolo task=detect mode=predict model=yolov8n.pt source="/tmp/ai_generated_skimobile.png"

yolo task=segment mode=predict model=yolov8n-seg.pt source="/tmp/ai_generated_skimobile.png"

# OTTERS

yolo task=detect mode=predict model=yolov8n.pt source="/tmp/ai_generated_otters.png"

yolo task=segment mode=predict model=yolov8n-seg.pt source="/tmp/ai_generated_otters.png"

yolo task=detect mode=predict model=yolov8x.pt source="/tmp/ai_generated_otters.png"

yolo task=segment mode=predict model=yolov8x-seg.pt source="/tmp/ai_generated_otters.png"

yolo task=classify mode=predict model=yolov8n-cls.pt source="/tmp/ai_generated_otters.png"

yolo task=classify mode=predict model=yolov8x-cls.pt source="/tmp/ai_generated_otters.png"

small model = n03207941 "dishwasher"
big model = n02111500 "Great Pyrenees"


"""

from ultralytics import YOLO

for model_name in [
    "yolov8n.pt",
    # "yolov8s.pt",
    # "yolov8m.pt",
    # "yolov8l.pt",
    "yolov8x.pt",
]:
    model = YOLO(model_name)

    model.info(verbose=True)

    outputs = model.predict("/tmp/ai_generated_skimobile.png", show=True, visualize=True)
    # for output in outputs:
    #     print(output["det"])  # np.ndarray, (N, 6), xyxy, score, cls