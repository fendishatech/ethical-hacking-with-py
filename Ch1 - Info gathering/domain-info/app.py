import whois
import requests
import argparse


class DomainInfo():
    def __init__(self, domain_name) -> None:
        self.domain_name = domain_name

    def get_domain_registry(self):
        """
        A function that returns a boolean indicating weather a 'domain_name' is registered.
        """
        try:
            w = whois.whois(self.domain_name)
        except Exception:
            return False
        else:
            return bool(w.domain_name)

    def get_domain_info(self):
        print(f"Domain registry is : {self.get_domain_registry()} ")

    def get_subdomains(self, subdomains_list):
        if (self.get_domain_registry()):
            discovered = []

            for subdomain in subdomains_list:
                url = f"http://{subdomain}.{self.domain_name}"

                try:
                    # if this raises an ERROR, that means the subdomain does not exist
                    requests.get(url, timeout=5)
                except requests.ConnectionError:
                    # if the subdomain does not exist, just pass, print nothing
                    pass
                else:
                    print("[+] Discovered subdomain:", url)
                    # append the discovered subdomain to our list
                    discovered.append(url)

            return discovered


def main():
    google_info = DomainInfo("google.com")
    google_info.get_domain_info()


if __name__ == "__main__":
    main()
