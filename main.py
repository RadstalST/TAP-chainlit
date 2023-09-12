from langchain import PromptTemplate, OpenAI, LLMChain
import chainlit as cl

# template = """Question: {question}

# Answer: Let's think step by step."""


# @cl.on_chat_start
# def main():
#     # Instantiate the chain for that user session
#     prompt = PromptTemplate(template=template, input_variables=["question"])
#     llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0), verbose=True)

#     # Store the chain in the user session
#     cl.user_session.set("llm_chain", llm_chain)


# @cl.on_message
# async def main(message: str):
#     # Retrieve the chain from the user session
#     llm_chain = cl.user_session.get("llm_chain")  # type: LLMChain

#     # Call the chain asynchronously
#     res = await llm_chain.acall(message, callbacks=[cl.AsyncLangchainCallbackHandler()])

#     # Do any post processing here

#     # "res" is a Dict. For this chain, we get the response by reading the "text" key.
#     # This varies from chain to chain, you should check which key to read.
#     await cl.Message(content=res["text"]).send()


import json

from langchain.agents import AgentExecutor

from chainlit.langflow import load_flow
import chainlit as cl


with open("/Users/suchattangjarukij/Downloads/Vector Store.json", "r") as f:
    schema = json.load(f)


@cl.on_chat_start
async def start():
    flow = await load_flow(schema=schema)
    cl.user_session.set("flow", flow)


@cl.on_message
async def main(message):
    # Load the flow from the user session
    flow = cl.user_session.get("flow")  # type: AgentExecutor

    # Run the flow
    res = await cl.make_async(flow.run)(
        message, callbacks=[cl.LangchainCallbackHandler()]
    )

    # Send the response
    await cl.Message(content=res).send()
