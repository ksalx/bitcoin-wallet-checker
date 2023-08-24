from bitcoin import sha256, privtopub, pubtoaddr


def gen_wallets(password: str) -> dict:
    private_key = sha256(password)
    public = privtopub(private_key)
    address = pubtoaddr(public)
    return {
        'address': address,
        'privkey': private_key,
        'passphare': password
    }
