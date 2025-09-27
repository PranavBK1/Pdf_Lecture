#!/bin/bash
export PYTHONPATH="$PYTHONPATH:$(pwd)"
streamlit run flattened_app/streamlit_app.py
