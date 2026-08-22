from orchestration.orchestrator import run

REFERENCE_CONTEXT = {
    "objective": "professor assistant academic support",
    "course_content_reviewed": True,
    "assessment_reviewed": True,
    "academic_integrity_reviewed": True,
    "student_privacy_reviewed": True,
    "accessibility_reviewed": True,
    "authorship_reviewed": True,
    "faculty_approval": True,
}

if __name__ == "__main__":
    print(run(REFERENCE_CONTEXT))
