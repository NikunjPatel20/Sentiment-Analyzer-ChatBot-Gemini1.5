from imports.imports import *

app = Flask(__name__)
CORS(app) # CORS is used from handling cross origin requests it will be needed in time of the deployment. 

load_dotenv('.env')
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

@app.route('/', methods=['POST'])
def main() -> jsonify:
    return jsonify({
        "message" : handle_query(request.get_json()["message"])
    })

def handle_query(message: str) -> str:
    try:
        llm = ChatGoogleGenerativeAI( #Gemini Chat Model
            model = 'gemini-1.5-pro', # API key only gives this model for our usecase
            google_api_key = GEMINI_API_KEY,
            temprature = 0.2, # Value near 0 gives more factual answers, value near 1 gives more imagenary answer
            verbose=True,
        )
        # Model expects a dictionary type prompt, we are currently using this only for testing prompt template may change.
        chain = PromptTemplate.from_template('Give me response. {message}') 
        llm_chain = chain | llm

        response = llm_chain.invoke(message)

        return response  
        
        
    except Exception as e:
        logger.error(f"Error in handle_query Function: {e}")


if __name__=="__main__":
    topic = "how ai is really cool"
    resp = handle_query(topic)

    print(resp)

    # app.run(debug=True)


