# Day 3 Task – ReAct Agent, Tools, and Failure Handling

## 1. Introduction

In this task, I worked with an LLM-based agent and learned how an AI model can use external tools instead of depending only on the information it already has.

I built a simple ReAct-style agent where the model can look at a question, decide whether it needs a tool, call that tool, receive the result, and then give the final answer.

I used two tools in this task:

1. `calculator` – used to perform basic arithmetic calculations.
2. `read_webpage` – used to read information from a web page or a local HTML/text file.

I also tested a few situations where the agent could fail, and then created a fixed version with some basic safety checks.

---

## 2. Project Files

The main files I worked with are:

- `my_tools.py` – contains the calculator and webpage reader tools.
- `my_agent.py` – contains the basic agent.
- `my_agent_fixed.py` – contains the improved version with failure handling.
- `notice.html` – a local HTML file used to test the webpage reader.
- `no_tool.py` – used for the no-tool comparison.
- `tool_agent.py` – used for the tool-enabled comparison.
- `fees.txt` and `course_tool.py` – used for the course-fee example.
- `screenshots/` – contains screenshots of the different outputs.

---

## 3. Tools Used

### 3.1 Calculator Tool

The `calculator` tool takes an arithmetic expression and returns the result.

I tested expressions such as:

```text
(12000 + 18000) * 0.9
2 ** 10
```

I also tested an invalid input:

```text
import os
```

For example:

```text
(12000 + 18000) * 0.9
```

gives:

```text
27000.0
```

One important thing I used here was Python's `ast` module instead of directly using `eval()`.

This means the calculator only allows the arithmetic operations that I have defined. It does not simply execute any Python code given to it. This makes the calculator safer.

If the input is invalid, the tool returns an error message instead of stopping the whole program.

---

### 3.2 Webpage Reader Tool

The `read_webpage` tool can read:

- a web URL, such as `https://example.com`
- a local file, such as `notice.html`

For the local test, I created `notice.html` with some course-fee information.

The tool removes HTML tags and also removes script and style content, so the model receives mainly the useful text from the page.

I also added a `max_chars` limit. This is useful because a web page can contain a lot of text, and sending everything to the model would unnecessarily increase the context size.

If the file does not exist or the web request fails, the tool returns an error message as text instead of crashing the program.

---

## 4. How the ReAct Agent Works

The basic agent in `my_agent.py` follows a simple flow:

```text
User Question
      |
      v
     LLM
      |
      | Does it need a tool?
      v
  Tool Call
      |
      v
    Tool
      |
      v
 Tool Result
      |
      v
     LLM
      |
      v
 Final Answer
```

For example, if I ask the agent to calculate something, it can choose the calculator tool.

If I ask it to find information from the local HTML file, it can choose the webpage reader.

After the tool runs, its result is sent back to the model. The model can then use that result to prepare the final answer.

So, instead of only generating an answer, the agent has the ability to take an action in between the question and the final answer.

---

## 5. Tool Schema

For the model to use a tool, it needs to know what the tool does and what information the tool expects.

The tool schema contains things such as:

- tool name
- description
- parameters
- parameter types
- required parameters

For example, the calculator description tells the model that it is meant for arithmetic calculations.

The webpage reader description tells the model that it can read a web page or a local HTML/text file.

This information is important because the model needs to understand the purpose of a tool before it can decide whether the tool is useful for a particular question.

---

## 6. Testing the Local Webpage

I created a local file called `notice.html` for testing the webpage reader.

It contains course-fee information for:

- CS101 – Programming Fundamentals
- AI202 – Machine Learning
- DS303 – Data Engineering

The HTML file also contains a script section.

When the webpage reader processes the file, it extracts the readable content and removes the HTML, script, and style parts.

This was useful for testing because I could clearly see whether the tool was returning the actual page information instead of returning the raw HTML code.

---

## 7. No-Tool and Tool-Enabled Comparison

I also created two small programs:

- `no_tool.py`
- `tool_agent.py`

### No-tool run

In `no_tool.py`, the question is sent directly to the LLM.

The model does not have access to the external course-fee file or the course-fee function.

So, the model has to answer using the information available to it.

This shows the difference between simply asking an LLM a question and giving it access to an external source.

### Tool-enabled run

In `tool_agent.py`, the model is given access to the course-fee tool.

When the question needs the information from the file, the model can request the tool.

The tool reads the file and returns the information. That result is then given back to the model, which uses it to produce the final answer.

I captured screenshots of both runs to compare the outputs.

