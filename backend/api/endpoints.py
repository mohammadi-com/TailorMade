from datetime import datetime
import os

from fastapi import APIRouter

import backend.core.ai_service as ai_service
from backend.models.job import Job
from backend.models.latex import Latex
from backend.models.profile import Profile, Resume
from backend.models.question import Question
from backend.models.tailoring_options import TailoringOptions
from backend.models.templates import (
    Template_Details,
    john_doe_legal_authorization,
    john_doe_preferences,
    john_doe_resume,
)
from backend.utils.file_ops import generate_pdf_from_latex, save_pdf
from fastapi import APIRouter

func_router = APIRouter()


@func_router.post("/determine_eligibility")
def determine_eligibility(job: Job, profile: Profile = Profile(resume=Resume(john_doe_resume),legal_authorization=john_doe_legal_authorization), tailoring_options: TailoringOptions = TailoringOptions()):
    """
    Gets profile and job description and determines eligibility for applying to the job
    """
    eligibility, reason = ai_service.consider_eligibility(job.description, profile.legal_authorization, tailoring_options.ai_model)
    return {
        "eligibility": eligibility,
        "reason": reason
    }

@func_router.post("/determine_suitability")
def determine_suitability(job: Job, profile: Profile = Profile(resume=Resume(john_doe_resume), preferences=john_doe_preferences), tailoring_options: TailoringOptions = TailoringOptions()):
    """
    Gets profile and job description and determines suitability for applying to the job 
    """
    suitability, reason = ai_service.consider_suitability(job.description, profile.preferences, tailoring_options.ai_model)
    return {
        "suitability": suitability,
        "reason": reason
    }

@func_router.post("/generate-tailored-plain-resume")
def generate_tailored_plain_resume(job: Job, profile: Profile = Profile(resume=Resume(john_doe_resume)), tailoring_options: TailoringOptions = TailoringOptions()) -> str:
    """
    Gets resume and job description in plain text and returns tailored resume as a string
    """
    return ai_service.create_tailored_plain_resume(profile.resume.text, job.description, tailoring_options.ai_model, tailoring_options.resume_template)

@func_router.post("/generate-tailored-plain-coverletter")
def generate_tailored_plain_coverletter(job: Job, profile: Profile = Profile(Resume(john_doe_resume)), tailoring_options: TailoringOptions = TailoringOptions()) -> str:  # We should not pass tailoring options everytime, should be a config for each user. It could be kept with a session for example.
    """
    Gets resume and job description in plain text and returns customized cover letter as a string
    """
    return ai_service.create_tailored_plain_coverletter(profile.resume.text, job.description, tailoring_options.ai_model)

@func_router.post("/generate-latex-resume-save")
def generate_tailored_latex_resume_save(job: Job, profile: Profile = Profile(Resume(john_doe_resume)), tailoring_options: TailoringOptions = TailoringOptions()):
    """
    Gets resume and job description in plain text and saves tailored resume
    """
    tailored_plain_resume = generate_tailored_plain_resume(job, profile, tailoring_options)
    company_name = ai_service.get_company_name(job.description)
    
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pdf_path = f'Application/Resumes/{current_time}_{company_name}'
    os.makedirs(pdf_path, exist_ok=True)
    latex_compiler_response, latex_code = ai_service.covert_plain_resume_to_latex(
        current_time,
        company_name,
        tailored_plain_resume,
        tailoring_options.ai_model,
        tailoring_options.resume_template
    )
    pdf_file_path = save_pdf(pdf_path, latex_compiler_response.content)
    
    return {
        "success": f"Generated resume saved at here: {pdf_file_path}",
        "pdf_file_path": pdf_file_path,
        "latex_code": latex_code
    }

@func_router.post("/answer-application-questions")
def answer_application_questions(
    job: Job,
    question: Question,
    profile: Profile = Profile(Resume(john_doe_resume)),
    tailoring_options: TailoringOptions = TailoringOptions()
) -> str:
    """
    Gets resume, job description, and questions in the job applicaton and answer to them based on resume and job description.
    """
    return ai_service.generate_answer_questions(
        profile.resume.text,
        job.description,
        question.description,
        tailoring_options.ai_model
    )

@func_router.post("/save-latex-resume")
def save_latex_resume(
    latex: Latex,
    tailoring_options: TailoringOptions
):
    """
    Saves the edited LaTeX code as PDF
    """
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    company_name = "edited"
    compiler = Template_Details[tailoring_options.resume_template]['compiler']
    latex_compiler_response = generate_pdf_from_latex(
        current_time,
        company_name,
        latex.latex_code,
        compiler
    )
    pdf_path = f'./Resumes/edited/{current_time}'
    pdf_file_path = save_pdf(pdf_path, latex_compiler_response.content)
    return {"path": pdf_file_path}