export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(value) {
    this._amount = value;
  }

  get currency() {
    return this._currency;
  }

  set currency(value) {
    this._currency = value;
  }

  displayFullPrice() {
    const currencyAll = this._currency.displayFullCurrency();
    return `${this._amount} ${currencyAll}`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
