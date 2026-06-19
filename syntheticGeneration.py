import os
import json
import time
import random
import pandas as pd
from openai import OpenAI

# Initialize the client (Requires an OPENAI_API_KEY environment variable)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ==========================================
# 1. Configurable Variables
# ==========================================

# Added "Ticket Subject" to the required output schema
OUTPUT_FIELDS = [
    "Ticket Type", 
    "Ticket Subject",
    "Ticket Description", 
    "Resolution", 
    "Ticket Priority", 
    "Minutes to resolve"
]

# Changed from a list to a dictionary to establish parent-child relationships
TICKET_HIERARCHY = {
    "Appointment Scheduling": [
        "Double Booking Error", "Cannot Cancel Appointment", "Sync Issue with Google Calendar", "Walk-in Integration Error"
    ],
    "Billing and Invoicing": [
        "Payment Gateway Failure", "Incorrect Tax Calculation", "Refund Processing Error", "Insurance Claim Reject"
    ],
    "Medical Records/Notes": [
        "Cannot Upload Lab Results", "Consultation Notes Not Saving", "Vaccination History Missing", "Merge Duplicate Pet Profiles"
    ],
    "Client Communication (Email/SMS)": [
        "SMS Reminders Not Sending", "Email Template Formatting Broken", "Opt-out Sync Issue", "Bulk Campaign Failed"
    ],
    "Login and Access": [
        "2FA Not Working", "Password Reset Loop", "Role-Based Access Denied", "Session Timeout Too Fast"
    ],
    "System Integration (Labs/Hardware)": [
        "Idexx Lab Integration Down", "Barcode Scanner Not Reading", "X-Ray Image Upload Failed", "Receipt Printer Disconnected"
    ]
}

# Priority tiers
PRIORITIES = ["Low", "Medium", "High", "Critical"]

# Complexity tiers to drive logical resolution times
COMPLEXITIES = ["Easy", "Medium", "Hard"]

# Generation parameters
TARGET_TOTAL_ROWS = 3500
ROWS_PER_BATCH = 20 
BATCHES = TARGET_TOTAL_ROWS // ROWS_PER_BATCH

# ==========================================
# 2. Generation Loop
# ==========================================

all_tickets = []

print(f"Starting generation of {TARGET_TOTAL_ROWS} synthetic VetTrack tickets...")

for i in range(BATCHES):
    # Randomly select a parent type, then randomly select one of its specific subjects
    batch_type = random.choice(list(TICKET_HIERARCHY.keys()))
    batch_subject = random.choice(TICKET_HIERARCHY[batch_type])
    
    batch_priority = random.choice(PRIORITIES)
    batch_complexity = random.choice(COMPLEXITIES)
    
    # System prompt defines the persona and the strict output rules
    system_prompt = f"""
    You are a data generation engine for VetTrack, a SaaS CRM used by veterinary clinics.
    VetTrack handles appointment scheduling, billing, pet medical records, and client communications.
    
    Your task is to generate highly realistic, domain-specific IT helpdesk tickets.
    
    CRITICAL RULES:
    1. Output valid JSON containing a single key "tickets", which holds a list of {ROWS_PER_BATCH} objects.
    2. Each object MUST contain EXACTLY these keys: {OUTPUT_FIELDS}.
    3. The 'Ticket Description' should be written from the perspective of a vet or clinic staff member. Keep it concise but plausible (2-4 sentences). It MUST align perfectly with the Ticket Subject.
    4. The 'Resolution' should be written by the IT helpdesk. It must be dense, logical, and clearly solve the specific Ticket Subject.
    5. The 'Minutes to resolve' must be an integer that logically aligns with the complexity of the issue.
    """
    
    # User prompt enforces the randomized constraints and the new sub-type for this specific loop
    user_prompt = f"""
    Generate {ROWS_PER_BATCH} tickets for this batch.
    
    Focus this batch heavily (but not exclusively) on:
    - Ticket Type: {batch_type}
    - Ticket Subject: {batch_subject}
    - Priority Level: {batch_priority}
    - Complexity: {batch_complexity}
    
    Logic Check: Ensure the description and resolution make sense for the highly specific Ticket Subject ({batch_subject}).
    Logic Check: If the complexity is '{batch_complexity}', ensure the 'Minutes to resolve' reflects that accurately. 
    Easy issues should take 5-15 minutes. Medium 15-60 minutes. Hard issues might take hours or days (represented in total minutes).
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini", 
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7 
        )
        
        # Parse the JSON response
        batch_data = json.loads(response.choices[0].message.content)
        all_tickets.extend(batch_data['tickets'])
        
        print(f"Batch {i+1}/{BATCHES} complete. Generated {len(all_tickets)} total rows.")
        
    except Exception as e:
        print(f"Error on batch {i+1}: {e}")
        # If the API fails, sleep and retry to avoid crashing the whole script
        time.sleep(5)
        
# ==========================================
# 3. Export to CSV
# ==========================================

df = pd.DataFrame(all_tickets)

# Ensure the DataFrame only contains the requested fields
df = df[OUTPUT_FIELDS]

file_name = "vettrack_synthetic_tickets_with_subjects.csv"
df.to_csv(file_name, index=False)

print(f"\nSuccess! Saved {len(df)} records to {file_name}.")