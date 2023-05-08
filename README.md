# NeuralDecompiler: Assembly to C Translation



## Overview
Reading Assembly is challenging. Students in Professor Malte Schwarzkopf’s [CSCI 0300 computer systems course](http://cs300.systems/) at Brown University, for example, are required to explain the functionality of an Assembly program during exams. Assembly can be produced during the process of compiling a C program into an executable file. Going the opposite direction—converting Assembly instructions to human readable C code—is much harder. This repository represents our attempt to train a neural Assembly to C decompiler based on the transformer architecture.

## References
The following online resources were utilized in the data generation process.
1. LeetCode: [https://leetcode.com/](https://leetcode.com/)
2. CompilerExplore API: [https://github.com/compiler-explorer](https://github.com/compiler-explorer)
3. ChatGPT: [https://chat.openai.com/](https://chat.openai.com/)

This project was inspired by the following papers.
1. [Baptiste Roziere. Unsupervised Translation of Programming Languages. Neural and Evolutionary
Computing [cs.NE]. Université Paris sciences et lettres, 2022. English. ffNNT : 2022UPSLD015ff. fftel03852612](https://theses.hal.science/tel-03852612/document)
2. [Vaswani Ashish, Shazeer Noam, Parmar Niki, Uszkoreit Jakob, Jones Llion, Gomez Aidan N., Kaiser Łukasz, and Polosukhin Illia. 2017. Attention is all you need. In Proceedings of the 31st International Conference on Neural Information Processing Systems (NIPS’17). Curran Associates Inc., Red Hook, NY, 6000–6010.](https://arxiv.org/abs/1706.03762)

## Dependencies
Model:
1. NumPy
2. TensorFlow
3. NLTK

Demo Site:
1. Flask
2. Flask-Cors

## Contributors
NeuralDecompiler was developed by [Andrew Yang](https://github.com/ajy25), [Tiger Ji](https://github.com/taiga-forestry), [Frank Chiu](https://github.com/frankchiu12), and [Justin Cheng](https://github.com/jqhc) to fulfill the final project requirement of [CSCI 1470/2470 - Deep Learning](https://brown-deep-learning.github.io/dl-website-s23/), which was taught by Professor Ritambhara Singh at Brown University. 

Andrew Yang contributed to the preprocessing and tokenization of training data. Andrew also implemented the transformer model.

Tiger Ji contributed to the compiling process of C to Assembly as well as the cleaning of C and Assembly files. Tiger also wrote the script to rename function, struct, and variable names in the C files. Finally, Tiger wrote the client facing code.

Frank Chiu contributed to the scraping of Leetcode C user solutions. Frank also contributed to the renaming process of function, struct, and variable names in the C files. 

Justin Cheng contributed to the ChatGPT script. Justin also aided Andrew, Tiger, and Frank in the overall development, debugging, and training process. 