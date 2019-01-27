# protein-ss-pred

GOR method and an SVM-based method for protein secondary structure prediction.\
Detailed description of the methods and datasets can be found in the [project report](reports/Project%20Report.pdf).

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
Pretrained model ([model.npz](models/model.npz)) is available.\
Prediction from the GOR method can be obtained using:
```
python gor-predict.py [-h] (--pssm PSSM | --fasta FASTA) filename_model
```
For example:
```
python src/gor-predict.py --pssm data/blindTest/pssm/4S1H\:A.pssm models/model.npz
```

### SVM
Pretrained model ([model.sav.tar.gz](models/model.sav.tar.gz)) is available.\
Before it can be used it must be extracted in the following way:
```
tar -xzvf models/model.sav.tar.gz -C models/
```
Prediction from the SVM-based method can be obtained using:
```
python svm-predict.py [-h] (--pssm PSSM | --fasta FASTA) [--probs] filename_model
```
For example:
```
python src/svm-predict.py --pssm data/blindTest/pssm/4S1H\:A.pssm models/model.sav
```

## Training

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

## Performance

<table>
    <thead>
        <tr>
            <th></th>
            <th colspan=2>GOR</th>
            <th colspan=2>SVM</th>
        </tr>
    </thead>
    <tbody align="right">
        <tr align="center">
            <td></td>
            <td>CV</td>
            <td>Blind test</td>
            <td>CV</td>
            <td>Blind test</td>
        </tr>
        <tr>
            <td>SEN_H</td>
            <td>0.86±0.01</td>
            <td>0.83</td>
            <td></td>
            <td>0.72</td>
        </tr>
        <tr>
            <td>SEN_E</td>
            <td>0.62±0.01</td>
            <td>0.60</td>
            <td></td>
            <td>0.62</td>
        </tr>
        <tr>
            <td>SEN_C</td>
            <td>0.42±0.01</td>
            <td>0.42</td>
            <td></td>
            <td>0.85</td>
        </tr>
        <tr>
            <td>PPV_H</td>
            <td>0.58±0.01</td>
            <td>0.60</td>
            <td></td>
            <td>0.85</td>
        </tr>
        <tr>
            <td>PPV_E</td>
            <td>0.54±0.01</td>
            <td>0.58</td>
            <td></td>
            <td>0.80</td>
        </tr>
        <tr>
            <td>PPV_C</td>
            <td>0.80±0.01</td>
            <td>0.73</td>
            <td></td>
            <td>0.65</td>
        </tr>
        <tr>
            <td>MCC_H</td>
            <td>0.50±0.01</td>
            <td>0.46</td>
            <td></td>
            <td>0.67</td>
        </tr>
        <tr>
            <td>MCC_E</td>
            <td>0.45±0.01</td>
            <td>0.46</td>
            <td></td>
            <td>0.63</td>
        </tr>
        <tr>
            <td>MCC_C</td>
            <td>0.40±0.01</td>
            <td>0.39</td>
            <td></td>
            <td>0.56</td>
        </tr>
        <tr>
            <td>SOV_H</td>
            <td>65.48±0.99</td>
            <td>62.70</td>
            <td></td>
            <td>68.64</td>
        </tr>
        <tr>
            <td>SOV_E</td>
            <td>58.64±1.35</td>
            <td>63.18</td>
            <td></td>
            <td>67.19</td>
        </tr>
        <tr>
            <td>SOV_C</td>
            <td>43.09±0.69</td>
            <td>45.57</td>
            <td></td>
            <td>70.93</td>
        </tr>
        <tr>
            <td>ACC</td>
            <td>0.62±0.00</td>
            <td>0.62</td>
            <td></td>
            <td>0.75</td>
        </tr>
    </tbody>
</table>

## License
[MIT](LICENSE) @ Katarina Elez
