def extract_entities(requirement):
    """
    Extracts key entities from the requirement statement using pattern matching.
    """
    modules = []
    if "login" in requirement.lower():
        modules.append("Authentication Module")
    if "payment" in requirement.lower():
        modules.append("Payment Module")
    if "dashboard" in requirement.lower():
        modules.append("Dashboard Module")
    if "analytics" in requirement.lower():
        modules.append("Analytics Module")
    if "notifications" in requirement.lower():
        modules.append("Notification Module")
    return modules
