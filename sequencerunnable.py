from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)

model = ChatMistralAI(model = "mistral-small-latest")

parser = StrOutputParser()

#formatted_prompt = prompt.format_messages(topic = "Machine Learning")

#response = model.invoke(formatted_prompt)

#final_output = parser.parse(response.content)

#print(final_output)


chain = prompt | model | parser

result = chain.invoke("Machine Learning")
print(result)
