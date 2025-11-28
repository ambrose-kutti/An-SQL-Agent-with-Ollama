#APPROACH -1 WITH SQL QUERY, REFERENCES, RETRIEVAL AND ANSWER

from langchain_community.utilities.sql_database import SQLDatabase
from langchain.agents import create_sql_agent
#from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

#Connect to DB
db = SQLDatabase.from_uri(
    
)

# Choose LLM
llm = Ollama(model="mistral", temperature=0.1)

# Build toolkit
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Create agent
sql_agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type="zero-shot-react-description",
    handle_parsing_errors=True
)

parsed_agent = sql_agent | StrOutputParser()

print("\nSQL Chatbot Ready. Type 'exit' to quit.\n")

while True:
    question = input(" Ask: ").strip()
    if question.lower() in {"exit", "quit"}:
        print(" Goodbye!")
        break
    if not question:
        continue

    try:
        result = sql_agent.invoke(question)
        print(f" Answer: {result}\n")
    except Exception as e:
        print(f" Error: {e}\n")

#=========================*******************=============================

#APPROACH -2 DIRECT RETRIEVAL AND ANSWER WITH TIME LOGGING

from langchain_community.utilities.sql_database import SQLDatabase
from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import time

# Connect to DB
db = SQLDatabase.from_uri(

)

# Choose LLM with only valid parameters
llm = Ollama(
    model="mistral", 
    temperature=0.1
    # Remove invalid parameters: num_predict, num_thread, top_k, top_p
)

# Build toolkit
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Create agent with optimized parameters
sql_agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=False,  # Turn off verbose to reduce output
    agent_type="zero-shot-react-description",
    handle_parsing_errors=True,
    max_iterations=5,  # Limit iterations for speed
    early_stopping_method="force"
)

# Simple output parser for clean Q&A
def clean_output_parser(result):
    """Extract only the final answer from agent response"""
    if isinstance(result, dict) and 'output' in result:
        return result['output']
    elif isinstance(result, str):
        # Remove intermediate steps and keep only final answer
        if "Final Answer:" in result:
            return result.split("Final Answer:")[-1].strip()
        return result
    return str(result)

print("\nSQL Chatbot Ready. Type 'exit' to quit.\n")

while True:
    question = input("You: ").strip()
    if question.lower() in {"exit", "quit", "bye"}:
        print("Goodbye!")
        break
    if not question:
        continue

    try:
        start_time = time.time()
        
        # Get response
        result = sql_agent.invoke({"input": question})
        
        # Clean the output
        clean_answer = clean_output_parser(result)
        
        end_time = time.time()
        
        print(f"\nAnswer: {clean_answer}")
        print(f"Response time: {end_time - start_time:.2f} seconds\n")
        
    except Exception as e:

        print(f"Error: {e}\n")
