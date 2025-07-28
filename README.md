# GrammarFix
# 📝 AI Grammar Corrector

A simple and efficient web application built with Streamlit that corrects grammatical errors in a given text using a pre-trained T5 model from the Hugging Face Hub.

---

## ✨ Features

-   **Simple Interface**: A clean and straightforward UI for entering text and receiving corrections.
-   **AI-Powered Corrections**: Leverages the `vennify/t5-base-grammar-correction` model to provide accurate grammatical fixes.
-   **Efficient Model Loading**: Uses Streamlit's caching (`st.cache_resource`) to load the model only once, ensuring fast performance on subsequent runs.
-   **User-Friendly**: Provides clear instructions and feedback, including loading spinners and input validation.

---

## 🛠️ Tech Stack

-   **Language**: Python
-   **Framework**: Streamlit
-   **Machine Learning**: Hugging Face Transformers
-   **Model**: T5 (Text-To-Text Transfer Transformer)

---

## 🚀 Setup

### ### 1. Prerequisites

-   Python 3.8+
-   An internet connection to download the model on the first run.

### ### 2. Installation

1.  Create a file named `requirements.txt` in your project directory with the following content. You will also need to install PyTorch.

    ```txt
    streamlit
    transformers
    torch
    ```
    *Note: Depending on your system (e.g., if you have an NVIDIA GPU and want CUDA support), you might need a specific version of PyTorch. For most standard use cases, the command below will suffice.*

2.  Open a terminal and install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ Usage

1.  Save the code as `app.py` in your project directory.

2.  Run the application from your terminal:
    ```bash
    streamlit run app.py
    ```

3.  The application will open in your browser. Type or paste a sentence into the text area.

4.  Click the "Correct Grammar" button to get the corrected version of your text.

