from flask import Flask, render_template, request, jsonify
import openai
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

app = Flask(__name__)

# Configure OpenAI API key
load_dotenv()

##helper functions
def getLLMChain():
    llm = OpenAI()

    prompt_template = """You are a Youtube SEO expert and you are helping an 11 year old boy to expand his YOuTube Channel. 
    Given the description of his upcoming video give an SEO promising {promptType}. Just give the {promptType} of length {length} and nothing else.
    # Description: {description}
    """
    prompt = PromptTemplate(input_variables=["promptType", "description", "length"], template = prompt_template)
    llm = OpenAI(temperature=0)
    llm_chain = LLMChain(
        llm=llm,
        prompt=prompt
    )
    return llm_chain




@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_title():
    data = request.get_json()
    description = data["description"]

    ## get the LLMChain
    ytChain = getLLMChain()

    ## generate description
    description = ytChain.predict(description = description, promptType = "description", length = 250)
    
    ## generate title
    title = ytChain.predict(description = description, promptType = "title", length = 50)
    
    ## generate hashtags
    hashtags = ytChain.predict(description = description, promptType = "hashtags", length = 250)
    
    return jsonify({"title": title.strip(), "description": description.strip(), "hashtags": hashtags.strip()})

if __name__ == "__main":
    app.run(debug=True)