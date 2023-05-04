# How can the detection of brain tumors be automated?

The research question of this bachelor thesis is “How can the detection of brain tumors be automated?”. With this research question, I want to ensure that brain tumors can be detected early and accurately and save a patient's life.

This research is divided into two parts. One part deals with classifying brain tumors. Different CNN models were used for this. The second part deals with segmenting the tumor itself. Two different segmentation models were used for this: UNet and Deeplabv3+.

On the basis of the various tests performed, it is evaluated which methods of practical implementation would work best. In particular, the accuracy, f1 score of the tumor class and the training speed are taken into account.

The number of false positives and the accuracy are very important aspects in classifying the brain tumors. It is very crucial that the model makes more false positives (false alarm of tumor) predictions than false negatives (tumor present, but not predicted). This is because it can save a life. In the segmentation part, the dice_coef, training rate and the reconstructed images are critical.

This study showed that ensemble learning achieved better results than when using a single model for predictions. 

The conclusion of this study is that it is possible to automate the detection of brain tumors by using of Deep Learning techniques.

The models used in the proof of concept application achieved a very high accuracy score.

- Research file ->>  Research_project.ipynb
- Proof of concept application ->> Application_tumor_detection.ipynb
