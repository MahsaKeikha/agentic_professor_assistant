from orchestration.orchestrator import run


def base():
    return {
        "course_content_reviewed": True,
        "assessment_reviewed": True,
        "academic_integrity_reviewed": True,
        "student_privacy_reviewed": True,
        "accessibility_reviewed": True,
        "authorship_reviewed": True,
        "faculty_approval": True,
    }


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "faculty_approval": False}, False),
    ({**base(), "privacy_violation": True}, False),
    ({**base(), "accessibility_gap": True}, False),
    ({**base(), "grading_bias_risk": True}, False),
    ({**base(), "authorship_misattribution": True}, False),
    ({**base(), "academic_integrity_uncertain": True}, False),
    ({**base(), "unsupported_student_claim": True}, False),
    ({**base(), "student_privacy_reviewed": False}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += run(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
