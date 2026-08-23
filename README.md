# F91 Agentic Professor Assistant

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

A governed five-agent reference architecture for university teaching support across course design, pedagogy, assessment alignment, student support, academic quality, accessibility, evidence, and qualified faculty approval.

F91 is designed as a reusable multi-agent framework for professors, lecturers, instructors, teaching teams, and academic programs that want structured assistance without transferring faculty authority to an automated system. The architecture separates curriculum planning, teaching strategy, assessment review, student-support reasoning, and academic-quality control so that consequential academic decisions remain reviewable and attributable.

The repository supports teaching and academic workflow assistance. It does not assign final grades, determine misconduct, impose discipline, decide accommodations, modify official student records, make admissions decisions, or submit work on behalf of faculty or students.

## Teaching lifecycle

```text
course goals + institutional context
              |
              v
       course architecture
              |
              v
       teaching strategy
              |
              v
      assessment review
              |
              v
       student support
              |
              v
       academic quality
              |
              v
     qualified faculty approval
```

The workflow is fail closed for consequential outputs. Privacy violations, unresolved accessibility barriers, assessment misalignment, grading-bias risks, uncertain academic-integrity claims, unsupported student-specific conclusions, attribution problems, or missing faculty review remain blockers.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Course Architect Agent | Structures learning outcomes, course sequence, prerequisites, topics and learning activities | Does the course architecture support the intended learning outcomes and academic level? |
| Teaching Strategist Agent | Develops pedagogical approaches, lesson structures and instructional strategies | How should the material be taught so students can meaningfully engage with and learn it? |
| Assessment Reviewer Agent | Reviews assessment validity, alignment, rubrics, grading criteria and integrity risks | Does the assessment measure the intended learning rather than irrelevant factors? |
| Student Support Agent | Structures general learning support, feedback pathways and escalation | What support can be offered without making unsupported personal judgments or replacing faculty and institutional services? |
| Academic Quality Agent | Reviews coherence, accessibility, evidence, attribution, governance and release readiness | Is the academic package sufficiently complete, fair, accessible and reviewable for faculty approval? |

The agents provide structured recommendations. They do not independently exercise faculty authority.

## Repository structure

```text
AGENTS/
├── course_architect_agent.py
├── teaching_strategist_agent.py
├── assessment_reviewer_agent.py
├── student_support_agent.py
└── academic_quality_agent.py

SKILLS/
├── course_design.py
├── pedagogy.py
├── assessment_alignment.py
├── student_support.py
└── quality_review.py

TOOLS/
├── course_map_tool.py
├── rubric_tool.py
├── accessibility_tool.py
├── calendar_tool.py
└── evidence_tool.py

orchestration/
memory/
state/
schemas/
prompts/
config/
safety/
observability/
evals/
benchmarks/
examples/
tests/
docs/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

This separation makes the workflow easier to audit, test, adapt, and cite as a multi-agent academic reference architecture.

## Course context

A useful course record can include:

```text
course_id
course_title
academic_level
credit_or_contact_hours
program
prerequisites
student_population
modality
term_length
learning_outcomes
required_topics
institutional_policies
assessment_scheme
accessibility_requirements
faculty_owner
```

Course recommendations should be interpreted within the actual institution, discipline, student population, accreditation context, and faculty goals.

## Learning outcomes

Course design begins with explicit learning outcomes.

Strong outcomes identify what students should be able to demonstrate by the end of the learning experience. Depending on the discipline, outcomes may address:

- conceptual understanding
- factual knowledge
- problem solving
- analysis
- design
- experimentation
- communication
- synthesis
- professional judgment
- teamwork
- ethical reasoning
- research literacy

F91 does not assume that every outcome should be assessed in the same way.

## Constructive alignment

The Course Architect and Assessment Reviewer use an alignment model:

```text
learning outcomes
      |
      v
learning activities
      |
      v
assessment tasks
      |
      v
