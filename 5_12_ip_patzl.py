# Christian Patzl 1BHIF
# Pruefen ob eine IP gueltig is


def ist_ip_gueltig(s: str) -> bool:
    """Prueft ob eine IP gueltig ist

    Args:
        s (str): Die IP als String

    Returns:
        bool: ob die IP gueltig ist
    """
    return len(a := s.split(".")) == 4 and all(i.isdecimal() for i in a) and all(
        int(i) in range(256) for i in a)

a = input("Ip address: ")
print("gültig" if ist_ip_gueltig(a) else "ungültig")