

Folder Structure:
LegalEase/
├── backend/
│   ├── main.py
│   ├── routes.py
│   └── ai_core/
│       └── gemini_generator.py
├── frontend/
│   └── app.py  (Streamlit Website)
├── .env
└── requirements.txt
1. `requirements.txt`
fastapi
uvicorn
streamlit
google-generativeai
python-dotenv
python-docx
fpdf2
2. `.env` file
GEMINI_API_KEY=unga_google_api_key_inga_podunga
Key eduka: https://aistudio.google.com/app/apikey

3. `backend/ai_core/gemini_generator.py`
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiDocumentGenerator:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_document(self, doc_type, parties, terms, dates):
        prompt = f"""
        You are an expert legal document writer.
        Create a professional legal document.

        Document Type: {doc_type}
        Parties Involved: {parties}
        Key Terms & Clauses: {terms}
        Effective Date: {dates}

        Format:
        1. Give a Title
        2. Introduction with parties
        3. Numbered Clauses for terms
        4. Date and Signature section
        5. Use professional legal language.

        Make it ready to use.
        """
        response = self.model.generate_content(prompt)
        return response.text
4. `backend/routes.py`
from fastapi import APIRouter
from pydantic import BaseModel
from .ai_core.gemini_generator import GeminiDocumentGenerator

router = APIRouter()
generator = GeminiDocumentGenerator()

class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    dates: str

@router.post("/generate")
def generate_doc(request: DocumentRequest):
    result = generator.generate_document(
        request.document_type,
        request.parties,
        request.terms,
        request.dates
    )
    return {"document": result}
5. `backend/main.py`
from fastapi import FastAPI
from .routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="LegalEase API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "LegalEase Backend Running..."}
6. `frontend/app.py` - Ithu than Website
import streamlit as st
import requests
from docx import Document
from fpdf import FPDF
import io

st.set_page_config(page_title="LegalEase - AI Legal Generator", layout="centered", page_icon="⚖️")

--- CSS for good look ---
st.markdown("""
<style>
.stTextInput>div>div>input, .stTextArea>div>textarea {border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

--- Header ---
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/1040/1040230.png", width=100)
st.markdown("<h1 style='text-align:center;'>LegalEase</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>AI-Powered Legal Document Generator</p>", unsafe_allow_html=True)
st.divider()

--- Inputs ---
doc_type = st.selectbox("Document Type", ["Employment Contract", "NDA", "Lease Agreement", "Freelance Contract", "Partnership Agreement", "Other"])
if doc_type == "Other":
    doc_type = st.text_input("Enter Document Type")

parties = st.text_input("Parties Involved", placeholder="Ex: John Doe (Freelancer), ABC Corp (Client)")
terms = st.text_area("Key Terms (Use ; to separate)", placeholder="Ex: Payment is $500 per month; Confidentiality for 2 years; Work from home allowed")
dates = st.date_input("Effective Date")

if st.button("✨ Generate Document", use_container_width=True, type="primary"):
    if not parties or not terms:
        st.error("Parties & Terms fill pannu da!")
    else:
        with st.spinner("Gemini AI document generate panuthu..."):
            payload = {
                "document_type": doc_type,
                "parties": parties,
                "terms": terms,
                "dates": str(dates)
            }
            # Backend call
            # Local test ku direct function call pannalam, but API maadhiri seiya:
            try:
                # If backend running separately, use this:
                # res = requests.post("http://127.0.0.1:8000/generate", json=payload)
                # doc_text = res.json()['document']
                
                # For single app (without separate backend) - direct call:
                from backend.ai_core.gemini_generator import GeminiDocumentGenerator
                gen = GeminiDocumentGenerator()
                doc_text = gen.generate_document(doc_type, parties, terms, str(dates))
                
                st.success("Document Ready!")
                edited_text = st.text_area("Preview & Edit:", value=doc_text, height=400)

                # --- Downloads ---
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.download_button("Download TXT", edited_text, file_name=f"{doc_type}.txt")
                with col_b:
                    # DOCX
                    doc = Document()
                    doc.add_paragraph(edited_text)
                    bio = io.BytesIO()
                    doc.save(bio)
                    st.download_button("Download DOCX", bio.getvalue(), file_name=f"{doc_type}.docx")
                with col_c:
                    # PDF
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_auto_page_break(auto=True, margin=15)
                    pdf.set_font("Arial", size=11)
                    for line in edited_text.split('\n'):
                        pdf.multi_cell(0, 8, line.encode('latin-1', 'replace').decode('latin-1'))
                    pdf_bytes = pdf.output(dest='S').encode('latin-1')
                    st.download_button("Download PDF", pdf_bytes, file_name=f"{doc_type}.pdf")

            except Exception as e:
                st.error(f"Error: {e}")

st.markdown("---")
st.markdown("<p style='text-align:center; font-size:12px;'>Built with FastAPI + Streamlit + Gemini 1.5 Flash</p>", unsafe_allow_html=True)
Run Panna Steps:

*Step 1:* Setup
pip install -r requirements.txt
*Step 2:* Backend-a separate-a run panna venumna (Optional):
uvicorn backend.main:app --reload
*Step 3:* Website run pannu:
streamlit run frontend/app.py
Ithu open aana `http://localhost:8501` la un website varum.

Unakku ithu *HTML/CSS/JS website-a venuma illa Streamlit website pothuma?*

HTML version venumna sollu, naan athayum ready panni tharen - Gemini API-a JavaScript la connect panni full responsive website-a.
