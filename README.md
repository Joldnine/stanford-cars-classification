# Stanford Cars Classification
Notebooks to do classification on Stanford Cars dataset.
# How to evaluate on private dataset
1. Install required packages.
2. Put images (must be jpg files) under the folder `./dataset/test/`. Do not forget to remove my sample images before this step.
3. Paste the fact labels into file `test_labels.txt` with the order of sorted file names in step 2.
4. Run the Jupyter notebook `model-evaluation.ipynb` throughly. It will download other necessary files and run the model on your private test dataset. Eventually, metrics including accuracy and confusion metrics will be presented in the notebook.
