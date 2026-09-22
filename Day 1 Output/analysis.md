# Day 1 - Chatbot vs Rule-Based Workflow vs AI Agent

## 1. Scenario

I used a simple **college course fee assistant** as my private-data scenario.

The system has the following course fees:

| Course |     Fee |
| ------ | ------: |
| CS101  | ₹12,000 |
| AI202  | ₹18,000 |
| DS303  | ₹15,000 |

Example questions are:

- What is the fee for AI202?
- What is the total fee for CS101 and AI202 after a 10% scholarship?
- I can pay ₹30,000. Which two courses can I take together?

The aim is to solve these questions using a plain chatbot, a rule-based workflow and an AI agent.

---

## 2. Plain Chatbot

A plain chatbot mainly uses an **LLM (Large Language Model)** to understand the user's question and generate a response.

In my implementation, the chatbot does not directly call the course-fee tools. It mainly depends on the model's response.

This approach is simple and works well for normal conversations. However, it is not ideal when the answer depends on private or external data because the chatbot does not have direct access to the course-fee data through a tool.

So, for this scenario, the chatbot is useful for simple questions but has limitations when accurate private data is required.

---

## 3. Rule-Based Workflow

The rule-based workflow follows **predefined steps and conditions** written by the programmer. It does not use an LLM to decide what to do.

In my implementation, the workflow can call `get_course_fee()` for the required courses and process the returned values according to its programmed logic.

The main advantage is that the output is predictable because the same rules are followed every time.

The limitation is flexibility. If the user asks a question that was not considered while writing the rules, the workflow may not know how to handle it.

For example, in my challenge, the workflow could retrieve all three course fees but returned:

> "Sorry, I can only answer questions about course fees."

This shows that it can follow predefined operations but cannot automatically change its approach for a new type of task.

---

## 4. AI Agent

An AI agent combines **LLM + Tools + Loop**.

The LLM first understands the user's request and decides which tool is needed. The selected tool is executed, its result is returned to the agent, and the agent can continue with another tool call.

My agent has two tools:

- `get_course_fee()` - retrieves the fee of a course.
- `calculator()` - performs arithmetic operations.

For example, for the ₹30,000 budget question, the agent retrieved the fees of all three courses and compared the possible combinations.

The result was:

- CS101 + AI202 = ₹30,000
- CS101 + DS303 = ₹27,000
- AI202 + DS303 = ₹33,000

This shows the **multi-step tool-calling** capability of an AI agent.

The main limitation is that the agent depends on the LLM correctly selecting and calling the available tools.

---

## 5. Comparison

| Basis                   | Plain Chatbot                             | Rule-Based Workflow                        | AI Agent                                        |
| ----------------------- | ----------------------------------------- | ------------------------------------------ | ----------------------------------------------- |
| **Flexibility**         | Good for normal conversation              | Limited to programmed rules                | High; can adapt steps based on the task         |
| **Decision-making**     | Mainly generates an LLM response          | Decisions are predefined                   | LLM decides which tool/action is needed         |
| **Tool usage**          | No direct tool usage in my implementation | Uses predefined functions                  | Dynamically selects and uses tools              |
| **Private-data access** | No direct access                          | Accesses data through programmed functions | Accesses data through tools                     |
| **Multi-step tasks**    | Limited                                   | Possible if already programmed             | Can perform multiple tool calls in a loop       |
| **Automation**          | Mainly response generation                | Good for fixed processes                   | Good for dynamic multi-step tasks               |
| **Reliability**         | Depends on the generated response         | Predictable when rules are correct         | Depends on correct tool selection and execution |

---

## 6. Suitability Analysis

For my course-fee scenario, the **AI agent approach fits the multi-step questions well** because it can use different tools and continue working based on their results.

The rule-based workflow is useful when the process is fixed and the required steps are already known. It gives predictable results but needs new rules when the type of question changes.

The plain chatbot is useful for simple conversational questions, but it is less suitable when the answer requires reliable access to private course data.

This comparison helped me understand that an AI agent is not just an LLM generating text. It can connect the LLM with **tools, external data and an execution loop** to complete a task.

---

## 7. Conclusion

This task helped me understand the practical difference between the three approaches.

A **chatbot** mainly generates responses using an LLM.

A **rule-based workflow** follows predefined logic written by the programmer.

An **AI agent** combines an LLM with tools and a loop to decide what actions are needed and continue until the task is completed.

As a Mechanical Engineering student learning software development, this exercise helped me understand how programming concepts such as **functions, conditions, loops and APIs** can be combined with AI to build useful applications.

In general, a chatbot is suitable for simple conversations, a rule-based workflow is suitable for fixed processes, and an AI agent is useful for tasks that require **flexible decision-making, tool usage and multiple steps**.
