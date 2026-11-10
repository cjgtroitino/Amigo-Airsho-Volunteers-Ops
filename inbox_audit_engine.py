"""
Amigo Airsho 2026: Automated Inbox Audit & Roster Reconciliation Script
Parses inbound emails from student organizations, validates RSVP status,
detects schedule conflicts, and reconciles headcount for the Oct 8 meeting.
"""
import re
from typing import Dict, List, Any

# Primary RSVP targets and regex heuristics
CONFIRMATION_KEYWORDS = [
    r"\bwill attend\b", r"\bwill be attending\b", r"\bplan to attend\b",
    r"\bi can make it\b", r"\bwe will be there\b", r"\bverify my attendance\b",
    r"\battend informational meeting\b"
]

DECLINE_KEYWORDS = [
    r"\bwon'?t be able to attend\b", r"\bnot able to attend\b", r"\bunable to attend\b",
    r"\binterfere with\b", r"\bout of town\b", r"\bcannot attend\b"
]

ROSTER_DIRECTORY = {
    "Natalie Nguyen": "UTEP Student Society of Health-System Pharmacists",
    "Miranda Lujan": "American Institute of Aeronautics and Astronautics (AIAA)",
    "Sofia I. Oaxaca": "Texas Society of Professional Engineers (TSPE)",
    "Jose Emilio Piñon": "UTEP School of Pharmacy Executive Team",
    "Finley E. Villegas": "Criminal Justice and Security Studies"
}

def analyze_email_intent(sender: str, body: str) -> Dict[str, Any]:
    text = body.lower()
    
    confirmed = any(re.search(pattern, text) for pattern in CONFIRMATION_KEYWORDS)
    declined = any(re.search(pattern, text) for pattern in DECLINE_KEYWORDS)
    
    # Check for quota queries (e.g., ICAS survey team 4-spot limit)
    quota_inquiry = bool(re.search(r"\b4 spots\b|\bonly 4\b|\bspots open\b", text))
    
    # Check for citizenship inquiries
    citizenship_inquiry = bool(re.search(r"\bcitizen\b|\bcitizenship\b|\bu\.?s\.? citizen\b", text))
    
    # Check for custom hours
    shift_split = bool(re.search(r"\b\d{1,2}\s*(am|pm)?\s*to\s*\d{1,2}\s*(am|pm)\b", text))
    
    status = "AMBIGUOUS"
    if confirmed and not declined:
        status = "CONFIRMED_PRIMARY"
    elif declined:
        status = "REQUIRES_FAILOVER_ROUTING"
        
    return {
        "sender": sender,
        "status": status,
        "quota_inquiry": quota_inquiry,
        "citizenship_inquiry": citizenship_inquiry,
        "shift_split": shift_split
    }

def generate_reconciliation_report(inbound_emails: List[Dict[str, str]]) -> Dict[str, Any]:
    confirmed_attendees = []
    failover_required = []
    
    for email in inbound_emails:
        analysis = analyze_email_intent(email["sender"], email["body"])
        if analysis["status"] == "CONFIRMED_PRIMARY":
            confirmed_attendees.append(analysis["sender"])
        elif analysis["status"] == "REQUIRES_FAILOVER_ROUTING":
            failover_required.append(analysis["sender"])
            
    return {
        "meeting": "October 8th, 2026 @ 5:30 PM - The Elmont Event Center",
        "confirmed_count": len(confirmed_attendees),
        "confirmed_list": confirmed_attendees,
        "failover_routing_queue": failover_required
    }
