# An SQL Agent with Ollama


This repository provides a Python script that creates a conversational SQL agent using LangChain and a locally hosted LLM via Ollama. The agent can understand natural language questions, convert them into SQL queries, execute them against a MySQL database, and return the answers.

## How It Works

The `chatbot.py` script demonstrates how to build and interact with an SQL agent. It includes two approaches:

1.  **Verbose Agent:** This approach shows the agent's entire thought process, including the SQL query it generates and the observations it makes. This is useful for debugging and understanding how the agent reasons.
2.  **Optimized Agent:** This version is configured for a cleaner user experience. It hides the intermediate steps, provides only the final answer, and logs the response time for each query.

The core components are:
*   **`Ollama`**: Integrates a locally running Large Language Model (e.g., `mistral`) for natural language understanding and generation.
*   **`SQLDatabase`**: Connects to and describes the target MySQL database schema for the agent.
*   **`SQLDatabaseToolkit`**: Provides the agent with a set of tools to interact with the database (e.g., list tables, check schema, run queries).
*   **`create_sql_agent`**: Assembles the LLM and the toolkit into an autonomous agent that can process a user's request from start to finish.

## Prerequisites

*   Python 3.8 and more
*   [Ollama](https://ollama.com/) installed and running on your local machine.
*   The `mistral` model available in Ollama. You can pull it by running: (or you can prefer your own model and pull)
    ```sh
    ollama run mistral (or your own LLM model of choice)
    ```
*   Access to a MySQL database.

## Setup and Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/ambrose-kutti/an-sql-agent-with-ollama.git
    cd an-sql-agent-with-ollama
    ```

2.  **Install the necessary Python packages:**
    ```sh
    pip install langchain langchain-community langchain-core ollama mysql-connector-python
    ```

3.  **Configure the Database Connection:**
    Open the `chatbot.py` file and update the database connection URI with your own MySQL credentials:
    **Remember to give the correct crendentials**
    ```python
    # Connect to DB
    db = SQLDatabase.from_uri(
        "mysql+mysqlconnector://YOUR_USERNAME:YOUR_PASSWORD@YOUR_HOST:YOUR_PORT/YOUR_DATABASE"
    ) (here I have used PhpMyAdmin to store MySQL Data)
    ```

## Usage

The script is set up to run the optimized agent (Approach 2) by default. To see the verbose agent in action, you can comment out the second half of the script and uncomment the first half.

1.  Ensure the Ollama application is running.

2.  Run the script from your terminal:
    ```sh
    python chatbot.py
    ```

3.  Once the chatbot is ready, you can start asking questions about your database in natural language.

    ```
    SQL Chatbot Ready. Type 'exit' to quit.

    You: Your Question?

    Answer: Answer (the model generate the Answer)
    Response time: 5.83 seconds (Time taken to generate the answer)

    You: exit
    Goodbye! (chat ends)
