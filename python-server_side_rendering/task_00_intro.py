def generate_invitations(template, attendees):
    if not isinstance(template, str):
        return "template is not string"
    
    if not isinstance(attendees, list):
        return "attendees is not list"
    
    if not all(isinstance(attendee, dict) for attendee in attendees):
        return "attendees is not list of dicts"

    if template == "":
        return "Template is empty, no output files generated."
    
    if attendees == []:
        return "No data provided, no output files generated."
    
    placeholders = ["name", "event_title", "event_date", "event_location"]
    default = "N/A"

    for index, attendee in enumerate(attendees, start=1):
        new_template = template
        for key in placeholders:
            value = attendee.get(key) or default
            new_template = new_template.replace(f"{{{key}}}", value)
        number = f"output_{index}.txt"
        with open(number, "w") as f:
            f.write(new_template)