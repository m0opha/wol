def MagicPacket(MAC_ADDR):
    """Return a magic packet WOL (WAKE UP ON LAN).
    Remember to turn on WOL in the BIOS of your machine."""

    HEXADECIMAL_MAC = b'\xFF' * 6 + bytes.fromhex(MAC_ADDR.replace(':', '')) * 16
    return HEXADECIMAL_MAC