import whois


def is_registered(domain_name):
    """
    A function that returns a boolean indicating weather a 'domain_name' is registered.
    """
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)