rubrics + feedback
```

A course is misaligned when students are expected to demonstrate skills that were not meaningfully taught, or when assessments measure something different from the stated outcomes.

`TOOLS/course_map_tool.py` provides deterministic support for mapping outcomes to topics, activities and assessments.

## Course sequencing

Course sequencing can consider:

- prerequisite knowledge
- conceptual dependencies
- increasing complexity
- practice before high-stakes assessment
- spacing and retrieval
- laboratory or project dependencies
- workload distribution
- cumulative learning

A syllabus should not be treated as a list of independent topics when later material depends on earlier concepts.

## Teaching strategy

The Teaching Strategist Agent supports pedagogical planning such as:

- lecture design
- active learning
- worked examples
- guided practice
- discussion
- case-based learning
- project-based learning
- problem-based learning
- laboratory integration
- peer learning
- formative assessment
- reflection
- retrieval practice

The appropriate strategy depends on the discipline, outcome, class size, modality, student preparation, and available resources.

## Evidence-informed pedagogy

`TOOLS/evidence_tool.py` supports evidence registration for teaching recommendations.

A recommendation should distinguish among:

- institutional policy
- disciplinary convention
- educational research
- instructor preference
- local experience
- student feedback
- hypothesis requiring evaluation

The system should not present a pedagogical preference as universally proven practice.

## Lesson and module planning

A module plan can include:

```text
module_id
learning_outcomes
preparation
core_concepts
instructional_activity
practice
formative_check
assessment_link
accessibility_notes
estimated_student_time
resources
```

The purpose is to connect each instructional activity to a reason for its inclusion.

## Workload and calendar planning

`TOOLS/calendar_tool.py` supports structured scheduling.

Planning should consider:

- contact hours
- preparation time
- assignments
- projects
- exams
- laboratory work
- reading load
- overlapping deadlines
- holidays
- institutional deadlines
- feedback turnaround

Course workload should be evaluated across the term rather than assignment by assignment.

## Assessment design

Assessment should measure the intended learning as directly and fairly as practical.

Assessment formats can include:

- examinations
- quizzes
- problem sets
- essays
- reports
- oral presentations
- laboratories
- projects
- portfolios
- demonstrations
- design reviews
- code or technical artifacts

The format should match the learning outcome. For example, a design outcome may require evidence beyond multiple-choice recall.

## Formative versus summative assessment

F91 distinguishes assessment used primarily for learning from assessment used primarily for final evaluation.

**Formative assessment** can identify misconceptions and guide improvement while learning is still occurring.

**Summative assessment** contributes to judgments about achievement after a learning period.

A mature course usually provides students opportunities to practice important skills before high-stakes evaluation.

## Rubrics

`TOOLS/rubric_tool.py` supports structured rubric design.

A defensible rubric can include:

```text
criterion
linked_learning_outcome
performance_levels
descriptors
weight
scoring_rule
feedback_guidance
```

Rubrics should avoid criteria unrelated to the intended construct unless those criteria are explicitly part of the learning outcome.

## Assessment validity

The Assessment Reviewer considers whether an assessment supports the interpretation faculty intend to make from it.

Potential validity concerns include:

- content underrepresentation
- irrelevant difficulty
- ambiguous questions
- hidden prerequisite knowledge
- excessive language complexity unrelated to the outcome
- inaccessible format
- scoring inconsistency
- rubric ambiguity
- excessive time pressure unrelated to the construct

An assessment can be difficult without being valid, and easy without being invalid.

## Reliability and consistency

Where grading consistency matters, review can consider:

- clear scoring criteria
- anchor examples
- grader calibration
- moderation
- double marking where appropriate
- handling of borderline cases
- documentation of exceptions

F91 can support these processes but does not issue final grades.

## Grading boundaries

The system must not autonomously:

- assign final course grades
- change grades
- determine pass or fail status
- modify transcripts
- make progression decisions
- make graduation decisions

It may assist with rubric design, draft feedback, consistency checks, or faculty-facing analysis when the instructor retains final authority.

## Grading bias and fairness

Academic quality review should consider whether assessment or grading procedures create unjustified differences.

Potential concerns include:

- inconsistent rubric application
- irrelevant demographic cues
- accessibility barriers
- language requirements unrelated to the outcome
- culturally narrow assumptions
- unequal access to required resources
- inconsistent exceptions

Where feasible, review should focus on observable assessment evidence rather than unsupported assumptions about students.

## Student privacy

Student information can be educationally sensitive.

The Student Support Agent should minimize collection and exposure of:

- names
- student identifiers
- grades
- accommodations
- disability information
- disciplinary information
- personal communications
- attendance records
- advising notes
- financial information

Only information necessary for the legitimate academic task should be used.

F91 should not infer sensitive student characteristics from writing style, behavior, grades, or other indirect signals.

## Student-specific claims

The system should not make unsupported conclusions such as:

- a student is lazy
- a student cheated
- a student has a disability
- a student lacks intelligence
- a student is dangerous
- a student has a mental-health condition

When evidence is incomplete, the workflow should describe observable academic evidence and escalate consequential judgments to qualified humans.

## Academic integrity

Academic-integrity review requires evidence, policy context, due process, and human judgment.

F91 may help organize:

- assignment requirements
- citation expectations
- authorship expectations
- permitted collaboration
- permitted tools
- evidence records
- policy references
- questions requiring faculty review

It must not autonomously declare that a student committed misconduct.

## AI use in coursework

Courses may permit, restrict, or condition the use of generative or agentic systems.

A clear course policy can specify:

- whether AI tools are allowed
- which activities permit them
- disclosure requirements
- citation or acknowledgment expectations
- prohibited uses
- authorship expectations
- privacy considerations
- assessment-specific rules

F91 does not assume that one AI policy is appropriate for every course.

## Authorship and attribution

Teaching materials and student work should preserve appropriate attribution.

Academic quality review can check for:

- missing citations
- unattributed quotations
- unclear authorship
- reused material
- licensed content
- source provenance

The system should never fabricate a citation or claim that a source supports material it has not verified.

## Accessibility

`TOOLS/accessibility_tool.py` provides structured accessibility checks.

Course design should consider, as appropriate:

- document structure
- headings
- alt text
- captions
- transcripts
- keyboard access
- readable contrast
- screen-reader compatibility
- accessible equations
- accessible tables
- timing
- alternative formats
- physical accessibility

Accessibility is a design responsibility, not merely an accommodation added after a barrier appears.

## Accommodation boundaries

F91 may identify that an assessment or activity could create an accessibility barrier, but it does not autonomously decide a student's formal accommodation.

Accommodation decisions remain with authorized institutional processes and qualified personnel.

## Universal design and flexible access

Where appropriate, course design can reduce unnecessary barriers through:

- multiple ways to access material
- clear instructions
- predictable navigation
- accessible digital content
- flexible practice opportunities
- transparent assessment criteria

Flexibility should preserve the essential academic requirements of the course.

## Student support

The Student Support Agent can help structure general academic support such as:

- study guidance
- concept review
- feedback interpretation
- office-hour preparation
- resource navigation
- assignment clarification
- learning strategies

It should not replace professional advising, disability services, counseling, crisis services, disciplinary processes, or other specialized institutional functions.

## Feedback

Useful feedback is connected to evidence and actionable next steps.

A feedback structure can include:

```text
observed_work
linked_criterion
what_is_working
what_needs_improvement
specific_next_step
```

Feedback should avoid personal judgments when the academic evidence only supports comments about the work.

## Office hours and communication

F91 can help organize:

- office-hour topics
- frequently asked questions
- announcement drafts
- assignment clarifications
- response templates
- discussion prompts

External communication remains subject to faculty review when it represents the instructor or institution.

## Course policies

A course package may include policies for:

- attendance
- participation
- late work
- extensions
- collaboration
- academic integrity
- AI use
- accessibility
- communication
- grading
- regrading

Policies should be consistent with institutional requirements and clearly communicated before they are enforced.

## Evidence and provenance

Academic recommendations should preserve the basis for important claims.

Useful provenance can include:

```text
source
source_type
version_or_date
claim_supported
applicability
limitations
review_state
```

Evidence provenance is especially important for policy, accreditation, assessment, and disciplinary contexts.

## Academic quality review

The Academic Quality Agent reviews the complete teaching package for:

- outcome alignment
- content coherence
- assessment validity
- grading fairness
- accessibility
- privacy
- attribution
- workload
- policy consistency
- evidence quality
- faculty-review readiness

This role is intentionally separate from course generation so that quality review is not performed solely by the same reasoning path that produced the material.

## Institutional and accreditation context

Courses may need to satisfy program, departmental, institutional, professional, or accreditation requirements.

F91 can map requirements to course evidence but does not determine formal accreditation compliance or institutional approval.

## Memory and state

The `memory/` and `state/` layers can retain structured workflow information such as:

- course configuration
- learning outcomes
- assessment mappings
- unresolved review items
- faculty decisions
- evidence references

Implementations should avoid retaining unnecessary student-level personal information.

## Observability

The `observability/` layer supports traceability of the multi-agent workflow.

Useful academic telemetry includes:

- outcome mappings
- assessment-alignment findings
- accessibility flags
- privacy flags
- evidence gaps
- academic-integrity escalations
- grading-boundary violations
- faculty-review state

Observability supports audit and debugging. It does not create academic authority.

## Fail-closed governance

Advisory release is blocked when material issues remain unresolved.

Reference blockers include:

- course outcomes incomplete
- course map misaligned
- assessment not aligned to outcomes
- rubric criteria unsupported
- grading-bias risk unresolved
- accessibility review incomplete
- student privacy violation
- unsupported student-specific claim
- academic-integrity finding requested without human process
- attribution or authorship problem
- institutional policy conflict
- evidence provenance missing
- final grading action requested
- student-record modification requested
- accommodation decision requested
- qualified faculty approval missing

The workflow should surface the blocker rather than silently producing a consequential academic decision.

## Human authority boundaries

F91 must not autonomously:

- assign or change final grades
- determine misconduct
- impose discipline
- modify student records
- decide accommodations
- make admissions decisions
- make progression or graduation decisions
- submit student work
- impersonate a student or professor
- send consequential institutional communications without authorization
- fabricate academic evidence or citations
- claim institutional approval

Final academic authority remains with qualified faculty and authorized institutional processes.

## End-to-end reference workflow

A typical F91 workflow follows this sequence:

1. Define the course context, academic level, modality and institutional constraints.
2. Define measurable learning outcomes.
3. Map topics and activities to those outcomes.
4. Select pedagogical strategies appropriate to the outcomes and student context.
5. Design formative and summative assessments.
6. Map each assessment to the outcomes it measures.
7. Build or review transparent rubrics.
8. Review workload and calendar distribution.
9. Review accessibility and student privacy.
10. Review authorship, attribution and AI-use policies.
11. Review academic-integrity boundaries and escalation processes.
12. Review grading fairness and unsupported student-specific claims.
13. Run academic-quality checks across the full course package.
14. Apply fail-closed governance gates.
15. Require qualified faculty approval before consequential release or use.

## Evaluation and held-out governance suite

The repository includes evaluation logic under `evals/` and benchmark material under `benchmarks/`.

Evaluation should test both educational usefulness and governance behavior.

Useful dimensions include:

- course-design coherence
- outcome alignment
- pedagogy appropriateness
- assessment validity
- rubric quality
- accessibility enforcement
- privacy enforcement
- grading-authority boundaries
- academic-integrity boundaries
- authorship and attribution discipline
- evidence provenance
- faculty-approval enforcement

The held-out suite includes scenarios intended to test whether the system refuses to cross academic-authority boundaries even when doing so would appear convenient.

## Failure states

Useful explicit states include:

```text
COURSE OUTCOMES INCOMPLETE
COURSE MAP MISALIGNED
ASSESSMENT ALIGNMENT FAILURE
RUBRIC REVIEW REQUIRED
GRADING BIAS RISK
ACCESSIBILITY GAP
STUDENT PRIVACY VIOLATION
STUDENT-SPECIFIC CLAIM UNSUPPORTED
ACADEMIC INTEGRITY HUMAN REVIEW REQUIRED
AUTHORSHIP OR ATTRIBUTION ISSUE
INSTITUTIONAL POLICY CONFLICT
EVIDENCE PROVENANCE MISSING
FINAL GRADING AUTHORITY PROHIBITED
STUDENT RECORD MODIFICATION PROHIBITED
ACCOMMODATION DECISION PROHIBITED
FACULTY APPROVAL REQUIRED
```

The system should never fabricate student evidence, citations, misconduct findings, accommodations, grades, institutional approval, or faculty review.

## Reproduce the reference implementation

Install development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run the repository checks:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python examples/example.py
python run.py
```

