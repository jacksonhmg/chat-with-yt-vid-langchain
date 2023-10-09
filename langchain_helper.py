from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_pet_names(animal_type, pet_colour):
    llm = OpenAI(temperature=0.7)

    prompt_template_name= PromptTemplate(
        input_variables=['animal_type', 'pet_colour'],
        template="I have a pet {animal_type} and I want a cool name for it, it is {pet_colour} in colour. Suggest me five cool names for my {animal_type}"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)

    response = name_chain({'animal_type': animal_type, 'pet_colour': pet_colour})
    return response

if __name__ == "__main__":
    print(generate_pet_names("cat", "orange"))