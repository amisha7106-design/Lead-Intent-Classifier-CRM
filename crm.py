import csv
from pathlib import Path


CRM_FILE = Path("data/crm_leads.csv")


def save_lead(name, email, message, intent):
    """
    Save a lead and its predicted intent into the CRM.
    """

    # Create data folder if it does not exist
    CRM_FILE.parent.mkdir(parents=True, exist_ok=True)

    file_exists = CRM_FILE.exists()

    with open(CRM_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Add header only for a new file
        if not file_exists:
            writer.writerow([
                "name",
                "email",
                "message",
                "intent",
                "status"
            ])

        writer.writerow([
            name,
            email,
            message,
            intent,
            "New"
        ])

    print("Lead saved to CRM successfully!")