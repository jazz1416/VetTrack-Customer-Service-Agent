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
- LLM based Architecture
- Synthetic Data Generation from LLM Pipeline
- LLM as a Judge Evaluation
- ROI Analysis

## Project Structure (To be updated)
VetTrack-Customer-Service-Agent/
│
|── 01_DataEngineering.ipynb     # Data preparation/cleaning and EDA
├── README.md                       # Project documentation
```

## Dataset Overview
Original: Sourced from Kaggle: Customer Support Tickets Dataset (200k+ Records)

Final: Synthetically Generated (~2,700 closed cases) Modeled after VetTrack background

We decided on a synthetically generated dataset opposed to the orignal dataset with over 200,000 records, because the original dataset lacked the proper data to train and evaluate our agent. 

This dataset contains 18 features and 2769 rows when only evaluating closed cases. Features include information about the customer that submitted the ticket as well as classifications and resolutions for the ticket regarding subject, status and priority. A column included is named "Product_Purchased" which will be disregarded in our model but appears due to our synthetic creation being based off of a Kaggle dataset named Customer Support Ticket Dataset. 

## Agent Architecture
The agent uses DSPy architecture with two main signatures:

VetTrack Classifer : This takes a ticket and determines if it is relevant to VetTrack or not, then assigns a priority level to the ticket.

VetTrack Resolver : This takes the subject and classification of the ticket and tries to find relevant information in the knowledge database. 


## Models Tested
- Mistral 7B our baseline model
- Llama 3.1 our testing/comparison model

## Evaluation Approach
An LLM as a judge approach was used to score the agents responses on: relevance, accuracy and professionalism. 

## Challenges
Our dataset quality was a challenge we overcame. All customer support ticket datasets had insufficent data to train and evaluate a model on, requiring the team to proceed with synthetic data. This synthic data can produce unrealistic patterns making the agent bias. 
