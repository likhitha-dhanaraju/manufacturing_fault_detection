# manufacturing_fault_detection

## Introduction

This is the code repository of my Major project work, **"Manufacturing Fault Detection using Deep Learning"**

The objective of this project is,

*"To develop a universal model for the detection of faults of various manufacturing defect datasets irrespective of the nature of the defects or the products and to develop a streamlined process for preprocessing and training the model for any dataset."*


## The datasets used in this project
 ![datasets](https://user-images.githubusercontent.com/34205126/114338063-ede7d200-9b6f-11eb-97a0-0d53465320fc.png)


**References**

1.	Taviraj Sinha, R. (2020, August). Casting dataset. Retrieved from https://www.kaggle.com/ravirajsinh45/real-life-industrial-dataset-of-casting-product.
2.	Özgenel, Çağlar Fırat (2019), “Concrete Crack Images for Classification”, Mendeley Data, v2 http://dx.doi.org/10.17632/5y9wdsg2zt.2 
3.	Severstal: Steel Defect Detection dataset (2020). Retrieved from Kaggle website. https://www.kaggle.com/c/severstal-steel-defect-detection  
4.	Lv X, Duan F, Jiang JJ, Fu X, Gan L. Deep Metallic Surface Defect Detection: The New Benchmark and Detection Network. Sensors (Basel). 2020;20(6):1562. Published 2020 Mar 11. doi:10.3390/s20061562
5.	Buerhop-Lutz, C.; Deitsch, S.; Maier, A.; Gallwitz, F.; Berger, S.; Doll, B.; Hauch, J.; Camus, C. & Brabec, C. J. A Benchmark for Visual Identification of Defective Solar Cells in Electroluminescence Imagery. European PV Solar Energy Conference and Exhibition (EU PVSEC), 2018. DOI: 10.4229/35thEUPVSEC20182018-5CV.3.15
6.	Deitsch, S.; Buerhop-Lutz, C.; Maier, A. K.; Gallwitz, F. & Riess, C. Segmentation of Photovoltaic Module Cells in Electroluminescence Images. CoRR, 2018, abs/1806.06530
7.	Deitsch, S.; Christlein, V.; Berger, S.; Buerhop-Lutz, C.; Maier, A.; Gallwitz, F. & Riess, C. Automatic classification of defective photovoltaic module cells in electroluminescence images. Solar Energy, Elsevier BV, 2019, 185, 455-468. DOI: 10.1016/j.solener.2019.02.067
8.	Bacioiu, D., Melton, G., Papaelias, M., & Shaw, R. (2019). Automated defect classification of Aluminium 5083 TIG welding using HDR camera and neural networks. Journal of Manufacturing Processes, 45, 603-613.


## Preprocessing

### Dataset structure reorganisation:

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

Each notebook contains all the steps from preprocessing steps - data augmentation, training to testing steps. Each version notebooks contains different models. Each model was developoped along with the custom mapping layer, whose outputs are used for localising the defects.