---

## 8. Failure Experiment 1 – Repeated Tool Calls

The first failure I looked at was repeated tool calling.

If an agent keeps going through the tool-use cycle without a proper stopping condition, it may continue making tool calls instead of giving a final answer.

This can cause:

- unnecessary API calls
- more token usage
- longer execution time
- the agent getting stuck without producing a final answer

To avoid this, the fixed version uses limits on how many times the agent can continue the loop.

This gives the agent a clear stopping point.

---

## 9. Failure Experiment 2 – Invalid or Hallucinated Tool

The second failure is when the model tries to call a tool that does not actually exist.

For example, the model might generate the name of a tool that is not present in the program.

The program should not try to execute every tool name it receives.

Instead, it should first check whether the requested tool exists in the tool registry.

If it does not exist, the program can return a clear error message instead of crashing.

This is a simple but important check when building tool-using agents.

---

## 10. Failure Experiment 3 – Context Overflow

The third problem I looked at was context growth.

An agent keeps information from the conversation and tool results in its message history. If very large results are repeatedly added, the context can become too large.

This can cause:

- higher token usage
- slower responses
- context-limit errors
- less reliable responses

The webpage reader already helps with this by limiting its output using `max_chars`.

Keeping the tool output reasonably small is important because the model usually does not need an entire large web page when only a small part of it is relevant.

---

## 11. Error Handling

One thing I noticed while building the tools is that errors should be handled properly.

Instead of allowing an exception to completely stop the program, the tool returns the error as text.

For example:

```text
Calculator error: ...
```

or:

```text
Read error: ...
```

This is useful because the error becomes part of the normal tool result.

The LLM can then see that something went wrong and decide what to do next.

If the Python program simply crashed, the model would not get the error information and the agent would stop unexpectedly.

---

## 12. Fixed Agent

After testing the failure cases, I worked with `my_agent_fixed.py`, which is the safer version of the agent.

The main improvements are:

- limiting repeated agent iterations
- checking whether a requested tool actually exists
- handling tool errors without crashing
- limiting the amount of webpage content returned
- avoiding unnecessary growth of the conversation history

The purpose of the fixed version is not to make the program unnecessarily complicated.

The main goal is to make the agent behave in a more controlled and predictable way.

---

## 13. Observations

From the testing, I observed that the calculator works correctly for the supported arithmetic expressions.

For an invalid expression, it gives an error message instead of executing arbitrary code or stopping the program.

The webpage reader was able to read the local HTML file and return its readable content. It also handled a missing file by returning an error message.

The basic agent showed how the model can decide to use a tool when a question needs a calculation or information from an external source.

The failure tests also showed that giving tools to an LLM is not enough by itself. The agent also needs some basic controls to handle unexpected situations.

The main problems I observed were:

- repeated tool calls
- invalid tool names
- too much information being added to the context

The fixed version adds checks to handle these situations better.

---

## 14. Why Tool Errors Should Be Returned as Text

I think returning tool errors as text is a better approach for an agent.

For example:

```text
Read error: 'no_such_file.html' is not a URL and no such file exists.
```

The model can understand this message and respond accordingly.

If the tool instead raises an exception that completely stops the Python program, the agent will not get a chance to handle the problem.

By returning the error as text, the tool and the LLM can continue communicating through the same tool-result flow.

---

## 15. ReAct Flow in Simple Terms

The complete process can be understood in these steps:

```text
1. User asks a question
2. LLM looks at the question
3. LLM decides whether a tool is needed
4. LLM creates a tool call
5. Program checks the tool call
6. Tool runs
7. Tool returns a result or an error
8. Result is sent back to the LLM
9. LLM uses the result
10. Agent gives the final answer
```

The main difference between a normal chatbot and this type of agent is that the agent can perform an action using a tool before giving the final answer.

---

## 16. Conclusion

Through this task, I understood the basic working of an agentic AI system better.

A normal LLM can generate answers from the information available to it, but it cannot automatically perform every external operation. By giving it tools, we can allow it to perform calculations or access information from outside the model.

The calculator tool showed how the model can use a separate function for arithmetic. The webpage reader showed how the model can get information from a local file or web page.

I also learned that tool use alone is not enough. An agent should have basic safety and error-handling mechanisms. Limiting repeated calls, checking tool names, handling errors, and controlling context size can make the agent more reliable.

Overall, this task helped me understand the basic idea behind tool-using agents: **the LLM decides what action is needed, the tool performs that action, and the LLM uses the result to give the final response.**
