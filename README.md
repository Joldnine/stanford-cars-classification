# Stanford Cars Classification
Do classification on Stanford Cars dataset. The top-1 accuracy on an unseen images dataset (randomly shuffled 15%) is about **91%** and the top-5 accuracy is **98.6%**.

## How to evaluate on private dataset
1. git clone this project and install required packages with the `requirements.txt`.
    ```bash
    git clone https://github.com/Joldnine/stanford-cars-classification.git
    cd stanford-cars-classification
    pip install -r requirements.txt
    ```
2. Remove my sample images under the folder `./dataset/test/`. Put images (must be jpg files) inside.

3. Paste the fact labels, ie. y_true, into file `test_labels.txt` with the order of sorted file names in step 2.

4. Go through the Jupyter notebook `model-evaluation.ipynb`. It will download other necessary files and run the model on your private test dataset. Eventually, metrics including accuracy and confusion metrics will be presented in the notebook.

## Deployment
The trained model has been deployed in my blog website: https://joldnine.github.io/#/cars-classification

The front-end is developed by vuejs and deployed on Github Page; the back-end with the PyTorch JIT model is deployed in AWS Lambda. Please expect a longer response time (~6s) for the first prediction, because AWS Lambda needs some time do the "cold start", and the following predictions' response time would be within 800 ms.

Screenshot:
![alt text](resources/images/demo.png "Demo Screenshot")
