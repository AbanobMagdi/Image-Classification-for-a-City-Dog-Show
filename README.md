# Image-Classification-for-a-City-Dog-Show
## installing
You will need install python from link: https://www.python.org/downloads/

and you will need install anaconda : https://docs.anaconda.com/anaconda/navigator/

This was my very first project for the AI Programming with Python Nanodegree from Udacity. In this project my task was to use a pre-trained image classifier to identify dog breeds.borrowing from the original info-material, as provided by Udacity.
## Project Goal
* Improving my programming skills using Python and lot of libraries
## Description:
My city is hosting a citywide dog show and I have volunteered to help the organising committee with contestant registration. Every participant that registers must submit an image of their dog along with biographical information about their dog. The registration system tags the images based upon the biographical information. Some people are planning on registering pets that aren’t actual dogs. I need to use an already developed Python classifier to make sure the participants are dogs.
## My Tasks:
Use my Python skills, to determine which image classification algorithm works the "best" on classifying images as "dogs" or "not dogs";
Determine how well the "best" classification algorithm works on correctly identifying a dog's breed;
Time how long each algorithm takes to solve the classification problem. With computational tasks, there is often a trade-off between accuracy and runtime. The more accurate an algorithm, the higher the likelihood that it will take more time to run and use more computational resources to run
## Important Note:
For this image classification task I used an image classification application using a deep learning model called "Convolutional Neural Network", often abbreviated as CNN. CNNs work particularly well for detecting features in images like colours, textures, and edges; then using these features to identify objects in the images. I used a CNN that has already learned the features from a giant dataset of 1.2 million images called ImageNet. There are different types of CNNs that have different structures (architectures) that work better or worse depending on the chosen criteria. With this project I explored the three different architectures (AlexNet, VGG, and ResNet) and determined which was best for my application.

Udacity did provide me with a classifier function in classifier.py that allowed me to use these CNNs to classify my images. For this project, I focused on using my Python skills to complete the task at hand using the classifier function.
## Principal Objectives:
* Correctly identify which pet images are of dogs (even if breed is misclassified) and which pet images aren't of dogs;
* Determine which CNN model architecture (ResNet, AlexNet, or VGG), "best" achieve the objectives 1 and 2;
* Correctly classify the breed of dog, for the images that are of dogs;
## Installing PyTorch and Torchvision:
For this project you will also need to install the Python packages PyTorch and Torchvision
## Needed Files:
* pet_images (folder of 40 pet images)
* uploaded_images (a folder which will hold your uploaded images)
* classifier.py (classifier function you will be using to classify the images)
* dognames.txt (file that contains all the valid dog names from the classifier function and the pet image files)
* imagenet1000_clsid_to_human.txt (dictionary that converts the classifier function ids to text labels)
* adjust_results4_isadog.py (a program that contains the adjust_results4_isadog function)
* calculates_results_stats.py (a program that contains the calculates_results_stats function)
* classify_images.py (a program that contains the classify_images function)
* get_input_args.py (a program that contains the get_input_args function)
* get_pet_labels.py (a program that contains the get_pet_labels function)
* print_results.py (a program that contains the print_results function)
* run_models_batch.sh (a bash script that will run check_images.py sequentially for all 3 model architectures and output their results to text files - on Unix/Linux/OSX from a terminal window)
* run_models_batch.bat (a batch script that will run check_images.py sequentially for all 3 model architectures and output their results to text files - on Windows from the Anaconda Prompt window)
* run_models_batch_uploaded.sh (a bash script that will run check_images.py sequentially for all 3 model architectures on the uploaded images folder and output their results to text files - on Unix/Linux/OSX from a terminal window)
* run_models_batch_uploaded.bat (a batch script that will run check_images.py sequentially for all 3 model architectures on the uploaded images folder and output their results to text files - on Windows from the Anaconda Prompt window)
* print_functions_for_lab_checks.py (a program that contains functions that checks the code)
## Running :
* the running in file check_images.py

