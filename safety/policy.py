"""Fail-closed academic governance for F91 Professor Assistant."""

PROTECTED_ACTIONS = {
    "final_grade",
    "disciplinary_action",
    "student_record_change",
    "external_submission",
    "academic_integrity_finding",
    "accommodation_decision",
}

REQUIRED_REVIEWS = (
    "course_content_reviewed",
    "assessment_reviewed",
    "academic_integrity_reviewed",
    "student_privacy_reviewed",
    "accessibility_reviewed",
    "authorship_reviewed",
    "faculty_approval",
)


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "protected academic action requires direct qualified human authority"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required academic review", "missing": missing}

    blockers = []
    if context.get("privacy_violation"):
        blockers.append("student privacy violation unresolved")
    if context.get("accessibility_gap"):
        blockers.append("accessibility requirement unresolved")
    if context.get("grading_bias_risk"):
        blockers.append("grading bias risk unresolved")
    if context.get("authorship_misattribution"):
        blockers.append("authorship or attribution issue unresolved")
    if context.get("academic_integrity_uncertain"):
        blockers.append("academic integrity determination is uncertain")
    if context.get("unsupported_student_claim"):
        blockers.append("student-specific claim lacks adequate evidence")

    if blockers:
        return {"allowed": False, "reason": "academic governance blocker", "blockers": blockers}

    return {"allowed": True, "reason": "advisory academic package approved after qualified faculty review"}


def enforce(action: str, approved: bool) -> None:
    if review_required(action) and not approved:
        raise PermissionError("Qualified human approval is required for this action.")
