# VetTrack-Customer-Service-Agent

## Project Introduction
Our project objective was to create an automated customer support agent for VetTrack's veterinary CRM platform, built to classify, prioritize, respond, and escalate support tickets. As veterinary teams handle high volume of support tickets, this agent reduces resolution time by classifying incoming tickets, suggesting responses, and escalating to human intervention when needed.

## Team
- Evelin Bustamante 
- Jasmine Duong 
- Daniel Sims
  
We shared the roles of project manager, Data Engineer, and AI Engineer

## Why an Agent
Multi-step Reasoning: Unlike a traditional model or simple lookup functions, this tasks has multiple decisions in sequence. The agent must be able to classify an input, search for similar past tickets, evaluate a response, deem necessity for human intervention, and then produce a response.  Each step relys on the previous decision, this is what defines the need for an agent. 

Support Tickets are Natural Language: The customer support tickets are coming through in natural language. It is impossible to train a model on every possible outcome, which is the second reason why an agent is necessary. 

Determination Factor: The escalation decision has a deterministic function in place, deeming if human intervention is necessary for the proper response. This factor needs reasoning over context. 

## Methods Used
- Vector Search
- LLM Based Architecture
- Synthetic Data Generation from LLM Pipeline
- LLM as a Judge Evaluation
- ROI Analysis

## Project Structure
```
VetTrack-Customer-Service-Agent/
│
├── 01_DataEngineering.ipynb     # Data preparation/cleaning and EDA
├── README.md                       # Project documentation
├── VetTrack Golden Evals.PNG       # Screenshot of traces from Databricks
├── agentJudgeEval.ipynb      # Agent and judge creation and testing
├── golden_evaluation_results.json    # JSON file of traces
├── syntheticGeneration.py         # Code for the creation of the synthetic dataset
├── synthetic_customer_support_tickets.csv  # Synthetic dataset created
│
```

## Dataset Overview
Original: Sourced from Kaggle: Customer Support Tickets Dataset (200k+ Records)

Final: Synthetically Generated (~2,700 closed cases) Modeled after VetTrack background

We decided on a synthetically generated dataset opposed to the orignal dataset with over 200,000 records, because the original dataset lacked the proper data to train and evaluate our agent. The creation of this dataset can be found in the Generation-Code branch. 

This dataset contains 18 features and 2769 rows when only evaluating closed cases. Features include information about the customer that submitted the ticket as well as classifications and resolutions for the ticket regarding subject, status and priority. A column included is named "Product_Purchased" which will be disregarded in our model but appears due to our synthetic creation being based off of a Kaggle dataset named Customer Support Ticket Dataset. 

## Agent Architecture
The agent uses DSPy architecture with 5 tools we created:

VetTrack Classifer : This takes a ticket and determines if it is relevant to VetTrack or not, then assigns a priority level to the ticket.

VetTrack Resolver : This takes the subject and classification of the ticket and tries to find relevant information in the knowledge database. 

VetTrack Summarizer: This takes in the ticket subject, ticket description, and resolution and outputs a one sentence summary of both when a ticket is escalated or null if the ticket was not escalated.

VetTrack Confidence Score: This takes in the ticket subject, ticket description, and resolution and outputs a confidence score describing how confident the agent is in its resolution. 

VetTrack Escalation Reason: This takes in the ticket subject, ticket description, and resolution and outputs a description for why a ticket was escalated if it was, and null otherwise. 

## Models Tested
- Llama-3.3-70B our baseline model
- Qwen3-Next-80B-A3B-Instruct our testing/comparison model

## Evaluation Approach
An LLM as a judge approach was used to score the agents responses on: relevance, accuracy and professionalism. 

## Model Comparison
Our two models performed pretty similar to each other, llama-70b scoring a 5.0 on average versus qwen3-80b scoring a 4.8, likely do to llama-70b producing more direct answers. The gap in performance on evaluating a smaller dataset is very small and can be ignored in this case, but should be evaluated on a larger scale in the future. 

## Challenges
Our dataset quality was a challenge we overcame. All customer support ticket datasets had insufficent data to train and evaluate a model on, requiring the team to proceed with synthetic data. This synthic data can produce unrealistic patterns making the agent bias. 

## Contributions
- Evelin completed the EDA, generated and evaluated the comparison our two models, and aided in the completion of the README.
- Jasmine created and managed the GitHub Repository, completed the data preparation, helped create tools for the agent, and aided in the compeltion of the README.
- Daniel created the synthetic dataset, and wrote the initial code to create the agent, judge, and evaluation queries.
