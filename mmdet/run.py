""" Testing out MMDetection. """

import os
import mmdet
import mmdet.apis
from mim import download

for config_file, checkpoint_file in [
    # ('yolov3_mobilenetv2_320_300e_coco.py', 'yolov3_mobilenetv2_320_300e_coco_20210719_215349-d18dff72.pth'),
    ('mmdetection/configs/resnest/faster_rcnn_s101_fpn_syncbn-backbone+head_mstrain-range_1x_coco.py', 'faster_rcnn_s101_fpn_syncbn-backbone+head_mstrain-range_1x_coco_20201006_021058-421517f1.pth'),
]:
    # download('mmdet', ['yolov3_mobilenetv2_320_300e_coco'], dest_root=os.getcwd())

    for image in [
        '/tmp/aiastronaut.png',
        '/tmp/aiastronaut_crispy.png',
        # '/tmp/aicowboy.png',
        # '/tmp/people.png',
    ]:
        for device in [
            # 'cpu',
            'cuda:0',
        ]:
            model = mmdet.apis.init_detector(
                config_file, checkpoint_file, device=device)
            result = mmdet.apis.inference_detector(model, image)
            print(f"Device: {device}")
            print(result)
            mmdet.apis.show_result_pyplot(model, image, result)
