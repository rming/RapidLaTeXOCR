# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com
from rapid_latex_ocr import LaTeXOCR


def load_model(use_cuda: bool = True) -> LaTeXOCR:
    """Load the LaTeXOCR model."""
    return LaTeXOCR(use_cuda=use_cuda)


def run_with_gpu():
    model = load_model(use_cuda=True)
    img_path = "tests/test_files/6.png"
    with open(img_path, "rb") as f:
        data = f.read()
    res, elapse = model(data)
    print("GPU result:", res)
    print("GPU time:", elapse)


def run_with_cpu():
    model = load_model(use_cuda=False)
    img_path = "tests/test_files/6.png"
    with open(img_path, "rb") as f:
        data = f.read()
    res, elapse = model(data)
    print("CPU result:", res)
    print("CPU time:", elapse)


if __name__ == "__main__":
    run_with_gpu()
    run_with_cpu()
