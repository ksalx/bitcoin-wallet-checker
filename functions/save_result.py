from decimal import Decimal


def save_with_balance(wallet_info: tuple, wallets: list[dict]):
    if wallet_info[1]["final_balance"] > 0:
        for wallet in wallets:
            if wallet_info[0] == wallet['address']:
                with open('With Balance.txt', 'a', encoding='utf-8') as file:
                    file.writelines(f'Address : {wallet_info[0]}\n'
                                    f'Public Key : {wallet["privkey"]}\n'
                                    f'Passphrase : {wallet["passphare"]}\n'
                                    f'Transactions : {wallet_info[1]["n_tx"]}\n'
                                    f'Total received : {Decimal(wallet_info[1]["total_received"] / 1e8) :.8f}\n'
                                    f'Balance : {Decimal(wallet_info[1]["final_balance"] / 1e8) :.8f}\n\n\n'
                                    )


def save_with_transaction(wallet_info: tuple, wallets: list[dict]):
    if wallet_info[1]["n_tx"] > 0:
        for wallet in wallets:
            if wallet_info[0] == wallet['address']:
                with open('With Transactions.txt', 'a', encoding='utf-8') as file:
                    file.writelines(f'Address : {wallet_info[0]}\n'
                                    f'Public Key : {wallet["privkey"]}\n'
                                    f'Passphrase : {wallet["passphare"]}\n'
                                    f'Transactions : {wallet_info[1]["n_tx"]}\n'
                                    f'Total received : {Decimal(wallet_info[1]["total_received"] / 1e8) :.8f}\n'
                                    f'Balance : {Decimal(wallet_info[1]["final_balance"] / 1e8) :.8f}\n\n\n'
                                    )
