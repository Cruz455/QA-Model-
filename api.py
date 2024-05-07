import re
import requests
from bs4 import BeautifulSoup
from transformers import pipeline
import gradio as gr

qa_pipeline = pipeline('question-answering', model='deepset/roberta-large-squad2')

def fetch_webpage_content(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None, "Failed to retrieve the webpage. Please check the URL or your internet connection."
    soup = BeautifulSoup(response.text, 'lxml')
    content_sections = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol'])
    content = ' '.join([section.text for section in content_sections])
    return content, None

def clean_references(answer):
    return re.sub(r"\[\d+\]", "", answer)

def expand_answer(context, answer):
    start_index = context.find(answer)
    end_index = start_index + len(answer)
    pre_context = max(0, context.rfind('.', 0, start_index) + 1)
    post_context = context.find('.', end_index)
    expanded_answer = context[pre_context:post_context+1].strip()
    return expanded_answer

def answer_question(url, question):
    content, error_message = fetch_webpage_content(url)
    if error_message:
        return error_message, 0.0
    
    result = qa_pipeline(question=question, context=content)
    answer = clean_references(result['answer'])
    score = result['score']

    if score < 0.05:
        answer = "I don't know the answer due to low confidence in the results."
    else:
        answer = expand_answer(content, answer)

    return answer, score

iface = gr.Interface(
    fn=answer_question,
    inputs=[
        gr.Textbox(label="URL"),
        gr.Textbox(label="Question")
    ],
    outputs=[
        gr.Textbox(label="Answer"),
        gr.Number(label="Confidence Score")
    ],
    title="Question Answering",
    description="Enter a URL and a question, and the model will try to answer it based on the webpage content."
)

if __name__ == '__main__':
    iface.launch()