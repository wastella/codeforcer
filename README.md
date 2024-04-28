# codeforcer

A tool to get detailed Codeforces solutions and explanations in C++ using deepseek-coder-6.7b-instruct.

deepseek-coder-6.7b-instruct is an open source LLM that can be easily run on most computers for free. It is specially tuned to coding, which is why I chose it for this project. It's also a mid-size model, so it gives the best answers without sacrificing performance.

## How Do I Use This?

To use this tool, first you have to pull the repository to your local computer using:
`git pull https://github.com/wastella/codeforcer.git`

Once you have it in your local computer, navigate to the directory.

After that you have to download the requirements using:
`pip install -r requirements.txt`

Once the requirements are downloaded, all you have to do is run:
`streamlit run codeforcer.py`

A browser app should pop up, that looks something like this:

![demo picture](https://github.com/wastella/codeforcer/blob/main/demo-pic.png?raw=true)

After that just put the link to the codeforcer problem your stuck on, and press submit!
