# Deployment of streamlit application into Huggingface platform in Notebok
from src.langgraphagenticai.main import load_langgraph_agenticai_app


if __name__=="__main__":
    import streamlit as st
    load_langgraph_agenticai_app()