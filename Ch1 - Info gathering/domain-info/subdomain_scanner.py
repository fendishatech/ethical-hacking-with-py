import requests

domain_name = "google.com"


def get_possible_subdomains(subdomains_file):
    with open(subdomains_file) as file:
        subdomains = file.read()
        subdomains_list = subdomains.splitlines()

    return subdomains_list


def get_discovered_subdomains(subdomains_list):
    discovered = []

    for subdomain in subdomains_list:
        url = f"http://{subdomain}.{domain_name}"

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


def save_discovered_subdomains(discovered_subdomains):
    # save the discovered subdomains into a file
    with open("discovered_subdomains.txt", "w") as f:
        for subdomain in discovered_subdomains:
            print(subdomain, file=f)


def main():

    # read possible subdomains file
    subdomains_file = "subdomains.txt"
    subdomains_list = get_possible_subdomains(subdomains_file)

    discovered = get_discovered_subdomains(subdomains_list)
    save_discovered_subdomains(discovered)
    print(discovered)

    # print(subdomains_list)
    # print(f"Globals globals() => ", globals())
    # print(f"Dict __doc__ => ", __dict__)


if __name__ == "__main__":
    main()
