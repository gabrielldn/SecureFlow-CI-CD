import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bg_remove import convert_image
from PIL import Image
import io

def test_convert_image():
    img = Image.new("RGB", (100, 100), color="red")
    
    img_bytes = convert_image(img)
    
    assert isinstance(img_bytes, bytes)
    assert len(img_bytes) > 0

    buf = io.BytesIO(img_bytes)
    loaded_img = Image.open(buf)
    assert loaded_img.size == (100, 100)
