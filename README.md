# AutoCorpus-Dynamic
A dynamic automatic corpus builder with semantic inference for online language.

1. Overview

AutoCorpus-Dynamic is a two-phase system for automatically constructing a continuously updating corpus from online platforms and performing semantic inference on modern digital language.
The project supports:

Dynamic data acquisition from Reddit, Quora, StackOverflow, and StackExchange
Real-time corpus growth with state persistence
Automatic cleaning, HTML removal, emoji extraction
Short-form meaning inference using Word2Vec + affirmation model
Emoji semantic profiling using Pointwise Mutual Information (PMI)
Text normalization driven by learned and hand-built semantics

This repository contains all modules, scripts, and notebooks required to build the corpus, validate its linguistic quality, and derive semantic interpretations based on learned patterns.

2. Requirements

The system is designed to run in Google Colab.

Required libraries:
requests
emoji
pandas
beautifulsoup4
gensim
numpy
nltk

All required packages are installed automatically in the setup notebooks.

3. Phase 1 — Dynamic Corpus Builder

Phase 1 handles data acquisition, cleaning, emoji extraction, and JSONL corpus generation.

File Descriptions (Phase 1)
01_setup_environment.py

Installs required dependencies and prepares the environment.
Output: Confirmation of installed libraries.

02_text_utils.py

Provides core utility functions:

extract_emojis(text)

clean_text(text)

epoch_to_time(timestamp)

Output: Utility module imported by other scripts.

03_state_manager.py

Handles persistent tracking for incremental corpus building:

Saves last_seen_id.txt

Prevents duplicate processing

Output: Updates or reads last_seen_id.txt.

04_stackexchange_collector.py

Implements the API collector with:

Pagination

Backoff handling / rate-limit recovery

Retrieval of answer bodies

Output: Raw text responses + timestamps.

05_corpus_writer.py

Writes cleaned entries to the corpus file:

Appends to scifi_dynamic_corpus.jsonl in JSONL format

Output: Updated corpus file.

06_autocorpus_runner.py (Main Engine)

Continuously runs:

Loads last_seen_id

Fetches new answers

Cleans HTML + extracts emoji

Appends to corpus

Updates last_seen_id

Sleeps for scheduled interval

Expected Output:
A growing corpus updated in real time.

07_corpus_preview.ipynb

Loads JSONL corpus, displays:

First rows

Total entries

Structure

Output: DataFrame preview.

08_export_corpus.ipynb

Exports plain-text corpus:

Removes emoji

Outputs corpus_text_only.txt

Output: Download-ready text corpus.

4. Phase 2 — Meaning Inference Engine

Phase 2 computes semantic inference using the corpus built in Phase 1.

File Descriptions (Phase 2)
09_setup_phase2_environment.py

Installs Phase 2 dependencies (gensim, nltk, emoji).
Output: Ready environment.

10_corpus_loader.ipynb

Loads the JSONL corpus and prints:

Head

Total rows

Schema

Output: DataFrame loaded successfully.

11_text_preprocessing.py

Provides:

HTML cleaning

Tokenization

Output: Clean tokens for modeling.

12_word2vec_train.py

Trains Word2Vec:

vector_size=100

window=5

min_count=2

Output:
Trained word embedding model + vocabulary size.

13_shortform_detector.py

Identifies candidate short forms:

<= 4 characters

Context window extraction

Output: Raw short-form frequency table + contexts.

14_shortform_candidate_extractor.py

Filters short forms using:

Stopwords

Frequency ≥ 3

Output: Candidate short-form list.

15_shortform_affirmation_model.py

Builds an affirmation centroid from:

["true", "really", "honestly", "facts", "legit", ...]


Output:
A semantic anchor vector for “agreement/affirmation-language”.

16_meaning_lexicons.py

Contains:

Built-in short-form expansions

Built-in emoji gloss sets

Output: Fallback dictionary for normalization.

17_embedding_utils.py

Provides:

phrase_embedding()

Embedding averaging

Output: Phrase-level semantic vectors.

18_shortform_inference_engine.py

Infers short-form meaning using:

Cosine similarity

Affirmation score

Expansion similarity

Output:
shortform_lexicon dictionary with:

freq

semantic type

affirmation score

learned expansion

19_export_shortform_lexicon.py

Exports:

shortform_lexicon.json


Output: JSON file.

20_emoji_stats_builder.py

Counts:

Emoji frequency

Word frequency

Emoji–word co-occurrence

Output: Frequency tables.

21_emoji_pmi_engine.py

Computes PMI:

PMI(e,w) = log2( P(E,W) / (P(E) P(W)) )


Output:
Top 10 semantic words per emoji → emoji_semantics dict.

22_export_emoji_semantics.py

Saves:

emoji_semantics.json


Output: JSON file.

23_normalization_engine.py

Normalizes text by:

Replacing short forms with learned expansions

Attaching emoji glosses

Merging learned + fallback semantics

Output:
Normalized sentence + emoji semantic map.

24_normalization_tests.py

Provides sample test cases.
Output Example:

Original: that episode was fr 😭😭
Normalized: that episode was for real
Emoji semantics: { ... }

How to Run the Entire System
Phase 1 Execution

Open Google Colab

Upload the phase1 folder

Run sequentially:

01_setup_environment.py  
02_text_utils.py  
03_state_manager.py  
04_stackexchange_collector.py  
05_corpus_writer.py  
06_autocorpus_runner.py  
07_corpus_preview.ipynb  
08_export_corpus.ipynb


Important:
Keep 06_autocorpus_runner.py running to continuously update the corpus.

Phase 2 Execution

Upload the phase2 folder and run in order:

09_setup_phase2_environment.py  
10_corpus_loader.ipynb  
11_text_preprocessing.py  
12_word2vec_train.py  
13_shortform_detector.py  
14_shortform_candidate_extractor.py  
15_shortform_affirmation_model.py  
16_meaning_lexicons.py  
17_embedding_utils.py  
18_shortform_inference_engine.py  
19_export_shortform_lexicon.py  
20_emoji_stats_builder.py  
21_emoji_pmi_engine.py  
22_export_emoji_semantics.py  
23_normalization_engine.py  
24_normalization_tests.py

6. Final Outputs Produced
Output File	Description
scifi_dynamic_corpus.jsonl	Fully dynamic JSONL corpus
corpus_text_only.txt	Clean text-only corpus
shortform_lexicon.json	Learned short-form meanings
emoji_semantics.json	PMI-based emoji gloss clusters
Normalized Outputs	Final cleaned + expanded sentences

8. Citation

AutoCorpus-Dynamic: An Automatic Dynamic Corpus Builder with a
Meaning Inference Model for Continuously Updating Multimodal
Modern Digital Language(2025)
