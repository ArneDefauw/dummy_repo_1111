from rasterio import Affine

from dummy.some.data import some_test


def test_some_test():
    affine = some_test()
    assert isinstance(affine, Affine)
