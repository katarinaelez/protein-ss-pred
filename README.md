# protein-ss-pred

GOR method and an SVM-based method for protein secondary structure prediction.

## Getting started

### Requirements
The implementations require [numpy](https://github.com/numpy/numpy) and [scikit-learn](https://github.com/scikit-learn/scikit-learn) packages.
```bash
pip install numpy
pip install scikit-learn
```
In order to play with the notebooks make sure to install [Jupyter Notebook](https://github.com/jupyter/notebook).
```bash
pip install notebook
```

### Installation
```bash
git clone https://github.com/katarinaelez/protein-ss-pred
```

## Usage

### GOR
GOR model can be trained using:
```
python gor-train.py [-h] [--filename_model FILENAME_MODEL]
                    [--window_size WINDOW_SIZE]
                    filename_id_list dir_pssm dir_dssp
```
For example:
```
python src/gor-train.py data/training/list.txt data/training/pssm data/training/dssp --filename_model models/model
```
Pretrained model ([model.npz](models/model.npz)) is available.\
Prediction from the GOR model can be obtained using:
```
python gor-predict.py [-h] (--pssm PSSM | --fasta FASTA) filename_model
```
For example:
```
python src/gor-predict.py --pssm data/blindTest/pssm/4S1H\:A.pssm models/model.npz
```

### SVM
SVM model can be trained using:
```
python svm-train.py [-h] [--filename_model FILENAME_MODEL]
                    [--window_size WINDOW_SIZE]
                    filename_id_list dir_pssm dir_dssp
```
For example:
```
python src/svm-train.py data/training/list.txt data/training/pssm data/training/dssp --filename_model models/model
```
Pretrained model ([model.sav](models/model.sav)) is available.\
Prediction from the SVM model can be obtained using:
```
python svm-predict.py [-h] (--pssm PSSM | --fasta FASTA) [--probs] filename_model
```
For example:
```
python src/svm-predict.py --pssm data/blindTest/pssm/4S1H\:A.pssm models/model.sav
```

## Datasets

## Results

## License
[MIT](LICENSE) @ Katarina Elez
