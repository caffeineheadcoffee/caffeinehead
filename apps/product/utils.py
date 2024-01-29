from django.utils.text import slugify

from apps.core.utils import generate_filename


def upload_product_image_to(instance, filename):
    """
    Returns path to upload to
    :param instance: instance of model
    :param filename: original filename
    :return: path
    """
    return 'product/{}-{}'.format(
        slugify(instance.product.name),
        generate_filename(
            filename=filename,
            keyword=str(instance.pk)
        )
    )
