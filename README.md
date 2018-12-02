# metabolite
==========================

## Setting up development environment

Make sure you are using virtualenv

The development environment can be setup either like a pythonista
with the usual python module setup.

## How to install?

Ensure that you have an updated version of pip

```
pip --version
```
Should atleast be 1.5.4
To update pip use

```
pip install -U pip
```
This will upgrade pip version to the latest

From the module folder install the dependencies. This also installs
the module itself in a very pythonic way.

```
pip install -r requirements.txt
```

## APIS Documentation
API to fetch Bank Details with IFSC Code
```
https://indian-bank.herokuapp.com/bank/ifsccode/SBIN0000431
```

API to fetch Banks Details citywise
```
https://indian-bank.herokuapp.com/bank/city/kajora
```

To filter with bank name use bank_name in query params

```
https://indian-bank.herokuapp.com/bank/city/kajora?bank_name=HDFC
```
