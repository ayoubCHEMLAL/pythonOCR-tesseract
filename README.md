# pythonOCR-tesseract
Text recognition using Python 3.6 with Tesseract + OpenCV.

## Install Tesseract 4.0 on Ubuntu 14.04, 16.04, 17.04, 17.10
```
sudo add-apt-repository ppa:alex-p/tesseract-ocr
sudo apt-get update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
sudo pip install pytesseract
```

## Checking Tesseract version
```tesseract --version```

## Tesseract Basic Usage
We can use the command line utility or use the Tesseract API to integrate it in our C++ and Python application. In the very basic usage, we specify the following

**1. Input filename:** We use image.jpg in the examples below.
**2. OCR language:** The language in our basic examples is set to English (eng). On the command line and pytesseract, it is specified using the `-l` option.
**3. OCR Engine Mode (oem):** Tesseract 4 has two OCR engines — 1) Legacy Tesseract engine 2) LSTM engine. There are four modes of operation chosen using the `--oem` option.

```
  0    Legacy engine only.
  1    Neural nets LSTM engine only.
  2    Legacy + LSTM engines.
  3    Default, based on what is available.
```

**4. Page Segmentation Mode (psm):** PSM can be very useful when you have additional information about the structure of the text. We will cover some of these modes in a followup tutorial. In this tutorial we will stick to psm = 3 (i.e. PSM_AUTO).
Note: When the PSM is not specified, it defaults to 3 in the command line and python versions, but to 6 in the C++ API. If you are not getting the same results using the command line version and the C++ API, explicitly set the PSM.
