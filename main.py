from decimal import Decimal

from rich.console import Console

from functions.balance_checker import check_balance
from functions.bitcoin_wallets_generation import gen_wallets
from functions.save_result import save_with_balance, save_with_transaction
from functions.upload_passwords import get_passwords


class Color:
    fuchsia = '[#FF00FF]'
    green = '[#FF1493]'
    red = '[#FF0000]'
    yellow = '[#FFFF00]'
    dark = '[#9400D3]'


def main():
    count_wallets_print = 0
    data_passwords = get_passwords(file_mame, count_wallets)
    for password in data_passwords:
        wallets = [gen_wallets(x) for x in password]
        addresses = '|'.join([w['address'] for w in wallets])
        response_info_wallet = check_balance(url, addresses)
        try:
            for value in response_info_wallet.items():
                count_wallets_print += 1
                console.print(
                    f"{count_wallets_print} "
                    f"{Color.green}Адрес:{Color.yellow}{value[0]} "
                    f"{Color.fuchsia}Всего транзакций: {Color.yellow}{value[1]['n_tx']} "
                    f"{Color.dark}Всего получено: {Color.yellow}{Decimal(value[1]['total_received'] / 1e8):.8f} "
                    f"{Color.green}Баланс: {Color.yellow}{value[1]['final_balance']} "
                )
                save_with_balance(value, wallets)
                save_with_transaction(value, wallets)
        except AttributeError:
            console.print(f"{Color.red}'NoneType' object has no attribute 'items'")


if __name__ == "__main__":
    console = Console()
    url = 'https://blockchain.info/balance?active='
    file_mame = 'passwords.txt'
    count_wallets = int(input('Количество кошельков за раз: '))
    main()
