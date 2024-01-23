# Input shape: (244, 244, 3)
# Output shape: (2)

import torch
import torch.nn as nn
import torch.nn.functional as F

class EyeTrackingCNN(nn.Module):
    def __init__(self):
        super(EyeTrackingCNN, self).__init__()

        # Convolutional layers
        self.conv1 = nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1)

        # Max pooling layers
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)

        # Fully connected layers
        self.fc1 = nn.Linear(256 * 64 * 64, 512)
        self.fc2 = nn.Linear(512, 2)  # Output is a 2D vector representing the gaze point

    def forward(self, x):
        # Convolutional layers with ReLU activation and max pooling
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        x = F.relu(self.conv3(x))
        x = self.pool(x)

        # Flatten the output for fully connected layers
        x = x.view(-1, 256 * 64 * 64)

        # Fully connected layers with ReLU activation
        x = F.relu(self.fc1(x))
        x = self.fc2(x)

        return x

# Instantiate the model
model = EyeTrackingCNN()
