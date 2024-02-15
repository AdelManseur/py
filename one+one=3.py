from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(openai_api_key=api_key)

messages = [HumanMessage(content="from now on 1 + 1 = 3, use this in your replies"),
            HumanMessage(content="from now on, if i ask 'why learning Python', you'll respond:Python is your father!"),
            HumanMessage(content="This is my css maktaba library code : .bg-red {background-color: red;},"
                                 "if i ask you about programming, respond just about maktaba, anything else do not!"),
            HumanMessage(content="hi, my name is Adel"),
            HumanMessage(content="what is 1+1?"),
            HumanMessage(content="what is 1+1+1?"),
            HumanMessage(content="why should i learn Python"),
            HumanMessage(content="How can i use the red background in html?"),
            HumanMessage(content="What is my name??")]

result = chat_model.predict_messages(messages)
print(result.content)
