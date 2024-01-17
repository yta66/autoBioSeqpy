 
An innovative inducer of platelet production, isochlorogenic acid A, is uncovered through the application of deep neural networks

Author
=============================
ljs@swmu.edu.cn
yta17634447991@163.com

Overview
==============================
Radiation-induced thrombocytopenia (RIT) often occurs in cancer patients undergoing radiation therapy, which can result in morbidity and even death. However, a notable deficiency exists in the availability of specific drugs designed for the treatment of RIT. In our pursuit of new drugs for RIT treatment, we employed three deep learning (DL) algorithms: convolutional neural network (CNN), deep neural networks (DNN), and a hybrid neural network that combines the computational characteristics of the two. These algorithms construct computational models that can screen compounds for drug activity by utilizing the distinct physicochemical properties of the molecules. Notably, the Hybrid CNN+DNN (HCD) model demonstrated the most effective predictive performance on the test dataset, achieving an accuracy of 98.3% and a precision of 97.0%, both of which surpassed the performance of the other models. The best model underwent testing using a set of 10 drugs endorsed by the US Food and Drug Administration (FDA) specifically for the treatment of thrombocytopenia. Notably, seven of these drugs were predicted to exhibit activity. Isochlorogenic acid A, identified through screening the Chinese Pharmacopoeia Natural Product Library, was subsequently subjected to experimental verification. The results indicated a substantial enhancement in the differentiation and maturation of megakaryocytes (MKs), along with a notable increase in platelet production. This underscores the potential therapeutic efficacy of isochlorogenic acid A in addressing RIT. 

Files
================================
data file
pos_train.txt: MACCS key fingerprints of 500  active compounds  (Training dataset)
neg_train.txt: MACCS key fingerprints of 500 inactive compounds  (Training dataset)
pos_train_feature.txt: Morgan fingerprints of 500  active compounds  (Training dataset)
neg_train_feature.txt: Morgan fingerprints of 500 inactive compounds  (Training dataset)
FDA.txt: MACCS key fingerprints of 10 FDA-approved drugs for the treatment of human thrombocytopenia
FDA_feature.txt: Morgan fingerprints of 10 FDA-approved drugs for the treatment of human thrombocytopenia
CPNP-Library.txt: MACCS key fingerprints of 2070 compounds of unknown activity
model file
CPNP-Library_feature.txt: Morgan fingerprints of 2070 compounds of unknown activity
model file

CNN.py: convolutional neural networks
CNN_hybrid.py: convolutional neural networks
DNN.py: dynamic neural network
DNN_hybrid.py: dynamic neural network

Usage
=================================
When training a deep leanring model, the user can enter the following commands in the command terminal. Take the CNN architecture as an example: 

For the CNN architecture: 

python running.py --dataType other --dataEncodingType other --dataTrainFilePaths examples/ICGA-A/data/pos_train.txt examples/ICGA-A/data/neg_train.txt --dataTrainLabel 1 0 --dataSplitScale 0.8 --modelLoadFile examples/ICGA-A/model/CNN.py --verbose 1 --outSaveFolderPath tmpOut --savePrediction 1 --saveFig 1 --batch_size 32 --epochs 20 --shuffleDataTrain 1 --spcLen 167 --modelSaveName tmpMod.json --weightSaveName tmpWeight.bin --noGPU 1 --paraSaveName parameters.txt --optimizer optimizers.Adam(lr=0.001,amsgrad=False,decay=False)

For the DNN architecture: 

python running.py --dataType other --dataEncodingType other --dataTrainFilePaths examples/ICGA-A/data/pos_train_feature.txt examples/ICGA-A/data/neg_train_feature.txt --dataTrainLabel 1 0 --dataSplitScale 0.8 --modelLoadFile examples/ICGA-A/model/DNN.py --verbose 1 --outSaveFolderPath tmpOut --savePrediction 1 --saveFig 1 --batch_size 32 --epochs 20 --shuffleDataTrain 1 --spcLen 2048 --modelSaveName tmpMod.json --weightSaveName tmpWeight.bin --noGPU 1 --paraSaveName parameters.txt --optimizer optimizers.Adam(lr=0.001,amsgrad=False,decay=False)

====================================================================

For the HCD architecture:

python running.py --dataType other other --dataEncodingType other other --dataTrainFilePaths examples/ICGA-A/data/pos_train.txt examples/ICGA-A/data/neg_train.txt examples/ICGA-A/data/pos_train_feature.txt examples/ICGA-A/data/neg_train_feature.txt --dataTrainLabel 1 0 1 0 --dataSplitScale 0.8 --modelLoadFile examples/ICGA-A/model/CNN.py examples/ICGA-A/model/DNN_hybrid.py --verbose 1 --outSaveFolderPath tmpOut --savePrediction 1 --saveFig 1 --batch_size 64 --epochs 20 --shuffleDataTrain 1 --spcLen 167 2048 --modelSaveName tmpMod.json --weightSaveName tmpWeight.bin --noGPU 1 --paraSaveName parameters.txt --optimizer optimizers.Adam(lr=0.001,amsgrad=False,decay=False) --dataTrainModelInd 0 0 1 1
Users can refer to the Manual.docx of autoBioSeqpy tool for detailed parameter information. After training, the prediction results, probability, model parameters, weights, optimizer states and generated figures, (including acc-loss curve, ROC curve and PR curve) are all saved in the tmpOut file. Please note that becasue the training set is re-shuffled during each training process, the results may be different each time.

Use the procedure below to validate the feasibility of the model to screen for platelet-promoting compounds:

python predicting.py --paraFile tmpOut/parameters.txt --dataTestFilePaths examples/ICGA-A/data/FDA.txt examples/ICGA-A/data/FDA_feature.txt --predictionSavePath tmpout/indPredictions.txt --dataTestModelInd 0 1

When the users want to use the build model to predict the dataset, the following commands are available: 

python predicting.py --paraFile tmpOut/parameters.txt --dataTestFilePaths examples/ICGA-A/data/CPNP-Library.txt examples/ICGA-A/data/CPNP-Library_feature.txt --predictionSavePath tmpout/indPredictions.txt --dataTestModelInd 0 1

The prediction results are saved in the indPredictions.txt.

Requirements and installation
============================
Please see the README.md of auotBioSeqpy















