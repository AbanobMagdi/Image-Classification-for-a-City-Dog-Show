#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER:Abanob Magdy
# DATE CREATED:23/4/2020                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
# Imports only listdir function from OS module 
from os import listdir  
# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    in_files = listdir(image_dir) #to read files
    # Creates empty dictionary named results_dic
    results_dic = dict()
    # Adds new key-value pairs to dictionary ONLY when key doesn't already exist. This dictionary's value is
    # a List that contains only one item - the pet image label
    for idx in range(0, len(in_files), 1):
        #we should skip thw file which start with . 
        if in_files[idx][0]!=".":
            # Create pet_name starting as empty string
            pet_name = "" 
            # Splits lower case string by _ to break into words
            pet_list = str(in_files[idx]).lower().split("_")
            # Loops to check if word in pet name is only
            # alphabetic characters - if true append word
            # to pet_name separated by trailing space 
            for word in pet_list:
                if word.isalpha():
                    pet_name += word + " "  
            pet_name=pet_name.strip()
            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_name]
            else:
                print("** Warning: Key=", in_files[idx], "already exists in results_dic with value =", results_dic[in_files[idx]])
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
