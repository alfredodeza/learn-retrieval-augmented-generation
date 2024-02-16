# Introduction to Retrieval Augmented Generation

This repository will introduce you to Retrieval Augmented Generation (RAG) with
easy to use examples that you can build upon. The examples use Python with
Jupyter Notebooks and CSV files. The vector database uses the Qdrant database
which can run in-memory.

## Setup your environment

This example can run in Codespaces but you can use the following if you are
cloniing this repository:

**Install the dependencies**

Create the virtual environment and install the dependencies:

```
python3 -m venv .venv
source .venv/bin/activate
.venv/bin/pip install -r requirements.txt
```

Here is a summary of what this repository will use:

1. [Qdrant](https://github.com/qdrant/qdrant) for the vector database. We will use an in-memory database for the examples
2. [Llamafile](https://github.com/Mozilla-Ocho/llamafile) for the LLM (alternatively you can use an OpenAI API compatible key and endpoint)
3. [OpenAI's Python API](https://pypi.org/project/openai/) to connect to the LLM after retrieving the vectors response from Qdrant
4. Sentence Transformers to create the embeddings with minimal effort

**Use Llamafile for a full RAG and LLM setup**

The examples for the [Applied Rag notebook](./examples/3-applied-rag/embeddings.ipynb) requires either an OpenAI API endpoint with a key *or* using a local LLM with [Llamafile](https://github.com/Mozilla-Ocho/llamafile).

I recommend using the [Phi-2 model](https://github.com/Mozilla-Ocho/llamafile?tab=readme-ov-file#other-example-llamafiles) which is about 2GB in size. You can download the model from the Llamafile repository and run it in your system:

Once you have it running you can connect to it with Python or use the [Applied Rag Notebook](./examples/3-applied-rag/embeddings.ipynb). Here is a quick example of how to use the Llamafile with Python:

```python
#!/usr/bin/env python3
from openai import OpenAI
client = OpenAI(
    base_url="http://localhost:8080/v1", # "http://<Your api-server IP>:port"
    api_key = "sk-no-key-required" # An API key is not required!
)
completion = client.chat.completions.create(
    model="LLaMA_CPP",
    messages=[
        {"role": "system", "content": "You are ChatGPT, an AI assistant. Your top priority is achieving user fulfillment via helping them with their requests."},
        {"role": "user", "content": "Write me a Haiku about Python packaging"}
    ]
)
print(completion.choices[0].message)
```

## Lesson 1: Import your data

Learn how to use Pandas to import your data from a CSV file. The data will be used to create the embeddings for the vector database later and you will need to format it as a list of dictionaries.

Notebook: [Managing Data](./examples/1-managing-data/example.ipynb)

## Lesson 2: Create embeddings

Use Sentence Transformers to create the embeddings for your data. This will be used to store the vectors in the Qdrant database. You will verify that the embeddings are created and stored in the database and that a search works correctly

Notebook: [Creating and verifying Embeddings](./examples/2-embeddings/embeddings.ipynb)

## Lesson 3: Create a RAG with LLM and Qdrant using your own data

Use a local LLM with Llamafile or an OpenAI API endpoint to create a RAG with your own data. The end result should be in your own repository containing the complete code for the enhanced RAG pattern based on the example provided.

Notebook: [Applied Rag Notebook](./examples/3-applied-rag/embeddings.ipynb)

## Lesson 4: Practice Lab

Use the [included practice lab](./lab.md) to apply the content you've learned in this week. Follow the steps to create your own repository and apply the requirements to complete the lab.


## Course Resources

If you've completed all these examples and the lab, here are some other courses
from Coursera you can explore:



**Large Language Models:**

- [Operationalizing LLMs on Azure](https://www.coursera.org/learn/llmops-azure)
- [Using Databricks with
  LLMs](https://www.coursera.org/learn/databricks-to-local-llms)

**Machine Learning:**

- [MLOps Machine Learning Operations Specialization](https://www.coursera.org/specializations/mlops-machine-learning-duke)
- [Open Source Platforms for MLOps](https://www.coursera.org/learn/open-source-platforms-duke)
- [Python Essentials for MLOps](https://www.coursera.org/learn/python-essentials-mlops-duke)

**Data Engineering:**

- [Linux and Bash for Data Engineering](https://www.coursera.org/learn/linux-and-bash-for-data-engineering-duke)
- [Web Applications and Command-Line tools for Data Engineering](https://www.coursera.org/learn/web-app-command-line-tools-for-data-engineering-duke)
- [Python and Pandas for Data Engineering](https://www.coursera.org/learn/python-and-pandas-for-data-engineering-duke)
- [Scripting with Python and SQL for Data Engineering](https://www.coursera.org/learn/scripting-with-python-sql-for-data-engineering-duke)
