from google.cloud import vision


def localize_objects(binary_info):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """

    object_names = ['Lighting',
                    'Television',
                    'Refrigerator',
                    'Dishwasher',
                    'Microwave oven',
                    'Laptop',
                    'Washing machine',
                    'Mobile phone'
                    ]

    client = vision.ImageAnnotatorClient()

    image = vision.Image(content=binary_info)

    objects = client.object_localization(image=image).localized_object_annotations

    if len(objects) == 0:
        return None

    object_name = objects[0].name

    if object_name not in object_names:
        return None
    return object_name


# if __name__ == "__main__":
#     localize_objects('./cell phone.jpeg')
