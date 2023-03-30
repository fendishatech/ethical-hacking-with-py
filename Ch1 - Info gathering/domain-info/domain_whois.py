import whois
from domain_validator import is_registered

domain_name = "https://dramatica.com"


def domain_info(domain_name):
    """
    A Function that extracts domain information if it is a registered domain.
    """

    if is_registered(domain_name):
        whois_info = whois.whois(domain_name)

        # registrar
        print("domain Registrar : ", whois_info.registrar)

        # server
        print("domain Server : ", whois_info.whois_server)

        # date created
        print("Date Created : ", whois_info.creation_date)

        # Expiration date
        print("Expires at : ", whois_info.expiration_date)

        print(whois_info)

    else:
        print("The domain name does not exist in the registry.")
