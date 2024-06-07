import os

from flask import Flask, request, jsonify
from flask_cors import CORS

from imports.config import logger

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain   