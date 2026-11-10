# ✈️ Amigo Airsho 2026: Volunteer Operations Architecture

An end-to-end engineering, logistics, and data architecture built to manage a workforce of **500+ credentialed volunteers** during the 2026 Amigo Airsho at Biggs Army Airfield (Fort Bliss, TX). 

This project bridges systems engineering and live aviation operations, detailing how an automated Python/Google Workspace data pipeline processed intake for over 1,000+ organizations and successfully sustained dynamic flight-line logistics for a massive 100,000-person public event.

---

## 📊 Quantifiable Mission Impact & Operational Headcount

* **Event Scale:** ~100,000 spectators across a 2-day live-fire and aerial demonstration schedule at Biggs Army Airfield.
* **Estimated Ground Deployment:** **500+ total field volunteers** deployed across 31 operational roles, including high-density crossing guards, flightline crowd separation, and static ramp security.
* **Digitally Verified Telemetry:**
  * **2,108.7 logged hours** across **237 approved shift records** captured through the digital volunteer portal.
  * **182 uniquely audited volunteers** averaging 11.6 hours each.
  * **Peak Staffing:** Saturday, Oct 24 alone accounted for 1,321.7 hours (62.7% of total weekend hours).
* **Field Telemetry vs. Ground Reality (Systems Analysis):**
  * While digital terminals audited 182 core volunteers, peak morning gate throughput and remote airfield staging necessitated secondary physical dispatch (high-vis vests and zone wristbands) for an estimated ~300+ additional partner and student volunteers.
  * *Operational Lesson Learned:* Scaled mobile scanner density and distributed check-in pods are scheduled for deployment in the 2027 season to eliminate check-in bottlenecks.
* **Partner Group Impact:** 49.3% of all recorded hours (1,038.6 hours) came from structured partner organizations (e.g., SOAC, El Dorado HS Orchestra, EDHS Aztec Robotics), verifying the conversion efficiency of the automated outreach pipeline.
* **Compliance & Safety:** 100% digital liability waiver completion prior to airfield entry, zero security gate turnaways at Fort Bliss access control points, and zero runway safety incursions during Blue Angels and F-22 demonstration freezes.

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
