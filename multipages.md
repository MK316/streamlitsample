# II. Building a Multipage Streamlit App

In the previous tutorial, you learned how to:

- fork a GitHub repository
- understand `app.py`
- use `requirements.txt`
- deploy a Streamlit app online

Now, we will extend that idea and build a **multipage Streamlit app**.

A multipage app allows users to move between different pages inside one Streamlit project.

---

## Why Use Multiple Pages?

For English Education, one app can contain several learning tools.

For example:

```text
English Learning App
│
├── Home
├── Vocabulary Practice
├── Listening Practice
├── Pronunciation Practice
└── TTS Tool
```

Instead of creating a separate website for each activity, you can organize several activities inside one Streamlit app.

---

## Step 1. Create a `pages` Folder

Your project may currently look like this:

```text
my-streamlit-app/
│
├── app.py
├── requirements.txt
└── README.md
```

Create a new folder called:

```text
pages
```

Your project will now look like this:

```text
my-streamlit-app/
│
├── app.py
├── requirements.txt
├── README.md
│
└── pages/
```

---

## Step 2. Add Python Files to the `pages` Folder

Each Python file inside the `pages` folder becomes a new page.

For example:

```text
my-streamlit-app/
│
├── app.py
├── requirements.txt
│
└── pages/
    ├── 1_Vocabulary.py
    ├── 2_Listening.py
    └── 3_TTS.py
```

Streamlit automatically creates navigation for these pages.

---

## Step 3. Write a Simple Main Page

The main `app.py` can work as the home page.

```python
import streamlit as st

st.set_page_config(
    page_title="English Learning App",
    page_icon="📚"
)

st.title("📚 English Learning App")

st.write(
    "Welcome! Use the navigation menu to explore "
    "different English learning activities."
)
```

---

## Step 4. Create a Page

For example, create:

```text
pages/1_Vocabulary.py
```

Then add:

```python
import streamlit as st

st.title("📝 Vocabulary Practice")

word = st.text_input("Enter an English word")

if word:
    st.write("You entered:", word)
```

Now create another file:

```text
pages/2_Listening.py
```

Example:

```python
import streamlit as st

st.title("🎧 Listening Practice")

st.write(
    "This page can later contain audio files, "
    "listening questions, or TTS activities."
)
```

---

## Step 5. Run or Deploy the App

You do not need to change your Streamlit deployment settings.

Streamlit will automatically detect the `pages` folder.

After deployment, users can move between pages using the navigation menu.

---

## File Structure

A simple multipage project may look like this:

```text
my-streamlit-app/
│
├── app.py
├── requirements.txt
├── README.md
│
└── pages/
    ├── 1_Vocabulary.py
    ├── 2_Listening.py
    └── 3_TTS.py
```

---

## Naming Pages

Numbers help control the order of pages.

For example:

```text
1_Vocabulary.py
2_Listening.py
3_Pronunciation.py
4_TTS.py
```

The numbers determine the order in the navigation menu.

You can also use emojis:

```text
1_📝_Vocabulary.py
2_🎧_Listening.py
3_🗣️_Pronunciation.py
```

---

## Try It Yourself

Add at least two new pages to your Streamlit project.

Possible ideas:

- vocabulary quiz
- listening activity
- pronunciation tool
- reading activity
- grammar practice
- TTS tool

Keep each page simple at first.

The goal is to understand how **one Streamlit project can contain multiple learning activities**.

---

## Key Idea

```text
app.py
   +
pages folder
   +
Python files
   ↓
Multipage Streamlit App
```

You are now ready to organize several English learning tools inside one application.
