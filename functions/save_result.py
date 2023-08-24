from decimal import Decimal


def save_with_balance(wallet_info: tuple, wallets: list[dict]):
    if wallet_info[1]["final_balance"] > 0:
        for wallet in wallets:
            if wallet_info[0] == wallet['address']:
                with open('With Balance.txt', 'a', encoding='utf-8') as file:
                    file.writelines(f'Адрес : {wallet_info[0]}\n'
                                    f'Ключ : {wallet["privkey"]}\n'
                                    f'Пароль : {wallet["passphare"]}\n'
                                    f'Транзакции : {wallet_info[1]["n_tx"]}\n'
                                    f'Всего получено : {Decimal(wallet_info[1]["total_received"] / 1e8) :.8f}\n'
                                    f'Баланс : {Decimal(wallet_info[1]["final_balance"] / 1e8) :.8f}\n\n\n'
                                    )


def save_with_transaction(wallet_info: tuple, wallets: list[dict]):
    if wallet_info[1]["n_tx"] > 0:
        for wallet in wallets:
            if wallet_info[0] == wallet['address']:
                with open('With Transactions.txt', 'a', encoding='utf-8') as file:
                    file.writelines(f'Адрес : {wallet_info[0]}\n'
                                    f'Ключ : {wallet["privkey"]}\n'
                                    f'Пароль : {wallet["passphare"]}\n'
                                    f'Транзакции : {wallet_info[1]["n_tx"]}\n'
                                    f'Всего получено : {Decimal(wallet_info[1]["total_received"] / 1e8) :.8f}\n'
                                    f'Баланс : {Decimal(wallet_info[1]["final_balance"] / 1e8) :.8f}\n\n\n'
                                    )