CI under `.github/workflows/ci.yml` validates Python 3.10, 3.11 and 3.12.

## Reproducibility

For a course design or academic review intended to be reproducible, version at minimum:

- course context
- learning outcomes
- course map
- syllabus version
- assessment specifications
- rubric versions
- policy versions
- accessibility review
- evidence sources
- configuration
- evaluation results
- unresolved issues
- faculty decisions

Material course changes should create a new version rather than silently replacing the prior academic record.

## L3 Gold Standard

F91 follows the library's L3 Gold Standard structure through five specialist agents, deterministic academic tools, explicit orchestration and state, safety boundaries, observability, held-out governance evaluation, CI, fail-closed advisory gates, and mandatory qualified faculty review.

This maturity designation describes the repository's engineering and governance structure. It is not institutional accreditation, faculty appointment, legal compliance, formal course approval, or authorization to make consequential student decisions.

## Extending F91

Common extensions include:

- learning-management systems
- syllabus systems
- curriculum maps
- institutional policy repositories
- accessibility checkers
- assessment platforms
- rubric libraries
- citation systems
- calendar systems
- course analytics
- student-support directories
- accreditation evidence systems

New integrations should preserve privacy, access control, evidence provenance, institutional policy, faculty authority, and student rights.

## Example applications

F91 can serve as a reference architecture for:

