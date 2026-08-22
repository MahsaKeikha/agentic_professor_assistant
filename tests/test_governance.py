from orchestration.orchestrator import run
from safety.policy import authorize


def valid_context():
    return {
        "course_content_reviewed": True,
        "assessment_reviewed": True,
        "academic_integrity_reviewed": True,
        "student_privacy_reviewed": True,
        "accessibility_reviewed": True,
        "authorship_reviewed": True,
        "faculty_approval": True,
    }


def test_complete_review_can_release_advisory_package():
    result = run(valid_context())
    assert result["release_allowed"] is True
    assert result["autonomous_grading_authority"] is False


def test_missing_faculty_approval_fails_closed():
    context = valid_context()
    context["faculty_approval"] = False
    assert run(context)["release_allowed"] is False


def test_final_grade_is_never_autonomously_authorized():
    assert authorize("final_grade", valid_context())["allowed"] is False


def test_privacy_violation_blocks_release():
    context = valid_context()
    context["privacy_violation"] = True
    assert run(context)["release_allowed"] is False


def test_accessibility_gap_blocks_release():
    context = valid_context()
    context["accessibility_gap"] = True
    assert run(context)["release_allowed"] is False


def test_grading_bias_risk_blocks_release():
    context = valid_context()
    context["grading_bias_risk"] = True
    assert run(context)["release_allowed"] is False


def test_authorship_issue_blocks_release():
    context = valid_context()
    context["authorship_misattribution"] = True
    assert run(context)["release_allowed"] is False


def test_uncertain_integrity_finding_blocks_release():
    context = valid_context()
    context["academic_integrity_uncertain"] = True
    assert run(context)["release_allowed"] is False
