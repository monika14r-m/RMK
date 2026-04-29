import numpy as np
from core.removal import remove_watermark

def test_remove_watermark_runs():
    # Create a dummy image (100x100 black square)
    img = np.zeros((100, 100, 3), dtype=np.uint8)

    # Run removal function
    result = remove_watermark(img)

    # Check output shape matches input
    assert result.shape == img.shape
