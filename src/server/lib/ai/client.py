from google import genai

# The client automatically picks up the API key from the environment variable.
__client: genai.Client = None

def get_client() -> genai.Client:
    """Loads and returns connection to Gemini API"""
    global __client
    if __client == None:
        print('Connecting to Gemini API')
        __client = genai.Client()
        print('Connected to Gemini API')
    return __client