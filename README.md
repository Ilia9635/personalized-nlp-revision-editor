## Personalized NLP Revision Editor

Author-style NLP revision pipeline for supervised fine-tuning and transformer-based text editing.

## Overview

This project is an in-progress natural language processing pipeline designed to model author-specific revision patterns from paired draft and revised text examples. The goal is to build a personalized writing-style revision editor capable of improving fiction prose while preserving voice, tone, emotional intent, and scene-level structure.

The project focuses on supervised text editing using paired examples of original draft text and revised text. These examples are converted into structured JSONL format for future transformer-based fine-tuning experiments.

## Project Goals

* Build a supervised NLP dataset from author-specific draft/revision pairs
* Convert CSV-based revision datasets into JSONL format for machine learning workflows
* Preserve author voice while modeling edits related to pacing, dialogue, characterization, emotional beats, and prose clarity
* Experiment with transformer-based text revision methods
* Develop a reusable preprocessing pipeline for long-form fiction revision tasks

## Current Status

This project is currently in progress.

Completed so far:

* Created structured supervised learning datasets from long-form fiction revisions
* Built paragraph-level and scene-level revision pairs
* Organized examples by revision type, including dialogue, pacing, characterization, emotional beats, prose polish, and scene expansion
* Implemented CSV-to-JSONL preprocessing scripts
* Began preparing the project structure for future model training and evaluation

Planned next steps:

* Add dataset validation checks
* Create train/validation/test splits
* Build a baseline text editing model
* Experiment with transformer-based fine-tuning
* Evaluate model outputs against held-out revision examples

## Repository Structure

```text
personalized-nlp-revision-editor/
│
├── data/
│   ├── raw/
│   │   └── README.md
│   ├── processed/
│   │   └── README.md
│
├── src/
│   └── convert_csv_to_jsonl.py
│
├── notebooks/
│   └── README.md
│
├── outputs/
│   └── README.md
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Dataset

The supervised dataset is built from paired writing revisions:

```text
original draft text → revised text
```

Each example includes metadata such as:

* revision ID
* chapter or section number
* original version
* revised version
* revision category
* word counts
* similarity score, when available

Example revision categories include:

* dialogue
* pacing
* characterization
* emotional beats
* prose polish
* scene expansion
* structural revision

Due to copyright and privacy considerations, the full writing dataset is not included in this public repository. The repository focuses on the preprocessing and modeling pipeline.

## Example JSONL Format

The processed dataset is intended to use a JSONL structure similar to:

```json
{
  "id": "example_001",
  "instruction": "Revise the following fiction passage while preserving the author's voice, tone, and scene intent.",
  "input": "Original draft text goes here.",
  "output": "Revised text goes here.",
  "metadata": {
    "revision_category": "emotional_beats",
    "old_word_count": 650,
    "new_word_count": 720
  }
}
```

## Preprocessing Workflow

The preprocessing pipeline is designed to:

1. Load CSV files containing paired revision examples
2. Validate required columns
3. Handle encoding issues from Excel or Windows-generated CSV files
4. Convert rows into JSONL format
5. Preserve long-form text formatting as much as possible
6. Save processed files for model training

## Technologies

* Python
* CSV / JSONL preprocessing
* Natural language processing
* Supervised fine-tuning dataset preparation
* Transformer-based text editing workflows

Planned tools and libraries:

* pandas
* scikit-learn
* Hugging Face Transformers
* Hugging Face Datasets
* PyTorch

## Motivation

This project combines my interest in machine learning with my background in long-form fiction writing. Rather than building a generic grammar correction tool, I wanted to explore whether supervised learning can model a specific author’s revision behavior.

The project is especially focused on edits that are difficult to capture with simple grammar tools, such as:

* strengthening emotional tension
* improving scene pacing
* preserving character voice
* refining dialogue rhythm
* expanding or compressing scene beats
* maintaining consistency across long-form prose

## Future Work

Future development will focus on:

* Training a baseline revision model
* Comparing different prompt and dataset formats
* Evaluating model performance on unseen draft passages
* Adding automated quality checks for revision pairs
* Creating a small demo interface for testing model outputs
* Exploring model behavior across different revision categories

## Ethical and Data Considerations

The dataset used for this project contains original creative writing. For that reason, the full dataset is kept private and is not distributed in this repository.

This repository is intended to share the preprocessing, formatting, and modeling workflow without publicly releasing proprietary creative writing data.

## Author

Ilia
Graduate Student, Computational Biological Engineering
University of Kansas
