
### ✅ **Propositions d'attributs utiles à suivre** :

| Field              | Description |
|-------------------|-------------|
| `keyword`         | Main role or title (e.g., DevOps Engineer) |
| `company`         | Name of the company |
| `location`        | Country or region |
| `city`            | Optional, if relevant |
| `remote`          | Boolean to indicate if remote work is possible |
| `experience`      | Required experience (e.g., "3+ years") |
| `salary_range`    | If available (e.g., "$70k–$90k") |
| `date_posted`     | When the job was posted |
| `link`            | Direct link to the job posting |
| `status`          | Application status: `to_apply`, `applied`, `interview`, `rejected`, `offer`, etc. |
| `priority`        | Your interest level (1–5 or low/medium/high) |
| `language`        | Languages required (e.g., English, French) |
| `tech_stack`      | Relevant technologies listed (e.g., AWS, Kubernetes, Terraform) |
| `notes`           | Any additional thoughts or comments |
| `deadline`        | Application deadline if available |

---

### 🧱 **Sample JSON structure**

```json
[
  {
    "keyword": "DevOps Engineer",
    "company": "TechCorp",
    "location": "France",
    "city": "Paris",
    "remote": true,
    "experience": "3+ years",
    "salary_range": "€50k–€65k",
    "date_posted": "2025-04-06",
    "deadline": "2025-04-30",
    "link": "https://example.com/job/devops-techcorp",
    "status": "to_apply",
    "priority": "high",
    "language": ["English", "French"],
    "tech_stack": ["AWS", "Terraform", "Kubernetes", "Docker"],
    "notes": "Interesting culture, hybrid setup, Terraform heavy"
  },
  {
    "keyword": "Site Reliability Engineer",
    "company": "CloudOps Ltd.",
    "location": "Germany",
    "city": "Berlin",
    "remote": false,
    "experience": "5 years",
    "salary_range": null,
    "date_posted": "2025-04-07",
    "deadline": null,
    "link": "https://example.com/job/sre-cloudops",
    "status": "applied",
    "priority": "medium",
    "language": ["English"],
    "tech_stack": ["GCP", "Prometheus", "Grafana"],
    "notes": "Applied on April 8 – Waiting for response"
  }
]
```

