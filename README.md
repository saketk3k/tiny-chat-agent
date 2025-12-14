# Tiny Chat Agent

A lightweight, interactive chat agent built with **Streamlit**.

## Purpose
This POC demonstrates how to build a stateful Conversational UI in pure Python, which is a common requirement for internal AI tools.

## Features
-   **Chat Interface**: Uses Streamlit's native `st.chat_message` components.
-   **State Management**: Persists chat history across re-runs.
-   **Tool Routing**: Simple keyword detection simulates "Agentic" behavior (choosing which tool to run based on input).

## Usage

1.  **Install**:
    ```bash
    pip install streamlit
    ```

2.  **Run**:
    ```bash
    streamlit run app.py
    ```

3.  **Interact**:
    Open your browser to `http://localhost:8501`.
    Try commands like:
    -   "What time is it?"
    -   "Tell me a joke"
    -   "System status"
