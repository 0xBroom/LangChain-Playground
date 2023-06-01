from langchain.llms import OpenAI

OPENAI_API_KEY = "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"

def simple_prompt():
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    text = "What would be a good company name for a company that makes colorful socks?"
    print(llm(text))

def prompt_template


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    simple_prompt()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
