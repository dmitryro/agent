# Thoughtful AI Customer Support Agent

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.37.1-red)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](./LICENSE)
[![Dependencies](https://img.shields.io/badge/Dependencies-requirements.txt-brightgreen)](./requirements.txt)
[![Status](https://img.shields.io/badge/Status-Prototype-yellow)](https://github.com/)

**Author**: Dmitry Roitman  
**Version**: 1.0.0  
**License**: [MIT License](./LICENSE) - This project is licensed under the MIT License, which allows for free use, modification, and distribution, subject to the terms in the LICENSE file.

A simple customer support AI agent built for Thoughtful AI using Streamlit and Python. The agent answers questions about Thoughtful AI's agents (EVA, CAM, PHIL) using a predefined dataset and falls back to generic responses for unmatched queries cherry picked by Dmitry Roitman.

## Features
- Web-based UI using Streamlit
- Fuzzy matching for question similarity (using `fuzzywuzzy`)
- Predefined dataset for Thoughtful AI agent information
- Fallback to generic responses for unmatched questions
- Conversation history tracking
- Error handling for invalid inputs
- Clean, responsive design

## Setup
1. Clone the repository:
   ```bash
   git clone git@github.com:dmitryro/agent.git thoughtful-ai-agent
   cd thoughtful-ai-agent
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```
   Open your browser at http://localhost:8501 to verify the agent works as expected.

## Dependencies
- Python 3.8+
- Streamlit
- fuzzywuzzy
- python-Levenshtein (optional, for faster fuzzy matching)
- pillow>=10.1.0 (to avoid conflicts with other packages)

## Usage
1. Open the web app in your browser (default: `http://localhost:8501`).
2. Enter a question about Thoughtful AI's agents (e.g., "What does EVA do?").
3. View the response and conversation history.

## Testing the Agent
To thoroughly evaluate the agent, test it with questions covering direct matches, variations, unrelated queries, edge cases, and conversational flow. Below are specific examples formatted as "Entering [question] should result in [response]," along with the purpose of each test.

### Test Examples
1. **Direct Matches** (Test exact dataset retrieval):
   - **Example**: Entering "What does the eligibility verification agent (EVA) do?" should result in "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
     - **Purpose**: Verifies exact matches to dataset questions.
   - **Example**: Entering "Tell me about Thoughtful AI's Agents." should result in "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
     - **Purpose**: Confirms broad dataset questions are handled.

2. **Variations of Predefined Questions** (Test fuzzy matching):
   - **Example**: Entering "What is EVA used for?" should result in "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
     - **Purpose**: Tests fuzzy matching for rephrased questions.
   - **Example**: Entering "How does CAM process claims?" should result in "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
     - **Purpose**: Ensures rephrased questions are matched correctly.

3. **Unrelated Questions** (Test fallback response):
   - **Example**: Entering "What's the weather like today?" should result in "I'm sorry, I don't have specific information about that. Could you please rephrase or ask another question about Thoughtful AI's agents?"
     - **Purpose**: Verifies the fallback for irrelevant questions.
   - **Example**: Entering "Who founded Thoughtful AI?" should result in "I'm sorry, I don't have specific information about that. Could you please rephrase or ask another question about Thoughtful AI's agents?"
     - **Purpose**: Tests fallback for unsupported Thoughtful AI questions.

4. **Edge Cases** (Test robustness):
   - **Example**: Entering "a" should result in an error message in the UI: "Please enter a valid question (at least 3 characters)."
     - **Purpose**: Tests input validation for short inputs.
   - **Example**: Entering "What does eva do?" should result in "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
     - **Purpose**: Verifies case-insensitive fuzzy matching.
   - **Example**: Entering "   " (whitespace only) should result in an error message in the UI: "Please enter a valid question (at least 3 characters)."
     - **Purpose**: Ensures whitespace inputs are rejected.

5. **Conversational Flow** (Test UI and history):
   - **Example**: Entering the sequence:
     1. "What does EVA do?"
     2. "Tell me about CAM."
     3. "What are the benefits of Thoughtful AI's agents?"
     should result in:
     - For "What does EVA do?": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
     - For "Tell me about CAM.": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
     - For "What are the benefits of Thoughtful AI's agents?": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
     - The "Conversation History" section should show all three questions and answers in reverse order (most recent first), formatted as **Q1**, **A1**, etc.
     - **Purpose**: Verifies session state and UI history display (up to 5 exchanges).

### How to Test
1. **Run the App**:
   ```bash
   streamlit run app.py
   ```
   Open `http://localhost:8501` in your browser.
2. **Ask Questions**:
   - Enter each test question in the text input box and click "Ask."
   - Observe the response in the "Answer" section and check the "Conversation History."
3. **Verify Behavior**:
   - **Correctness**: Ensure responses match the expected results above.
   - **UI**: Confirm answers and history are displayed clearly with proper styling (blue input borders, button colors).
   - **Robustness**: Check that edge cases (e.g., short inputs) trigger appropriate error messages.
   - **Fuzzy Matching**: Verify rephrased questions return correct dataset answers.
   - **Fallback**: Ensure unrelated questions trigger the fallback message.
4. **Stress Test** (Optional):
   - Ask 6+ questions to confirm only the last 5 appear in history.
   - Try a long question (e.g., "What does EVA do and how does it help with claims?") to test fuzzy matching.
   - Submit questions rapidly to ensure UI stability.

### Expected Results Summary
- **Direct matches** return exact dataset answers.
- **Rephrased questions** match the most relevant dataset answer (if similarity >70%).
- **Unrelated questions** trigger the fallback message.
- **Invalid inputs** (e.g., <3 characters) show an error in the UI.
- **History** logs up to 5 question-answer pairs, displayed in reverse chronological order.

## Notes
- The agent uses fuzzy matching with a threshold of 70% to find relevant answers.
- For unmatched questions, it returns a generic fallback response.
- Conversation history shows the last 5 exchanges.
- Error handling ensures valid input (minimum 3 characters).
- Use a virtual environment to avoid dependency conflicts (e.g., with `pillow`).

