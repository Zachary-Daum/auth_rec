# **Auth_Rec Project**
## V. alpha 0.1
### Goals:
* Accurately identify all authors in the Reuters 50/50 dataset.
* Run in under 15 seconds for 5 testing files and 20 authors (each with 10 corpus files).
* Build up user-friendly GUI for desktop and web.
* No GPU required to do any of the processing.
____
### Installation
``pip install -r requirements.txt``
#### Installing NLTK
1. Open up the cmd and type py (or python or python3 depending on your setup).
2. Type nltk.download() and download the NLTK library.
____
### Running the Script
In command line (bash, cmd, etc.)
``py auth_rec.py -corpus [corpus-folder] -in [testing-folder]``
- If py does not work try python or python3