from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

OPENAI_API_KEY = ""


def simple_prompt():
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    text = "What would be a good company name for a company that makes colorful socks?"
    print(llm(text))


def prompt_template():
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )
    print(prompt.format(product="colorful socks"))


def simple_chain():
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    print(chain.run("colorful socks"))


if __name__ == '__main__':
    simple_chain()

