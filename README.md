# VetTrack-Customer-Service-Agent

## Project Introduction
Our project objective was to create an automated customer support agent for VetTrack's veterinary CRM platform,built to classify, prioritize, respond, and escalate support tickets. As veterinary teams handle high volume of support tickets, this agent reduces resolution time by classifying incoming tickets, suggesting responses, and escalating to human intervention when needed.

## Team
- Evelin Bustamante 
- Jasmine Duong 
- Daniel Sims 
We shared the roles of project manager, Data Engineer, and AI Engineer

## Why an Agent
Multi-step Reasoning: Unlike a traditional model or simple lookup functions, this tasks has multiple decisions in sequence. The agent must be able to classify an input, search for similar past tickets, evaluate a response, deem necessary for human intervention, and then produce a response.  Each step relys on the previous decision, this is what defines the necessity for an agent. 
Support Tickets are Natural Language: The customer support tickets are coming through in natural language. It is impossible to train a model on every possible outcome, which is the second reason why an agent is necessary. 
Determination Factor: The escalation decision has a deterministic function in place, deeming if human intervention is necessary for the proper response. This factor needs reasoning over context. 

## Methods Used
- Vector Search
- LLM based Architecture
- Synthetic Data Generation from LLM Pipeline
- LLM as a Judge Evaluation
- ROI Analysis

## Project Structure
(TO BE UPDATED)

## Dataset
Original: Sourced from Kaggle: Customer Support Tickets Dataset (200k+ Records)
Final: Synthetically Generated (~2,700 closed cases) Modeled after VetTrack background

We decided on a synthetically generated dataset opposed to the orignal dataset with over 200,000 records, because the original dataset lacked the proper data to train and evaluate our agent. 

## Agent Architecture
The agent uses DSPy architecture with the following tools:

Search_similar_instructions : semantic search over the knowledge database to find similar past tickets
summarize : summarizes a ticket description 
classify : classifies the tickets into ticket type categories
escalate : flags a ticket for human intervention when a topic is too complex
ticket_id_lookup : simple function to retrieve a ticket based on the ID


## Models Tested
- Mistral 7B our baseline model
- Llama 3.1 our testing/comparison model

## Evaluation Approach
(TO BE UPDATED)

## Challenges
Our dataset quality was a challenge we overcame. All Customer Support Ticket datasets had insufficent data to train and evaluate a model on, requiring the team to proceed with synthetic data. This synthic data can produce unrealistic patterns making the agent bias. 
