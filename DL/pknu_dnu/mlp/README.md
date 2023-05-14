# Basic MLP model using PyTorch and notMNIST dataset

## Purpose
The purpose of this project is to build a basic MLP model using PyTorch and the notMNIST dataset, and to train the model to classify images of the letters A-J.

## Dataset
The notMNIST dataset is a set of images of letters from A-J in different fonts. It consists of two subsets: notMNIST_large and notMNIST_small. The notMNIST_large subset contains 500k training images and the notMNIST_small subset contains 18k testing images.

## How to use
1. Clone this repository to your local machine.
2. Download the notMNIST dataset from [here](http://yaroslavvb.com/upload/notMNIST/notMNIST_small.tar.gz) and [here](http://yaroslavvb.com/upload/notMNIST/notMNIST_large.tar.gz), and extract them to the `data` folder in the project directory.
3. Create a virtual environment and install the required packages using `pip install -r requirements.txt`.
4. Train the model using the `train.py` script in the `src` folder. The script takes the following arguments: `--batch_size`, `--num_epochs`, `--learning_rate`, `--momentum`, and `--weight_decay`. For example: `python src/train.py --batch_size 128 --num_epochs 50 --learning_rate 0.001 --momentum 0.9 --weight_decay 0.0001`.
5. Evaluate the model using the `evaluate.py` script in the `src` folder. The script takes the following arguments: `--model_path`, `--test_batch_size`, and `--cuda`. For example: `python src/evaluate.py --model_path models/best_epoch.pt --test_batch_size 128 --cuda`.
6. View the performance graph in the `results` folder, which shows the training and validation accuracy over time.

## Results
The results of the model training and evaluation can be found in the `models` folder and the `results` folder, respectively. The `models` folder contains the trained model weights, including the best performing model weights saved as `best_epoch.pt`. The `results` folder contains a graph of the training and validation accuracy over time, which can be viewed using a tool such as `matplotlib`.