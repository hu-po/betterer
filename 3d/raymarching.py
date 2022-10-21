""" Toy Implementation of Ray Marching."""

import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image

IMAGE_SIZE_W: int = 256
IMAGE_SIZE_H: int = 256
STEP_SIZE: float = 0.1
NUMBER_OF_STEPS: int = 32
MIN_HIT_DISTANCE: float = 0.001
MAX_HIT_DISTANCE: float = 1000.0
CENTER_OF_SPHERE: np.ndarray = np.array([0, 0, 5])
RADIUS_OF_SPHERE: float = 1.0
CENTER_OF_CAMERA: np.ndarray = np.array([0, 0, -5])
CENTER_OF_IMAGE_PLANE: np.ndarray = np.array([0, 0, 0])
CENTER_OF_LIGHT: np.ndarray = np.array([4, 4, 5])
IMAGE_PLANE_SIZE_X: float = 1.0
IMAGE_PLANE_SIZE_Y: float = 1.0
COLOR_BACKGROUND: np.ndarray = np.array([0, 0, 0])
COLOR_OBJECT: np.ndarray = np.array([1, 0, 0])
NORMAL_DERIVATIVE_DELTA: float = 0.0001


def distance_from_sphere(point: np.ndarray,
                         center: np.ndarray = CENTER_OF_SPHERE,
                         radius: float = RADIUS_OF_SPHERE) -> float:
    """ Distance from a sphere of a point."""
    return np.linalg.norm(point - center) - radius


def normals_on_sphere(point: np.ndarray, center: np.ndarray) -> np.ndarray:
    """ Normals on a sphere of a point."""
    return (point - center) / np.linalg.norm(point - center)


def sdf(point: np.ndarray) -> float:
    """ Signed Distance Function."""
    displacement = np.sin(point[0] * 10.0) * np.sin(point[1] * 10.0) * np.sin(point[2] * 10.0) * 0.25
    return distance_from_sphere(point) + displacement


def normal(point: np.ndarray) -> np.ndarray:
    """ Normal calculated with a derivative trick."""
    normal_vector = np.array([
        sdf(point + np.array([NORMAL_DERIVATIVE_DELTA, 0, 0])) -
        sdf(point - np.array([NORMAL_DERIVATIVE_DELTA, 0, 0])),
        sdf(point + np.array([0, NORMAL_DERIVATIVE_DELTA, 0])) -
        sdf(point - np.array([0, NORMAL_DERIVATIVE_DELTA, 0])),
        sdf(point + np.array([0, 0, NORMAL_DERIVATIVE_DELTA])) -
        sdf(point - np.array([0, 0, NORMAL_DERIVATIVE_DELTA]))
    ])
    return normal_vector / np.linalg.norm(normal_vector)


def ray_march(ray_origin: np.ndarray, ray_direction: np.ndarray) -> np.ndarray:
    """ Ray Marching, returns an RGB color."""
    total_distance: float = 0.0
    for _ in range(NUMBER_OF_STEPS):
        cur_pos: np.ndarray = ray_origin + ray_direction * total_distance
        distance: float = sdf(cur_pos)
        # Hit an object (SDF is either close to 0 or negative)
        if distance < MIN_HIT_DISTANCE:
            # # Just return the color of the object
            # return COLOR_OBJECT
            
            # # Lets calculate the normal vector at this point
            # normal_vector: np.ndarray = normal(cur_pos)
            # normal_vector = normal_vector * 0.5 + 0.5
            # return normal_vector

            # Calculate some diffuse lighting
            normal_vector: np.ndarray = normal(cur_pos)
            light_vector: np.ndarray = cur_pos - CENTER_OF_LIGHT
            light_vector = light_vector / np.linalg.norm(light_vector)
            diffuse_light: float = max(0.0, np.dot(normal_vector, light_vector))
            return COLOR_OBJECT * diffuse_light

        # Missed all objects, our ray is going further than we want
        if distance > MAX_HIT_DISTANCE:
            break
        # Add accumulated distance
        total_distance += distance
    return COLOR_BACKGROUND


# Empty image buffer
image = np.zeros((IMAGE_SIZE_W, IMAGE_SIZE_H, 3), dtype=np.float32)

# Generate a grid of points in the image plane
image_plane_x, image_plane_y = np.meshgrid(
    np.linspace(-IMAGE_PLANE_SIZE_X/2, IMAGE_PLANE_SIZE_X/2, IMAGE_SIZE_W),
    np.linspace(-IMAGE_PLANE_SIZE_Y/2, IMAGE_PLANE_SIZE_Y/2, IMAGE_SIZE_H),
)

# Generate all the rays coming from the camera
for x in range(IMAGE_SIZE_W):
    for y in range(IMAGE_SIZE_H):
        image_plane_point: np.ndarray = np.array(
            [CENTER_OF_IMAGE_PLANE[0] + image_plane_x[x][y],
             CENTER_OF_IMAGE_PLANE[1] + image_plane_y[x][y],
             CENTER_OF_IMAGE_PLANE[2]])
        ray_center = CENTER_OF_CAMERA
        ray_direction = image_plane_point - ray_center
        ray_direction = ray_direction / np.linalg.norm(ray_direction)
        pixel_color = ray_march(ray_center, ray_direction)
        image[x, y, :] = pixel_color

# Convert to 8-bit image (0, 255)
image *= 255
image = image.astype(np.uint8)

# Save to image
Image.fromarray(image).save('render.png')
