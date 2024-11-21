import random


def ran():
  r = random.choice("1234567890")
  return {'id': int(r)}
