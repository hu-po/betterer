""" Zero-shot classification with LiT using natural language.

Sample command:
> python zero-shot.py --image_dir ~/dev/betterer/lit/buboo_images

"""


import argparse
import logging
import os
from typing import List

import jax
import jax.numpy as jnp
import numpy as np
import pandas as pd
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds
import tqdm
from matplotlib import pyplot as plt
from vit_jax import models

parser = argparse.ArgumentParser()
parser.add_argument('--image_dir', type=str, default='data/imagenet')

if __name__ == '__main__':

    # Parse arguments
    args = parser.parse_args()

    # Make tensorflow less spammy
    tf.get_logger().setLevel(logging.ERROR)

    # What hardware is this running on?
    print(f'jax.device_count() {jax.device_count()}')
    print(f'jax.local_device_count() {jax.local_device_count()}')
    for i, device in enumerate(jax.devices()):
        print(f' --- found device: {i} ')
        print(f'device_kind {device.device_kind}')
        print(f'platform {device.platform}')
        print(f'host_id {device.host_id}')

    # Load the model
    all_model_names = ['LiT-B16B', 'LiT-L16L', 'LiT-L16S', 'LiT-L16Ti']
    model_name = 'LiT-L16S'
    model = models.get_model(model_name)
    # Loading the variables from cloud can take a while the first time...
    lit_variables = model.load_variables()
    # Creating tokens from freeform text (see next section).
    tokenizer = model.get_tokenizer()
    # Resizing images & converting value range to -1..1 (see next section).
    image_preprocessing = model.get_image_preprocessing()
    # Preprocessing op for use in tfds pipeline (see last section).
    pp = model.get_pp()

    # Clean up Image path
    image_dir: str = os.path.expanduser(args.image_dir)
    assert os.path.exists(image_dir), f'Image directory not found: {image_dir}'

    # Load the dataset using tfds
    # ds: tf.data.Dataset = tfds.load('imagenet2012', data_dir=image_dir)

    image_name_list: List[str] = [
        '001.png',
        '002.png',
        '003.png',
    ]

    # Load the images into numpy arrays using PIL
    image_list: List[np.ndarray] = []
    for image_name in image_name_list:
        image_filepath: str = os.path.join(image_dir, image_name)
        _image = PIL.Image.open(image_filepath).convert('RGB')
        image: np.ndarray = np.array(_image)
        print(f'Image shape: {image.shape}')
        image_list.append(image)
    
    # View image
    images = image_preprocessing(image_list)
    # plt.figure(figsize=(15, 4))
    # plt.imshow(np.hstack(images) * .5 + .5)
    # plt.axis('off')
    # plt.show()

    # Possible classifications using natural language
    texts = [
        'cat sitting on a yoga mat',
        'cat laying on a computer mat',
        'two men in black clothing walking on street',
    ]
    tokens = tokenizer(texts)
    
    # Embed both texts and images with a single model call.
    # See next section for embedding images/texts separately.
    zimg, ztxt, out = model.apply(lit_variables, images=images, tokens=tokens)

    # @jax.jit
    # def embed_images(variables, images):
    #     zimg, _, _ = model.apply(variables, images=images)
    #     return zimg

    # @jax.jit
    # def embed_texts(variables, text_tokens):
    #     _, ztxt, _ = model.apply(variables, tokens=text_tokens)
    #     return ztxt

    # Display results
    probs = np.array(jax.nn.softmax(out['t'] * ztxt @ zimg.T, axis=1))
    for i, row in enumerate(probs):
        for t, prob in enumerate(row):
            print(f'The probability that {image_name_list[i]} is {texts[t]}: {prob:.2f}')