- university course design
- lecture planning
- graduate seminars
- engineering education
- laboratory courses
- project-based courses
- online and hybrid teaching
- assessment review
- rubric development
- course redesign
- faculty teaching support
- academic-quality review

Each implementation should be adapted to the institution, discipline, academic level, and applicable policies.

## Design principles

1. Start with explicit learning outcomes and course context.
2. Align instruction, practice, assessment, rubrics, and feedback.
3. Use evidence-informed pedagogy without pretending one method fits every course.
4. Design accessibility into the course rather than treating it only as remediation.
5. Protect student privacy and avoid unsupported personal inferences.
6. Treat academic-integrity findings as consequential human decisions.
7. Keep grading and accommodation authority with authorized humans.
8. Preserve authorship, attribution, evidence, and policy provenance.
9. Use independent academic-quality review before consequential release.
10. Keep final teaching and academic authority with qualified faculty and institutional processes.

## Documentation

Additional architecture documentation is available under `docs/`, including `docs/ARCHITECTURE.md`.

## Citation and reuse

Use the repository metadata and citation information supplied by the project when referencing this implementation. The repository can be studied, cited, adapted, and extended subject to its license terms.

## Responsible use

Use F91 as a professor-assistance and academic-governance reference architecture. Validate teaching materials, assessments, accessibility, academic-integrity processes, student-support practices, and institutional requirements against the actual course and university context. Final academic decisions remain with appropriately qualified and authorized humans.