# ✈️ Amigo Airsho 2026: Volunteer Operations Architecture

An end-to-end engineering, logistics, and data architecture built to manage a workforce of **500+ credentialed volunteers** during the 2026 Amigo Airsho at Biggs Army Airfield (Fort Bliss, TX). 

This project bridges systems engineering and live aviation operations, detailing how an automated Python/Google Workspace data pipeline processed intake for over 1,000+ organizations and successfully sustained dynamic flight-line logistics for a massive 100,000-person public event.

---

## 📊 Quantifiable Mission Impact
* **Event Scale:** ~100,000 spectators across a 2-day live-fire and aerial demonstration schedule.
* **Workforce Deployed:** **500+** waiver-compliant, credentialed volunteers deployed across Flightline Ops, ICAS Survey, Static Displays, and Ticketing.
* **Hours Logged:** Volunteers delivered **over 2,109 recorded hours** across **237 approved shift records**, averaging 11.6 hours contributed per volunteer. 
* **Critical Coverage:** Crossing Guards and Gate Check-In volunteers carried significant portions of the workload, ensuring safe pedestrian flow amidst a crowd of 100,000 attendees.
* **Partner Group Impact:** Nearly 50% of the total volunteer hours were supplied by strategic partner groups (e.g., SOAC, El Dorado HS Orchestra, Aztec Robotics), proving the efficacy of the automated organizational outreach engine.
* **Automation Gains:** 95% reduction in outreach latency, complete elimination of paper waiver liability (0.0% failure rate), and a 77% reduction in scheduling attrition via a 3-tier routing engine.
* **Safety & Security:** Zero security gate rejections and 100% compliant execution of Fort Bliss Base Pass and Flightline Driver operations.

---

## 🏗️ Technical Stack & Pipeline

The infrastructure replaced legacy manual spreadsheets with an automated, policy-enforced ingestion pipeline:

1. **Inbound Regex Parser (`scripts/inbox_audit_engine.py`):** An automated Python execution script that monitored thread responses from 1,000+ UTEP clubs and student societies. It analyzed intent, validated RSVP status, detected schedule constraints (e.g., split shifts), and resolved micro-quota caps (e.g., ICAS survey limits).
2. **3-Tier Routing Logic:** A multi-layered scheduling algorithm designed to minimize student attrition by catching conflicts and automatically rerouting groups to secondary (Oct 12) or tertiary (Oct 19) failover onboarding dates.
3. **Master Database Sync (`scripts/Code.gs`):** A Google Apps Script integration that extracted data from the Galaxy Digital API (mandating 100% digital waivers) and bidirectionally synced verified volunteers into the `MSSGAA Master` Google Sheet.

---

## 🚁 Live Field Execution & Zone Allocations

Field execution required integrating digital rosters with physical access-control checkpoints during strict military performance airspace windows (Blue Angels, F-22 Raptor, Golden Knights). 

* **Checkpoint Alpha (Installation Gate):** Real-ID and Fort Bliss Online Pass verification.
* **Checkpoint Bravo (Staging HQ):** Master Roster lookup, Galaxy Digital waiver validation, and credential issuance (Zone Wristbands & High-Vis Vests).
* **Checkpoint Charlie (Dispatch):** Flightline driver verification and radio protocol handoffs prior to active deployment onto active taxiways and static ramp perimeters.
* **Dynamic Surge Routing:** During active 30-minute flightline freezes, unassigned volunteers were aggregated in an on-deck reserve pool and deployed algorithmically to relieve morning shifts.

---

## 📁 Repository Map
* `scripts/`: Python regex engines and Google Workspace JS sync codes.
* `data_schemas/`: JSON payload models and SQL table architecture for the Master Database.
* `config/`: System YAML dictating event quotas, constraints, and locations.
* `assets/`: Operational proof-of-work (flightline photos, drive infrastructure screenshots, credential templates).
