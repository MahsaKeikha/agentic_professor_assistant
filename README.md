# F91 | Agentic Professor Assistant | L3 Gold Standard | v1.0

A governed multi-agent education reference system for course planning, teaching support, assessment review, student support, and academic quality control.

## Agents

- [Course Architect](AGENTS/course_architect_agent.py)
- [Teaching Strategist](AGENTS/teaching_strategist_agent.py)
- [Assessment Reviewer](AGENTS/assessment_reviewer_agent.py)
- [Student Support](AGENTS/student_support_agent.py)
- [Academic Quality](AGENTS/academic_quality_agent.py)

## Gold-standard academic governance

F91 is fail closed. Advisory release requires reviewed course content, assessments, academic-integrity handling, student privacy, accessibility, authorship, and explicit qualified faculty approval.

Release is blocked for student privacy violations, unresolved accessibility gaps, grading-bias risk, authorship or attribution problems, uncertain academic-integrity findings, and unsupported student-specific claims.

The reference system has no autonomous authority to assign final grades, impose disciplinary action, change student records, make academic-integrity findings, decide accommodations, or submit externally on behalf of faculty or students.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

The verification layer includes eight direct governance tests and a 10-scenario held-out academic-governance suite.
