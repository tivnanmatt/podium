import torch
from torchvision import datasets, transforms
import matplotlib.pyplot as plt 
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'


# Downloading and loading CIFAR10 dataset 
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
trainset = datasets .CIFAR10(root='./data', train=True , download=True , transform=transform)   # training data set 
testset = datasets .CIFAR10(root='./data', train=False , download=True , transform=transform)    # test data set 
classes = ('plane', 'car', 'bird', 'cat','deer', 'dog', 'frog', 'horse', 'ship' ,'truck') # classes of the dataset

# # Sample data 
sample_data = torch.utils.data .DataLoader(trainset, batch_size=4, shuffle=True)   # sample 4 images from training set 

iterCount = 0
# plotting the sampled images using matplotlib and setting title string to class label text 
for iSample, samp_dat in enumerate(sample_data):    # looping through each image in sample data  
    image , label = samp_dat    # assigning each image and its corresponding label to a variable 

    fig = plt.figure(figsize=(4, 4))  # setting figure size
    # change from [3, 32, 32] to [32, 32, 3]
    imageRGB = image[0].permute(1, 2, 0)      # changing the shape of the image from [3, 32, 32] to [32, 32, 3]
    plt.imshow(imageRGB)             # plotting first image of the batch (batch size is 4 so there are four images)    
    plt.title(classes[label[0]])     # setting title string as class label text for that particular image 

    plt.savefig('figures/cifar10_examples/sample_' + str(iSample).zfill(2) + '.png')

    if iSample >=16:
        break
