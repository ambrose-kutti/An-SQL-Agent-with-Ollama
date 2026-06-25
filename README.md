# ⚡ Conversational SQL Agent with Ollama

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/ambrose-kutti/An-SQL-Agent-with-Ollama?style=for-the-badge)](https://github.com/ambrose-kutti/An-SQL-Agent-with-Ollama/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ambrose-kutti/An-SQL-Agent-with-Ollama?style=for-the-badge)](https://github.com/ambrose-kutti/An-SQL-Agent-with-Ollama/network)
[![GitHub issues](https://img.shields.io/github/issues/ambrose-kutti/An-SQL-Agent-with-Ollama?style=for-the-badge)](https://github.com/ambrose-kutti/An-SQL-Agent-with-Ollama/issues)
[![GitHub license](https://img.shields.io/github/license/ambrose-kutti/An-SQL-Agent-with-Ollama?style=for-the-badge)](LICENSE) <!-- TODO: Add actual license file -->
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)

**Unlock your database with natural language – a conversational SQL agent powered by local LLMs via Ollama.**

</div>

## 📖 Overview

This project introduces a robust Python-based conversational SQL agent designed to simplify database interactions. By leveraging `LangChain` for orchestration and `Ollama` for local Large Language Model (LLM) inference, the agent allows users to query and retrieve information from a `MySQL` database using natural language. It intelligently converts human questions into precise SQL queries, executes them against the database, and presents the results in an understandable format, eliminating the need for manual SQL writing.

## ✨ Features

-   **Natural Language to SQL Conversion**: Translate plain English questions into valid SQL queries automatically.
-   **Local LLM Integration**: Powered by `Ollama` to utilize locally hosted language models (e.g., Mistral) for privacy and performance.
-   **MySQL Database Interaction**: Execute generated SQL queries directly against a MySQL database.
-   **Conversational Interface**: Maintain context throughout a conversation, allowing for follow-up questions and refined queries.
-   **Database Schema Awareness**: Introspects the database schema to generate accurate and relevant SQL queries.
-   **Interactive CLI**: Engage with the agent through a simple command-line interface.

## 🛠️ Tech Stack

**Runtime:**
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)

**AI/ML Frameworks:**
![LangChain](https://img.shields.io/badge/LangChain-Python-green?style=for-the-badge&logo=langchain)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-success?style=for-the-badge&logo=ollama)

**Database:**
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql)
![mysql-connector-python](https://img.shields.io/badge/mysql--connector--python-DB%20Driver-blueviolet?style=for-the-badge&logo=python)

**Utilities:**
![python-dotenv](https://img.shields.io/badge/python--dotenv-Env%20Mgmt-yellowgreen?style=for-the-badge)

## 🚀 Quick Start

Follow these steps to get your SQL Agent up and running locally.

### Prerequisites

Before you begin, ensure you have the following installed and configured:

-   **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
-   **MySQL Server**: A running MySQL instance with a database and user credentials.
    -   You can use `phpMyAdmin` or `MySQL Workbench` for easy database management.
-   **Ollama**: Install Ollama and pull a suitable model (e.g., `mistral`).
    ```bash
    # Install Ollama (refer to https://ollama.com/download)
    # Pull a model (e.g., Mistral)
    ollama pull mistral
    ```

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/ambrose-kutti/An-SQL-Agent-with-Ollama.git
    cd An-SQL-Agent-with-Ollama
    ```

2.  **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    # On macOS/Linux
    source venv/bin/activate
    # On Windows
    .\venv\Scripts\activate
    ```

3.  **Install dependencies**
    ```bash
    pip install langchain-community mysql-connector-python python-dotenv
    # Note: If you prefer PyMySQL over mysql-connector-python, use:
    # pip install langchain-community pymysql python-dotenv
    ```

4.  **Environment setup**
    Create a `.env` file in the project root with the following content and configure your database and Ollama settings.

    ```
    # .env
    DB_HOST=localhost
    DB_USER=your_mysql_user
    DB_PASSWORD=your_mysql_password
    DB_NAME=your_database_name

    OLLAMA_BASE_URL=http://localhost:11434
    OLLAMA_MODEL=mistral # Or any other model you pulled with Ollama
    ```
    **Note**: Replace placeholder values with your actual MySQL credentials and Ollama configuration.

5.  **Database setup**
    Ensure your MySQL database (`your_database_name`) exists and is accessible with the provided credentials. The agent will interact with the tables within this database. You can manually create it and grant privileges if it doesn't exist:
    ```sql
    CREATE DATABASE your_database_name;
    CREATE USER 'your_mysql_user'@'localhost' IDENTIFIED BY 'your_mysql_password';
    GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_mysql_user'@'localhost';
    FLUSH PRIVILEGES;
    ```

### Run the Agent

Once all prerequisites and installations are complete, you can start the conversational SQL agent:

```bash
python chatbot.py
```

The agent will initialize and prompt you to enter your natural language questions. Type `exit` or `quit` to end the session.

## 📁 Project Structure

```
An-SQL-Agent-with-Ollama/
├── chatbot.py           # Main script containing the SQL agent logic
├── .env                 # Environment variables (created from the example above)
└── README.md            # Project documentation
```

## ⚙️ Configuration

### Environment Variables

The agent relies on environment variables for sensitive information and configuration. These are loaded from the `.env` file.

| Variable        | Description                                       | Default             | Required |
|-----------------|---------------------------------------------------|---------------------|----------|
| `DB_HOST`       | MySQL database host                               | `localhost`         | Yes      |
| `DB_USER`       | MySQL username                                    | -                   | Yes      |
| `DB_PASSWORD`   | MySQL password                                    | -                   | Yes      |
| `DB_NAME`       | MySQL database name to query                      | -                   | Yes      |
| `OLLAMA_BASE_URL` | URL of the running Ollama server                 | `http://localhost:11434` | Yes      |
| `OLLAMA_MODEL`  | Name of the LLM model pulled in Ollama (e.g., `mistral`) | `mistral`           | Yes      |

## 🤝 Contributing

We welcome contributions to enhance this SQL agent! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your features or bug fixes.
3.  Implement your changes and ensure they adhere to Python best practices.
4.  Write clear, concise commit messages.
5.  Submit a pull request.

### Development Setup for Contributors

To set up your development environment:

1.  Follow the **Installation** steps outlined above.
2.  After activating your virtual environment, you can modify `chatbot.py` or add new modules.

## 📄 License

This project is licensed under the [LICENSE_NAME](LICENSE) - see the LICENSE file for details. <!-- TODO: Add actual license file -->

## 🙏 Acknowledgments

-   **LangChain**: For providing a powerful framework for developing LLM-powered applications.
-   **Ollama**: For making local LLM inference accessible and easy.
-   **MySQL**: The robust and widely used relational database system.

## 📞 Support & Contact

-   🐛 Issues: [GitHub Issues](https://github.com/ambrose-kutti/An-SQL-Agent-with-Ollama/issues)
-   📧 Owner: [Ambrose Kutti](mailto:contact@example.com) <!-- TODO: Add actual contact email for Ambrose Kutti -->

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

Made with ❤️ by [ambrose-kutti](https://github.com/ambrose-kutti)

</div>
