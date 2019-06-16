# Stanford Cars Classification
Do classification on Stanford Cars dataset.

## How to evaluate on private dataset
1. git clone this project and install required packages with the `requirements.txt`.
2. Put images (must be jpg files) under the folder `./dataset/test/`. Do not forget to remove my sample images before this step.
3. Paste the fact labels into file `test_labels.txt` with the order of sorted file names in step 2.
4. Go through the Jupyter notebook `model-evaluation.ipynb`. It will download other necessary files and run the model on your private test dataset. Eventually, metrics including accuracy and confusion metrics will be presented in the notebook.

## Deployment
The trained model has been deployed here: https://joldnine.github.io/#/cars-classification

The front-end is hold by Github, while the back-end is deployed in Azure Function App.
