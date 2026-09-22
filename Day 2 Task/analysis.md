# Day 2 Task – Reasoning and Acting: Comparing Direct Prompting, Chain-of-Thought, and ReAct

## Scenario

College course-fee comparison scenario.

## 3.1 Explanation of Each Approach

### Direct Prompting

Explains:

- what it does
- no tool access
- limitations in the course-fee scenario

### Chain-of-Thought Prompting

Explains:

- multi-step reasoning
- limitations without external tools
- your actual CoT experiment results

### ReAct Agent

Explains:

- Thought → Action → Observation
- actual course-fee tool calls
- actual calculator calls
- final ₹6,750 difference

## 3.2 Comparison Table

| Basis                  | Direct | CoT    | ReAct  |
| ---------------------- | ------ | ------ | ------ |
| Reasoning depth        | Low    | Higher | Higher |
| Tool usage             | No     | No     | Yes    |
| Multi-step reliability | ...    | ...    | ...    |
| Transparency           | ...    | ...    | ...    |
| Speed / cost           | ...    | ...    | ...    |
| Consistency            | ...    | ...    | ...    |

## 3.3 Self-Consistency Observation

Uses your actual results:

- Temperature 0.8
- 5 runs
- 9562.5 results
- formatting variation in one run
- Temperature 0 → 5/5 same result

## 3.4 Suitability Analysis

Explains why ReAct fits the selected scenario because it requires:

- external information
- multi-step calculation
- tool usage

## 3.5 Conclusion

Explains when:

- Direct Prompting is appropriate
- CoT is appropriate
- ReAct is appropriate
