from AGENTS.academic_quality_agent import run as quality
from AGENTS.assessment_reviewer_agent import run as assess
from AGENTS.course_architect_agent import run as course
from AGENTS.student_support_agent import run as support
from AGENTS.teaching_strategist_agent import run as teach
from safety.policy import authorize


def orchestrate(context: dict) -> dict:
    """Run academic specialists and apply fail-closed faculty governance."""
    outputs = [course(context), teach(context), assess(context), support(context), quality(context)]
    governance = authorize("advisory_release", context)
    return {
        "system": "F91",
        "outputs": outputs,
        "governance": governance,
        "release_allowed": governance["allowed"],
        "human_review_required": True,
        "autonomous_grading_authority": False,
        "autonomous_disciplinary_authority": False,
        "autonomous_record_change_authority": False,
    }


def run(context: dict) -> dict:
    return orchestrate(context)
