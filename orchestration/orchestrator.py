from AGENTS.course_architect_agent import run as course
from AGENTS.teaching_strategist_agent import run as teach
from AGENTS.assessment_reviewer_agent import run as assess
from AGENTS.student_support_agent import run as support
from AGENTS.academic_quality_agent import run as quality

def orchestrate(context):
    return [course(context), teach(context), assess(context), support(context), quality(context)]
