# Personalized NLP Revision Editor

Author-style NLP revision pipeline for supervised fine-tuning and transformer-based text editing.

## Overview

This project is an in-progress NLP editing system designed to revise text for grammar, clarity, flow, and readability while preserving an author's personal writing style. The long-term goal is to build a personalized revision editor that can learn from paired draft/revised examples and use author-specific style context during text editing.

The project currently includes dataset preprocessing, prompt construction, and local Hugging Face inference testing. Future versions will explore retrieval-augmented generation, supervised fine-tuning, and a simple demo interface.

## Project Goals

* Convert author-specific revision datasets from CSV to JSONL format.
* Build supervised editing examples from paired draft and revised text.
* Create a prompt-based baseline for grammar and style-preserving revision.
* Test local Hugging Face model inference using the Transformers library.
* Add retrieval-augmented generation using a private writing corpus as style context.
* Explore fine-tuning options for transformer-based text revision.
* Package the final editing workflow into a Gradio demo.

## Current Status

Completed:

* Created supervised editing datasets from paragraph- and scene-level revisions.
* Converted CSV datasets into JSONL files for NLP preprocessing.
* Built a prompt-construction baseline using few-shot revision examples.
* Manually tested the baseline prompt using ChatGPT while API access is pending.
* Implemented a local Hugging Face inference smoke test.
* Verified local inference using `distilgpt2`.
* Tested an instruction-style Hugging Face model with a simple grammar revision example.

In progress:

* Cleaning project structure for GitHub.
* Documenting private-data handling.
* Preparing a Hugging Face-compatible baseline script.
* Planning RAG retrieval using polished writing as style context.

Planned:

* Add train/validation/test splitting.
* Implement retrieval over a private style corpus.
* Test hosted API or Colab-based model generation.
* Explore supervised fine-tuning.
* Create a Gradio interface for demo/testing.

## Repository Structure

```text
personalized-nlp-revision-editor/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── README.md
├── outputs/
│   └── README.md
└── src/
    ├── prepare_dataset.py
    ├── baseline_editor.py
    └── baseline_hf.py
```

## Data

The dataset used for this project is built from paired writing revisions:

```text
original draft text → revised text
```

Each example may include:

* revision ID
* chapter or section number
* original version
* revised version
* revision category
* word counts
* similarity score

Example revision categories include:

* grammar correction
* prose polish
* dialogue
* pacing
* characterization
* emotional beats
* scene expansion
* structural revision

The full writing datasets are private and are not included in this public repository. This repository focuses on the preprocessing, prompt construction, and modeling workflow.

## Baseline Methods

### Baseline 1: Prompt Construction

The first baseline loads JSONL revision examples and formats them into a few-shot editing prompt. The prompt asks the model to revise grammar, clarity, flow, and readability while preserving author voice, tone, rhythm, and scene intent.

### Baseline 2: Manual Model Output Test

The generated prompt was manually tested through ChatGPT while API billing/access is pending. This allowed the prompt design to be evaluated before connecting it to an automated API workflow.

### Baseline 3: Hugging Face Local Inference

A local Hugging Face Transformers pipeline was tested to verify that open-source model inference works on the development machine.

Initial smoke test:

```text
Input: She walk to the garden and seen the prince.
Output: She made her way to the garden and saw the prince.
```

This confirmed that local inference can run successfully, although larger model training will require hosted GPU resources or Google Colab.

## Technologies

* Python
* JSONL preprocessing
* Hugging Face Transformers
* PyTorch
* OpenAI API-compatible prompt workflow
* Local model inference
* Planned: RAG retrieval
* Planned: Gradio demo

## Installation

```bash
pip install -r requirements.txt
```

Recommended dependencies:

```text
openai
transformers
torch
accelerate
```

## Usage

### Convert CSV datasets to JSONL

```bash
python src/prepare_dataset.py
```

### Build a prompt-based editing baseline

```bash
python src/baseline_editor.py
```

### Run local Hugging Face inference test

```bash
python src/baseline_hf.py
```

## Hardware Notes

This project is being developed on a machine with strong CPU/RAM resources but integrated graphics. Local preprocessing, prompt construction, and small Hugging Face inference tests are supported.

Larger model inference, RAG experiments, and fine-tuning will likely be moved to a hosted API, Google Colab, or another GPU-enabled environment.

## Privacy and Data Considerations

The private writing corpus and full supervised revision datasets are not included in this repository. Public files only include code, documentation, and project structure.

The `.gitignore` excludes:

* raw CSV files
* processed JSONL files
* private writing corpus files
* generated outputs
* API keys
* virtual environments

## Future Work

* Add dataset validation and summary statistics.
* Build train/validation/test splits.
* Implement retrieval-augmented generation using a private writing corpus.
* Compare prompt-only editing against retrieval-augmented editing.
* Explore supervised fine-tuning in a GPU-enabled environment.
* Build a Gradio demo for interactive text revision.
* Add evaluation examples comparing original passages, baseline outputs, and revised targets.

## Author

Ilia
Graduate Student, Computational Biological Engineering
University of Kansas
