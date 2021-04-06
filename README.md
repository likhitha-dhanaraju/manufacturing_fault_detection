</p># manufacturing_fault_detection

## Introduction

This is the code repository of my Major project work, **"Manufacturing Fault Detection using Deep Learning"**

The objective of this project is,

*"To develop a universal model for the detection of faults of various manufacturing defect datasets irrespective of the nature of the defects or the products and to develop a streamlined process for preprocessing and training the model for any dataset."*

---

## The datasets used in this project


#### 1. Casting dataset: </br>

- This dataset is of casting manufacturing products.  
- The pictures are the top view of a submersible pump impeller. The dataset contains a total 7348 image data. These all are the size of (300x300) pixels grey-scaled images. In all images, augmentation already applied. 
- The dataset also contains images of size of 512x512 grayscale. This data set is without data augmentation. This contains 519 “ok front” and 781 “defective front” impeller images.

<p align="center">
  
<img src="https://user-images.githubusercontent.com/34205126/113442554-ddb45200-940d-11eb-9a3c-fcb47324068a.jpeg">
<img src="https://user-images.githubusercontent.com/34205126/113442558-dee57f00-940d-11eb-8fc0-5eb9ddbc92db.jpeg">

<p align="center">
Defective products
</p></p>

<p align="center">
  
<img src="https://user-images.githubusercontent.com/34205126/113442561-df7e1580-940d-11eb-85e6-e97fb456a568.jpeg">
<img src="https://user-images.githubusercontent.com/34205126/113442562-e016ac00-940d-11eb-9417-5a072e0637c7.jpeg">
![cast_def_0_197](
<p align="center">
Non defective products
</p>

#### 2.	Civil Surface Crack Dataset: </br>

- Crack detection plays a major role in the building inspection, finding the cracks and determining the building health.
- The dataset contains images of various concrete surfaces with and without crack. The image data is divided into two as negative (without crack) and positive (with crack) in a separate folder for image classification. 
- Each class has 20000 images with a total of 40000 images with 227 x 227 pixels with RGB channels.

<p align="center">
  
<img src="https://user-images.githubusercontent.com/34205126/113442859-7054f100-940e-11eb-9c37-632f4b033b6c.jpg">
<img src="https://user-images.githubusercontent.com/34205126/113442860-71861e00-940e-11eb-8bc8-5afa92cb07d5.jpg">

</p>
<p align="center">
Non-cracked walls ( Negative )
</p>

<p align="center">
  
<img src="https://user-images.githubusercontent.com/34205126/113442862-734fe180-940e-11eb-9c4f-604268773703.jpg">
<img src="https://user-images.githubusercontent.com/34205126/113442864-734fe180-940e-11eb-914f-1f8b6cbe16a0.jpg">
</p>

<p align="center">
  <b>Cracked walls ( Positive )</b>
</p>

#### 3. Steel Defect Dataset: </br>

- Severstal is leading the charge in efficient steel mining and production. The production process of flat sheet steel is especially delicate. 
- From heating and rolling, to drying and cutting, several machines touch flat steel by the time it’s ready to ship. 
- The dataset is annotated for the purpose of classification as well as object detection. Contains 3000 images of size 256 x 1600 of four different classes. 

<p align="center">

<img src="https://user-images.githubusercontent.com/34205126/113724645-2e7ac200-9710-11eb-9976-2f7a1926261c.jpg">
Class_: 
<img src="https://user-images.githubusercontent.com/34205126/113724661-3175b280-9710-11eb-9236-315c6c61f2d8.jpg">

<img src="https://user-images.githubusercontent.com/34205126/113724730-43efec00-9710-11eb-8fc5-0ce6ec7ddaa4.jpg">

<img src="https://user-images.githubusercontent.com/34205126/113724738-46eadc80-9710-11eb-88d0-56fcb90f982c.jpg">

<p>

#### 4.	GC10 Metal Surface Dataset: </br>
- Severstal is leading the charge in efficient steel mining and production. The production process of flat sheet steel is especially delicate. 
- From heating and rolling, to drying and cutting, several machines touch flat steel by the time it’s ready to ship. 
- The dataset is annotated for the purpose of classification as well as object detection. Contains 3000 images of size 256 x 1600 of four different classes. 
 
 
#### 5. Solar Cells dataset: </br>

- The dataset contains 2,624 samples of 300x300 pixels 8-bit grayscale images of functional and defective solar cells with varying degrees of degradations extracted from 44 different solar modules. 
- The defects in the annotated images are either of intrinsic or extrinsic type and are known to reduce the power efficiency of solar modules.All images are normalized with respect to size and perspective. 
- Every image is annotated with a defect probability (a floating point value between 0 and 1) and the type of the solar module (either mono- or polycrystalline) the solar cell image was originally extracted from. 

####  6.	Welding Dataset: </br>

- This dataset was developed from a system for assessing tungsten inert gas (TIG) welding using a high dynamic range (HDR) camera with the help of artificial neural networks (ANN) for image processing. 
- The images were of the TIG welding process in the visible spectrum with improved contrast, similar to what a welder would normally see. The dataset contains around 30000 images of 6 classes.

####   7.	Metal Surface Dataset: </br>

- This dataset was downloaded from NEU Metal Surface Defects database which contains six kinds of typical surface defects of the hot-rolled steel strip are collected, i.e., rolled-in scale (RS), patches (Pa), crazing (Cr), pitted surface (PS), inclusion (In) and scratches (Sc). 
- The database includes 1,800 grayscale images: 300 samples each of six different kinds of typical surface defects.



## Preprocessing

### 1. Dataset structure:

After the datasets are downloaded from their respective sources, they have to be put in a certain folder structure to make it feasible for training. For the same, python programs have been written for each dataset to arrange them in the desired folder structure as shown below:

```python
- dataset
    - train
        - category a
        - category b
        - category c
    - test
        - category a
        - category b
        - category c
```

## Models

### Version 1
### Version 2
### Version 3



