# Create a RAG with LLM and Qdrant using your own data

In this lab you will implement the RAG pattern with your own data. Use the example code in this repository from the [./examples/3-applied-rag/embeddings.ipynb](Applied Rag notebook) as reference. The end result should be in your own repository containing the complete code for the enhanced RAG pattern based on the example provided.

**Learning Objectives:**

* Implement the RAG pattern with your own data
* Apply your own data to solve a problem using RAG
* Understand how to leverage an LLM and a vector database like Qdrant for useful responses

## Steps

1. Create a new repository in your account for your project. Alternatively, you can use this repository as a starting point by forking the repository. [https://github.com/alfredodeza/learn-retrieval-augmented-generation/generate](Use this link to create it in one step). 
2. use the [./examples/3-applied-rag/embeddings.ipynb](Applied Rag notebook) as a starting point
3. Replace the example data with your own data. Make sure to format it as a list of dictionaries for easier ingestion into the vector database
4. Run the LLM with Llamafile or connect your appliation to a valied OpenAI API endpoint
5. Run the notebook or Python application and verify your work

## Concepts Covered

* Retrieval Augmented Generation
* Large Language Models using Llamafile
* Using Vector databases like Qdrant
* Creating embeddings with Sentence Transformers
* Using OpenAI's Python API to connect to the LLM and produce responses

By completing this lab you will have a working example of the RAG pattern with your own data. You will also have a better understanding of how to use LLMs and vector databases to create useful responses for your applications.