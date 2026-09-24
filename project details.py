def generate_legal_agreement(project_title, overview, team, tech_stack, phases, demo_link):
    """Generates a simple legal agreement text based on project details."""

    agreement_text = f"**{project_title} AI Document Generation Agreement**\n\n"

    # Introduction Section
    agreement_text += "This AI Document Generation Agreement (\"Agreement\") is made as of [Date], by and between [Generating Party] and the parties involved in the creation of the project detailed below.\n\n"
    
    # Project Details Section
    agreement_text += "## 1. Project Information\n\n"
    agreement_text += f"**Project Title:** {project_title}\n\n"
    agreement_text += f"**Project Overview:** {overview}\n\n"

    # Team Members Section
    agreement_text += "## 2. Team Details\n\n"
    agreement_text += "The following team members are the key contributors to this project:\n"
    for member in team:
        agreement_text += f"* {member}\n"
    agreement_text += "\n"

    # Tech Stack Section
    agreement_text += "## 3. Technology Stack\n\n"
    agreement_text += "The project leverages the following technologies:\n"
    agreement_text += f"* Language: {tech_stack['language']}\n"
    agreement_text += f"* AI Model: {tech_stack['ai_model']}\n"
    agreement_text += f"* UI / Platform: {tech_stack['platform']}\n"
    agreement_text += "\n"

    # Project Phases Section
    agreement_text += "## 4. Development Phases\n\n"
    agreement_text += "The project development followed these phases:\n"
    for phase in phases:
        agreement_text += f"* [ ] {phase}\n" # Simplified for plain text
    agreement_text += "\n"

    # Project Demo Section
    agreement_text += "## 5. Project Demonstration\n\n"
    agreement_text += f"A demonstration of the project is available for viewing at the following location:\n{demo_link}\n\n"

    # Terms and Conditions (Placeholder)
    agreement_text += "## 6. Terms and Conditions\n\n"
    agreement_text += "The use of the LegalEase AI-powered document generation system is subject to the general terms and conditions [Link to Terms and Conditions]. "
    agreement_text += "All generated documents are for informational and planning purposes only and should be reviewed by a legal professional. "
    agreement_text += "By generating this document, you acknowledge and agree to these terms.\n\n"
    
    agreement_text += "**Disclaimer:** LegalEase AI is an AI-powered tool and does not provide legal advice. "
    agreement_text += "The accuracy and completeness of generated documents are not guaranteed."

    return agreement_text

# --- Details extracted from the provided image ---

project_title_image = "LegalEase AI-powered Document Generator" # Updated title as requested
project_overview_image = "LegalEase AI is an AI-powered legal document generation platform designed to streamline the creation of various legal documents like contracts, agreements, NDAs, and more. It uses advanced AI models to simplify legal processes, making them faster and more accessible." # Modified for context
team_details_image = [
    "Poorvika  M(Team Lead)",
    "santhiya M",
    "Aruna Devi S",
    "Ramalakshmi S"
]
tech_stack_image = {
    "language": "Python",
    "ai_model": "Google Gemini API (simulated)", 
    "platform": "Streamlit / Python"
}
project_phases_image = [
    "Brainstorming & Ideation",
    "Requirement Analysis",
    "Project Design",
    "Project Planning",
    "Project Development",
    "Project Testing",
    "Project Documentation",
    "Project Demonstration"
]
demo_video_link_image = "https://drive.google.com/uc?id=1eA9B0C1D2E3F4G5H6I7J8K9L0M1N2O3P" # Example Google Drive video link format

# --- Generate the legal agreement ---

generated_legal_doc = generate_legal_agreement(
    project_title_image,
    project_overview_image,
    team_details_image,
    tech_stack_image,
    project_phases_image,
    demo_video_link_image
)

# --- Print the generated document ---

print(generated_legal_doc)
