# SteelBlastQC: Shot-blasted Steel Surface Dataset with Interpretable Detection of Surface Defects
This is the official repository for SteelBlastQC, accepted to IJCNN 2025.

## Intro
We present SteelBlastQC, a dataset of steel surface images before and after shot-blasting - a vital treatment that prepares the metal for painting - created to train automated quality control models. The images were collected in collaboration with industrial experts at a manufacturing facility. We tested three deep learning classification methods: Compact Convolutional Transformer (CCT), Support Vector Machine (SVM) classifier using ResNet feature extraction, and a CAE-based classifier. Additionally, for each method we generated heatmaps to visualize the reasoning behind the classification outputs.

## Example images



## Dataset access & overview
SteelBlastQC is available for download at https://dataverse.nl/dataset.xhtml?persistentId=doi:10.34894/EKZNN0. 

Follow the link, click Access Dataset > Download ZIP > Accept (license) - and find the folder in your downloads:

```tree
dataverse_files/
├── MANIFEST.txt
├── SteelBlastQC_Readme.txt
└── SteelBlastQC/
    ├── test/
    │   ├── good/ (138 .png images)
    │   └── not-good/ (112 .png images)
    └── train/
        ├── good/ (750 .png images)
        └── not-good/ (654 .png images)
```

Or use the support/download.py script provided in this repo.

## Repo overview

The scripts download_data.py and load_data.py can be called to automatically retrieve the dataset from DataverseNL and load it into memory with pytorch.

The notebooks show example uses of the dataset, including data (down)loading, model definition, training and evaluation.

Additionally, there is convert_to_grayscale.py which can be used experiments on black-and-white images, so that only the texture is taken into account.

## Results

| **Method** | **Accuracy** | **Precision** | **Recall** | **F1-score** |
|------------|-------------|--------------|-----------|-------------|
| CCT        | 0.950       | 0.950        | 0.950     | 0.950       |
| SVM        | 0.945       | 0.945        | 0.955     | 0.950       |
| CAE        | 0.676       | 0.610        | 0.768     | 0.680       |

## Citation 
Please cite this dataset/paper as follows:

```bibtex
@data{EKZNN0_2025,
    author = {Ruzavina, Irina and Theis, Lisa Sophie and Lemeer, Jesse and de Groen, Rutger and Ebeling, Leo and Hulak, Andrej and Ali, Jouaria and Tang, Guangzhi and Mockel, Rico},
    publisher = {DataverseNL},
    title = {{SteelBlastQC Dataset}},
    year = {2025},
    version = {V1},
    doi = {10.34894/EKZNN0},
    url = {https://doi.org/10.34894/EKZNN0}
}
```
```bibtex
TBA
```


## License

## Contact

