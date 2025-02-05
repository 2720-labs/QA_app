#  Copyright Mitra Mirshafiee, 2022 Licensed under MIT License.
#  See the LICENSE.txt for more information.


import streamlit as st
from PIL import Image
import os

image = Image.open(os.path.join("assets", "NLP1.png"))
st.image(image, use_column_width  = True)
st.markdown("[source](https://www.steadforce.com/blog/natural-language-processing-tools)")

# display topic input slot
st.title("What is NLP?", "")
st.markdown("""
Natural language processing (NLP) refers to the branch of computer science—and more specifically, 
the branch of artificial intelligence or AI—concerned with giving computers the ability to 
understand text and spoken words in much the same way human beings can.

NLP combines computational linguistics—rule-based modeling of human language—with 
statistical, machine learning, and deep learning models. 
Together, these technologies enable computers to process human language in the
form of text or voice data and to understand its full meaning, 
complete with the speaker or writer's intent and sentiment.

NLP drives computer programs that translate text from one language to another, 
respond to spoken commands, and summarize large volumes of text rapidly—even in real time. 
There's a good chance you've interacted with NLP in the form of voice-operated GPS systems,
digital assistants, speech-to-text dictation software, customer service chat bots, and other consumer conveniences. 
But NLP also plays a growing role in enterprise solutions that help streamline business operations,
increase employee productivity, and simplify mission-critical business processes.
""")
st.markdown("[*](https://www.ibm.com/cloud/learn/natural-language-processing#:~:text=Natural%20language%20processing%20(NLP)%20refers,same%20way%20human%20beings%20can.)")


st.title("What is Question Answering in NLP?")
st.markdown("""
Question Answering models are able to retrieve the answer to a question from a given text.
    This is useful for searching for an answer in a document.
    Depending on the model used, the answer can be directly extracted from text or generated from scratch.
""")
st.markdown("[*](https://medium.com/nlplanet/two-minutes-nlp-quick-intro-to-question-answering-124a0930577c)")


st.title("What are some types of Q&A?")
st.markdown("""
QA systems differ in the way answers are created.

- Extractive QA: The model extracts the answer from a context and provides it directly to the user. It is usually solved with BERT-like models.
- Generative QA: The model generates free text directly based on the context. 
It leverages Text Generation models.
Moreover, QA systems differ in where answers are taken from.

- Open QA: The answer is taken from a context.
- Closed QA: No context is provided and the answer is completely generated by a model.

Based on the definitions above, our model is an **extractive QA** with answers
taken from a text.""")