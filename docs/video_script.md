# Q1(e) demonstration video script (target length 1:50)

**Audience:** senior executives. **Tone:** confident, plain business language.

**How to record:** use Microsoft Teams (Meet now, then Record) or PowerPoint's Record feature, sharing your browser with the Dialogflow CX simulator open. Then upload to Microsoft Stream and share with the teaching team.

**Before you record:**
- Open the Test Agent and click Reset.
- Open the flow graph in a second tab.
- Have these lines ready to paste: `I want to report a problem` → `water leak` → `Building A` → `server room` → `yes` → `anonymous` → `yes`. Then, after a Reset: `I want to report a problem` → `there's smoke in the building`.

---

## 0:00–0:20 | The problem (show the flow graph)
> "Every week, small sustainability problems go unreported: a tap leaking all weekend, air-con cooling an empty floor, batteries in the general bin. Staff notice them but don't know who to tell. That costs us water, energy and money, and leaves gaps in our ESG reporting. EcoReport fixes that."

## 0:20–1:05 | Live demo (simulator)
Type `I want to report a problem`, then answer `water leak`, `Building A`, `server room`.
> "A staff member just reports what they see. EcoReport asks four short questions, each with examples. If they type it all in one sentence, it skips the questions it already understood."

Answer `yes` to the risk question.
> "Because they said people or electrical equipment are at risk, the report is automatically flagged HIGH priority for the on-call facilities team."

Answer `anonymous`, then `yes` at the confirmation.
> "Staff can report anonymously. The bot reads the report back before submitting it, then routes it to the right team, here Facilities Maintenance."

Click Reset, type `I want to report a problem`, then `there's smoke in the building`.
> "And if anyone mentions an emergency at any point, EcoReport stops the form and tells them to call 000. Safety comes before data."

## 1:05–1:35 | Design rationale (back to the flow graph)
> "Three design choices make this safe to deploy. First, privacy by default: we collect only what's needed to fix the issue, and staff can report anonymously. Second, a human is always one message away: every time the bot doesn't understand, it offers to connect you to a person. Third, the routing is rule-based, not generative, so every decision is predictable and auditable."

## 1:35–1:55 | Business value and ask
> "The result: faster fixes, fewer wasted resources, and every report becomes structured data for our ESG dashboard and disclosures. We recommend a six-week pilot in one building, connected to our ticketing system. Thank you."

---

**Checklist:** under 2:00 · your face or voice introduces it · the risk branch, routing, fallback or emergency route, and business value are all shown.
