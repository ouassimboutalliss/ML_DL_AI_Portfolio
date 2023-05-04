# How can the detection of brain tumors be automated?
The primary research question of this bachelor's thesis is focused on automating the detection of brain tumors to ensure early and accurate diagnosis and potentially save patients' lives.

The research is divided into two parts: the first part aims to classify brain tumors using various CNN models, while the second part deals with segmenting the tumor itself using UNet and Deeplabv3+ models.

Based on several tests performed, the research evaluates the most practical implementation methods, considering accuracy, f1 score of the tumor class, and training speed.

The accuracy and number of false positives are crucial aspects of brain tumor classification since it can be life-threatening if the model makes more false negatives (tumor present but not predicted) than false positives (false alarm of tumor). In the segmentation part, dice_coef, training rate, and reconstructed images are critical.

The research demonstrated that ensemble learning outperformed single model prediction in achieving better results.

In conclusion, this study indicates that the detection of brain tumors can be automated using Deep Learning techniques, and the proof-of-concept application based on high-accuracy models confirms its feasibility.

The research file and proof of concept application are available as:

- Research file ->>  Research_project.ipynb
- Proof of concept application ->> Application_tumor_detection.ipynb

The bachelor's thesis is written in Dutch. If you have any questions, please do not hesitate to contact me at ouassim.boutalliss@hotmail.com."
