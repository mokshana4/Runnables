from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda


model = ChatMistralAI(model = "mistral-small-latest")
parser = StrOutputParser()

#two-different prompts
short_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in 1-2 lines"
)

detailed_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in detail"
)

#input
#topic = "Machine Learning"

#formatted_short = short_prompt.format_messages(topic = topic)
#response_short = model.invoke(formatted_short)
#str_out = parser.parse(response_short.content)

#parallel 

chain = RunnableParallel({    #-->dictinary - convert to runnable
    "short" :RunnableLambda(lambda x : x ['short']) | short_prompt | model | parser,
    "detailed" :RunnableLambda(lambda x : x['detailed']) | detailed_prompt | model | parser
})
result = chain.invoke({
    "short" : {"topic":"Machine Learning"},
    "detailed" :{"topic":"Deep Learning"}
})

print(result['short'])
print(result['detailed'])