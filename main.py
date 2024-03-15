import json


def main():
    with open("input.json") as f:
        data = json.load(f)

    volume = 0
    for fill_order in data:
        if fill_order["symbol"] != "USDT_USDC":
            volume += float(fill_order["quantity"]) * float(fill_order["price"])

    print(f"Total volume without USDT_USDC pair: {volume}")


if __name__ == "__main__":
    main()
