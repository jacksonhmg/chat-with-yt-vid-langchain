from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

from dotenv import load_dotenv

load_dotenv()

def generate_pet_names(animal_type, pet_colour):
    llm = OpenAI(temperature=0.7)

    prompt_template_name= PromptTemplate(
        input_variables=['animal_type', 'pet_colour'],
        template="I have a pet {animal_type} and I want a cool name for it, it is {pet_colour} in colour. Suggest me five cool names for my {animal_type}"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="pet_name")

    response = name_chain({'animal_type': animal_type, 'pet_colour': pet_colour})
    return response

def langchain_agent():
    llm = OpenAI(temperature=0.5)

    tools = load_tools(["wikipedia", "llm-math"], llm = llm)

    agent = initialize_agent(
        agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        llm = llm,
        tools = tools,
        verbose = True
    )

    result = agent.run(
        "What is the average age of a dog? Multiply the age by 3"
    )

if __name__ == "__main__":
    langchain_agent()
    # print(generate_pet_names("cat", "orange"))