#Vectorizer

This tools are used to vectorize text (e.g. tweets).
Fasttext is used to vectorized a file using facebooks pretrained models (not inclided in repo, see facebook's fasttext). The following command can be used to read a file in and vectorize every word.

`text | ./fasttext print-word-vectors wiki.xx.bin`

##FastText compressed classification models
    @article{joulin2016fasttext,
    title={FastText.zip: Compressing text classification models},
    author={Joulin, Armand and Grave, Edouard and Bojanowski, Piotr and Douze, Matthijs and J{\'e}gou, H{\'e}rve and Mikolov, Tomas},
    journal={arXiv preprint arXiv:1612.03651},
    year={2016}
    }
